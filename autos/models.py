from django.db import models
from django.contrib.auth.models import User

class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class CarModel(models.Model):
    name = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.brand.name} {self.name}"

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Car(models.Model):
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='cars/')
    description = models.TextField()

    def __str__(self):
        return f"{self.model.name} - {self.year}"

class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.car}"

class Favorite(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} favorited {self.car}"

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        if self.comment:
            return f"{self.user.username} liked comment {self.comment}"
        return f"{self.user.username} liked car {self.car}"

class CarView(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} viewed {self.car}"

# Optional additional models

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Order by {self.user.username} for {self.car} on {self.order_date}"

class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return f"Profile of {self.user.username}"

class Review(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)  
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    title = models.CharField(max_length=255) 
    content = models.TextField()  
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)]) 
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return f"Review by {self.user.username} for {self.car} with Rating: {self.rating}"

    class Meta:
        unique_together = ('user', 'car')  
