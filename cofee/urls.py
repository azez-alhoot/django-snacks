from django.urls import path
from .views import CofeeHomeView, cofeeAboutView
urlpatterns = [
    path('',CofeeHomeView.as_view(), name='home-cofee'), # Home page rout
    path('about',cofeeAboutView.as_view(), name='about-cofee') # About page rout
]