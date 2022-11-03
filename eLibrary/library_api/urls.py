# Creating endpoint urls for the users api

# Importing necessary modules

from django.urls import path
from . import views


urlpatterns = [
    path('book-list/', views.BookList.as_view(), name='book-list'),
    path('book-list/add-book/', views.AddBook.as_view(), name='add-book'),
    path('book-list/<int:pk>/', views.BookDetail.as_view(),
         name='book-detail'),
    path('book-list/<int:pk>/update/', views.UpdateBook.as_view(),
         name='update-book'),
    path('book-list/<int:pk>/borrow/', views.BorrowBook.as_view(),
         name='borrow-book')
]
