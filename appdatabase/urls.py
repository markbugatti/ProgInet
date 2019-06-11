from django.contrib import admin
from django.urls import path
from . import  views
from .views import List

urlpatterns = [
    path('list/', List.as_view())
]