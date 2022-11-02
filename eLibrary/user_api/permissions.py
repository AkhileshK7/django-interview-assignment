# Creating custom permission class to distinguish
# a Librarian user role and a Member user role
#
# Importing necessary modules

from rest_framework import permissions


class is_Librarian(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_role == 1
