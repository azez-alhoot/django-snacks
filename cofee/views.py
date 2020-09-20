from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class CofeeHomeView(TemplateView):
    template_name = 'cofee-home.html'

class cofeeAboutView(TemplateView):
    template_name = 'cofee-about.html'