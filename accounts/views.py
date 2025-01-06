from .models import CustomUser
from django.urls import reverse_lazy
from django.views.generic import CreateView


class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    model = CustomUser
    success_url = reverse_lazy('login')