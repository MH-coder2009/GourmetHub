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

    def clean(self):
        cleaned_data = super().clean()
        item_name = cleaned_data.get("item_name")
        item_desc = cleaned_data.get("item_desc")

        if item_name and item_desc and item_name.lower() in item_desc.lower():
            raise forms.ValidationError("they shouldnt be same")
        return cleaned_data
