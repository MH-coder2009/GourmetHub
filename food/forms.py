from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["item_name", "item_desc", "item_price", "item_image"]
        widgets = {
            "item_desc": forms.Textarea(attrs={"rows": 4}),
        }

    def clean_item_price(self):
        price = self.cleaned_data.get("item_price")
        if price > 50:
            raise forms.ValidationError(
                "it is too expensive it should be less than $50"
            )
        return price
