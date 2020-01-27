from rest_framework import serializers
from tracker.models import BillingDetail

class BillingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingDetail
        fields = [
            'salutation_code',
            'first_name',
            'surname',
            'street_name',
            'house_number',
            'zipcode',
            'city',
            'country_code',
            'email'
        ]