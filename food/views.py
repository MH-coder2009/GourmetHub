from django.http import HttpResponse
from django.shortcuts import render
from .models import Item


def index(request):
    items = Item.objects.all()
    context = {"items": items}
    return render(request, "food/index.html", context)


def details(request, id):
    item = Item.objects.get(id=id)
    context = {"item": item}
    return render(request, "food/detail.html", context)


def item(request):
    return HttpResponse("hello")
