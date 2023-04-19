from django import forms
from store.models import Order


# rappel : choices = une liste de tuples
class OrderForm(forms.ModelForm):
    # je modifie le widget utilisé
    # modifier la qté dans le panier :
    quantity = forms.ChoiceField(choices=[(i, i) for i in range(1, 11)])
    # supprimer un article du panier :
    delete = forms.BooleanField(initial=False, required=False, label='supprimer')

    class Meta:
        model = Order
        fields = ["quantity"]

    # relier le delete avec save
    def save(self, *args, **kwargs):
        # récupérer les données de mon formulaire :
        # avec cleaned_data qui est un dictionnaire, données de mon formulaire après qu'il ait été validé
        if self.cleaned_data['delete']:
            # if self.cleaned_data['delete'] is True:
            return self.instance.delete()
        return super().save(*args, **kwargs)
