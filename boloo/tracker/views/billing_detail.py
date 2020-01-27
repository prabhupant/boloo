from tracker.models import BillingDetail
from tracker.serializers import BillingDetailSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class BillingDetailList(APIView):

    def get(self, request, format=None):
        billing_detail = BillingDetail.objects.all()
        serializer = BillingDetailSerializer(billing_detail, many=True)
        return Response(serializer.data)

    
    def post(self, request, format=None):
        serializer = BillingDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

    
class BillingDetailDetail(APIView):
    
    def get_object(self, pk):
        try:
            return BillingDetail.objects.get(pk=pk)
        except BillingDetail.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        billing_detail = self.get_object(pk)
        serializer = BillingDetailSerializer(billing_detail)
        return Response(serializer.data)


    def put(self, request, pk, format=None):
        billing_detail = self.get_object(pk)
        serializer = BillingDetailSerializer(billing_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, billing_detail, format=None):
        billing_detail = self.get_object(pk)
        billing_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)