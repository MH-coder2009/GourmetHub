from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .forms import ItemForm
from .models import Item


@login_required
def index(request):
    items = Item.objects.all()
    context = {"items": items}
    return render(request, "food/index.html", context)


class IndexClassView(ListView):
    model = Item
    template_name = "food/index.html"
    context_object_name = "items"


def details(request, id):
    item = get_object_or_404(Item, id=id)
    context = {"item": item}
    return render(request, "food/details.html", context)


@login_required
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


@login_required
def update_item(request, id):
    item = get_object_or_404(Item, id=id)

    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("food:index")
    else:
        form = ItemForm(instance=item)

    context = {"form": form}
    return render(request, "food/item-form.html", context)


@login_required
def delete_item(request, id):
    item = get_object_or_404(Item, id=id)

    if request.method == "POST":
        item.delete()
        return redirect("food:index")

    context = {"item": item}
    return render(request, "food/item-delete.html", context)
