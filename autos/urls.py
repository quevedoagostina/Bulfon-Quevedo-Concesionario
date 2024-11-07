from django.urls import path, include
from .views import (
    CarListView, CarDetailView, CarCreateView, CarUpdateView, CarDeleteView,
    add_comment, CommentDeleteView, ReviewListView, ReviewCreateView, 
    FavoriteListView, toggle_favorite, LikeToggleView, CustomerProfileDetailView,
    register_view, CarListAPIView, CarCommentsAPIView, UserCreateAPIView
)
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomLoginForm

urlpatterns = [
    # Rutas para las Vistas Normales
    path('', CarListView.as_view(), name='car_list'),
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('car/new/', CarCreateView.as_view(), name='car_create'),
    path('car/<int:pk>/edit/', CarUpdateView.as_view(), name='car_update'),
    path('car/<int:pk>/delete/', CarDeleteView.as_view(), name='car_delete'),
    path('car/<int:pk>/comment/', add_comment, name='add_comment'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    path('car/<int:pk>/reviews/', ReviewListView.as_view(), name='review_list'),
    path('car/<int:pk>/review/', ReviewCreateView.as_view(), name='review_create'),
    path('favorites/', FavoriteListView.as_view(), name='favorite_list'),
    path('car/<int:pk>/favorite/', toggle_favorite, name='toggle_favorite'),
    path('car/<int:pk>/like/', LikeToggleView.as_view(), name='toggle_like'),
    path('profile/', CustomerProfileDetailView.as_view(), name='customer_profile'),
    path('register/', register_view, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', LogoutView.as_view(), name='logout'), 

    # Rutas de la API
    path('api/cars/', CarListAPIView.as_view(), name='car-list-api'),
    path('api/cars/<int:car_id>/comments/', CarCommentsAPIView.as_view(), name='car-comments-api'),
    path('api/users/create/', UserCreateAPIView.as_view(), name='user-create-api'),
]
