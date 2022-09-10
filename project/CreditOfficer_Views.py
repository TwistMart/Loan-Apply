from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from app.models import CustomUser,Customer,Loan,CreditOfficer
from django.contrib import messages # using messages


@login_required(login_url='/')
def CreditOfficerHome(request):
    return render(request, "CreditOfficer/CreditOfficerHome.html")




# def calculate_interest(principal, months, interest):
#   #  principal*(1+(interest/100)*months) 
#     ((npf.pmt(interest, months , principal)) * -1)+principal   

#calculate_interest=      

def CreditOfficerLoanCustomersInfo(request):
    if request.method=="POST":        
        principal=request.POST.get('principal')
        interest=request.POST.get('interest')
        months=request.POST.get('months')     
       
        creditofficers= CreditOfficer.objects.get(admin=request.user.id)

        customerinfo=Loan(
            creditofficer=creditofficers,  
            principal=principal,
            interest=interest,
            months=months,        
                   
        )
        customerinfo.save()
        messages.success(request,  "Loan Info successfully added ") 
        return redirect('addoffice')    


    return render(request, "CreditOfficer/CustomerLoan.html")

def CreditOfficerViewCustomers(request):
    return render(request, "CreditOfficer/ViewCustomers.html")



  