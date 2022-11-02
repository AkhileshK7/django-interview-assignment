from django.db import models

# Create your models here.
#
# Creating a custom user model based on the
# AbstractUser model in django authentication models
#
# Custom model has 2 roles;
#
# Librarian : Can add, update and remove other non librarian users
#             Can add, update and remove Books in the system
#
# Member : Can delete own account
#          Can view, borrow and return books in the system
#
# Importing necessary modules

from django.contrib.auth.models import AbstractUser


class LibraryUser(AbstractUser):

    USER_ROLE_TYPES = (
        (1, 'Librarian'),
        (2, 'Member'),
    )

    user_role = models.PositiveSmallIntegerField(choices=USER_ROLE_TYPES)

    def __str__(self):
        return self.username
