from django.urls import path
from django.views.decorators.cache import cache_page
from . import views

from rest_framework.routers import DefaultRouter

app_name = "food"

router = DefaultRouter()
router.register(r"items", views.ItemViewSet, basename="item")

urlpatterns = [
    path("", cache_page(60 * 15)(views.IndexClassView.as_view()), name="index"),
    path(
        "<int:pk>/",
        cache_page(60 * 15)(views.DetailsClassView.as_view()),
        name="details",
    ),
    path("add/", views.CreateItemClassView.as_view(), name="create"),
    path("update/<int:pk>/", views.UpdateItemClassView.as_view(), name="update_item"),
    path("delete/<int:pk>/", views.DeleteItemClassView.as_view(), name="delete_item"),
    path("item-api/", views.ItemListCreateAPIView.as_view(), name="get_list_api"),
    path(
        "item-details/<int:pk>/",
        views.ItemRetrieveUpdateDestroyAPIView.as_view(),
        name="get_details_item",
    ),
]
