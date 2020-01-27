from django.urls import path
from tracker import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('billing_detail/', views.BillingDetailDetail.as_view()),
    path('billing_detail/<int:pk>/', views.BillingDetailList.as_view()),
    path('customer_detail/', views.CustomerDetailList.as_view()),
    path('customer_detail/<int:pk>/', views.CustomerDetailDetail.as_view()),
    path('transport/', views.TransportList.as_view()),
    path('transport/<int:transport_id>', views.TransportDetail.as_view()),
    path('shipment_item/', views.ShipmentItemList.as_view()),
    path('shipment_item/<int:order_id>', views.ShipmentItemDetail.as_view()),
    path('shipment/', views.ShipmentList.as_view()),
    path('shipment/<int:shipment_id>', views.ShipmentDetail.as_view())
]