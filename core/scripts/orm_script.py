from django.contrib.auth.models import User
from core.models import Restaurant, Rating, Sale
from django.utils import timezone
from django.db import connection
from pprint import pprint

def run():
     
     print(Restaurant.objects.count())
     print(Rating.objects.count())
     print(Sale.objects.count())
     pprint(connection.queries)