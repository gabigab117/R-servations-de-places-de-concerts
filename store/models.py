from django.db import models
from django.template.defaultfilters import slugify
from iso3166 import countries
from project.settings import AUTH_USER_MODEL


class Artist(models.Model):
    name = models.CharField(max_length=300, unique=True, verbose_name="Artiste")
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)


class Town(models.Model):
    name = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)


class Concert(models.Model):
    choices = [
        ("hm", "Hard Rock / Metal"),
        ("jz", "Jazz"),
        ("rp", "Rap"),
        ("cl", "Classique"),
        ("el", "Electro"),
        ("var", "Variété")
    ]
    name = models.ForeignKey(Artist, on_delete=models.CASCADE, verbose_name="Artiste")
    slug = models.SlugField(unique=True, blank=True)
    type = models.CharField(max_length=100, choices=choices, verbose_name="Genre")
    places_count = models.IntegerField(verbose_name="Nombre de places")
    place = models.CharField(max_length=300, verbose_name="Salle")
    city = models.ForeignKey(Town, verbose_name="Ville", on_delete=models.CASCADE)
    country = models.CharField(max_length=300, choices=[(c.alpha2.lower(), c.name) for c in countries],
                               verbose_name="Pays")
    date = models.DateTimeField(verbose_name="Date / heure")
    thumbnail = models.ImageField(upload_to="concerts")

    def __str__(self):

        return f"{self.name}, {self.city.name}"

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)


class Ticket(models.Model):
    # relation avec les concerts, plusieurs types de tickets...
    name = models.CharField(max_length=100, verbose_name="Ticket")
    concert_name = models.ForeignKey(Concert, on_delete=models.CASCADE, verbose_name="Artiste")

    def __str__(self):

        return f"{self.name}, {self.concert_name.name}"


class Order(models.Model):
    # c'est ce qui va être dans le panier
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    # un utilisateur peut avoir plusieurs "Order"
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):

        return f"{self.ticket.name}, {self.quantity}"


class Cart(models.Model):
    # un utilisateur ne peut avoir qu'un panier
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)


'''
voir pour un panier, et un order comme le tuto e-commerce ?
Penser au __str__ méthode, à admin.py pour utiliser les filtres, et ce qui sera éditable, méthode save...
Et slugifier !
Lorsque la commande est passée je veux retirer les qtés au nombre (place de concert)

on_delete : si je supprime l'artiste je supprime forcément le concert et donc le ticket
'''
