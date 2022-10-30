from django.urls import path
from . import views

urlpatterns = [
    path('', views.member, name='member'),
    path('borrowbook/<int:id>', views.borrowbook, name='borrowbook'),
    path('returnbook/<int:id>', views.returnbook, name='returnbook'),
]
