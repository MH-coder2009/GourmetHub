from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from .forms import RegisterForm


@csrf_protect
@ensure_csrf_cookie
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        email = request.POST.get("email")

        email_error = None

        if not email:
            email_error = "Email is required."
        elif "@" not in email or "." not in email:
            email_error = "Please enter a valid email address."
        elif User.objects.filter(email=email).exists():
            email_error = "This email is already registered."
        else:
            try:
                validate_email(email)
            except ValidationError:
                email_error = "Please enter a valid email address."

        if email_error:
            messages.error(request, email_error)
            context = {"form": form, "email_error": email_error, "email_value": email}
            return render(request, "users/register.html", context)

        if form.is_valid():
            user = form.save(commit=False)
            user.email = email
            user.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Account created successfully! Welcome {username} 🎉"
            )
            return redirect("food:index")
        else:
            context = {"form": form, "email_value": email}
            return render(request, "users/register.html", context)

    else:
        form = RegisterForm()

    context = {"form": form}
    return render(request, "users/register.html", context)
