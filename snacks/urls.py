from .views import HomeView,AboutView
from django.urls import path

# creating the routs that we need
urlpatterns = [
    path('',HomeView.as_view(), name='snacks-home'), # Home page rout
    path('about',AboutView.as_view(), name='snacks-about') # About page rout
]