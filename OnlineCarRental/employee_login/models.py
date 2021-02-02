from django.db import models


# Create your models here.
class Employee(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    employee_username = models.CharField(max_length=20)
    employee_password = models.CharField(max_length=20)
    employee_name = models.CharField(max_length=50)
    employee_email = models.CharField(max_length=30)
    employee_phone_no = models.CharField(max_length=10)
    employee_aadhar_no = models.CharField(max_length=12)
    employee_address = models.TextField()
    employee_dob = models.DateTimeField()
    employee_salary = models.IntegerField()
    employee_designation = models.CharField(max_length=30)
    date_of_join = models.DateTimeField()
    check_availability = models.BooleanField()