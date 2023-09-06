from django.db import models


# Create your models here.
class categorydb(models.Model):
    Category_Name = models.CharField(max_length=100, null=True, blank=True)
    Discription = models.CharField(max_length=100, null=True, blank=True)
    C_Image = models.ImageField(upload_to='category', null=True, blank=True)


class Productdb(models.Model):
    Category_names = models.CharField(max_length=100, null=True, blank=True)
    Car_name = models.CharField(max_length=100, null=True, blank=True)
    Model = models.IntegerField(null=True, blank=True)
    Hpower = models.IntegerField(null=True, blank=True)
    Ceat = models.IntegerField(null=True, blank=True)
    Body = models.IntegerField(null=True, blank=True)
    Price = models.CharField(max_length=100, null=True, blank=True)
    Colour = models.CharField(max_length=100, null=True, blank=True)
    Discriptions = models.CharField(max_length=500, null=True, blank=True)
    Transmission = models.CharField(max_length=500, null=True, blank=True)
    Airbag = models.IntegerField(null=True, blank=True)
    P_Image1 = models.ImageField(upload_to='product',null=True,blank=True)
    P_Image2 = models.ImageField(upload_to='product',null=True,blank=True)

    P_Image3 = models.ImageField(upload_to='product',null=True,blank=True)


class Contactdb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Number = models.IntegerField(null=True, blank=True)
    Message = models.CharField(max_length=1000, null=True, blank=True)
