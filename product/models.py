from django.db import models

from django.conf import settings


from django.contrib.auth import get_user_model
User = get_user_model()

class Product(models.Model):
	title = models.CharField(max_length=400, default=0)
	desc = models.CharField(max_length=400, default=0)
	user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
	price = models.IntegerField(default=0)
	image = models.ImageField(upload_to = '', default = 'none/no-img.jpg')
	slug = models.SlugField()
	def __str__(self):
		return self.title


class Cart(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
	finish = models.BooleanField(default=False)
	def __str__(self):
		return self.product.title


class Order(models.Model):
	author = models.IntegerField(default=0)
	carts = models.ManyToManyField(Cart)
	finish = models.BooleanField(default=False)
	user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL, blank=True, null=True)
	pay_stripe = models.ForeignKey('PayStripe', on_delete=models.SET_NULL, blank=True, null=True)

	def __str__(self):
		return self.user.username

	def get_sum(self):
		total = 0
		for order_item in self.carts.all():
			total = order_item.product.price + total
		return total

	def get_item_count(self):
		result = self.carts.all().count()
		return result


class PayStripe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    stripe_id = models.CharField(max_length=100)
    total = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username