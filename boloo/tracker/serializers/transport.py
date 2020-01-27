from rest_framework import serializers
from tracker.models import Transport

class TransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        fields = [
            'transport_id',
            'transport_code',
            'track_and_trace'
        ]

        