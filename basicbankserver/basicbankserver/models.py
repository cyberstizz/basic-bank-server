from django.db import models

class accounts(models.Model):
    account_number = models.CharField(max_length=30)
    account_balance = models.CharField(max_length=30)
    account_name = models.CharField(max_length=30)

    class Meta:
        app_label = 'basicbankserver'