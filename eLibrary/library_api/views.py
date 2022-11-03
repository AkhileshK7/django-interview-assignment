# from django.shortcuts import render

# Create your views here.
# Creating endpoints for for the library api
# Required endpoints are :
#
# BookList : List of all available books in the system
# AddBook : Add book if user is a librarian
# BookDetail : Details of a specific book in the system
# UpdateBook : Update details of or delete a book in th system as a librarian
#              type user
# BorrowBook : Borrowing a book as a member role user
#
# Importing necessary modules

from django.shortcuts import redirect
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework.permissions import IsAuthenticated
from user_api.permissions import is_Librarian

from .serializers import (BookListSerializer, AddBookSerializer,
                          BookDetailSerializer, BorrowBookSerializer,
                          BookSerializer)
from .models import Book


# Endpoint to list out all the books in the system
class BookList(generics.GenericAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request):
        """Display list of all the books in the system\n
        Accessible after authentication"""
        books = Book.objects.all()
        serializer = BookListSerializer(books, context={'request': request},
                                        many=True)
        return Response(serializer.data)

    def post(self, request):
        """Redirect to a form to add a new book\n
        Accessible after authentication"""
        return redirect(reverse('add-book', request=request))


# Endpoint to add new book
class AddBook(generics.CreateAPIView):
    """Add a new book.\n
    Accessible after authentication if a librarian type user"""
    permission_classes = [IsAuthenticated, is_Librarian, ]
    queryset = Book.objects.all()
    serializer_class = AddBookSerializer


# Endpoint to view a particular book
class BookDetail(generics.RetrieveAPIView):
    """Display detail of a specific book in the system\n
    Accessible after authentication"""
    permission_classes = [IsAuthenticated, ]
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer


# Endpoint to update book
class UpdateBook(generics.RetrieveUpdateDestroyAPIView):
    """Display detail of or delete a specific book  in the system\n
    Accessible after authentication if a librarian type user"""
    permission_classes = [IsAuthenticated, is_Librarian, ]
    queryset = Book.objects.all()
    serializer_class = AddBookSerializer


# Endpoint to borrow a book
class BorrowBook(generics.GenericAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, pk):
        """Display detail of the specific book in the system\n
        Accessible after authentication"""
        book = self.get_object()
        serializer = BorrowBookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk):
        """Borrow or return the book\n
        Accessible after authentication"""
        try:
            book = self.get_object()
            user_obj = request.user
            if book.status == 'BORROWED' and request.user.id == book.borrower:
                serializer = BorrowBookSerializer(instance=book, data={
                                            'status': 'AVAILABLE',
                                            'borrower': None},
                                            partial=True)

            elif book.status == 'AVAILABLE':
                serializer = BorrowBookSerializer(instance=book, data={
                                            'status': 'BORROWED',
                                            'borrower': user_obj.id},
                                            partial=True)

            else:
                return Response({
                    'message': 'Action not permitted',
                    })
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response({
                'message': 'Action completed successfully',
                'data': serializer.data
            })
        except Exception as e:
            print(e)
            return Response('error')
