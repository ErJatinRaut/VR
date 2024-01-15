from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def cust_registeration(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        mobile_number = request.POST.get('mobile_number')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')
        mydata = VrUser(first_name=first_name, last_name=last_name, email=email, mobile_number=mobile_number,is_Vruser=True,is_customer=True,is_active=True)
        mydata.set_password(password)
        mydata.save()

        
    return render(request,'login/customer_register.html')


def cust_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate user
        VrUser = authenticate(email=email, password=password)
        print("userr",VrUser)

        if VrUser is not None and VrUser.is_customer:
            # Log in the user
            login(request,VrUser)
            
            return redirect('/customer_after_login/')  
        else:
           
            error_message = "Invalid login credentials. Please try again."
            messages.error(request, error_message)
            # return render(request, 'registeration/customer_register.html', {'error_message': error_message})

    return render(request, 'login/customer_login.html')

@login_required
def customer_after_login(request):
    return render(request,"customer_base.html")


def seller_registeration(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        mobile_number = request.POST.get('mobile_number')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')
        mydata = VrUser(first_name=first_name, last_name=last_name, email=email,username=email, mobile_number=mobile_number,is_Vruser=True,is_active=True,is_seller=True)
        mydata.set_password(password)
        mydata.save()
    return render(request,'login/seller_registration.html')


def seller_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate user
        VrUser = authenticate(email=email, password=password)
        print("userr",VrUser)

        if VrUser is not None and VrUser.is_seller:
            # Log in the user
            login(request,VrUser)
            
            return redirect('/seller_dashboard/')  
        else:
           
            error_message = "Invalid login credentials. Please try again."
            messages.error(request, error_message)
            # return render(request, 'registeration/customer_register.html', {'error_message': error_message})

    return render(request, 'login/seller_login.html')

def seller_dashboard(request):
    return render(request,'seller_base.html')


def admin_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate user
        VrUser = authenticate(email=email, password=password)
        print("userr",VrUser)

        if VrUser is not None and VrUser.is_superuser:
            # Log in the user
            login(request,VrUser)
            
            return redirect('/admin_dashboard/')  
        else:
           
            error_message = "Invalid login credentials. Please try again."
            messages.error(request, error_message)
            # return render(request, 'registeration/customer_register.html', {'error_message': error_message})

    return render(request, 'login/admin_login.html')

def admin_dashboard(request):
    return render(request,'admin_base.html')
