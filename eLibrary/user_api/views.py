# from django.shortcuts import render

# Create your views here.
# Creating endpoints for the user api
# The required endpoints are:
#
# Index page : redirects to librarian register,
#              Member register and login pages
# Librarian register page : Form to register a Librarian user role
# Member register page : Form to register a Member user role
# Login : login authentication using JWT
# Librarian Viewset : Displays members in system
#                     Can then be updated or deleted by Librarian user
# Member Viewset : Can delete own account
#
# Importing required modules

from .models import LibraryUser
from .permissions import is_Librarian
from .serializers import (LibrarianRegisterSerializer,
                          MemberRegisterSerializer, UserSerializer)

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view

from rest_framework.permissions import IsAuthenticated, AllowAny
# from rest_framework.authentication import TokenAuthentication


# Index to navigate to different user functions
@api_view(['GET'])
def index(request, format=None):
    return Response({
        'Register a Librarian': reverse('librarian-register',
                                        request=request, format=format),
        'Register a Member': reverse('member-register',
                                     request=request, format=format),
        'View user': reverse('user', request=request, format=format),
        'View existing Members': reverse('members-list',
                                         request=request, format=format),
        'View books': reverse('book-list', request=request, format=format),
    })


# Endpoint to register a Librarian user
class LibrarianRegister(generics.CreateAPIView):
    queryset = LibraryUser.objects.all()
    permission_classes = [AllowAny, ]
    serializer_class = LibrarianRegisterSerializer


# Endpoint to register a Member User
class MemberRegister(generics.CreateAPIView):
    queryset = LibraryUser.objects.all()
    permission_classes = [AllowAny, ]
    serializer_class = MemberRegisterSerializer


# Endpoint for listing members
class Members(generics.ListCreateAPIView):
    queryset = LibraryUser.objects.all()
    permission_classes = [IsAuthenticated, is_Librarian, ]
    serializer_class = MemberRegisterSerializer

    def get(self, request):
        members = LibraryUser.objects.all()
        serializer = UserSerializer(members, many=True)
        return Response(serializer.data)


# Endpoind for viewing details of a particular member
class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LibraryUser.objects.all()
    permission_classes = [IsAuthenticated, is_Librarian]
    serializer_class = UserSerializer

    def delete(self, request, pk):
        member = self.get_object()
        if member.user_role == 2 or (member.user_role == 1
                                     and member.id == request.user.id):
            member.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


# Endpoint for viewing details of current user
class UserDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = UserSerializer

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
        return Response(serializer.data)
