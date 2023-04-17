from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CustomUserCreation, ProfilForm
from django.contrib.auth import authenticate, login, logout
from django.forms import model_to_dict
from .models import Shopper, ShippingAddress


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreation(request.POST)
        if form.is_valid():
            form.save()
            # user = authenticate(username=request.POST.get("email"), password=request.POST.get("password1"))
            # login(request, user)
            return redirect('index')

    else:

        form = CustomUserCreation()

    return render(request, "accounts/signup.html", context={"form": form})


def login_user(request):
    context = {}
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("index")

        else:
            context["error"] = "email ou mot de passe invalide."

    return render(request, "accounts/login.html", context=context)


def logout_user(request):
    logout(request)
    return redirect('index')


@login_required(login_url='account:login')
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


@login_required(login_url='account:login')
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
