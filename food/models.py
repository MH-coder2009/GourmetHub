from django.db import models


class Item(models.Model):
    item_name = models.CharField(max_length=250)
    item_desc = models.CharField(max_length=850)
    item_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    item_image = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.item_name
