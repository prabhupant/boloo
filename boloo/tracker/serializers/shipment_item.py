from rest_framework import serializers
from tracker.models import ShipmentItem

class ShipmentItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShipmentItem
        fields = [
            'order_id',
            'order_item_id',
            'order_date',
            'last_delivery_date',
            'ean',
            'title',
            'quantity',
            'offer_price',
            'offer_condition',
            'fulfilment_method'
        ]

        