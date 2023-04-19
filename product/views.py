from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class GetProducts(APIView):
    authentication_class = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):

        obj = Products.objects.all()

        serializer = PSerializer(obj, many=True)

        return Response(serializer.data, status=200)


class AddtoCart(APIView):
    authentication_class = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Fail to add to cart"})


class PlaceOrder(APIView):
    def post(self, request):
        serializer = OSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Fail to place order"})


class getOrders(APIView):
    authentication_class = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):

        obj = Orders.objects.filter(cu=request.user)

        serializer = OSerializer(obj, many=True)

        return Response(serializer.data, status=200)
