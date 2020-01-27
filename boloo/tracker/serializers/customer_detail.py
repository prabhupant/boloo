from rest_framework import serializers
from tracker.models import CustomerDetail

class CustomerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDetail
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