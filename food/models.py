from django.db import models

# Create your models here.


class Item(models.Model):

    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=250)
    item_desc = models.CharField(max_length=850)
    item_price = models.IntegerField()
