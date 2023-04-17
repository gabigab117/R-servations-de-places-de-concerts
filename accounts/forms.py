from .models import Shopper
from django.contrib.auth.forms import UserCreationForm
from django import forms


# création d'un compte
class CustomUserCreation(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Shopper
        fields = ('email', 'genre', 'last_name', 'first_name', 'tel')


# formulaire pour le profil , ModelForm car relié à un modèle
class ProfilForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Shopper
        fields = ["email", "password", "genre", "last_name", "first_name", "tel"]
