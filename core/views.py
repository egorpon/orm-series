from django.shortcuts import render
from .forms import  RestaurantForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST or None)
        if form.is_valid():
            # form.save()
            print(form.cleaned_data)
        else:
            return render(request,'core/index.html',{'form':form})
    form = RestaurantForm()
    return render(request, 'core/index.html',{'form':form})