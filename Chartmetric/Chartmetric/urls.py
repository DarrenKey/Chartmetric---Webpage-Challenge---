"""Chartmetric URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from HandleCSV import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = "index"),
    path('<str:username>/recentposts/', views.recentposts, name = "recentposts"),
    path('<str:username>/topposts/', views.topposts, name = "topposts"),
    path('<str:username>/commercialposts/', views.commercialposts, name = "commercialposts"),
    path('<str:username>/stats/', views.stats, name = "stats"),
    path('api/<str:username>/reportinfo/', views.reportinfo, name = "reportinfo"),
    path('api/<str:username>/userprofile/', views.userprofile, name = "userprofile"),
    path('api/<str:username>/audiencelikers/', views.audiencelikers, name = "audiencelikers"),
    path('api/<str:username>/audiencefollowers/', views.audiencefollowers, name = "audiencefollowers"),
    path('api/<str:username>/audiencecommenters/', views.audiencecommenters, name = "audiencecommenters"),
    path('api/<str:username>/extra/', views.extra, name = "extra"),
    path('api/<str:username>/', views.loginall, name = "loginapiall")
]
