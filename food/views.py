from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.core.paginator import Paginator

from .models import Item
from .forms import ItemForm


from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Item


class IndexClassView(LoginRequiredMixin, ListView):
    model = Item
    template_name = "food/index.html"
    context_object_name = "items"
    paginate_by = 5
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
    template_name = "food/item_update_form.html"
    success_url = reverse_lazy("food:index")
    login_url = "users:login"


class DeleteItemClassView(LoginRequiredMixin, DeleteView):
    model = Item
    template_name = "food/item_delete.html"
    success_url = reverse_lazy("food:index")
    login_url = "users:login"

    def form_valid(self, form):

        self.object = self.get_object()

        self.object.delete()

        return HttpResponseRedirect(self.get_success_url())
