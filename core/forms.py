from django import forms
from core.models import Rating, Restaurant, Order, Transfer


class ProductStockException(Exception):
    pass

class TransferMoneyException(Exception):
    pass

class ProductOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('product', 'number_of_items')
    
    def save(self, commit = True):
        order = super().save(commit=False)
        if order.product.number_in_stock < order.number_of_items:
            raise ProductStockException(f'Not enough items in stock for product: {order.product}')
        
        if commit:
            order.save()
        return order 
    
class TransferMoneyForm(forms.ModelForm):
    class Meta:
        model = Transfer
        fields = ('from_account','to_account','amount')

    def clean(self):
        transfer =  super().clean()
        from_account = transfer.get('from_account')
        to_account = transfer.get('to_account')
        if from_account and to_account and from_account.name == to_account.name:
            raise forms.ValidationError("You can't transfer money to yourself")
        if from_account  and from_account.balance <=0 :
            raise forms.ValidationError("You can't transfer money if your balance is negative")
        
        return transfer

    # def save(self, commit = True):
    #     transfer = super().save(commit=False)

    #     if transfer.from_account.name == transfer.to_account.name:
    #         raise TransferMoneyException(f"You can't transfer money to yourself")
        
    #     if commit:
    #         transfer.save()
    #     return transfer
