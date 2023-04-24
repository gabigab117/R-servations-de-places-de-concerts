from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
import iso3166
import stripe
from project.settings import STRIPE_APIKEY

stripe.api_key = STRIPE_APIKEY

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


# à savoir que j'ai des \n à chaque saut de ligne
ADDRESS_FORMAT = """
{name}
{address_1}
{address_2}
{zip_code} - {city}
{country}
"""


class ShippingAddress(models.Model):
    # related_name permet d'éviter le _set entre autre
    user: Shopper = models.ForeignKey(Shopper, on_delete=models.CASCADE, verbose_name="utilisateur",
                                      related_name="addresses")
    name = models.CharField(max_length=200, verbose_name="nom de l'adresse")
    address_1 = models.CharField(max_length=1024, help_text="Voirie, numéro de rue", verbose_name="Adresse 1")
    address_2 = models.CharField(max_length=1024, help_text="Bât, étage, lieu-dit", verbose_name="Adresse 2",
                                 blank=True)
    city = models.CharField(max_length=1024, verbose_name="Commune")
    zip_code = models.CharField(max_length=32, verbose_name="Code Postal")
    country = models.CharField(max_length=2, choices=[(c.alpha2.lower(), c.name) for c in iso3166.countries])
    default = models.BooleanField(default=False)

    def __str__(self):
        # une copie pour ne pas modifier les attributs de notre instance
        data = self.__dict__.copy()
        # mettre à jour country
        data.update(country=self.get_country_display())
        # on a pas de retour à la ligne car pas interprété par le HTML. Donc mettre le filtre linebreaks
        # strip enlève les éléments au début et à la fin
        return ADDRESS_FORMAT.format(**data).strip("\n")

    def set_default(self):
        # https://stripe.com/docs/api/customers/update
        # vérifier si l'utilisateur a un stripe ID
        if not self.user.stripe_id:
            raise ValueError(f"{self.user.email} n'a pas de stripe ID")
        '''
        Ce que je fais dans la vue set_adresse_default, j'aurais dû le faire ici
        self.user.addresses.update(default=False)
        self.default = True
        self.save()
        '''

        stripe.Customer.modify(
            self.user.stripe_id,
            shipping={
                "address": {
                    "city": self.city,
                    "country": self.country,
                    "line1": self.address_1,
                    "line2": self.address_2,
                    "postal_code": self.zip_code
                },
                "name": self.name
            },
            # j'ai deux dictionnaires identiques dans chaque paramètre. Je pourrais attribuer à une var.
            address={
                "city": self.city,
                "country": self.country,
                "line1": self.address_1,
                "line2": self.address_2,
                "postal_code": self.zip_code
            }
        )
