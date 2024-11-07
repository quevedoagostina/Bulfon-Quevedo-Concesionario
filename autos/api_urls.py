from django.urls import path
from .api_views import CarListAPIView, CarDetailAPIView, CarCommentsAPIView, UserCreateAPIView, CommentCreateAPIView, CommentDetailAPIView

urlpatterns = [
    path('cars/', CarListAPIView.as_view(), name='car-list-api'),
    path('cars/<int:pk>/', CarDetailAPIView.as_view(), name='car-detail-api'),  # CRUD completo de Car
    path('cars/<int:car_id>/comments/', CarCommentsAPIView.as_view(), name='car-comments-api'),
    path('users/create/', UserCreateAPIView.as_view(), name='user-create-api'),
    path('comments/', CommentCreateAPIView.as_view(), name='comment-create-api'),
    path('comments/<int:pk>/', CommentDetailAPIView.as_view(), name='comment-detail-api'),

]
