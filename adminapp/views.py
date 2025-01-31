from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control
from django.contrib import messages
from mainapp.models import Customer, Enquiry
from . models import CarInfo
from custapp.models import Booking
# Create your views here.
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def adminhome(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            return render(request,'adminhome.html',locals())
    except KeyError:
        return redirect('mainapp:login')
def adminlogout(request):
    try:
        del request.session['adminid']        
    except KeyError:
        return redirect('mainapp:login')
    return redirect('mainapp:login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def customermgmt(request):
    try:
        if request.session['adminid']!=None:
            cust=Customer.objects.all()
            adminid=request.session['adminid']
            return render(request,'customermgmt.html',locals())
    except KeyError:
        return redirect('mainapp:login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def carmgmt(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            carinfo=CarInfo.objects.all()
            if request.method=='POST':
                carname=request.POST['carname']
                carno=request.POST['carno']
                drivername=request.POST['drivername']
                carrent=request.POST['carrent']
                carpic=request.FILES['carpic']    
                availability='available'           
                ci=CarInfo(carname=carname,carno=carno,drivername=drivername,carrent=carrent,carpic=carpic,availability=availability)
                ci.save()
                messages.success(request,'Car is added')
            return render(request,'carmgmt.html',locals())
    except KeyError:
        return redirect('mainapp:login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def enquirymgmt(request):
    try:
        if request.session['adminid']!=None:
            enq=Enquiry.objects.all()
            adminid=request.session['adminid']
            return render(request,'enquirymgmt.html',locals())
    except KeyError:
        return redirect('mainapp:login')
    
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def bookedcars(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            bookedcars = Booking.objects.all()
            return render(request,'bookedcars.html',locals())
    except KeyError:
        return redirect('mainapp:login')