from django.contrib import admin
from leaveReq.models import leavereq
class leaveAdmin(admin.ModelAdmin):
    list_display = ["nameEp" , "email" , "leavereason"]
admin.site.register(leavereq,leaveAdmin)

# Register your models here.
