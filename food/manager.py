from django.db import models


class ItemManager(models.Manager):
    def cheap_item(self):
        return self.filter(item_price__lt=6)

    def expensive_item(self):
        return self.filter(item_price__gt=6)

    def search(self, keyword):
        return self.filter(item_name__icontains=keyword)
