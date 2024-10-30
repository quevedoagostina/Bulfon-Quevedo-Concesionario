from django.contrib import admin
from django.urls import path, include
from autos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.CarListView.as_view(), name='car_list'),
    path('car/<int:pk>/', views.CarDetailView.as_view(), name='car_detail'),
    path('car/<int:pk>/comment/', views.add_comment, name='add_comment'),
    path('car/comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
    path('car/<int:pk>/review/', views.ReviewCreateView.as_view(), name='review_create'),
    path('register/', views.register_view, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/', include('autos.urls')),  # Incluye las rutas de la API aquí
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
