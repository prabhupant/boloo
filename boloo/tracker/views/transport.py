from tracker.models import Transport
from tracker.serializers import TransportSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class TransportList(APIView):
    """
    List all shipment, or create a new shipment
    """

    def get(self, request, format=None):
        transport = Transport.objects.all()
        serializer = TransportSerializer(transport, many=True)
        return Response(serializer.data)

    
    def post(self, request, format=None):
        serializer = TransportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

    
class TransportDetail(APIView):
    """
    Retrieve, update or delete a transport instance.
    """
    
    def get_object(self, transport_id):
        try:
            return Transport.objects.get(transport_id=transport_id)
        except Transport.DoesNotExist:
            raise Http404


    def get(self, request, transport_id, format=None):
        transport = self.get_object(transport_id)
        serializer = TransportSerializer(transport)
        return Response(serializer.data)


    def put(self, request, transport_id, format=None):
        transport = self.get_object(transport_id)
        serializer = TransportSerializer(transport, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, transport_id, format=None):
        transport = self.get_object(transport_id)
        transport.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)