from django.urls import path
from .views import signup, login_user, logout_user, profil, set_address_default


app_name = "account"
urlpatterns = [
    path("signup/", signup, name="signup"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("profil/", profil, name="profil"),
    path("set-address-default/<int:pk>", set_address_default, name="address-default"),
]
