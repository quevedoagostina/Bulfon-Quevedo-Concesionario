from django.contrib import admin
from django.urls import path, include
from autos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.CarListView.as_view(), name='car_list'),
    path('car/<int:pk>/', views.CarDetailView.as_view(), name='car_detail'),
    path('accounts/', include('django.contrib.auth.urls')),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
