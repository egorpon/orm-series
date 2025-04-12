from django.contrib.auth.models import User
from core.models import Restaurant, Rating, Sale, Staff, Staff_Restaurant
from django.db.models.functions import Upper, Length, Concat
from django.db.models import Max, Min, Case, When, CharField,\
    Value, Avg, Sum, Count, F, Q, Prefetch, ExpressionWrapper, DecimalField
from django.utils import timezone
from django.db import connection
from pprint import pprint
from django.db.models.functions import Lower, Coalesce
import random
from django.utils import timezone
import itertools

def run():

    first_sale = Sale.objects.aggregate(first_sale_date=Min('datetime'))['first_sale_date']
    last_sale = Sale.objects.aggregate(last_sale_date=Max('datetime'))['last_sale_date']
    
    dates = []
    count = itertools.count()

    while (dt := first_sale + timezone.timedelta(days=10*next(count)))<=last_sale:
        dates.append(dt)

    whens = [
         When(datetime__range=(dt, dt+timezone.timedelta(days=10)), then=Value(dt.date()))
         for dt in dates
             ]
    
    case = Case(
        *whens,
        output_field=CharField()
    )

    print(Sale.objects.annotate(
        daterange = case
    ).values('daterange').annotate(total_sales=Sum('income')))
    pprint(connection.queries)