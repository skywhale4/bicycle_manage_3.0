"""bicycle_manage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from BicycleApp import views

urlpatterns = [
    path('', views.login),
path('login/', views.login,name='login'),
path('index_a/', views.index_a),
path('index_u/', views.index_u),
path('logout/', views.logout),
path('register/', views.register,name='register'),
path('bicycleinfo/', views.bicycleinfo),
    path('updatebicycle/',views.updatebicycle),
path('delbicycle/',views.delbicycle),
path('userinfo/',views.userinfo),
    path('addbicycle/',views.addbicycle),
    path('recordinfo/',views.recordinfo),
    path('bookingcar/',views.bookingcar),
    path('userrecord/',views.userrecord),
    path('returncar/',views.returncar),
    path('returncar_o/',views.returncar_o),
    path('usercarinfo/',views.usercarinfo),
path('usercarinfo2/',views.usercarinfo2),
]
