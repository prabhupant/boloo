from tracker.models import ShipmentItem
from tracker.serializers import ShipmentItemSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ShipmentItemList(APIView):

    def get(self, request, format=None):
        shipment_item = ShipmentItem.objects.all()
        serializer = ShipmentItemSerializer(shipment_item, many=True)
        return Response(serializer.data)

    
    def post(self, request, format=None):
        serializer = ShipmentItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

    
class ShipmentItemDetail(APIView):
    
    def get_object(self, order_id):
        try:
            return ShipmentItem.objects.get(order_id=order_id)
        except ShipmentItem.DoesNotExist:
            raise Http404


    def get(self, request, order_id, format=None):
        shipment_item = self.get_object(order_id)
        serializer = ShipmentItemSerializer(shipment_item)
        return Response(serializer.data)


    def put(self, request, order_id, format=None):
        shipment_item = self.get_object(order_id)
        serializer = ShipmentItemSerializer(shipment_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, order_id, format=None):
        shipment_item = self.get_object(order_id)
        shipment_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)