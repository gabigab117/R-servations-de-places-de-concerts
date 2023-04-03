from .models import Shopper
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreation(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Shopper
        fields = ('email', 'genre', 'last_name', 'first_name', 'tel')
