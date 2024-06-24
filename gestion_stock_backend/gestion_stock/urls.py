from django.urls import path
from .views import ProductListCreate, StockListCreate, OrderItemListCreate, OrderListCreate

urlpatterns = [
    path('products/', ProductListCreate.as_view(), name='product-list-create'),
    path('stock/', StockListCreate.as_view(), name='stock-list-create'),
    path('order-items/', OrderItemListCreate.as_view(), name='orderitem-list-create'),
    path('orders/', OrderListCreate.as_view(), name='order-list-create'),
]
