from django.contrib import admin
from .forms import StockCreateForm 

# Register your models here.
from .models import Stock


class StockCreateAdmin(admin.ModelAdmin):
    list_display = ['item_code','item_name', 'category', 'quantity']
    form = StockCreateForm
    list_filter = ['category']
    search_fields = ['category', 'item_name']
    


admin.site.register(Stock, StockCreateAdmin)
