from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone


class Item(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=250, db_index=True)
    item_desc = models.CharField(max_length=850)
    item_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00, db_index=True
    )
    item_image = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse("food:details", kwargs={"pk": self.pk})

    class Meta:
        indexes = [
            models.Index(
                fields=["item_name", "item_price"]
            ),  # ← item_name نه itme_name
        ]
