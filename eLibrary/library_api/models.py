from django.db import models

# Create your models here.
#
# Creating a book model
#
# Book model has attribures :
#
# title : Title of the book, required field
# author : Author of the book
# publisher : Publisher of the book
# year : Year of publication
# edition : Edition of the book
# available : Boolean status of the book
#             True -> Available, False -> Borrowed
# borrower : Member id of the borrower of the book when borrowed
#            Null when available


class Book(models.Model):

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, null=True)
    publisher = models.CharField(max_length=255, null=True)
    year = models.PositiveSmallIntegerField(null=True)
    edition = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=255, default='AVAILABLE')
    borrower = models.PositiveIntegerField(null=True)
