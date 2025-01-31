from django.db import models

# Create your models here.
class CarInfo(models.Model):
    carid=models.AutoField(primary_key=True)
    carname=models.CharField(max_length=100)
    carno=models.CharField(max_length=50)
    drivername=models.CharField(max_length=50)
    carrent=models.IntegerField()
    carpic=models.FileField(upload_to='')
    availability=models.CharField(max_length=50)    
