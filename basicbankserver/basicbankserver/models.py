from django.db import models
from django.contrib.auth.models import User


# class customers(models.Model):
#     username=models.CharField(max_length=30, unique=True)
#     password=models.CharField(max_length=30)


class accounts(models.Model):
    account_number = models.IntegerField(unique=True)
    account_balance = models.IntegerField()
    account_type = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

