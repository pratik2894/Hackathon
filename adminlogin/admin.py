from django.contrib import admin
from adminlogin.models import adminSignup
class RegisterAdmin(admin.ModelAdmin):
    list_display=['name','email','phone' , 'password']
# Register your models here.
admin.site.register(adminSignup,RegisterAdmin)


# Register your models here.
