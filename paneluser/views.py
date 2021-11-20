from django.shortcuts import render
from .models import User,ticket,orders,payment,packs,ticketpm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from .forms import SignUpForm
from django.views.generic import View,ListView,DeleteView,UpdateView,CreateView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
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
    
    
#Products
    
class AdminProducts(ListView):
    model = packs
    paginate_by = 5

class ProductsDeleteView(DeleteView):
    model = packs
    success_url = '/administrator/products/'
    success_message = "پاکسازی انجام شد"
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ProductsDeleteView, self).delete(request, *args, **kwargs)

class ProductsUpdateView(SuccessMessageMixin,UpdateView):
    model = packs
    fields = '__all__'
    success_url = '/administrator/products/'
    success_message = "بروزرسانی انجام شد"

class ProductsCreateView(SuccessMessageMixin,CreateView):
    model = packs
    fields = '__all__'
    success_url = '/administrator/products/'
    success_message = "ساخت محصول انجام شد"


#Orders

class AdminOrders(ListView):
    model = orders
    paginate_by = 5
    
class OrdersDeleteView(DeleteView):
    model = orders
    success_url = '/administrator/orders/'
    success_message = "پاکسازی انجام شد"
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(OrdersDeleteView, self).delete(request, *args, **kwargs)

class OrdersUpdateView(SuccessMessageMixin,UpdateView):
    model = orders
    fields = '__all__'
    success_url = '/administrator/orders/'
    success_message = "بروزرسانی انجام شد"

class AdminUsers(ListView):
    model = User
    paginate_by = 5
    
class AdminTickets(ListView):
    model = ticket
    paginate_by = 5
    

