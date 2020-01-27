from django.db import models


class ShipmentItemMapper(models.Model):

    class Meta:
        db_table = 'shipment_item_mapper'

    shipment_id = models.IntegerField()
    order_id = models.CharField(max_length=10)