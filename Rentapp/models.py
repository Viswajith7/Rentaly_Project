from django.db import models

# Create your models here.

class user_reg(models.Model):
    Name=models.CharField(max_length=34,null=True,blank=True)
    Email=models.EmailField(max_length=50,null=True,blank=True)
    Password=models.CharField(max_length=40,null=True,blank=True)
    Cpassword=models.CharField(max_length=45,null=True,blank=True)



class Booking(models.Model):
    PickupLocation=models.CharField(max_length=200,null=True,blank=True)
    DropoffLocation=models.CharField(max_length=100,null=True,blank=True)
    PickUpDate=models.CharField(max_length=10,null=True,blank=True)
    PickUpTime=models.TimeField(null=True,blank=True)
    No_days=models.IntegerField(null=True,blank=True)
    Totalprice=models.IntegerField(null=True,blank=True)
    Car=models.CharField(max_length=122,null=True,blank=True)
    User = models.CharField(max_length=45, null=True, blank=True)
    P_image=models.ImageField(upload_to='product',null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)


class Payment(models.Model):
    Fname=models.CharField(max_length=122,null=True,blank=True)
    sname=models.CharField(max_length=122,null=True,blank=True)
    Country=models.CharField(max_length=122,null=True,blank=True)
    Address=models.CharField(max_length=122,null=True,blank=True)
    City=models.CharField(max_length=122,null=True,blank=True)
    Pin=models.IntegerField(null=True,blank=True)
    Phone=models.IntegerField(null=True,blank=True)
    Email=models.EmailField(max_length=122,null=True,blank=True)
    Payment=models.CharField(max_length=122,null=True,blank=True)


