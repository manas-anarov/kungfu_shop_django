# tokensite/blog/serializers.py

from rest_framework.serializers import (
	HyperlinkedIdentityField,
)

from rest_framework import serializers

from rest_framework.serializers import (
      ModelSerializer,
)
from rest_framework.response import Response

from product.models import Product, Order, Cart

add_cart_url = HyperlinkedIdentityField(
	view_name = 'api-product:api-create-cart',
	lookup_field = 'slug'
)

class postSerializer(ModelSerializer):
	cart_url = add_cart_url
	class Meta:
		model = Product
		fields = ['id',
			'title',
			'desc',
			'price',
			'image',
			'cart_url',
			'slug',
			]




class cartSerializer(ModelSerializer):
	product = postSerializer()
	class Meta:
		model = Cart
		fields = [
			'id',
			'product',
			]


