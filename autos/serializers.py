from rest_framework import serializers
from .models import Car, Brand, Comment, User, CarModel

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'car', 'user', 'content', 'created_at', 'updated_at']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class CarModelSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()  # Anidamos Brand dentro de CarModel

    class Meta:
        model = CarModel
        fields = ['id', 'name', 'brand']

class CarSerializer(serializers.ModelSerializer):
    model = CarModelSerializer()  # Anidamos CarModel dentro de Car para acceder al brand

    class Meta:
        model = Car
        fields = ['id', 'model', 'category', 'year', 'price', 'image', 'description']
