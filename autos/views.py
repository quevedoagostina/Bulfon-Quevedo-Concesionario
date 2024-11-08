from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from .models import Car, Comment, Review, Favorite
from .forms import CarForm, CommentForm, ReviewForm, CustomRegistrationForm
from django import forms
from django.http import HttpResponseForbidden
from rest_framework import generics
from .serializers import CarSerializer, CommentSerializer, UserSerializer
from rest_framework.permissions import IsAdminUser

# Define el StaffRequiredMixin
class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

# Car views
class CarListView(ListView):
    model = Car
    template_name = 'car_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

class CarDetailView(LoginRequiredMixin, DetailView):
    model = Car
    template_name = 'car_detail.html'

class CarCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = Car
    form_class = CarForm
    template_name = 'car_form.html'
    success_url = reverse_lazy('car_list')

class CarUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'car_form.html'
    success_url = reverse_lazy('car_list')

class CarDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Car
    template_name = 'car_confirm_delete.html'
    success_url = reverse_lazy('car_list')

class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Comment views
def add_comment(request, pk):
    car = Car.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.car = car
            comment.user = request.user
            comment.save()
            return redirect('car_detail', pk=car.pk)
    else:
        form = CommentForm()
    return render(request, 'add_comment.html', {'form': form})

class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'comment_confirm_delete.html'

    def get_success_url(self):
        comment = self.get_object()
        return reverse_lazy('car_detail', kwargs={'pk': comment.car.pk})

    def get_object(self, queryset=None):
        comment = super().get_object(queryset)
        if not comment.user == self.request.user and not self.request.user.is_staff:
            return HttpResponseForbidden()
        return comment

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment'] = self.get_object()
        return context

# Review views
class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.car = get_object_or_404(Car, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('car_detail', kwargs={'pk': self.object.car.pk})

# Favorite views
class FavoriteListView(LoginRequiredMixin, ListView):
    model = Favorite
    template_name = 'favorite_list.html'

def toggle_favorite(request, pk):
    car = Car.objects.get(pk=pk)
    favorite, created = Favorite.objects.get_or_create(car=car, user=request.user)
    if not created:
        favorite.delete()
    return redirect('car_detail', pk=pk)

# Like toggle view
class LikeToggleView(LoginRequiredMixin, View):
    def post(self, request, pk):
        car = Car.objects.get(pk=pk)
        if car.likes.filter(id=request.user.id).exists():
            car.likes.remove(request.user)
        else:
            car.likes.add(request.user)
        return redirect('car_detail', pk=pk)

# Customer profile view
class CustomerProfileDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'customer_profile.html'

# Registration view
def register_view(request):
    error = None
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                user.set_password(form.cleaned_data['password1']) 
                user.save()
                login(request, user)
                return redirect('car_list')
            except Exception as e:
                error = str(e)  
        else:
            error = form.errors.as_text()  
    else:
        form = CustomRegistrationForm()
    return render(request, 'registration/register.html', {'form': form, 'error': error})

def custom_login_view(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username and password:
            print("Attempting to authenticate:", username)  
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print("Authentication successful")  
                return redirect('car_list')
            else:
                error = 'Invalid username or password'
                print("Authentication failed")  
        else:
            error = 'Please provide both username and password'
    
    return render(request, 'registration/login.html', {'error': error})
