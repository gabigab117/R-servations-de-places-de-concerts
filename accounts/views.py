from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import CustomUserCreation, ProfilForm, UserPasswordChangeForm, UserSetPasswordForm
from django.contrib.auth import authenticate, login, logout
from django.forms import model_to_dict
from .models import Shopper, ShippingAddress
from verify_email.email_handler import send_verification_email


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreation(request.POST)
        if form.is_valid():
            inactive_user = send_verification_email(request, form)
            # form.save(), non utilisé car inactive_user à la place

            return redirect('index')

    else:

        form = CustomUserCreation()

    return render(request, "accounts/signup.html", context={"form": form})


def login_user(request):
    context = {}
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user: Shopper = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect("index")

        else:
            context["error"] = "email ou mot de passe invalide."

    return render(request, "accounts/login.html", context=context)


def logout_user(request):
    logout(request)
    return redirect('index')


@login_required()
def profil(request):
    context = {}
    # dans le initial je vais passer en dictionnaire mon instance user
    # authenticate pour vérifier si l'email est ok et mdp
    if request.method == "POST":
        user_ok = authenticate(email=request.POST["email"], password=request.POST["password"])
        if user_ok:
            user: Shopper = request.user
            user.genre = request.POST["genre"]
            user.last_name = request.POST["last_name"]
            user.first_name = request.POST["first_name"]
            user.tel = request.POST["tel"]
            user.save()
            return redirect("account:profil")
        else:
            context['error'] = "Email ou Mdp invalide"

    context['form'] = ProfilForm(initial=model_to_dict(request.user, exclude="password"))

    # j'évite le request.user.shippingaddress_set.all(), car je pars du champ pour chercher le modèle
    context['addresses'] = request.user.addresses.all()

    return render(request, 'accounts/profil.html', context=context)


@login_required()
def set_address_default(request, pk):
    user = request.user
    user_addresses: ShippingAddress = user.addresses.all()

    '''
    Au lieu de boucler j'aurais pu faire:
    user_addresses.update(default=False)
    Il aurait été mieux de le faire dans mon modèle méthode set_default()
    voir commentaire dans la méthode set_default()
    '''
    for user_addresse in user_addresses:
        user_addresse.default = False
        user_addresse.save()

    user_addresse_default = user.addresses.get(pk=pk)
    user_addresse_default.default = True
    user_addresse_default.set_default()
    user_addresse_default.save()

    return redirect('account:profil')


def delete_address(request, pk):
    user: Shopper = request.user
    address: ShippingAddress = user.addresses.get(pk=pk)
    address.delete()
    return redirect('account:profil')


class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name = "accounts/password_change.html"
    success_url = reverse_lazy("index")


class UserPasswordResetView(PasswordResetView):
    email_template_name = "accounts/password_reset_email.html"
    template_name = "accounts/password_reset_form.html"
    success_url = reverse_lazy("account:password-reset-done")


class UserPasswordResetDone(PasswordResetDoneView):
    template_name = "accounts/password_reset_done.html"


class UserPasswordResetConfirm(PasswordResetConfirmView):
    form_class = UserSetPasswordForm
    success_url = reverse_lazy("account:password-reset-complete")
    template_name = "accounts/password_reset_confirm.html"


class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "accounts/password_reset_complete.html"
