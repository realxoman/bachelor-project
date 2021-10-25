from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    phonenumber= models.CharField(max_length=50,null=True,blank=True)

class packs(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    enable_check = models.BooleanField(default=False)
    price = models.IntegerField(null=True,blank=True)
    short_desc = models.TextField(null=True,blank=True)
    full_desc = models.TextField(null=True,blank=True)
    def __str__(self):
        return name

class payment(models.Model):
    userid = models.ForeignKey("User", on_delete=models.DO_NOTHING)
    order_id = models.CharField(max_length=256,blank=True,null=True,unique=True)
    amount = models.CharField(max_length=256,blank=True,null=True)
    refnum = models.CharField(max_length=256,blank=True,null=True)
    irtoken = models.CharField(max_length=256,blank=True,null=True)
    transaction_id = models.CharField(max_length=256,blank=True,null=True)
    cardnum = models.CharField(max_length=256,blank=True,null=True)
    tracking_code = models.CharField(max_length=256,blank=True,null=True)
    verify_check = models.BooleanField(default=False,verbose_name="Purchase okay?")
    final_code = models.CharField(max_length=256,blank=True,null=True)
    packs = models.ForeignKey("packs")

    def __str__(self):
        return tracking_code

class orders(models.Model):
    user = models.ForeignKey("User", on_delete=models.DO_NOTHING)
    packs = models.ForeignKey("packs")
    def __str__(self):
        return user.first_name + " " + user.last_name + " " + packs.name + " " + id

class ticket(models.Model):

    def __str__(self):
        return subject
    
class ticketpm(models.Model):

    def __str__(self):
        return ticket.subject + " " + id