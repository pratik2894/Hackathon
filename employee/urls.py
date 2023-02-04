"""employee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from employee import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("" , views.landing ,  name ="landing"),
    path("Eplogin/" , views.Eplogin , name = "Eplogin" ),
    path("AdminLogin/" , views.AdminLogin, name="AdminLogin"),
    path("AdminSignup/" , views.AdminSignup , name = "AdminSignup"),
    path("Admin/" , views.Admin , name="Admin"),
    path("Employee_data/" , views.Employee_data , name = "Employee_data"),
    path("leavereq/" , views.leavereq , name="leavereq"),
    path("profile/" , views.profile , name="profile"),
    path("addep/" , views.addep , name="addep"),
    path("EpSignup/" ,views.EpSignup , name = "EpSignup" ),
    path('activate/<uidb64>/<token>' , views.activate, name="activate" ),
    path("Epreq/" , views.Epreq , name="Epreq"),
    path("leaveReqForm/" , views.leaveReqForm , name="leaveReqForm")
]
