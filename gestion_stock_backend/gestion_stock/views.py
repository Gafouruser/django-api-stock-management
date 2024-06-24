"""
from rest_framework import generics
from .models import Product, Stock, Order, OrderItem
from .serializers import ProductSerializer, StockSerializer, OrderItemSerializer, OrderSerializer


class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class StockListCreate(generics.ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class OrderItemListCreate(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class OrderListCreate(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
"""


from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from .models import Product, Stock, Order, OrderItem
from .serializers import ProductSerializer, StockSerializer, OrderItemSerializer, OrderSerializer
from rest_framework.authtoken.serializers import AuthTokenSerializer


class ObtainAuthToken(APIView):
    authentication_classes = []
    permission_classes = []

    @staticmethod
    def post(request):
        serializer = AuthTokenSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


class BaseListCreateAPIView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class ProductListCreate(BaseListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderItemListCreate(BaseListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class StockListCreate(generics.ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class OrderListCreate(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
