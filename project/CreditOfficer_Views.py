from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from app.models import CustomUser,Customer,CreditOfficer,Loan
from django.contrib import messages # using messages
from scripts.interest_parameter_checker import *
from scripts.compound_interest import compound_interest


@login_required(login_url='/')
def CreditOfficerHome(request):
    return render(request, "CreditOfficer/CreditOfficerHome.html")


def interest_calc(request):

	return render(request, 'CreditOfficer/CustomerLoan.html')


def results_interest(request): 
       

    if request.method=='POST':        

        amount=request.POST.get('amount')
        interest_rate=request.POST.get('interest_rate')
        num_times_interest=request.POST.get('num_times_interest ')
        time_period=request.POST.get('time_period')
        time_periods=request.POST.get('time_periods')          
	   
   
       
        creditor=CreditOfficer.objects.get(admin=request.user.id)
        print(creditor)
      
        customerloan=Loan(
            creditofficer=creditor,     
            amount=amount,
            interest_rate=interest_rate,
            num_times_interest= num_times_interest,
            time_period= time_period,
            time_periods= time_periods, 
                         
        )  
        is_valid = interest_parameter_checker(amount, interest_rate, num_times_interest, time_period, time_periods)
        if is_valid:                    
            compound_interest=compound_interest(amount, interest_rate, num_times_interest, time_period, time_periods)
        else:
            compound_interest=None 
             
        print(compound_interest)
        customerloan.save()
        messages.success(request, "Loan applied successfully")
        return redirect('creditviewcustomers')  

   

    return render(request, 'CreditOfficer/ViewCustomers.html')

	


  