from django.shortcuts import render
from .forms import  RestaurantForm
from core.models import Restaurant, Rating, Sale
from django.db.models import Sum, Prefetch
from django.utils import timezone

# Create your views here.
def index(request):

    seven_days_ago = timezone.now() - timezone.timedelta(days=7)
    seven_days_ago_sales = Sale.objects.filter(datetime__gte= seven_days_ago)
    weekly_sales = Prefetch('sales', queryset=seven_days_ago_sales)
    restaurants = Restaurant.objects.prefetch_related('ratings', weekly_sales).filter(ratings__rating__gte = 4).distinct()\
    .annotate(total = Sum('sales__income')).filter(total__gt=1000)
    print([r.total for r in restaurants])
    return render(request, 'core/index.html')