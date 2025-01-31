from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control
from django.contrib import messages
from adminapp.models import CarInfo
from . models import Booking, Response
from mainapp.models import Customer
import datetime
# Create your views here.
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def custhome(request):
    try:
        if request.session['custid']!=None:
            custid=request.session['custid']
            custname=Customer.objects.get(contactno=custid).name
            return render(request,'custhome.html',locals())
    except KeyError:
        return redirect('mainapp:login')
def custlogout(request):
    try:
        del request.session['custid']        
    except KeyError:
        return redirect('mainapp:login')
    return redirect('mainapp:login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewcars(request):
    try:
        if request.session['custid']!=None:
            custid=request.session['custid']
            custname=Customer.objects.get(contactno=custid).name
            carinfo=CarInfo.objects.filter(availability='available')
            return render(request,'viewcars.html',locals())
    except KeyError:
        return redirect('mainapp:login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def book(request,cid):
    try:
        if request.session['custid']!=None:
            custid=request.session['custid']
            custname=Customer.objects.get(contactno=custid).name
            carinfo=CarInfo.objects.get(carid=cid)
            carname=carinfo.carname
            carno=carinfo.carno
            drivername=carinfo.drivername
            carrent=carinfo.carrent
            cust=Customer.objects.get(contactno=custid)
            bookedby=cust.name
            contactno=cust.contactno
            bookingdate=datetime.datetime.today()
            Booking(carid=cid,bookedby=bookedby,contactno=contactno,carname=carname,carno=carno,drivername=drivername,carrent=carrent,bookingdate=bookingdate).save()
            CarInfo.objects.filter(carid=cid).update(availability='booked')
            return redirect('custapp:viewcars')
    except KeyError:
        return redirect('mainapp:login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewbookings(request):
    try:
        if request.session['custid']!=None:
            custid=request.session['custid']
            custname=Customer.objects.get(contactno=custid).name
            booking=Booking.objects.filter(contactno=custid)
            return render(request,'viewbookings.html',locals())
    except KeyError:
        return redirect('mainapp:login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def response(request):
    try:
        if request.session['custid']!=None:
            custid=request.session['custid']
            custname=Customer.objects.get(contactno=custid).name
            cust=Customer.objects.get(contactno=custid)
            if request.method=='POST':
                responsetype=request.POST['responsetype']
                subject=request.POST['subject']
                message=request.POST['message']
                posteddate=datetime.datetime.today()
                givenby=cust.name
                contactno=cust.contactno                
                sr=Response(givenby=givenby,contactno=contactno,responsetype=responsetype,subject=subject,message=message,posteddate=posteddate)
                sr.save()
                messages.success(request,'Response is submitted')
            return render(request,'response.html',locals())
    except KeyError:
        return redirect('mainapp:login')


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def returncar(request,id):
    try:
        if request.session['custid']!=None:
            car = CarInfo.objects.get(carid=id)
            car.availability = 'available'
            car.save()
            Booking.objects.filter(carid=id).delete()
            messages.success(request, 'Car is returned')
            return redirect('custapp:viewcars')
    except KeyError:
        return redirect('mainapp:login')