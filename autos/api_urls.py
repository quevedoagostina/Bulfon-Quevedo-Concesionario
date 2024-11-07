from django.urls import path
from .views import CarListAPIView, CarCommentsAPIView, UserCreateAPIView

urlpatterns = [
    path('cars/', CarListAPIView.as_view(), name='car-list-api'),
    path('cars/<int:car_id>/comments/', CarCommentsAPIView.as_view(), name='car-comments-api'),
    path('users/create/', UserCreateAPIView.as_view(), name='user-create-api'),
]
