from django.views.generic import (
    DeleteView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
)
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

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)


class UpdateItemClassView(LoginRequiredMixin, UpdateView):
    model = Item
    form_class = ItemForm
    template_name_suffix = "_update_form.html"
    success_url = reverse_lazy("food:index")
    login_url = "users:login"


class DeleteClassView(LoginRequiredMixin, DeleteView):
    model = Item
    success_url = reverse_lazy("food:index")
    login_url = "users:login"
