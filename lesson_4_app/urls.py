from django.urls import path
from .views import games, lesson4
urlpatterns = [
    path('', lesson4, name='lesson4'),
    path('games/', games, name='games'),
]