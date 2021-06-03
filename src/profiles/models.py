from django.db import models
from djmoney.models.fields import MoneyField


# Create your models here.

# class for defining profile info
class Profile(models.Model):
    Id = models.TextField(default='ID', primary_key=True)
    first_name = models.TextField(default='')
    last_name = models.TextField(default='')
    email = models.TextField(default='')


# class for defining transaction
class Transaction(models.Model):
    Transaction_Id = models.TextField(default='')
    User_id = models.TextField(default='')
    amount = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
    date = models.DateField()

