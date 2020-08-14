from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth.decorators import  login_required
from .decorators import unauthoncticated_user,allowed_users, admin_only


from .models import *
from .forms import  OrderForm, CreateUserForm, CustomerForm
from .filters import OrderFilter


#Registration View for customer
@unauthoncticated_user
def register_view(request):
    form = CreateUserForm()
    if request.method == 'POST' :
        form = CreateUserForm(request.POST)
        if form.is_valid() :   
            user = form.save()
            username = form.cleaned_data('username')
            group = Group.objects.get(name='admin')
            user.groups.add(group)
            Customer.objects.create(user = user)
            messages.success(request, f'Account was created for {username}')
                
            return redirect('login')  
    context={
        'form' : form
    }
    return render(request, 'accounts/register.html', context)

#Login View for customer


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password= password)
        if user is not None :
            login(request, user)
            return redirect('accounts:home')
        else:
            messages.info(request,'Username or password incorrect')
    
    context={}
    return render(request, 'accounts/login.html', context)

#logout View for cautomer
def log_out(request):
    logout(request)
    return redirect('login')




#Account settings
@login_required(login_url = 'login')
@allowed_users(allowed_roles=['customer','admin'])

def account_settings (request):
    customer = request.user.customer
    form = CustomerForm(instance = customer )
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        form.save()
    context = {'form': form}
    return render(request, 'accounts/account_setting.html', context)

#Customer View
@login_required(login_url = 'login')
@allowed_users(allowed_roles=['customer','admin'])

def user_view(request):
    orders = request.user.customer.order_set.all()
    total_orders = orders.count()
    pending = orders.filter(status ='Pending').count()
    out_for_delivery = orders.filter(status ='Out for delivery').count()
    delivered = orders.filter( status ='Delivered').count()
    context = {
       'orders' : orders,
        'total_orders' : total_orders,
        'pending' : pending,
        'out_for_delivery' : out_for_delivery,
        'delivered' : delivered,
    }
    return render(request, 'accounts/user.html', context)

#Dashboard View for super users 
@login_required(login_url='login')
@admin_only
def home_view(request):
    customers = Customer.objects.all()
    total_customers = customers.count()
    orders = Order.objects.all()
    total_orders = orders.count()
    pending = orders.filter(status ='Pending').count()
    out_for_delivery = orders.filter(status ='Out for delivery').count()
    delivered = orders.filter( status ='Delivered').count()
    context = {
        'customers' : customers,
        'total_customers' : total_customers, 
        'orders' : orders,
        'total_orders' : total_orders,
        'pending' : pending,
        'out_for_delivery' : out_for_delivery,
        'delivered' : delivered,
    }
    return render(request,'accounts/dashboard.html',  context )



#Products  View for super users
@login_required(login_url='login')
@allowed_users(allowed_roles = ['admin'])
def products_view(request):
    products = Product.objects.all()
    context = {
        'products' : products,
    }
    return render(request, 'accounts/products.html', context)



#Customer View for super users
@login_required(login_url='login')
@allowed_users(allowed_roles = ['customer', 'admin'])
def customer_view(request,pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    orders_count = orders.count()
    myfilter = OrderFilter(request.GET, queryset=orders)
    orders = myfilter.qs
    context =  {
        'myfilter': myfilter,
        'customer': customer,
        'orders' : orders,
        'orders_count' : orders_count
    }
    return render(request, 'accounts/customer.html', context)


#Create Order View for super users
@login_required(login_url='login')
@allowed_users(allowed_roles = ['admin'])
def create_Order (request,pk) :
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product','status' ), extra=3 )
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none() ,instance= customer)
    #form = OrderForm(initial={'customer': customer})
    
    formset = OrderFormSet( instance= customer)
    if request.method == 'POST':
        #form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance= customer)
        if formset.is_valid():
            formset.save()
            return redirect('home')
    context = {
      'formset'  :formset,
    
    }
    return render(request, 'accounts/order_form.html', context)


#Upadet order View for super users
@login_required(login_url='login')
@allowed_users(allowed_roles = ['admin'])
def update_Order (request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('home')
    context ={ 'form': form}
    return render(request, 'accounts/order_form.html', context)
    


#Delete View for super users
@login_required(login_url='login')  
@allowed_users(allowed_roles = ['admin'])
def delete_Order (request, pk) :
    order = Order.objects.get(id=pk)
    if request.POST == 'POST':
        order.delete()
        return redirect('home')
    context={
        'item' : order
    }
    return render(request, 'accounts/delete.html', context)