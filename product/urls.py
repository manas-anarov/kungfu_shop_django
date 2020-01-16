from django.urls import path
from .views import (
	ListPage,
	DetailPage,
	create_cart,
	# OrderSummaryView,
	clear,
	SummaPage,
)
from django.contrib.auth.decorators import login_required
app_name = 'core'

urlpatterns = [
	path('create-cart/<slug>/', login_required(create_cart), name='create-cart'),
	path('summary/', login_required(SummaPage), name='summary'),
	path('clear/', clear, name='clear'),
	path('<slug>/', DetailPage.as_view(), name='detail-product'),
	path('', ListPage.as_view(), name='list-product'),
]
