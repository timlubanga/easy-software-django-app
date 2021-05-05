from django.shortcuts import render
from userAuth.serializers import UserRegistrationSerializer, LoginSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from django.contrib.auth import get_user_model

UserAccount = get_user_model()
# Create your views here.


class UserRegistrationView(generics.GenericAPIView):
    serializer_class = UserRegistrationSerializer
    queryset = UserAccount.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class SigninView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    queryset = UserAccount.objects.all()

    def post(self, request):
        
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        return Response(data, status.HTTP_200_OK)
