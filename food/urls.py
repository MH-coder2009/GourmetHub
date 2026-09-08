from django.urls import path
from . import views

app_name = "food"

urlpatterns = [
    path("", views.IndexClassView.as_view(), name="index"),
    path("<int:pk>/", views.DetailsClassView.as_view(), name="details"),
    path("add/", views.CreateItemClassView.as_view(), name="create"),
    path("update/<int:pk>/", views.UpdateItemClassView.as_view(), name="update_item"),
    path("delete/<int:id>/", views.delete_item, name="delete_item"),
]
