from django import forms
from .models import Stock

class StockCreateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['category','item_code', 'item_name', 'quantity','issue_by']