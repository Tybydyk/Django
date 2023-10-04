from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('heads_tails/', views.heads_tails, name='heads_tails'),
    path('authors/', views.author_read, name='autors'),
    path('articles/', views.articles, name='articles'),
    path('article_by_author/', views.article_by_author, name='article_by_author'),
    path('view_article/<int:id_article>', views.view_article, name='view_article'),
    path('view_all_articles/', views.view_all_articles, name='view_all_articles'),
    path('create_author/', views.create_author, name='create_author'),
    path('create_article/', views.create_article, name='create_article'),
    path('create_article_form/', views.create_article_form, name='create_article_form'),
]