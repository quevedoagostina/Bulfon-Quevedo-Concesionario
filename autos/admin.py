# autos/admin.py

from django.contrib import admin
from .models import Brand, CarModel, Category, Car, Comment

admin.site.register(Brand)
admin.site.register(CarModel)
admin.site.register(Category)
admin.site.register(Car)
admin.site.register(Comment)
