from django.shortcuts import render

#Here we use drf gerneric view
from rest_framework import generics
from .serializers import CategorySerializer,BookSerializers,ProductSerializer
from .models import Category,Product,Book

class ListCategory(generics.ListCreateAPIView):
    queryset =Category.objects.all()
    serializer_class =CategorySerializer

class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class =CategorySerializer

class ListBook(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class =BookSerializers

class DetailBook(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class =BookSerializers


class ListProduct(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class =ProductSerializer