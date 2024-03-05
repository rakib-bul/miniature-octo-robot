from django.db import models

class Stock(models.Model):
    # Category of the stock item (e.g., Electronics, Clothing)
    category = models.CharField(max_length=50, blank=True, null=True)

    # Name of the stock item
    item_name = models.CharField(max_length=50, blank=True, null=True)

    item_code = models.CharField(max_length=50, blank=True, null=True)

    UOM = models.CharField(max_length=50, blank=True, null=True)

    # Current quantity of the stock item
    quantity = models.IntegerField(default=0, blank=True, null=True)

    # Quantity received for the stock item
    received_quantity = models.IntegerField(default=0, blank=True, null=True)

    # Person responsible for receiving the stock
    receive_by = models.CharField(max_length=50, blank=True, null=True)

    # Quantity issued for the stock item
    issue_quantity = models.IntegerField(default='0', blank=True, null=True)

    # Person responsible for issuing the stock
    issue_by = models.CharField(max_length=50, blank=True, null=True)

    # Person or entity to whom the stock is issued
    issue_to = models.CharField(max_length=50, blank=True, null=True)

    # Phone number associated with the stock item
    phone_number = models.CharField(max_length=50, blank=True, null=True)

    # Person who created the stock record
    created_by = models.CharField(max_length=50, blank=True, null=True)

    # Reorder level for the stock item
    reorder_level = models.IntegerField(default=0, blank=True, null=True)

    # Timestamp of the last update to the stock record
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    # Flag indicating whether the stock item should be exported to CSV
    export_to_csv = models.BooleanField(default=False)


    def __str__(self) -> str:
        return self.item_name +' = '+ str(self.quantity) + 'pcs'