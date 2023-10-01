from django.urls import path, include
from . import views


urlpatterns = [
    # path('', views.index, name='index'),
    path('hello2/', views.HelloView.as_view(), name='hello2'),
    path('/', views.HelloView.as_view(), name='hello2'),
    path('', views.my_view, name='index'),
    path('for/', views.view_for, name='for'),
    path('author/<int:author_id>/', views.author_posts, name='author_posts'),
    path('post/<int:post_id>/', views.post_full, name='post_full'),

]