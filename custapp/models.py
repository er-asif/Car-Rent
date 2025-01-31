from django.db import models

# Create your models here.
class Booking(models.Model):
    bid=models.AutoField(primary_key=True)
    carid=models.IntegerField()
    bookedby=models.CharField(max_length=50)
    contactno=models.CharField(max_length=10)
    carname=models.CharField(max_length=100)
    carno=models.CharField(max_length=50)
    drivername=models.CharField(max_length=50)
    carrent=models.IntegerField()
    bookingdate=models.CharField(max_length=30)
class Response(models.Model):
    givenby=models.CharField(max_length=50)
    contactno=models.CharField(max_length=10)
    responsetype=models.CharField(max_length=50)
    subject=models.CharField(max_length=500)
    message=models.CharField(max_length=5000)
    posteddate=models.CharField(max_length=30)
