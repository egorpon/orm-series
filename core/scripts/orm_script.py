from django.contrib.auth.models import User
from core.models import Restaurant, Rating, Sale, Staff, Staff_Restaurant
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

def run():

    pass

