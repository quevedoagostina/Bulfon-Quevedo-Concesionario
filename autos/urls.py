from django.urls import path, include  # Asegúrate de que 'include' esté aquí
from .views import (
    CarListView, CarDetailView, CarCreateView, CarUpdateView, CarDeleteView,
    add_comment, CommentDeleteView, ReviewCreateView,  # Eliminado ReviewListView
    FavoriteListView, toggle_favorite, LikeToggleView, CustomerProfileDetailView,
    register_view
)
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomLoginForm
from autos import views as autos_views

urlpatterns = [
    # Car URLs
    path('', CarListView.as_view(), name='car_list'),
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('car/new/', CarCreateView.as_view(), name='car_create'),
    path('car/<int:pk>/edit/', CarUpdateView.as_view(), name='car_update'),
    path('car/<int:pk>/delete/', CarDeleteView.as_view(), name='car_delete'),

    # Comment URLs
    path('car/<int:pk>/comment/', add_comment, name='add_comment'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),

    # Review URLs
    # path('car/<int:pk>/reviews/', ReviewListView.as_view(), name='review_list'),  # Esta línea ha sido comentada/eliminada
    path('car/<int:pk>/review/', ReviewCreateView.as_view(), name='review_create'),

    # Favorite URLs
    path('favorites/', FavoriteListView.as_view(), name='favorite_list'),
    path('car/<int:pk>/favorite/', toggle_favorite, name='toggle_favorite'),

    # Like URLs
    path('car/<int:pk>/like/', LikeToggleView.as_view(), name='toggle_like'),

    # Customer Profile URL
    path('profile/', CustomerProfileDetailView.as_view(), name='customer_profile'),

    # Authentication URLs
    path('login/', LoginView.as_view(template_name='registration/login.html', authentication_form=CustomLoginForm), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
    path('register/', autos_views.register_view, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
]

# API Endpoints
from . import api_views

urlpatterns += [
    path('api/cars/', api_views.CarListAPIView.as_view(), name='api_car_list'),
    path('api/brands/', api_views.BrandListAPIView.as_view(), name='api_brand_list'),
    path('api/users/', api_views.UserListAPIView.as_view(), name='api_user_list'),
    path('api/car/<int:car_id>/comments/', api_views.CarCommentsAPIView.as_view(), name='api_car_comments'),
    path('api/create-customer/', api_views.CreateCustomerAPIView.as_view(), name='api_create_customer'),
]
