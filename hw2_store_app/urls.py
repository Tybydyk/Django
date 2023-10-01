from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.users, name='users'),
    path('products/', views.products, name='products'),
    path('orders/', views.orders, name='orders'),
    path('user_orders/<int:user_id>', views.user_orders, name='user_orders'),
    path('user_products_per_time/<int:user_id>/<str:interval>', views.user_products_per_time, name='user_products_per_time'),
]