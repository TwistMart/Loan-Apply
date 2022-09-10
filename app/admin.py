from django.contrib import admin
from.models import *
from django.contrib.auth.admin import UserAdmin

class UserModel(UserAdmin):
    list_display=['username', 'user_type']

# Register your models here.
admin.site.register(CustomUser,UserModel)
admin.site.register(CreditOfficer)
admin.site.register(Customer)
admin.site.register(Supervisors)
admin.site.register(Office)
admin.site.register(Loan)
admin.site.register(CustomerApply_Loan)
