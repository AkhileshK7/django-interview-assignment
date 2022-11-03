# from django.shortcuts import render

# Create your views here.
# Creating endpoints for the user api
# The required endpoints are:
#
# Index page : redirects to librarian register,
#              Member register and login pages
# Librarian register page : Form to register a Librarian user role
# Member register page : Form to register a Member user role
# User details page: View details and delete current user
# Members list page : Displays members in system and add new member by
#                     Librarian type user
# Member details page : Updated Details or deleted by Librarian type user
#
# Importing required modules

from .models import LibraryUser
from .permissions import is_Librarian
from .serializers import (LibrarianRegisterSerializer,
                          MemberRegisterSerializer, UserSerializer,
                          MemberSerializer)

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework.permissions import IsAuthenticated, AllowAny


# Index to navigate to different user functions
class Index(generics.GenericAPIView):
    def get(self, request):
        """Index page to navigate to other functions"""
        return Response({
            'Register a Librarian': reverse('librarian-register',
                                            request=request),
            'Register a Member': reverse('member-register',
                                         request=request),
            'View user': reverse('user', request=request),
            'View existing Members': reverse('members-list',
                                             request=request),
            'View books': reverse('book-list', request=request),
            'Generate JWT': reverse('token_obtain_pair', request=request),
            'Refresh JWT': reverse('token_refresh', request=request),
            'View Documentation': reverse('swagger-ui', request=request),
        })


# Endpoint to register a Librarian user
class LibrarianRegister(generics.CreateAPIView):
    """Register a librarian type user"""
    queryset = LibraryUser.objects.all()
    permission_classes = [AllowAny, ]
    serializer_class = LibrarianRegisterSerializer


# Endpoint to register a Member User
class MemberRegister(generics.CreateAPIView):
    """Register a member type user"""
    queryset = LibraryUser.objects.all()
    permission_classes = [AllowAny, ]
    serializer_class = MemberRegisterSerializer


# Endpoint for viewing details of current user
class UserDetail(generics.RetrieveDestroyAPIView):
    """Delete current user\n
    Accessible after authentication"""
    permission_classes = [IsAuthenticated, ]
    serializer_class = UserSerializer

    def get(self, request):
        """Display details of the current user"""
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


# Endpoint for listing members
class Members(generics.ListCreateAPIView):
    """Display the list of current members in the system\n
    Add a new member\n
    Accessible after authentication if a librarian type user"""
    queryset = LibraryUser.objects.all()
    permission_classes = [IsAuthenticated, is_Librarian, ]
    serializer_class = MemberRegisterSerializer

    def get(self, request):
        members = LibraryUser.objects.all()
        serializer = MemberSerializer(members, context={'request': request},
                                      many=True)
        return Response(serializer.data)


# Endpoind for viewing details of a particular member
class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    """Display the details of a particular member in the system\n
    Can update the details of the member including promoting a member type user
    to a librarian type user and demoting a librarian type user to a member
    type user\n
    Accessible after authentication if a librarian type user"""
    queryset = LibraryUser.objects.all()
    permission_classes = [IsAuthenticated, is_Librarian]
    serializer_class = UserSerializer

    def delete(self, request, pk):
        """Can remove non librarian user."""
        member = self.get_object()
        if member.user_role == 2 or (member.user_role == 1
                                     and member.id == request.user.id):
            member.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
