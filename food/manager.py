from django.db import models


class ItemManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

    def deleted(self):
        return super().get_queryset().filter(is_deleted=True)

    def all_with_deleted(self):
        return super().get_queryset()

    def cheap_item(self):
        return self.filter(item_price__lt=2)

    def expensive_item(self):
        return self.filter(item_price__gt=2)

    def search(self, keyword):
        return self.filter(item_name__icontains=keyword)
