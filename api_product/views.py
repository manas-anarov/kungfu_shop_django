
from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import postSerializer, cartSerializer
from product.models import Product

from rest_framework.generics import (
	ListAPIView,
	RetrieveAPIView,
	)

from rest_framework import status

from product.models import Product, Cart, Order

from django.shortcuts import render, get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response


class ListProduct(ListAPIView):
	serializer_class = postSerializer
	queryset = Product.objects.all()



class DetailProduct(RetrieveAPIView):
	queryset = Product.objects.all()
	serializer_class = postSerializer
	lookup_field = 'slug'


class SummaPage(APIView):

	authentication_classes = (TokenAuthentication, SessionAuthentication)
	permission_classes = (IsAuthenticated,)

	
	def get(self, request):

		serializer_context = {
			'request': request,
		}
		if Order.objects.filter(user=request.user, finish=False).exists():
			order = Cart.objects.filter(user=request.user)
			get_total = Order.objects.get(user=request.user)
			total = get_total.get_sum()

			serializer = cartSerializer(order, many=True, context={'request': request})
			return Response({"cart": serializer.data, "total":total})
			
		return Response({"fail": "empty"}, status=status.HTTP_404_NOT_FOUND)

		



class CreateCart(APIView):

	authentication_classes = (TokenAuthentication, SessionAuthentication)
	permission_classes = (IsAuthenticated,)

	
	def get(self, request, **kwargs):

		slug=self.kwargs['slug']

		product = Product.objects.get(slug=slug)

		user_login = request.user
		cart_single = Cart.objects.create(
			product=product,
			user=user_login,
		)
		if Order.objects.filter(user=request.user, finish=False).exists():
			order = Order.objects.get(user=user_login, finish=False)
		else:
			order = Order.objects.create(user=user_login)
		order.carts.add(cart_single)

		content = {"detail": "Product sucessfull add to cart"}
		return Response(content, status=status.HTTP_200_OK)



class ClearCart(APIView):

	authentication_classes = (TokenAuthentication, SessionAuthentication)
	permission_classes = (IsAuthenticated,)

	
	def get(self, request):

		Order.objects.filter(user=request.user).delete()
		Cart.objects.filter(user=request.user).delete()

		content = {"detail": "sucessfully clear"}

		return Response(content, status=status.HTTP_200_OK)