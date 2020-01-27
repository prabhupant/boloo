from tracker.models import Shipment
from tracker.serializers import ShipmentSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ShipmentList(APIView):
    """
    List all shipment, or create a new shipment
    """

    def get(self, request, format=None):
        shipments = Shipment.objects.all()
        serializer = ShipmentSerializer(shipments, many=True)
        return Response(serializer.data)

    
    def post(self, request, format=None):
        serializer = ShipmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

    
class ShipmentDetail(APIView):
    """
    Retrieve, update or delete a shipment instance.
    """
    
    def get_object(self, shipment_id):
        try:
            return Shipment.objects.get(shipment_id=shipment_id)
        except Shipment.DoesNotExist:
            raise Http404


    def get(self, request, shipment_id, format=None):
        shipment = self.get_object(shipment_id)
        serializer = ShipmentSerializer(shipment)
        return Response(serializer.data)


    def put(self, request, shipment_id, format=None):
        shipment = self.get_object(shipment_id)
        serializer = ShipmentSerializer(shipment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, shipment_id, format=None):
        shipment = self.get_object(shipment_id)
        shipment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)