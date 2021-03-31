from django.urls import path

from .views import *

urlpatterns = [
    path('', get_products, name='get-products'),
    path('<int:id>/', get_product, name='get-product'),
]
