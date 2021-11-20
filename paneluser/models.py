from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import files
from ckeditor_uploader.fields import RichTextUploadingField
import random

# Create your models here.
class User(AbstractUser):
    phonenumber= models.CharField(max_length=50,null=True,blank=True,verbose_name="شماره تلفن همراه")

class packs(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True,verbose_name="نام محصول")
    enable_check = models.BooleanField(default=False,verbose_name="محصول برای فروش فعال باشد؟")
    price = models.IntegerField(null=True,blank=True,verbose_name="قیمت")
    short_desc = RichTextUploadingField(null=True,blank=True,verbose_name="توضیح کوتاه")
    full_desc = RichTextUploadingField(null=True,blank=True,verbose_name="توضیحات کامل")
    def __str__(self):
        return self.name


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
    packs = models.ForeignKey("packs", on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.tracking_code

order_status = [
    ('pending_pay','در انتظار پرداخت'),
    ('doing','درحال انجام'),
    ('cancel','لغو شده'),
    ('edit','درحال ویرایش'),
    ('success','انجام شده'),
]

# ------------------ orderfile Path ------------------
def order_file_path(instance, filename):
    return 'uploads/orders/{0}'.format(filename)
# ------------------ /orderfile Path ------------------

class orders(models.Model):
    user = models.ForeignKey("User", on_delete=models.DO_NOTHING,verbose_name="کاربر")
    packs = models.ForeignKey("packs", on_delete=models.DO_NOTHING,verbose_name="محصول")
    status = models.CharField(max_length=256,null=True, choices=order_status,verbose_name="وضعیت")
    description = RichTextUploadingField(null=True,blank=True,verbose_name="توضیحات")
    attachment = models.FileField(null=True,blank=True,upload_to=order_file_path,verbose_name="پیوست")
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name + " " + self.packs.name + " " + str(self.id)


# ------------------ ticket Path ------------------
def ticket_file_path(instance, filename):
    return 'uploads/tickets/{0}'.format(filename)
# ------------------ /ticket Path ------------------

departments = [
    ('finance','فروش و مالی'),
    ('technical','فنی'),
    ('moderator','مدیریت'),
]
ticket_force = [
    ('very_important','خیلی'),
    ('important','مهم'),
    ('simple','عادی'),
]
order_status = [
    ('created','دریافت شده'),
    ('customer_answer','پاسخ مشتری'),
    ('admin_answer','پاسخ فروشنده'),
    ('doing','در دست پیگیری'),
    ('closed','بسته شده'),
]
class ticket(models.Model):
    user = models.ForeignKey("User", on_delete=models.DO_NOTHING,verbose_name="کاربر")
    order = models.ForeignKey("orders",blank=True,null=True, on_delete=models.DO_NOTHING,verbose_name="سفارش")
    depertment = models.CharField(max_length=256,null=True, choices=departments,verbose_name="دپارتمان")
    priority = models.CharField(max_length=256,null=True, choices=ticket_force,verbose_name="میزان اهمیت")
    status = models.CharField(max_length=256,null=True, choices=order_status,verbose_name="وضعیت")
    subject = models.CharField(max_length=256,blank=True,null=True,verbose_name="عنوان")
    text = RichTextUploadingField(null=True,blank=True,verbose_name="متن پیام")
    attachment = models.FileField(null=True,blank=True,upload_to=ticket_file_path,verbose_name="پیوست")
    def __str__(self):
        return self.subject
    
class ticketpm(models.Model):
    user = models.ForeignKey("User", on_delete=models.DO_NOTHING,verbose_name="کاربر")
    ticket = models.ForeignKey("ticket", on_delete=models.DO_NOTHING,verbose_name="تیکت")
    text = RichTextUploadingField(null=True,blank=True,verbose_name="متن")
    attachment = models.FileField(null=True,blank=True,upload_to=ticket_file_path,verbose_name="پیوست")
    def __str__(self):
        return self.ticket.subject + " " + self.id