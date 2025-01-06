from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        fields = ['username', 'email', 'age']
        model = CustomUser


class CustomUserChangeForm(UserChangeForm):
    
    class Meta(UserChangeForm):
        fields = ['username', 'email', 'age']
        model = CustomUser