from django import forms
from store.models import Order


# rappel : choices = une liste de tuples
class OrderForm(forms.ModelForm):
    # je modifie le widget utilisé
    quantity = forms.ChoiceField(choices=[(i, i) for i in range(1, 11)])

    class Meta:
        model = Order
        fields = ["quantity"]
