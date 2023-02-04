from django.contrib import admin
from leave.models import leave

class leaveAdmin(admin.ModelAdmin):
    display = ['name' , 'mobile', 'date2' , 'email' , 'reason']
admin.site.register(leave , leaveAdmin)
# Register your models here.
