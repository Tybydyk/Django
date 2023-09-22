from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('heads_tails/', views.heads_tails, name='heads_tails'),
    path('rand_int/', views.rand_int, name='rand_int'),
    path('cube', views.cube, name='cube'),
]