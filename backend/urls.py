from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('sdadmin/', admin.site.urls),
    path('api-auth', include('rest_framework.urls')),
    path('api/orders/', include('orders.urls')),
    path('api/products/', include('products.urls')),
    path('api/users/', include('users.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
