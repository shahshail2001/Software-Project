from django.db import models
from customer_login.models import Customer
from employee_dashboard.models import Car


# Create your models here.
class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    customerid = models.IntegerField(default=0)
    customername = models.CharField(max_length=50, default=None)
    carid = models.IntegerField(default=0)
    carname = models.CharField(max_length=50, default=None)
    carnumber = models.CharField(max_length=25, default=None)
    bookingdate = models.DateTimeField(auto_now_add=True)
    carbookdate = models.DateField()
    carreturndate = models.DateField()
    totalpayment = models.IntegerField(default=0)
    total_no_of_days = models.IntegerField(default=0)
