from django.contrib.auth.models import User  # Cambia esta línea si no tienes un modelo personalizado de User
from rest_framework import serializers
from .models import Car, Brand, Comment, Review

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name']

class CarSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()  # Anidando Brand en Car

    class Meta:
        model = Car
        fields = ['id', 'model', 'brand', 'year', 'price', 'description', 'image']

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ['id', 'car', 'user', 'content', 'created_at']

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Review
        fields = ['id', 'car', 'user', 'title', 'content', 'rating', 'created_at']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}  # Oculta el password en respuestas

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
