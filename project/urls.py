
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views,CreditOfficer_Views,Office_Views,Supervisor_Views,Admin_Views,Customer_Views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('base', views.Base, name='base' ),

    # login paths
    path('', views.Login, name='login'),
    path('login', views.DoLogin, name='dologin'),
    path('logout', views.DoLogout, name='logout'),

    # Admin paths
    path('Admin/Home', Admin_Views.AdminHome, name='adminhome'), 
    path('Admin/Supervisor/Add', Admin_Views.AddSupervisor, name='addsupervisors'), 
    path('Admin/Credit/Add', Admin_Views.AddCreditOfficer, name='addcreditofficers'), 
    path('Admin/Customers/Add', Admin_Views.AddCustomer, name='addcustomers'), 
    path('Admin/Office/Add', Admin_Views.AddOffice, name='addoffice'), 
    path('Admin/Customer/Loan', Admin_Views.CustomerLoan, name='customerloan'), 
    path('Admin/Customer/Approve/Loan/<str:pk>', Admin_Views.CustomerApproveLoan, name='customerapproveloan'),
    path('Admin/Customer/Disapprove/Loan/<str:pk>', Admin_Views.CustomerDisapproveLoan, name='customerdisapproveloan'), 


    # CreditOfficer paths 
    path('Credit/Home', CreditOfficer_Views.CreditOfficerHome, name='credithome'), 
    path('interest_calculator/', CreditOfficer_Views.interest_calc, name = 'creditcustomersloan'),    
    path('interest_calculator/results/', CreditOfficer_Views.results_interest, name = 'creditviewcustomers'), 



    # Customer paths
    path('Customer/Home', Customer_Views.CustomerHome, name='customerhome'),
    path('Customer/Apply/Loan', Customer_Views.CustomerApplyLoan, name='customerapplyloan'),
    path('Customer/Apply/Loan/save', Customer_Views.CustomerApplyLoanSave, name='customerapplyloansave'),

    # Office paths
    path('Office/Home', Office_Views.OfficeHome, name='officehome'),

    # Supervisor paths
    path('Supervisor/Home', Supervisor_Views.SupervisorHome, name='supervisorhome'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
