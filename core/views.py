from django.shortcuts import render
from .forms import  RestaurantForm
from core.models import Restaurant, Rating, Sale, Staff_Restaurant
from django.db.models import Sum, Prefetch, Avg, Count, Min, Max
from django.utils import timezone
from django.db.models.functions import TruncDate

# Create your views here.
def index(request):

    rating = Rating.objects.prefetch_related('restaurant','user')

    for r in rating:
        print(r.restaurant.name)
        print(r.user.first_name)
    return render(request, 'core/index.html')