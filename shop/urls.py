
from django.contrib import admin
from django.urls import path

from django.conf.urls import include, url

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('pay/', include('pay.urls')),
    path('api/v1/', include(('api_product.urls', 'api-product'), namespace='api-product')),
    path('api/v1/accounts/', include(('api_accounts.urls', 'api-accounts'), namespace='api-accounts')),
    path('', include(('product.urls', 'product'), namespace='product')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

