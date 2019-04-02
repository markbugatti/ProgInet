
from django.contrib import admin
from django.urls import path
from . import  views

redirectpatterns = [
    path('redirect', views.redirect),
]

urlpatterns = [
    path('', views.application4),
    path('redirect', views.redirect),
    path('redirected', views.redirected),
    path('render-html', views.renderHtml),
    path('render-template', views.htmlFormTemplate),
    path('render-template/form-handler', views.formHandler),

]


