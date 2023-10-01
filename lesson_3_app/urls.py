from django.urls import path, include
from . import views


urlpatterns = [
    # path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('heads_tails/<int:n>', views.heads_tails, name='heads_tails'),
    path('dice/<int:n>', views.dice, name='dice'),
    path('rand/<int:n>', views.rand, name='rand'),
    path('gp/<int:n>', views.gp, name='gp'),

]