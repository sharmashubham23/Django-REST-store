from django.shortcuts import render
from .models import CustomUser
# from .models import Orders
from .serializer import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import HttpResponse
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class GetUser(APIView):
    def get(self, request):

        obj = CustomUser.objects.all()

        serializer = USerializer(obj, many=True)

        return Response(serializer.data)


class Register(APIView):
    def post(self, request):
        serializer = USerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "user already registered"})
