from django.shortcuts import render, redirect
from core.models import Restaurant, Rating, Sale, Staff_Restaurant
from django.db.models import Sum, Prefetch, Avg, Count, Min, Max
from django.utils import timezone
from django.db.models.functions import TruncDate
from django.db import transaction
from core.forms import ProductOrderForm
from functools import partial


def email_user(email):
    print(f'Dear {email}, Thanks for your order!')



# Create your views here.
def index(request):

    rating = Rating.objects.prefetch_related('restaurant','user')

    for r in rating:
        print(r.restaurant.name)
        print(r.user.first_name)
    return render(request, 'core/index.html')


def order_product(request):
    if request.method == 'POST':
        form = ProductOrderForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                order = form.save()

                # crash server
                # import sys
                # sys.exit(1)
                order.product.number_in_stock -= order.number_of_items
                order.product.save()
            transaction.on_commit(partial(email_user,'test@gmail.com'))
            return redirect('order-product')
        else:
            context = {'form': form}
            return render(request, 'core/order.html', context)

    form = ProductOrderForm()
    context = {'form':form}

    return render(request, 'core/order.html', context)