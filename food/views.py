from tracemalloc import get_object_traceback

from django.http import JsonResponse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from food.serializers import Itemserializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .forms import ItemForm
from django.core.cache import cache
import logging
from django.http import JsonResponse
from .models import Item

logger = logging.getLogger(__name__)


@api_view(["GET", "POST"])
def get_list_api(request):
    if request.method == "GET":
        items = Item.objects.all()
        serializer = Itemserializers(items, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = Itemserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


@api_view(["GET", "PUT"])
def get_details_item(request, pk):
    if request.method == "GET":
        item = get_object_or_404(Item, pk=pk)
        serializer = Itemserializers(item)
        return Response(serializer.data)
    elif request.method == "PUT":
        item = get_object_or_404(Item, pk=pk)
        serializer = Itemserializers(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


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

logger = logging.getLogger(__name__)


class UpdateItemClassView(LoginRequiredMixin, UpdateView):
    model = Item
    form_class = ItemForm
    template_name_suffix = "_update_form.html"
    success_url = reverse_lazy("food:index")
    login_url = "users:login"

    def get(self, request, *args, **kwargs):

        item = self.get_object()
        logger.debug(f"Editing item: {item.item_name} (ID: {item.id})")
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):

        response = super().form_valid(form)
        logger.info(f"Item updated: {form.instance.item_name} by {self.request.user}")
        return response


# ===== DELETE =====
class DeleteItemClassView(LoginRequiredMixin, DeleteView):

    model = Item
    template_name = "food/item_delete.html"
    success_url = reverse_lazy("food:index")
    login_url = "users:login"

    def form_valid(self, form):
        response = super().form_valid(form)
        cache.clear()
        return response
