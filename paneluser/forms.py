from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.forms import fields


class SignUpForm(UserCreationForm):
    phonenumber = forms.CharField(label="شماره تلفن همراه",help_text="مثلا : 09121234567")
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'phonenumber' , 'password1' , 'password2')