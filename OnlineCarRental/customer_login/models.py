from django.db import models


# Create your models here.
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_username = models.CharField(max_length=20)
    customer_password = models.CharField(max_length=20)
    customer_name = models.CharField(max_length=50)
    customer_email = models.CharField(max_length=30)
    customer_phone_no = models.CharField(max_length=10)
    customer_aadhar_no = models.CharField(max_length=12)
    customer_address = models.TextField()
    customer_dob = models.DateTimeField()
