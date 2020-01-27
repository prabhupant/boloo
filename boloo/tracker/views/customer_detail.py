from tracker.models import CustomerDetail
from tracker.serializers import CustomerDetailSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CustomerDetailList(APIView):

    def get(self, request, format=None):
        customer_detail = CustomerDetail.objects.all()
        serializer = CustomerDetailSerializer(customer_detail, many=True)
        return Response(serializer.data)

    
    def post(self, request, format=None):
        serializer = CustomerDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

    
class CustomerDetailDetail(APIView):
    
    def get_object(self, pk):
        try:
            return CustomerDetail.objects.get(pk=pk)
        except CustomerDetail.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        customer_detail = self.get_object(pk)
        serializer = CustomerDetailSerializer(customer_detail)
        return Response(serializer.data)


    def put(self, request, pk, format=None):
        customer_detail = self.get_object(pk)
        serializer = CustomerDetailSerializer(customer_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, customer_detail, format=None):
        customer_detail = self.get_object(pk)
        customer_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)