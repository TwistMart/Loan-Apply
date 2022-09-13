from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
import numpy_financial as npf
import numpy as np
from scripts.compound_interest import compound_interest

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
    customer_id= models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)   
    amount = models.FloatField(default=0, blank=True)
    interest_rate = models.FloatField(default=0, blank=True)
    num_times_interest=models.FloatField(default=0, blank=True, null=True)
    time_period=models.FloatField(default=0, blank=True)
    time_periods=models.CharField(max_length=12, default=0) 
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return  str(self.amount)

    @property    
    def compound_interest(amount, interest, num_times_int, time_period, time_period_in):
        amount = float(amount)
        interest = float(interest) / 100
        time_period = float(time_period)
    
    
        time_convert_dict = {'Days' : 365, 'Months' : 12, 'Years' : 1}
        interest_convert_dict = {'Yearly' : 1, 
                             'Quarterly' : 4,
                             'Monthly' : 12,
                             'Continuous' : 12}
    
        n = interest_convert_dict[num_times_int]
    
    
        time_period_years = time_period / time_convert_dict[time_period_in]
    
        print(n)
        print('Effective n is %i' % (n * time_period_years))
        total_investment = amount * (1 + (interest / n)) ** (n * time_period_years)
        if total_investment >= 1000000000:       


            total_investment = int(total_investment)
            return total_investment
 

class CustomerApply_Loan(models.Model):
    customer_id= models.ForeignKey(Customer, on_delete=models.CASCADE)
    date= models.CharField(max_length=100)
    message=models.TextField()
    status= models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer_id.admin.first_name + self.customer_id.admin.last_name