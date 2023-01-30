from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator


class accounts(models.Model):
    account_number = models.IntegerField(unique=True)
    account_balance = models.IntegerField(validators=[MaxLengthValidator(10)])
    account_name = models.CharField(max_length=30)

    class Meta:
        app_label = 'basicbankserver'