from django.urls import path

from . import views

app_name = "food"

urlpatterns = [
    path("", views.index),
    path("username/", views.item),
    path("<int:id>/", views.details, name="details"),
]
