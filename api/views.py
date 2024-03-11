from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.decorators import permission_classes
from .serializers import RegisterSerializer,UserSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User

# Create your views here.

class RegisterAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class CheckIfLoggedIn(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        return Response("uspjesno")