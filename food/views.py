from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Item
from .forms import ItemForm


class IndexClassView(LoginRequiredMixin, ListView):
    model = Item
    template_name = "food/index.html"
    context_object_name = "items"
    login_url = "users:login"


class DetailsClassView(LoginRequiredMixin, DetailView):
    model = Item
    template_name = "food/details.html"
    context_object_name = "item"
    login_url = "users:login"


class CreateItemClassView(LoginRequiredMixin, CreateView):
    model = Item
    form_class = ItemForm
    template_name = "food/item-form.html"
    success_url = reverse_lazy("food:index")
    login_url = "users:login"


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
