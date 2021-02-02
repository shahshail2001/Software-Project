from django.db import models


# Create your models here.
class Car(models.Model):
    car_id = models.IntegerField(primary_key=True)
    car_company = models.CharField(max_length=25)
    car_class_type = models.CharField(max_length=20)
    price_per_km = models.IntegerField()
    car_number = models.CharField(max_length=15)
    fuel_type = models.CharField(max_length=10)
    car_description = models.TextField()
    car_availability = models.BooleanField()
