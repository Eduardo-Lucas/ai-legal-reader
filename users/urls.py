from django.urls import path
from .views import register_view, EmailLoginView, EmailLogoutView

urlpatterns = [
    path("login/", EmailLoginView.as_view(), name="login"),
    path("logout/", EmailLogoutView.as_view(), name="logout"),
    path("register/", register_view, name="register"),
]
