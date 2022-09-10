from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from app.models import CustomUser,Customer,CustomerApply_Loan
from django.contrib import messages # using messages

@login_required(login_url='/')
def CustomerHome(request):
    return render(request, "Customer/CustomerHome.html")

def CustomerApplyLoan(request):
    customer=Customer.objects.filter(admin=request.user.id)

    for i in customer:
        customer_id=i.id
    customer_loan=CustomerApply_Loan.objects.filter(customer_id=customer_id)

    context={
        'customer_loan':customer_loan
    }

    return render(request, "Customer/ApplyLoan.html", context)

def CustomerApplyLoanSave(request):
    if request.method=='POST':

        apply_date=request.POST.get('apply_date')
        apply_message=request.POST.get('apply_message')
        
        customer=Customer.objects.get(admin=request.user.id)
        applyloan=CustomerApply_Loan(
            customer_id=customer,
            date=apply_date,
            message=apply_message
        )
        applyloan.save()
        messages.success(request, "Loan applied successfully")
        return redirect('customerapplyloan')
        
    return render(request,"Customer/ApplyLoan.html")