# Creating serializers for the REST api Framework endpoints
#
# The Required seerializers are:
#
# LibrarianRegisterSerializer: Librarian register
# MemberRegisterSerializer: Member register
# MyTokenObtainPairSerializer: Obtaining jwt for authentication
# UserSerializer: User details
# MemberViewSerializer: Member viewlist
#
# Importing necessary modules

from rest_framework import serializers
from .models import LibraryUser

from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


# Serializer for the librarian registration endpoint
class LibrarianRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=LibraryUser.objects.all())]
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
    )

    class Meta:
        model = LibraryUser
        fields = ('username', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Passwords do not match"}
            )
        return attrs

    def create(seld, validated_data):
        user = LibraryUser.objects.create(
            username=validated_data['username'],
            user_role=1,
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


# Serializer for the member registration endpoint
class MemberRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=LibraryUser.objects.all())]
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
    )

    class Meta:
        model = LibraryUser
        fields = ('username', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Passwords do not match"}
            )
        return attrs

    def create(seld, validated_data):
        user = LibraryUser.objects.create(
            username=validated_data['username'],
            user_role=2,
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


# Serializer for user details endpoint
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryUser
        fields = ['id', 'username', 'user_role']


# Serializer for member details endpoint
class MemberSerializer(serializers.ModelSerializer):
    view = serializers.HyperlinkedIdentityField(view_name='member')

    class Meta:
        model = LibraryUser
        fields = ['id', 'username', 'user_role', 'view']
