# autos/urls.py

from django.urls import path
from .views import (
    CarListView,
    CarDetailView,
    CarCreateView,
    CarUpdateView,
    CommentDeleteView,
    add_comment,
    register_view,
    login_view
)
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', CarListView.as_view(), name='car_list'),  # Home page showing all cars
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'),  # Detail view of a specific car
    path('car/new/', CarCreateView.as_view(), name='car_create'),  # Create a new car (staff only)
    path('car/<int:pk>/edit/', CarUpdateView.as_view(), name='car_update'),  # Edit a car (staff only)
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),  # Delete a comment
    path('car/<int:pk>/comment/', add_comment, name='add_comment'),  # Add a comment to a car
    path('register/', register_view, name='register'),  # User registration
    path('login/', login_view, name='login'),  # User login
    path('logout/', LogoutView.as_view(), name='logout'),  # User logout
]
