# Creating endpoint urls for the users api

# Importing necessary modules

from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('librarian-register/', views.LibrarianRegister.as_view(),
         name='librarian-register'),
    path('member-register/', views.MemberRegister.as_view(),
         name='member-register'),
    path('members-list/', views.Members.as_view(),
         name='members-list'),
    path('members-list/<int:pk>/', views.MemberDetail.as_view(),
         name='member'),
    path('user/', views.UserDetail.as_view(),
         name='user')
]
