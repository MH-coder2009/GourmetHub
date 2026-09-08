from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView
from .forms import ItemForm
from .models import Item


class IndexClassView(LoginRequiredMixin, ListView):
    model = Item
    template_name = "food/index.html"
    context_object_name = "items"


class DetailsClassView(LoginRequiredMixin, DetailView):
    model = Item
    template_name = "food/details.html"
    context_object_name = "item"


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
