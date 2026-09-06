from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def register(request):
    form = UserCreationForm()
    return render(request, "users/register.html", {"form": form})
