from django.urls import path
from . import views

app_name = "food"

urlpatterns = [
    path("", views.IndexClassView.as_view(), name="index"),
    path("<int:pk>/", views.DetailsClassView.as_view(), name="details"),
    path("add/", views.create_item, name="create"),
    path("update/<int:id>/", views.update_item, name="update_item"),
    path("delete/<int:id>/", views.delete_item, name="delete_item"),
]
