from django.db import models

class Fuel(models.Model):
    station = models.CharField(max_length=40)
    price = models.CharField(max_length=2)
    plate_number = models.IntegerField()
    filled_gas = models.IntegerField()
    Date = models.DateField(auto_now_add=True)
    employe_name = models.CharField(max_length=15)

class oil(models.Model):
    place = models.CharField(max_length=15)
    changed_oil = models.CharField(max_length=3)
    plate_number = models.IntegerField()
    Date = models.DateField(auto_now_add=True)
    employe_name = models.CharField(max_length=15)