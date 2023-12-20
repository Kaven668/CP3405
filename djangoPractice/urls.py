"""djangoPractice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from test01 import views

urlpatterns = [
    path("info/", views.info_list),
    path("learn/", views.test_fun),
    path("info/add/", views.login),
    path("info/delete/", views.delete),
    path("info/login/", views.login_01),
    path("testAdd/", views.test_db),
    path("testDlt/", views.test_dlt),
    path("test01/", views.test_db_01),
    path("test02/", views.test_db_02),
    path("test03/", views.test_db_03)
]
