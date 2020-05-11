from django.contrib.auth.forms import UserCreationForm
from .models import XxUser

class RegForm(UserCreationForm):
    class Meta:
        model = XxUser
        fields = ('username', 'password1', 'password2', 'email')