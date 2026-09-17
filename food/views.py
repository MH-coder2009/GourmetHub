from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Item
from .forms import ItemForm
import logging

logger = logging.getLogger(__name__)


# ===== INDEX =====
class IndexClassView(LoginRequiredMixin, ListView):
    logger.info("feching")
    model = Item
    logger.debug(f"found {Item.objects.count()}")
    template_name = "food/index.html"
    context_object_name = "items"
    paginate_by = 5
    login_url = "users:login"


# ===== DETAILS =====
class DetailsClassView(LoginRequiredMixin, DetailView):
    model = Item
    template_name = "food/details.html"
    context_object_name = "item"
    login_url = "users:login"


# ===== CREATE =====
class CreateItemClassView(LoginRequiredMixin, CreateView):
    model = Item
    form_class = ItemForm
    template_name = "food/item-form.html"
    success_url = reverse_lazy("food:index")
    login_url = "users:login"

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)


# ===== UPDATE =====
class UpdateItemClassView(LoginRequiredMixin, UpdateView):
    model = Item
    form_class = ItemForm
    template_name_suffix = "_update_form.html"
    success_url = reverse_lazy("food:index")
    login_url = "users:login"


# ===== DELETE =====
class DeleteItemClassView(LoginRequiredMixin, DeleteView):
    model = Item
    template_name_suffix = "_delete.html"
    success_url = reverse_lazy("food:index")
    login_url = "users:login"
