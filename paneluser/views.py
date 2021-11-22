from django.db.models.fields import Field
from django.shortcuts import render, redirect
from .models import User,ticket,orders,packs,ticketpm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from .forms import SignUpForm,OrderProductForm,TicketForm
from django.views.generic import View,ListView,DeleteView,UpdateView,CreateView,DetailView,FormView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
# Create your views here.

class AdminStaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

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


class AdminPanel(AdminStaffRequiredMixin,View):
    template_name = "dashboard.html"
    def get(self,request):
        ticketmodel = ticket.objects.all()
        ordersmodel = orders.objects.all()
        productsmodel = packs.objects.all()
        usersmodel = User.objects.all()
        context = {'ticket':ticketmodel,'orders':ordersmodel,'products':productsmodel,'user':usersmodel}
        return render(request,self.template_name,context=context)
    
    
#Products

class UserDashboard(LoginRequiredMixin,ListView):
    model = packs
    template_name = "dashboard-user.html"
    paginate_by = 9    

class AdminProducts(AdminStaffRequiredMixin,ListView):
    model = packs
    paginate_by = 5

class ProductsDeleteView(AdminStaffRequiredMixin,DeleteView):
    model = packs
    success_url = '/administrator/products/'
    success_message = "پاکسازی انجام شد"
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ProductsDeleteView, self).delete(request, *args, **kwargs)

class ProductsUpdateView(AdminStaffRequiredMixin,SuccessMessageMixin,UpdateView):
    model = packs
    fields = '__all__'
    success_url = '/administrator/products/'
    success_message = "بروزرسانی انجام شد"

class ProductsCreateView(AdminStaffRequiredMixin,SuccessMessageMixin,CreateView):
    model = packs
    fields = '__all__'
    success_url = '/administrator/products/'
    success_message = "ساخت محصول انجام شد"
    
class ProductsDetailView(LoginRequiredMixin,DetailView):
    model = packs


#Orders

class AdminOrders(AdminStaffRequiredMixin,ListView):
    model = orders
    paginate_by = 5
    
class UserOrders(LoginRequiredMixin,ListView):
    paginate_by = 5
    template_name = "paneluser/orders_list2.html"
    def get_queryset(self):
        queryset = orders.objects.filter(user=self.request.user)
        return queryset
    
class OrdersDetailView(LoginRequiredMixin,DetailView):
    model = orders
    
class OrdersDeleteView(AdminStaffRequiredMixin,DeleteView):
    model = orders
    success_url = '/administrator/orders/'
    success_message = "پاکسازی انجام شد"
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(OrdersDeleteView, self).delete(request, *args, **kwargs)

class OrdersUpdateView(AdminStaffRequiredMixin,SuccessMessageMixin,UpdateView):
    model = orders
    fields = '__all__'
    success_url = '/administrator/orders/'
    success_message = "بروزرسانی انجام شد"

class OrderPurchase(LoginRequiredMixin,SuccessMessageMixin,FormView):
    form_class = OrderProductForm
    template_name = "paneluser/ordering.html"
    success_url ="/usercp/orders/"
    success_message = "سفارش ثبت شد"
    def form_valid(self, form):
        mypacks = packs.objects.get(id=self.kwargs['orderid'])
        order = orders(
            user = self.request.user,
            status = "doing",
            description=form.cleaned_data['description'],
            packs = mypacks,
        )
        order.save()
        return super(OrderPurchase, self).form_valid(form)
    
#Users

class AdminUsers(AdminStaffRequiredMixin,ListView):
    model = User
    paginate_by = 5
    
class UserDeleteView(AdminStaffRequiredMixin,DeleteView):
    model = User
    success_url = '/administrator/users/'
    success_message = "پاکسازی انجام شد"
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(UserDeleteView, self).delete(request, *args, **kwargs)

class UserUpdateView(AdminStaffRequiredMixin,SuccessMessageMixin,UpdateView):
    model = User
    fields = ['username','first_name','last_name','password','phonenumber','email','is_superuser','is_staff']
    success_url = '/administrator/users/'
    success_message = "بروزرسانی انجام شد"
    
    
#ticket

class AdminTickets(AdminStaffRequiredMixin,ListView):
    model = ticket
    paginate_by = 5
    

class UserTickets(LoginRequiredMixin,ListView):
    model = ticket
    template_name = "paneluser/ticket_list2.html"
    paginate_by = 5
    
class TicketDeleteView(AdminStaffRequiredMixin,DeleteView):
    model = ticket
    success_url = '/administrator/users/'
    success_message = "پاکسازی انجام شد"
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(TicketDeleteView, self).delete(request, *args, **kwargs)
    
class TicketCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = ticket
    fields = ['order','depertment','priority','subject','text','attachment']
    template_name = "paneluser/ticket_form2.html"
    success_url = '/usercp/tickets/'
    success_message = "ساخت تیکت انجام شد"
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.status = 'created'
        return super().form_valid(form)
    
    
class AdminTicketCreateView(AdminStaffRequiredMixin,SuccessMessageMixin,CreateView):
    model = ticket
    fields = '__all__'
    success_url = '/administrator/tickets/'
    success_message = "ساخت تیکت انجام شد"
    
class UserUpdateTicketView(LoginRequiredMixin,SuccessMessageMixin,View):
    template_name="paneluser/ticket_update.html"
    form_class = TicketForm
    def get(self,request,ticketid):
        ticketid = ticket.objects.get(id=ticketid)
        ticketpms = ticketpm.objects.filter(ticketid=ticketid)
        form = self.form_class
        context = {'form':form,'ticketpms':ticketpms,'ticketid':ticketid}
        return render(request,self.template_name,context=context)
    def post(self,request,ticketid):
        ticketid = ticket.objects.get(id=ticketid)
        ticketpms = ticketpm.objects.filter(ticketid=ticketid)
        form = self.form_class(request.POST)
        if form.is_valid():
            desc = request.POST.get('text')
            attach = request.POST.get('attachment')
            ticketpm1 = ticketpm(user=request.user,ticketid=ticketid,text=desc,attachment=attach)
            ticketid.status = "customer_answer"
            ticketid.save()
            ticketpm1.save()
        context = {'form':form,'ticketpms':ticketpms,'ticketid':ticketid}
        return render(request,self.template_name,context=context)