# Creating serializers for the REST api Framework endpoints
#
# The Required seerializers are :
#
# BookViewSerializer for Booklist

from rest_framework import serializers
from .models import Book


class BookListSerializer(serializers.HyperlinkedModelSerializer):
    view = serializers.HyperlinkedIdentityField(view_name='book-detail')

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publisher',
                  'year', 'edition', 'status', 'view']


class AddBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publisher',
                  'year', 'edition']


class BookDetailSerializer(serializers.HyperlinkedModelSerializer):
    update = serializers.HyperlinkedIdentityField(view_name='update-book')
    borrow = serializers.HyperlinkedIdentityField(view_name='borrow-book')

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publisher',
                  'year', 'edition', 'status', 'borrower', 'borrow', 'update']


class BorrowBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publisher',
                  'year', 'edition', 'status', 'borrower']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = []
