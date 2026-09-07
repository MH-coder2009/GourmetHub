from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "users"

urlpatterns = [
    path("register/", views.register, name="register"),
    # ===== LOGIN =====
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="users/login.html", redirect_authenticated_user=True
        ),
        name="login",
    ),
    # ===== LOGOUT =====
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.profile, name="profile"),
]
