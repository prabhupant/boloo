from django.db import models

class ShipmentItem(models.Model):

    class Meta:
        db_table = 'shipment_item'

    order_id = models.CharField(primary_key=True, max_length=10)
    order_item_id = models.CharField(max_length=10)
    order_date = models.DateTimeField()
    last_delivery_date = models.DateTimeField()
    ean = models.CharField(max_length=15)
    title = models.CharField(max_length=128)
    quantity = models.IntegerField()
    offer_price = models.DecimalField(max_digits=4, decimal_places=2)
    offer_condition = models.CharField(max_length=10)
    fulfilment_method = models.CharField(max_length=10)


    def __str__(self):
        return "Shipment Item ID - {}".format(self.order_id)