from django.shortcuts import render
from .models import User,ticket,orders,payment,packs,ticketpm
# Create your views here.


def home(request):
    return render(request, "login.html")