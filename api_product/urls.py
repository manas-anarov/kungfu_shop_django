
from django.urls import path

from django.conf.urls import include, url
from api_product import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
	path('create-cart/<slug>/', views.CreateCart.as_view(), name='api-create-cart'),
	path('clear/', views.ClearCart.as_view(), name='api-clear'),
	path('list/', views.ListProduct.as_view() , name='api-list'),
	path('detail/<slug>/', views.DetailProduct.as_view(), name='api-show'),
	path('summary/', views.SummaPage.as_view(), name='api-summary'),
]