from django.shortcuts import render

# Create your views here.
# after creating the templtes folder
# import the tamplete view 
from django.views.generic import TemplateView
# create class for each teamplet 
# Home templet
class HomeView(TemplateView):
    template_name = 'snacks-home.html'

# About templet
class AboutView(TemplateView):
    template_name = 'snacks-about.html'