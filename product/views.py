
from django.views.generic import (
	ListView, 
	DetailView, 
	View
)


from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View
from django.shortcuts import redirect
from django.utils import timezone

from .models import Product, Cart, Order



from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404



class ListPage(ListView):
	model = Product
	paginate_by = 4
	template_name = "product/list.html"



class DetailPage(DetailView):
	model = Product
	template_name = "product/detail.html"



def create_cart(request, slug):
	product = get_object_or_404(Product, slug=slug)
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

	return redirect("core:detail-product", slug=slug)



def clear(request):
	Order.objects.filter(user=request.user).delete()
	Cart.objects.filter(user=request.user).delete()
	return redirect("/")




def SummaPage(request):
	if Order.objects.filter(user=request.user, finish=False).exists():
		order = Order.objects.get(user=request.user, finish=False)
		context = {
		'object': order
		}
		return render(request, 'product/order.html', context)
	else:
		messages.error(request, "Cart is empty")
		return redirect("/")
