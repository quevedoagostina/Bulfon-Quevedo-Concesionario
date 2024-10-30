from django.contrib.auth.models import User  # Cambia esta línea si no tienes un modelo personalizado de User
from rest_framework import generics, permissions
from .models import Car, Brand, Comment
from .serializers import CarSerializer, BrandSerializer, CommentSerializer, UserSerializer

class CarListAPIView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class BrandListAPIView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CarCommentsAPIView(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        car_id = self.kwargs['car_id']
        return Comment.objects.filter(car_id=car_id)

class CreateCustomerAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
