from django.db import models

# Create your models here.
# Databases used by the Librarian role i.e. Books and Members


class Books(models.Model):
    """docstring for Books.
    Creates the SQL database listing all the Books in the system"""

    name = models.CharField(max_length=255)
    author = models.CharField(default="", max_length=255)
    publisher = models.CharField(default="", max_length=255)
    year = models.CharField(default="", max_length=4)
    edition = models.CharField(default="", max_length=255)
    availability = models.BooleanField(default=True)


class Members(models.Model):
    """docstring for Members.
    Creates the SQL database listying all the Members in the system"""

    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    membernum = models.CharField(max_length=8)
