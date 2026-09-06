from django.shortcuts import render, redirect  # ← اینجا redirect رو import کن
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        email = request.POST.get("email")

        # ولیدیشن ایمیل
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
            messages.success(
                request, "Account created successfully! You can now login."
            )
            return redirect("food:index")  # ← اینجا redirect (بدون s)
        else:
            context = {"form": form, "email_value": email}
            return render(request, "users/register.html", context)

    else:
        form = UserCreationForm()

    context = {"form": form}
    return render(request, "users/register.html", context)
