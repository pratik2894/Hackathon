from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from adminlogin.models import adminSignup
from django.contrib import messages
from django.core.mail import send_mail,EmailMessage
from . tokens import generate_token
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from . tokens import generate_token
from django.contrib.auth import authenticate,login,logout
from django.template.loader import render_to_string
from employee import settings
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.core.mail import EmailMultiAlternatives
from leaveReq.models import leavereq
from leave.models import leave
from epdata.models import epdata




def landing(request):
    return render(request , "landing.html")

def Eplogin(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        password = request.POST.get('cpassword')
        myuser = authenticate(username = uname , password=password)
        if myuser is not None:
            login(request,myuser)
            return render(request , "req.html")
        else:
            return render(request,"index.html")

    return render(request , "index.html")
def EpSignup(request):
    if request.method == "POST" :
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        
        if User.objects.filter(username=username):
            messages.error(request , "username alredy exists!")
            return redirect('EpSignup')
        if User.objects.filter(email=email):
            messages.error(request , "email alredy exists!")
            return redirect('EpSignup')
        if len(username)>=7:
            messages.error(request , "username must be under 7 character!")
            return redirect('EpSignup')
        if password!=cpassword:
            messages.error(request , "password didn't match!")
            return redirect('EpSignup')

        myuser = User.objects.create_user(username , email, cpassword)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = False
        myuser.save() 
        subject = "Welcome"+  myuser.username
        from_email = "mohitepratik008@gmail.com"
        msg  = "<h1>Welcome to EpSystem</h1> <br><br><br><p>Hi !<br><br><p> Welcome to the team! We’re thrilled to have you at Epsystem.<br> We know you’re going to be a valuable asset to our company and can’t wait to see what you accomplish </p>"
        to = email
        msg = EmailMultiAlternatives(subject,msg,from_email,[to])
        msg.content_subtype='html'

        current_site = get_current_site(request)
        email_subject = "confirmation email"
        message2 = render_to_string('email_confirmation.html' ,{
            'name' : myuser.first_name,
            'domain' : current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token' : generate_token.make_token(myuser)

        })
        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email],

        )
        email.fail_silently = True
        email.send()
        return redirect("Eplogin")
    return render(request,"epSignup.html")

def activate(request,uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None
    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        return redirect('Eplogin')
    else:
        return render(request,'activation_failed.html')


def AdminLogin(request):
    if request.method == "POST" :
        username = request.POST.get('username')
        password = request.POST.get('password')
        myadmin = authenticate(username = username , password=password)
        if myadmin is not None :
            login(request , myadmin)
            return redirect("Admin")    
    return render(request , "adminLogin.html")

def AdminSignup(request):
    try:
        if request.method == 'POST' :
            username = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            password = request.POST.get('password')
            myadmin = User.objects.create_user(username , email, password)
            myadmin.is_active = False
            myadmin.save()
            subject = "Welcome"+  myadmin.username
            from_email = "mohitepratik008@gmail.com"
            msg  = "<h1>Welcome to EpSystem Admin Panel</h1> <br><br><br><p>Hi !<br><br><p> Welcome to the team! We’re thrilled to have you at Epsystem.<br> We know you’re going to be a valuable asset to our company and can’t wait to see what you accomplish </p>"
            to = email
            msg = EmailMultiAlternatives(subject,msg,from_email,[to])
            msg.content_subtype='html'
            subject = "Welcome"+  myadmin.username
            from_email = "mohitepratik008@gmail.com"
            msg  = "<h1>Welcome to EpSystem</h1> <br><br><br><p>Hi !<br><br><p> Welcome to the team! We’re thrilled to have you at Epsystem.<br> We know you’re going to be a valuable asset to our company and can’t wait to see what you accomplish </p>"
            to = email
            msg = EmailMultiAlternatives(subject,msg,from_email,[to])
            msg.content_subtype='html'
            msg.send()
        return redirect("AdminLogin")
    except :
        pass
    return render(request , "adminSignup.html")
def Admin(request):
    return render(request, "admin.html" )
def Employee_data(request):


    return render(request , "Employee_data.html")
def leavereq(request):
    req = leave.objects.all()
    data = {
        'req' : req
    }
    return render(request , "leaveReq.html" , data)
def leaveReqForm(request):
    if request.method == 'POST':
        name1 = request.POST.get("name1")
        email = request.POST.get("email1")
        date1 = request.POST.get("date1")
        date2 = request.POST.get("date2")
        reason = request.POST.get("reason")
        accept = request.POST.get("accept")
        reject = request.POST.get("reject")
        print(date1 , date2)
        if accept=="accept" :
            subject = "Hey"
            from_email = "mohitepratik008@gmail.com"
            msg  = "<h1>thanks for request!!</h1> <br><br><br><p>Hi !<br><br><p> we have accepted your leave request congratlation!! </p>"
            to = email
            msg = EmailMultiAlternatives(subject,msg,from_email,[to])
            msg.content_subtype='html'
            msg.send()
        if reject == "reject" :
            subject = "Hey"
            from_email = "mohitepratik008@gmail.com"
            msg  = "<h1>thanks for request!!</h1> <br><br><br><p>Hi !<br><br><p> we have reject your leave request congratlation!! </p>"
            to = email
            msg = EmailMultiAlternatives(subject,msg,from_email,[to])
            msg.send()
 

        leaveform = leave( name = name1 ,date1 = date1 , date2 = date2 , email = email , reason = reason )
        leaveform.save()

    return render(request , "leaveForm.html")
def profile(request):
    return render(request , "profile.html")
def addep(request):
    if request.method == "POST":
        name = request.POST.get("fname")
        dob = request.POST.get("dob")
        mail = request.POST.get("mail")
        mobile = request.POST.get("moblile")
        gen = request.POST.get("gender")
        specialization = request.POST.get("specialization")
        religion = request.POST.get("religion")
        bloodGroup = request.POST.get("bloodGroup")
        Duration = request.POST.get("Duration")
        data = epdata(name = name , email = mail , mobile = mobile ,specialization=specialization ,religion =religion ,Blood = bloodGroup , duration = Duration )
        data.save()


    return render(request , "addep.html")

def Epreq(request):
    return render(request , "req.html")
