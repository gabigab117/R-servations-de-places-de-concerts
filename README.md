Idée d'améliorations : <br>
filtres par types de concert etc...
<br>

# Réservation de places de concerts
 projet django style e commerce
<h1>API ! ! !</h1><br>
J'utilise Django rest frmw.<br>
Le router permet de gérer toutes mes opés CRUD.<br>
Obligatoire avec un ModelViewset.<br>
Avec mon ModelViwset il faut serializer_class et queryset ou def get_queryset<br>
ReadOnlyModelViewset si je veux être uniquement en lecture<br>
filtrer dans l'url dans le queryset : <br>
email = self.request.GET.get("email")<br>
        if email: modifier le queryset avec l'email


Stripe <br>
Récupérer la clé API (clé secrète) dans l'onglet développeur. Et la mettre dans le .env<br>
Procéder à la session de paiement : <br>
dans le panier utilise un <form action="url" method post avec un boutton submit. Penser à créer l'url puis la vue.<br>
https://stripe.com/docs/payments/checkout <br>
https://stripe.com/docs/payments/accept-a-payment (tout est détaillé)<br>
locale="fr" pour trad en FR<br>
https://stripe.com/docs/api/checkout/sessions/create <br>
ajouter un champ ID stripe dans ce que l'on vend. <br>
créer les produits sur stripe puis copier l'id.<br>

Il faut maintenant récupérer le panier dans ma vue.<br>
Puis le line_items supprimer la valeur attribuée pour remplacer par une variable line_items que l'on définit avant.<br>
dans line_items compréhension de liste avec mes produits. Pour voir ce que l'on peu <br>
mettre on peut aller voir dans la doc<br>
https://stripe.com/docs/api/financial_connections/sessions/object <br>
https://stripe.com/docs/api/checkout/sessions/line_items <br>
Puis je créer une vue de succès avec un return html.<br>
Il faut faire un reverse dans success_url mais il faut url absolue car je suis dans stripe<br>
request.build_absolute_uri <br>

Il faut ensuite créer un webhook et installer CLI avant<br>
https://stripe.com/docs/webhooks/signatures <br>
stripe listen --forward-to 127.0.0.1:8000/store/stripe-webhook/ <br>
dans ma vue webhook copier le code et définir un endpoint_secret <br>
puis faire le if event : https://stripe.com/docs/api/events <br>
Voir ce que j'ai fait et aussi la méthode set_default de ShippingAdress<br> <br>
--------<br>
Form Set Factory <br>
dans mon store je vais ajouter un forms.py<br>
dans ma vue cart on utilise le modelformset_factory(), on passe le modèle et le formulaire<br>
https://docs.djangoproject.com/fr/4.1/ref/forms/models/ <br>
On créer une classe puis une instance. On retourne au contexte<br>
<br>
<br>
Sécuriser l'accès aux api avec djangorestframework-simplejwt


