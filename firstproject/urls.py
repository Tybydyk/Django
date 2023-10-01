"""
URL configuration for firstproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('firstapp.urls')),
    path('main/', include('firstmainapp.urls')),
    path('about_me/', include('first_about_me_app.urls')),
    path('second/', include('second_app.urls')),
    path('lesson2/', include('lesson_2_app.urls')),
    path('hw2/', include('hw2_store_app.urls')),
    path('third/', include('s_third_app.urls')),
    path('lesson3/', include('lesson_3_app.urls')),
    ]
