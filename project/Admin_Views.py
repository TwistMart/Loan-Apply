from itertools import count
from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages # using messages
from app.models import CustomUser,CreditOfficer,Customer,Supervisors,Office,CustomerApply_Loan,Loan
#from project.scripts.compound_interest import compound_interest
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.template.loader import get_template


@login_required(login_url='/')
def AdminHome(request):
    loan_count=Loan.objects.all().count()
    customer_count= Customer.objects.all().count()
   # payableamount=Loan.objects.filter(id='amount').count()
    
    context={
        'loan_count':loan_count,
        'customer_count':customer_count,        
    }
    return render(request, "Admin/AdminHome.html",context)

def AddCreditOfficer(request):
    if request.method=="POST":        
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        address=request.POST.get('address')
        gender=request.POST.get('gender')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, "Email is already taken")
            return redirect('addcreditofficers')

        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, "Username is already taken")
            return redirect('addcreditofficers')      

        else:
            user=CustomUser(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,             
                user_type= 3,
            )
            user.set_password(password)
            user.save()    

            creditofficer=CreditOfficer(
                admin=user,
                address=address,              
                gender=gender,                
            )
            creditofficer.save()
            messages.success(request,  "successfully added " + user.first_name + " " +  user.last_name ) 
            return redirect('addcreditofficers') 

    return render(request, "Admin/AddCreditOfficers.html")

def AddCustomer(request):
    if request.method=="POST":        
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        address=request.POST.get('address')
        gender=request.POST.get('gender')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, "Email is already taken")
            return redirect('addcustomers')

        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, "Username is already taken")
            return redirect('addcustomers')      

        else:
            user=CustomUser(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,             
                user_type= 4,
            )
            user.set_password(password)
            user.save()    

            customer=Customer(
                admin=user,
                address=address,              
                gender=gender,                
            )
            customer.save()
            messages.success(request,  "successfully added " + user.first_name + " " +  user.last_name ) 
            return redirect('addcustomers') 

    return render(request, "Admin/AddCustomer.html")

def ViewCustomer(request):
    customer=Customer.objects.all

    context={
        'customer':customer,
    }
    return render(request, 'Admin/ViewCustomer.html', context)
    

def CustomerPdfReport(request):
    customers= Customer.objects.all()
    

    template_path = 'Admin/pdfview.html'
  
    context =  { 
   'customers': customers
   }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="customerlist.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response




def AddSupervisor(request):
    if request.method=="POST":        
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        address=request.POST.get('address')
        gender=request.POST.get('gender')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, "Email is already taken")
            return redirect('addsupervisors')

        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, "Username is already taken")
            return redirect('addsupervisors')      

        else:
            user=CustomUser(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,             
                user_type= 4,
            )
            user.set_password(password)
            user.save()    

            supervisor=Supervisors(
                admin=user,
                address=address,              
                gender=gender,                
            )
            supervisor.save()
            messages.success(request,  "successfully added " + user.first_name + " " +  user.last_name ) 
            return redirect('addsupervisors') 

    return render(request, "Admin/AddSupervisors.html")

def AddOffice(request):
    if request.method=="POST":        
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        address=request.POST.get('address')
        gender=request.POST.get('gender')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, "Email is already taken")
            return redirect('addoffice')

        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, "Username is already taken")
            return redirect('addoffice')      

        else:
            user=CustomUser(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,             
                user_type= 4,
            )
            user.set_password(password)
            user.save()    

            office=Office(
                admin=user,
                address=address,              
                gender=gender,                
            )
            office.save()
            messages.success(request,  "successfully added " + user.first_name + " " +  user.last_name ) 
            return redirect('addoffice') 

    return render(request, "Admin/AddOffice.html")


def CustomerLoan(request):
    customerloan=CustomerApply_Loan.objects.all()

    context={
        'customerloan':customerloan
    }

    return render(request, "Admin/CustomerLoan.html", context)

def CustomerApproveLoan(request,pk):
    customerloan=CustomerApply_Loan.objects.get(id=pk)
    customerloan.status=1
    customerloan.save()
    return redirect('customerloan')   

def CustomerDisapproveLoan(request,pk):
    customerloan=CustomerApply_Loan.objects.get(id=pk)
    customerloan.status=2
    customerloan.save()
    return redirect('customerloan')   


  
