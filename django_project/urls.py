"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from booking import views

app_name = 'booking'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.room_list, name='rooms'),
    path('register/', views.register, name='register'),
    path('rooms/<room_number>/book/', views.BookRoom, name='book'),
    path("rooms/<room_number>/", views.room_detail, name='room'),
    path('',include('django.contrib.auth.urls')),
]
