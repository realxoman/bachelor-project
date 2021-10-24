from django.db import models

# Create your models here.
class packs(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    enable_check = models.BooleanField(default=False)
    price = models.IntegerField(null=True,blank=True)
    short_desc = models.TextField(null=True,blank=True)
    full_desc = models.TextField(null=True,blank=True)
    def __str__(self):
        return name

class payment(models.Model):


    packs = models.ForeignKey("packs")
    def __str__(self):
        return transactionid

class orders(models.Model):


    packs = models.ForeignKey("packs")
    def __str__(self):
        return user.first_name + " " + user.last_name + " " + packs.name + " " + id