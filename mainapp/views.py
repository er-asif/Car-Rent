from django.shortcuts import render, redirect, reverse
from . models import Enquiry, Customer, Login
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"index.html")
def services(request):
    return render(request,"services.html")
def about(request):
    return render(request,"about.html")
def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        emailaddress=request.POST["emailaddress"]
        subject=request.POST["subject"]
        message=request.POST["message"]
        enq=Enquiry(name=name, emailaddress=emailaddress,subject=subject,message=message)
        enq.save()
        messages.success(request,'Enquiry is sent.')
        return render(request,"contact.html",locals())
    return render(request,"contact.html")
def registration(request):
    if request.method=="POST":
        name=request.POST["name"]
        contactno=request.POST["contactno"]
        emailaddress=request.POST["emailaddress"]
        password=request.POST["password"]
        dob=request.POST["dob"]
        gender=request.POST["gender"]
        address=request.POST["address"]
        city=request.POST["city"]
        state=request.POST["state"]
        zipcode=request.POST["zipcode"]
        cust=Customer(name=name,contactno=contactno,emailaddress=emailaddress,dob=dob,gender=gender,address=address,city=city,state=state,zipcode=zipcode)
        log=Login(userid=contactno,password=password,usertype='customer')
        cust.save()
        log.save()
        messages.success(request,'Registration is done')
        return render(request,"registration.html",locals())
    return render(request,"registration.html")
def login(request):
    if request.method=="POST":
        userid=request.POST['userid']
        password=request.POST['password']
        try:
            obj=Login.objects.get(userid=userid,password=password)
            if obj.usertype=='customer':
                request.session['custid']=userid
                return redirect(reverse('custapp:custhome'))
            elif obj.usertype=='admin':
                request.session['adminid']=userid                
                return redirect(reverse('adminapp:adminhome'))            
        except:
            messages.error(request,'Invalid User')    
    return render(request,"login.html",locals())
