from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Car, Comment, Review
from django.views.generic import CreateView

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

class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.car = get_object_or_404(Car, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('car_detail', kwargs={'pk': self.object.car.pk})
