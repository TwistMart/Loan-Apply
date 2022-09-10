from django.shortcuts import render,redirect,HttpResponse
from app.EmailBackend import EmailBackEnd
from django.contrib.auth import authenticate, logout, login # used to authenticate when logging in and logging out
from django.contrib import messages # using messages
from django.contrib.auth.decorators import login_required

def Base(request):
    return render(request, "base.html")


def DoLogout(request):
    logout(request)
    return redirect('login')


def Login(request):
    return render(request, "login.html")

def DoLogin(request):
    if request.method == "POST":        
        user=EmailBackEnd.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
        if user!=None:
            login(request,user)
            user_type=user.user_type
            if user_type == "1":
                return redirect('adminhome')             
            
            elif user_type == "2":
                return redirect('supervisorhome')                          
                
            elif user_type == "3":
                return redirect('credithome') 

            elif user_type == "4":
                return redirect('customerhome')                   
              
            elif user_type == "5":
                return redirect('officehome')             
                               
            else:
                messages.error(request,"Email and password are Invalid")
                return redirect('login')
        else:
            messages.error(request,"Email and password are Invalid")
            return redirect('login')




            
        

        
  
    

    