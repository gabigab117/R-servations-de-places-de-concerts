from .models import Shopper
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, SetPasswordForm
from django import forms


# création d'un compte
class CustomUserCreation(UserCreationForm):
    class Meta:
        model = Shopper
        fields = ('email', 'genre', 'last_name', 'first_name', 'tel')


# formulaire pour le profil , ModelForm car relié à un modèle
class ProfilForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Shopper
        fields = ("email", "password", "genre", "last_name", "first_name", "tel")


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput, label="Ancien mot de passe")
    new_password1 = forms.CharField(widget=forms.PasswordInput, label="Nouveau mot de passe", strip=False)
    new_password2 = forms.CharField(widget=forms.PasswordInput, label="Nouveau mot de passe (répéter)", strip=False)

    '''
    Inutile de déclarer une class Meta ?
    '''


class UserSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(), label="Nouveau mot de passe", strip=False)
    new_password2 = forms.CharField(widget=forms.PasswordInput(), label="Confirmation", strip=False)
    '''
    Inutile de déclarer une class Meta ?
    '''
