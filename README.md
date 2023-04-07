# Réservation de places de concerts
 projet django style e commerce

# créer une vue lorsque le panier est supprimé par une validation de paiement

Stripe <br>
Récupérer la clé API (clé secrète) dans l'onglet développeur. Et la mettre dans le .env<br>
Procéder à la session de paiement : <br>
dans le panier utilise un <form action="url" method post avec un boutton submit. Penser à créer l'url puis la vue.<br>
https://stripe.com/docs/payments/checkout <br>
https://stripe.com/docs/payments/accept-a-payment (tout est détaillé)<br>
locale="fr" pour trad en FR<br>
https://stripe.com/docs/api/checkout/sessions/create <br>
ajouter un champ ID stripe dans ce que l'on vend : 
