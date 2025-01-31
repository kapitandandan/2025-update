from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'age', 'phone_number')

class CustomUserChangeForm(UserChangeForm):
    class meta:
        model = CustomUser
        fields = ('username', 'email', 'age', 'phone_number')