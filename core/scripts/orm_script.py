from django.contrib.auth.models import User
from core.models import Restaurant, Rating, Sale, Staff, Staff_Restaurant, Product, Order
from django.db.models.functions import Upper, Length, Concat
from django.db.models import Max, Min, Case, When, CharField,FloatField,Subquery, OuterRef, Exists,\
    Value, Avg, Sum, Count, F, Q, Prefetch, ExpressionWrapper, DecimalField
from django.utils import timezone
from django.db import connection
from pprint import pprint
from django.db.models.functions import Lower, Coalesce
import random
from django.utils import timezone
import itertools
from django.db import transaction
import time


def run():

    with transaction.atomic():
        book = Product.objects.select_for_update().get(name='Book')
        time.sleep(60)

