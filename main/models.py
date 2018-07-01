import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UUIDModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True

class Image(UUIDModel):
    email = models.EmailField(_('メールアドレス'), unique=True)
    image = models.ImageField(_('画像'), upload_to='img/')
    is_selected = models.NullBooleanField(_('当選'))
    created_at = models.DateTimeField(_('作成日時'), auto_now_add=True)
    updated_at = models.DateTimeField(_('更新日時'), auto_now=True)

    class Meta:
        db_table = 'images'
        verbose_name = _('画像')
        verbose_name_plural = _('画像')

    def __str__(self):
        return '%s' % self.email
