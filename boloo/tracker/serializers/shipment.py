from rest_framework import serializers
from tracker.models import Shipment

class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = [
            'shipment_id', 
            'shipment_date', 
            'shipment_items_mapper',
            'transport',
            'customer_details',
            'billing_details'
        ]

        