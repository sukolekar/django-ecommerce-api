from rest_framework import serializers
# obj to json

from .models import Category,Book,Product

#we make serializer for everyone..

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Category

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Book


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Product