from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User,orders,ticketpm,ticket
from django.forms import fields
from django.forms import ModelForm
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class SignUpForm(UserCreationForm):
    phonenumber = forms.CharField(label="شماره تلفن همراه",help_text="مثلا : 09121234567")
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'phonenumber' , 'password1' , 'password2')
        
class OrderProductForm(forms.Form):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    
    
class TicketForm(ModelForm):
    class Meta:
        model = ticketpm
        fields = ('text','attachment')
        
        
order_status = [
    ('created','دریافت شده'),
    ('customer_answer','پاسخ مشتری'),
    ('admin_answer','پاسخ فروشنده'),
    ('doing','در دست پیگیری'),
    ('closed','بسته شده'),
]
class Ticket2Form(ModelForm):
    select = forms.CharField(
        widget=forms.Select(choices=order_status),
    )
    class Meta:
        model = ticketpm
        fields = ('text','attachment')
    
    