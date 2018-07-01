from django.urls import path
from . import views, models

app_name = 'main'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('thanks/', views.ThanksView.as_view(), name='thanks'),
]
