from django.urls import path
from .views import signup, login_user, logout_user, profil, set_address_default, delete_address, \
    UserPasswordChange, UserPasswordResetView, UserPasswordResetDone, UserPasswordResetConfirm, \
    UserPasswordResetCompleteView


app_name = "account"
urlpatterns = [
    path("signup/", signup, name="signup"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("profil/", profil, name="profil"),
    path("password-change/", UserPasswordChange.as_view(),
         name="password-change"),
    path("password-reset/", UserPasswordResetView.as_view(), name="password-reset"),
    path("password-reset-done/", UserPasswordResetDone.as_view(), name="password-reset-done"),
    path("password-reset-confirm/<str:uidb64>/<str:token>", UserPasswordResetConfirm.as_view(),
         name="password-reset-confirm"),
    path("password-reset-complete/", UserPasswordResetCompleteView.as_view(), name="password-reset-complete"),
    path("set-address-default/<int:pk>", set_address_default, name="address-default"),
    path("delete_address/<int:pk>/", delete_address, name="delete-address")
]
