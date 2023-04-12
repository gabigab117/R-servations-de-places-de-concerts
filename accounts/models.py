from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
import iso3166

'''
The prototype of create_user() should accept the username field, plus all required fields as arguments. For example, 
if your user model uses email as the username field, and has date_of_birth as a required field
'''


class CustomManager(BaseUserManager):
    def create_user(self, email, password, first_name, last_name, **kwargs):
        if not email:
            raise ValueError("Veuillez entrer un email svp")
        user = self.model(email=self.normalize_email(email), first_name=first_name, last_name=last_name, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, first_name, last_name, **kwargs):
        kwargs["is_staff"] = True
        kwargs["is_superuser"] = True
        kwargs["is_active"] = True
        return self.create_user(email=email, password=password, first_name=first_name, last_name=last_name, **kwargs)


class Shopper(AbstractUser):
    # I don't want username
    username = None
    email = models.EmailField(unique=True, max_length=300)
    genre = models.CharField(max_length=10, choices=[("nr", "Non renseigné"), ("mme", "Madame"), ("mr", "Monsieur")])
    first_name = models.CharField(max_length=300, verbose_name="Prénom")
    last_name = models.CharField(max_length=300, verbose_name="Nom")
    tel = models.CharField(blank=True, max_length=10, verbose_name="Téléphone")
    stripe_id = models.CharField(max_length=200, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]
    objects = CustomManager()


class ShippingAddress(models.Model):
    user: Shopper = models.ForeignKey(Shopper, on_delete=models.CASCADE, verbose_name="utilisateur")
    name = models.CharField(max_length=200, verbose_name="nom de l'adresse")
    address_1 = models.CharField(max_length=1024, help_text="Voirie, numéro de rue", verbose_name="Adresse 1")
    address_2 = models.CharField(max_length=1024, help_text="Bât, étage, lieu-dit", verbose_name="Adresse 2", blank=True)
    city = models.CharField(max_length=1024, verbose_name="Commune")
    zip_code = models.CharField(max_length=32, verbose_name="Code Postal")
    country = models.CharField(max_length=2, choices=[(c.alpha2.lower(), c.name) for c in iso3166.countries])
    default = models.BooleanField(default=False)
