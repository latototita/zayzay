from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

app_name = 'Main'

urlpatterns = [
    path('', index, name='index'),
    path('article', article, name='article'),
    path('terms', terms, name='terms'),
    path('privacy', privacy, name='privacy'),
]