from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CustomUserCreation
from django.contrib.auth import authenticate, login, logout


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
