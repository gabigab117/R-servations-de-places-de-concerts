from django import forms
from django.shortcuts import redirect

from store.models import Order


# rappel : choices = une liste de tuples
class OrderForm(forms.ModelForm):
    # je modifie le widget utilisé
    # modifier la qté dans le panier :
    quantity = forms.IntegerField(max_value=100, min_value=1)
    # supprimer un article du panier :
    delete = forms.BooleanField(initial=False, required=False, label='supprimer')

    class Meta:
        model = Order
        fields = ["quantity", 'delete']

    # relier le delete avec save
    def save(self, *args, **kwargs):
        # récupérer les données de mon formulaire :
        # avec cleaned_data qui est un dictionnaire, données de mon formulaire après qu'il ait été validé
        if self.cleaned_data['delete']:
            # if self.cleaned_data['delete'] is True:
            return self.instance.delete()
        if self.cleaned_data['quantity'] > self.instance.ticket.stock:
            return None

        return super().save(*args, **kwargs)
