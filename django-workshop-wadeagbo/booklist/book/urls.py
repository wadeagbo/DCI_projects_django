from django.urls import path
from .views import book_list, add_book

urlpatterns = [
    path('', book_list, name='book_list'),
    path('add_book/', add_book, name='add_book'),
]
