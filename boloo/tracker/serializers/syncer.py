from rest_framework import serializers
import base64, requests
from tracker.models import *


class SyncerSerializer(serializers.Serializer):
    client_id = serializers.IntegerField(required=True, max_length=200)
    client_secret = serializers.CharField(required=True, max_length=200)


    def create_shipments(self, data, headers):
        shipment_ids = []
        for shipment in data['shipments']:
            shipment_ids.append(shipment['shipmentId'])

        shipment_details = []

        # Get the shipment details 
        url = 'https://api.bol.com/retailer/shipments/{}'
        for i in shipment_ids:
            shipment_items_ids = []
            r = requests.get(url=url.format(i), headers=headers)
            res = r.json()

            transport, created = Transport.objects.get_or_create(
                transport_id=res['transport']['transportId'],
                transport_code=res['transport']['transporterCode'],
                track_and_trace=res['transport']['transporterCode'],
            )

            customer_detail = CustomerDetail.objects.get_or_create(
                salutation_code=res['customerDetails']['salutation_code']
                first_name=res['customerDetails']['first_name']
                surname=res['customerDetails']['surname']
                street_name=res['customerDetails']['street_name']
                house_number=res['customerDetails']['house_number']
                zipcode=res['customerDetails']['zipcode']
                city=res['customerDetails']['city']
                country_code=res['customerDetails']['country_code']
                email=res['customerDetails']['email']
            )

            billing_detail = BillingDetail.objects.get_or_create(
                salutation_code=res['billingDetails']['salutation_code']
                first_name=res['billingDetails']['first_name']
                surname=res['billingDetails']['surname']
                street_name=res['billingDetails']['street_name']
                house_number=res['billingDetails']['house_number']
                zipcode=res['billingDetails']['zipcode']
                city=res['billingDetails']['city']
                country_code=res['billingDetails']['country_code']
                email=res['billingDetails']['email']
            )

            for j in res['shipmentItems']:
                item = ShipmentItem.objects.get_or_create(
                    order_id=j['orderItemId'],
                    order_item_id=j['orderId'],
                    order_date=j['orderDate'],
                    last_delivery_date=j['latestDeliveryDate'],
                    ean=j['ean'],
                    title=j['title'],
                    quantity=j['quantity'],
                    offer_price=j['offerPrice'],
                    offer_condition=j['offerCondition'],
                    fulfilment_method=j['fulfilmentMethod']
                )
                shipment_items_ids.append(item.order_id)

         
            for _id in shipment_items_ids:
                p = ShipmentItemMapper.objects.get_or_create(
                    shipment_id=i,
                    order_id=_id
                )

            shipment = Shipment.objects.get_or_create(
                shipment_id=i,
                shipment_date=res['shipmentDate'],
                transport=transport,
                customer_details=customer_detail,
                billing_details=billing_detail
            )

            

    def create(self, validated_data):
        s = client_id + ':' + client_secret
        b = base64.b64encode(s.encode())
        headers = {
            'Authorization': 'Basic ' + str(b),
            'Accept': 'application/json'
        }
        r = requests.post(url='https://login.bol.com/token?grant_type=client_credentials', headers=headers)
        token = r.json['access_token']
        url = 'https://api.bol.com/retailer/shipments?fulfilment-method=FBR'
        headers = {
            'Authorization': 'Bearer ' + token,
            'Accept': 'vnd.retailer.v3+json'
        }
        r = requests.get(url=url, headers=headers)
        res = r.json()
        create_shipments(res, headers)

        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance