# autos/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Car, Comment

class CarListView(ListView):
    model = Car
    template_name = 'car_list.html'
    context_object_name = 'cars'

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'
    context_object_name = 'car'

class CarCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Car
    fields = ['model', 'category', 'year', 'price', 'image', 'description']
    template_name = 'car_form.html'
    success_url = reverse_lazy('car_list')

    def test_func(self):
        return self.request.user.is_staff

class CarUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Car
    fields = ['model', 'category', 'year', 'price', 'image', 'description']
    template_name = 'car_form.html'
    success_url = reverse_lazy('car_list')

    def test_func(self):
        return self.request.user.is_staff

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    success_url = reverse_lazy('car_list')

    def test_func(self):
        comment = self.get_object()
        return self.request.user.is_staff or self.request.user == comment.user

@login_required
def add_comment(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == "POST":
        content = request.POST.get('content')
        Comment.objects.create(car=car, user=request.user, content=content)
        return redirect('car_detail', pk=car.pk)
    return render(request, 'add_comment.html', {'car': car})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('car_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('car_list')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})
