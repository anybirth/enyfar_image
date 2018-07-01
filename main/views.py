from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django import http
from . import models, forms

# Create your views here.

class IndexView(generic.FormView):
    form_class = forms.ImageForm
    template_name = 'main/index.html'
    success_url = reverse_lazy('main:thanks')

    def get(self, request):
        email = request.GET.get('email')
        if email == None:
            raise http.Http404
        return super().get(request)

    def post(self, request):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        image = request.FILES['image']
        email = self.request.GET.get('email')
        if form.is_valid():
            instance = models.Image(image=image, email=email)
            instance.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class ThanksView(generic.TemplateView):
    template_name = 'main/thanks.html'
