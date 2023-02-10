from django.db import models


class customers(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    customer_ID = models.IntegerField(unique=True)

    class Meta():
        app_label = 'basicbankserver'

class accounts(models.Model):
    account_number = models.IntegerField(unique=True)
    account_balance = models.IntegerField()
    account_type = models.CharField(max_length=30)
    customer_ID = models.ForeignKey(customers, on_delete=models.CASCADE)

