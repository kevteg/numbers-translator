from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('num_to_english', include("apps.translator.urls")),
]
