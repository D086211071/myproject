from django.db import models
from django.db import models
class registerforms(models.Model):
    First_Name=models.CharField(max_length=30)
    Last_Name=models.CharField(max_length=30)
    Mobile_Number=models.IntegerField()
    Adhar_Number=models.CharField(max_length=20)
    Date_Of_Birth = models.DateField()
    Sex = models.CharField(max_length=10)
    Hospital_Name = models.CharField(max_length=100)
    Address = models.TextField(max_length=100)
    Doctor_Appointment_Date=models.DateField(blank=True,null=True)
    Slot_Booking_Date = models.DateTimeField(auto_now=True)
class authentication(models.Model):
    Hospital_Name=models.CharField(max_length=50)
    Mobile_Number=models.IntegerField()
    User_Name=models.IntegerField()
    Password=models.CharField(max_length=20)
class superusers(models.Model):
    Username=models.IntegerField()
    Password=models.CharField(max_length=20)






