from django.shortcuts import render, redirect
from core.models import Restaurant, Rating, Sale, Staff_Restaurant, Product, Account
from django.db.models import Sum, Prefetch, Avg, Count, Min, Max
from django.utils import timezone
from django.db.models.functions import TruncDate
from django.db import transaction
from core.forms import ProductOrderForm, TransferMoneyForm
from functools import partial


def email_user(email):
    print(f'Dear {email}, Thanks for your order!')


def account_name(name):
    print(f'Thank you for transfer, Mr. {name}')

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
                product = Product.objects.select_for_update().get(
                    id = form.cleaned_data['product'].pk
                )
                import time
                time.sleep(80)
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

def transfer_money(request):
    if request.method == 'POST':
        form = TransferMoneyForm(request.POST or None)
        if form.is_valid():
            with transaction.atomic():
                from_account = Account.objects.select_for_update(nowait=True).get(
                    id = form.cleaned_data['from_account'].id)
                to_account = Account.objects.select_for_update(nowait=True).get(
                    id = form.cleaned_data['to_account'].id)
                transfer = form.save()
                transfer.from_account.balance -= transfer.amount
                transfer.from_account.save()
                transfer.to_account.balance += transfer.amount
                transfer.to_account.save()
            transaction.on_commit(partial(account_name, transfer.from_account.name))
            return redirect('transfer-money')
        context = {'form':form}
        return render(request, 'core/transfer_money.html', context)
    form = TransferMoneyForm()
    context = {'form':form}
    return render(request, 'core/transfer_money.html', context)
    
        
