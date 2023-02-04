from django.contrib import admin
from epdata.models import epdata
class epdataadmin(admin.ModelAdmin):
    display = ['name' , 'mobile', 'email' , 'specialization']
admin.site.register( epdata , epdataadmin)

# Register your models here.
