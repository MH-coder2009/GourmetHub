from django.contrib import admin
from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "item_name", "item_price", "is_deleted", "deleted_at")
    list_filter = ("is_deleted",)

    def get_queryset(self, request):
        return Item._base_manager.all()
