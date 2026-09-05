from django.urls import path
from . import views

app_name = "food"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id>/", views.details, name="details"),
    path("add/", views.create_item, name="create"),
    path("update/<int:id>/", views.update_item, name="update_item"),
]
