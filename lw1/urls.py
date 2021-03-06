"""lw1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/pyen/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # path('Aplication0/', include('Aplication0.urls')),
    path('Application1/', include('Application1.urls')),
    path('', include('Application1.urls')),
    path('admin/', admin.site.urls),
    path('application2/', include('Application2Lw3.urls')),
    path('Application3/', include('Application3.urls')),
    path('Application4/', include('Application4.urls')),
    path('applicationmodels/', include('applicationmodels.urls')),
    path('appdatabase/', include('appdatabase.urls'))
    # path('new_patterns/', include('Application3.urls'))
]