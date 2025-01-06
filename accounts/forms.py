from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        fields = UserCreationForm.Meta.fields + ("age",)
        model = CustomUser


class CustomUserChangeForm(UserChangeForm):
    
    class Meta(UserChangeForm):
        fields = UserChangeForm.Meta.fields
        model = CustomUser