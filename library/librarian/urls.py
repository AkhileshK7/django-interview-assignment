from django.urls import path
from . import views

urlpatterns = [
    path('', views.librarian, name='librarian'),
    path('books/', views.books, name='books'),
    path('books/addbook/', views.addbook, name='addbook'),
    path('books/addbook/addbookrecord/',
         views.addbookrecord, name='addbookrecord'),
    path('books/deletebook/<int:id>', views.deletebook, name='deletebook'),
    path('books/updatebook/<int:id>', views.updatebook, name='updatebook'),
    path('books/updatebook/updatebookrecord/<int:id>',
         views.updatebookrecord, name='updatebookrecord'),
    path('members/', views.members, name='members'),
    path('members/addmember/', views.addmember, name='addmember'),
    path('members/addmember/addmemberrecord/',
         views.addmemberrecord, name='addmemberrecord'),
    path('members/deletemember/<int:id>',
         views.deletemember, name='deletemember'),
    path('members/updatemember/<int:id>',
         views.updatemember, name='updatemember'),
    path('members/updatemember/updatememberrecord/<int:id>',
         views.updatememberrecord, name='updatememberrecord'),
]
