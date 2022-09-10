from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
import numpy_financial as npf
import numpy as np

# Create your models here.
class CustomUser(AbstractUser):
    USER = (
        (1,'ADMIN'),
        (2, 'SUPERVISOR'),
        (3, 'CREDITOFFICER'),
        (4, 'CUSTOMER'),
        (5, 'OFFICE'),       

    )

    user_type= models.CharField(choices=USER, max_length=50, default=1)

class CreditOfficer(models.Model):
    admin=models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    gender=models.CharField(max_length=100,blank=True, null=True)
    address=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.first_name + "  " + self.admin.last_name


class Customer(models.Model): 
    admin=models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    gender=models.CharField(max_length=100,blank=True, null=True)
    address=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):        
        return self.admin.first_name + "  " + self.admin.last_name

class Supervisors(models.Model): 
    admin=models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    gender=models.CharField(max_length=100,blank=True, null=True)
    address=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):        
        return self.admin.first_name + "  " + self.admin.last_name
        

class Office(models.Model): 
    admin=models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    gender=models.CharField(max_length=100,blank=True, null=True)
    address=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):        
        return self.admin.first_name + "  " + self.admin.last_name


def validate_principal(value):
    if value < 7000:
        raise ValidationError('Principal Amount Cannot be less than 7000')

def calculate_interest(principal, months, interest):
    (principal*(1+(interest/100)*months))+300


class Loan(models.Model): 

    creditofficer= models.ForeignKey(CreditOfficer, on_delete=models.CASCADE)    
    principal = models.FloatField(default=7000, validators=[validate_principal])
    interest = models.FloatField(default=0)
    months = models.IntegerField(default=0)
    payable_amount = models.FloatField(default=0, validators=[calculate_interest])
    status = models.CharField(max_length=12, default=0)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return self.payable_amount

class CustomerApply_Loan(models.Model):
    customer_id= models.ForeignKey(Customer, on_delete=models.CASCADE)
    date= models.CharField(max_length=100)
    message=models.TextField()
    status= models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer_id.admin.first_name + self.customer_id.admin.last_name