from django.shortcuts import render
from .models import User,ticket,orders,payment,packs,ticketpm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from .forms import SignUpForm
from django.views.generic import View
# Create your views here.

def signup(request):
    payam = "شما در حال ساخت کاربر جدید هستید."
    if request.user.is_authenticated:
        return HttpResponseRedirect("/")
    else:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save()
                user.refresh_from_db()  # load the profile instance created by the signal
                user.phonenumber = form.cleaned_data.get('phonenumber')
                user.save()
                payam = "کاربر ساخته شد."
                render(request, 'signup.html', {'form': form , 'payam' : payam})
        else:
            form = SignUpForm()
        return render(request, 'signup.html', {'form': form , 'payam' : payam})
        

def login_(request):
    error=False
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            if request.user.is_staff:
                return HttpResponseRedirect("/administrator/")
            else:
                return HttpResponseRedirect("/usercp/")
        elif user is None:
            return render(request, "login.html")
    if request.user.is_authenticated:
        if request.user.is_staff:
            return HttpResponseRedirect("/administrator/")
        else:
            return HttpResponseRedirect("/usercp/")
    else:
        return render(request, "login.html", {"error":error})
    
def logout_(request):
    logout(request)
    return HttpResponseRedirect("/")


class AdminPanel(View):
    template_name = "dashboard.html"
    
    def get(self,request):
        return render(request,self.template_name)
    
class AdminProducts(View):
    template_name = "products.html"
    
    def get(self,request):
        return render(request,self.template_name)
    
class AdminOrders(View):
    template_name = "dashboard.html"
    
    def get(self,request):
        return render(request,self.template_name)

class AdminUsers(View):
    template_name = "dashboard.html"
    
    def get(self,request):
        return render(request,self.template_name)
    
class AdminTickets(View):
    template_name = "dashboard.html"
    
    def get(self,request):
        return render(request,self.template_name)