from django.shortcuts import render, redirect, get_object_or_404
from .forms import ItemForm
from .models import Item


def index(request):
    items = Item.objects.all()
    context = {"items": items}
    return render(request, "food/index.html", context)


def details(request, id):
    item = get_object_or_404(Item, id=id)
    context = {"item": item}
    return render(request, "food/details.html", context)


def create_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("food:index")
    else:
        form = ItemForm()

    context = {"form": form}
    return render(request, "food/item-form.html", context)


def update_item(request, id):
    item = get_object_or_404(Item, id=id)

    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("food:index")
    else:
        form = ItemForm(instance=item)

    context = {"form": form, "item": item}
    return render(request, "food/item-form.html", context)
