
from django.urls import path

from . import views

urlpatterns = [
	path('final/', views.final, name='final'),
    path('', views.Pay.as_view(), name='home'),
]