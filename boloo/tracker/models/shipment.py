from django.db import models
from tracker.models import ShipmentItem, Transport, CustomerDetail, BillingDetail

class Shipment(models.Model):

    class Meta:
        db_table = 'shipment'

    shipment_id = models.IntegerField(primary_key=True)
    shipment_date = models.DateTimeField()
    shipment_items_mapper = models.ForeignKey(ShipmentItem, on_delete=models.CASCADE)
    transport = models.ForeignKey(Transport, on_delete=models.CASCADE)
    customer_details = models.ForeignKey(CustomerDetail, on_delete=models.CASCADE)
    billing_details = models.ForeignKey(BillingDetail, on_delete=models.CASCADE)


    def __str__(self):
        return "Shipment ID - {}".format(self.shipment_id)