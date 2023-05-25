from django.urls import path
from delivery.views import Dashboard, OrderDetails
from shop.views import Checkout

urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('orders/<int:pk>/', OrderDetails.as_view(), name='order_details'),
    path('checkout/<int:pk>', Checkout.as_view(), name='checkout'),

]