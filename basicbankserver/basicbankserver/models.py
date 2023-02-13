from django.db import models



class customers(models.Model):
    username=models.CharField(max_length=30, unique=True)
    password=models.CharField(max_length=30)


class accounts(models.Model):
    account_number = models.IntegerField(unique=True)
    account_balance = models.IntegerField()
    account_type = models.CharField(max_length=30)
    user = models.ForeignKey(customers, on_delete=models.CASCADE)

