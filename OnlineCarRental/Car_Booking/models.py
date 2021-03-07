from django.db import models
from customer_login.models import Customer
from employee_dashboard.models import Car


# Create your models here.
class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    customerid = models.ForeignKey(Customer, on_delete=models.CASCADE)
    carid = models.ForeignKey(Car, on_delete=models.CASCADE)
    bookingdate = models.DateTimeField(auto_now_add=True)
    carbookdate = models.DateField()
    carreturndate = models.DateField()
    totalpayment = models.IntegerField()
