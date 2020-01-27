from rest_framework import serializers
from tracker.models import ShipmentItemMapper

class ShipmentItemMapperSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShipmentItemMapper
        fields = [
            'shipment_id',
            'order_id'
        ]