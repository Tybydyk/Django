from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('heads_tails/', views.heads_tails, name='heads_tails'),
    path('authors/', views.author_read, name='autors'),
    path('articles/', views.articles, name='articles'),
    path('article_by_author/', views.article_by_author, name='article_by_author'),
]