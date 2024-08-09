from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User  # Importa el modelo User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from .models import Car, Comment, Review, Favorite
from .forms import CarForm, CommentForm, ReviewForm, CustomRegistrationForm

# Car views
class CarListView(ListView):
    model = Car
    template_name = 'car_list.html'

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'

class CarCreateView(LoginRequiredMixin, CreateView):
    model = Car
    form_class = CarForm
    template_name = 'car_form.html'
    success_url = reverse_lazy('car_list')

class CarUpdateView(LoginRequiredMixin, UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'car_form.html'
    success_url = reverse_lazy('car_list')

class CarDeleteView(LoginRequiredMixin, DeleteView):
    model = Car
    template_name = 'car_confirm_delete.html'
    success_url = reverse_lazy('car_list')

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
    success_url = reverse_lazy('car_list')

# Review views
class ReviewListView(ListView):
    model = Review
    template_name = 'review_list.html'

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review_form.html'
    success_url = reverse_lazy('car_list')

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
    model = User  # Usa el modelo User en lugar de CustomUser
    template_name = 'customer_profile.html'

# Registration view
def register_view(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('car_list')
    else:
        form = CustomRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
