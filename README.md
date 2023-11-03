# Premier projet après la formation Docstring (Mars 2023)

## Résumé

- Projet orienté eCommerce : vente de places de concert
- Gestion des utilisateurs avec inscription, récupération de mot de passe, gestion des adresses, gestion du profil
  utilisateur
- Chaque concert comporte plusieurs types de billets, avec un stock
- Si on essaye d'ajouter plus de billets qu'il n'y a de stock, on lève une erreur
- Intégration d'un système de paiement avec l'API Stripe
- Si le paiement aboutit, une méthode va soustraire la quantité achetée au stock, et le ticket aura un statut "commandé"
- Intégration d'une API Django Rest Framework (de manière très basique)

### Apprentissage

Manipuler les modèles, querysets. Intégration pour la première fois d'un début de front (vraiment un début... :) ) avec
Bootstrap.
Utilisation et mise en place d'une API DRF de manière très basique. Le but est d'avoir une première approche de DRF.
Utilisation de l'api de Stripe