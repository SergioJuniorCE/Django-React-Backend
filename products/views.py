from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer

@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    sort_by = request.GET.get('sort_by')
    if sort_by == 'lowest_price':
        products = products.order_by('price')
    elif sort_by == 'highest_price':
        products = products.order_by('-price')
    serializer = ProductSerializer(products, many=True)
    data = serializer.data
    return Response(data)


@api_view(['GET'])
def get_product(request, id):
    product = get_object_or_404(Product, id=id)
    serializer = ProductSerializer(product)
    data = serializer.data
    return Response(data)