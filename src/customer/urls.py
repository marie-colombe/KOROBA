from django.urls import path, include
from rest_framework import routers

from customer.viewsets.orderItem_viewset import OrderItemViewSet
from customer.viewsets.order_viewset import OrderViewSet
from customer.viewsets.customer_viewset import CustomerViewSet
from customer.viewsets.cart_viewset import CartViewSet
from customer.viewsets.cartItem_viewset import CartItemViewSet

router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet)
# router.register(r'carts', CartViewSet)
# router.register(r'carts item', CartItemViewSet)
router.register(r'cart', CartViewSet, basename='cart')
router.register(r'cart-items', CartItemViewSet, basename='cartitem')
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'order-items', OrderItemViewSet, basename='orderitem')

urlpatterns = [
   path('', include(router.urls)), 
]