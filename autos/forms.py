from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Car, Comment, Review

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['model', 'category', 'year', 'price', 'image', 'description']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'content', 'rating']

class CustomLoginForm(AuthenticationForm):
    # Add custom fields or configurations if necessary
    pass

class CustomRegistrationForm(UserCreationForm):
    # Add custom fields or configurations if necessary
    pass
