


from django.conf import settings
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.views.generic import ListView, DetailView, View

from product.models import Order, Product, PayStripe
from django.shortcuts import redirect
from django.contrib import messages

import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

class Pay(TemplateView):
    template_name = 'pay/pay.html'

    def get_context_data(self,**kwargs):

        get_total = Order.objects.get(user=self.request.user, finish=False)
        total = get_total.get_sum()
        self.request.session['total'] = total
        self.request.session['total_amount'] = total * 100

        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLIC_KEY

        return context


def final(request):

    getted_total = request.session.get('total_amount', 0)

    if request.method == 'POST':

        charge = stripe.Charge.create(
            amount=getted_total,
            currency='usd',
            description='My charge',
            source=request.POST['stripeToken']
        )


        order = Order.objects.get(user=request.user, finish=False)
        payment = PayStripe.objects.create(user=request.user, stripe_id = charge['id'], total = order.get_sum())
        order.finish = True
        order.pay_stripe = payment
        order.save()

        messages.success(request, 'Success payment')

        return redirect("/")
