from django.contrib import admin
from django.urls import path
from .views import login, sample_api


urlpatterns = [
    path('api/login', login),
    path('api/sampleapi', sample_api),
    # path('signup/', Register),
]