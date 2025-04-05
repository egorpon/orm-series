from django.contrib.auth.models import User
from core.models import Restaurant, Rating, Sale
from django.utils import timezone
from django.db import connection
from pprint import pprint
from django.db.models.functions import Lower

def run():

     chinese = Restaurant.TypeChoices.CHINESE
     sales = Sale.objects.filter(restaurant__restaurant_type = chinese)
     print(sales)


     pprint(connection.queries)