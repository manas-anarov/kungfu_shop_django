from django import template
register = template.Library()

from product.models import Cart, Order
from django.db.models import Count

@register.simple_tag(takes_context=True)
def get_cart_item(context):
	try:
		request = context['request']

		get_total = Order.objects.get(user=request.user, finish=False)
		result = get_total.get_item_count()

		return result
	except Exception as e:
		return "0"