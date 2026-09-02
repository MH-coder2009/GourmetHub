from django.db import models

# Create your models here.


class Item(models.Model):

    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=250)
    item_desc = models.CharField(max_length=850)
    item_price = models.IntegerField()
    item_image = models.CharField(
        max_length=500,
        default="https://tse2.mm.bing.net/th/id/OIP.7OYh9Zt5JGrlaCVgiRz17AHaE8?r=0&rs=1&pid=ImgDetMain&o=7&rm=3",
    )
