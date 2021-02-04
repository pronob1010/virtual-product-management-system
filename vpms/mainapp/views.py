from django.shortcuts import render,get_object_or_404, redirect,HttpResponse
from .models import *
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User

# Create your views here.
from django.contrib.auth.forms import AuthenticationForm
def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username = username , password = password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else: 
                return redirect('/')
        else:
            return redirect('/')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {"form":form})

def logout_user(request):
    logout(request)
    return redirect('/')

from . forms import RegistrationForm
def register_user(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form':form})


def index(request):
    cardlist = card.objects.all()
    return render(request, 'index.html', {"cardlist":cardlist})

from . forms import customer_input_form
def process(request, id):
    c_info = get_object_or_404(card, id=id)
    if request.method == "POST":
        form = customer_input_form(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.customer = request.user
            data.product = c_info
            data.order_price = (c_info.card_selling_price*data.quantity)
            
            data.save()
            form.save_m2m()
            return redirect('success')
    else:
        form = customer_input_form()
        return render(request, 'process.html', {"c_info":c_info,"form":form })

# from . forms import customer_input
def success(request):
    # data = get_object_or_404(customer_input, id=id)
    key_id="rzp_test_sSj3DF8kI97bSo" 
    key_secret="UtzDhOevixD28yF1DyrakRv1"

    # print(data)

    import razorpay 
    client = razorpay.Client(auth=(key_id, key_secret))
    user_name = request.user
    print(user_name)
    data = {
    'amount': 100*500,
    'currency':"BDT",
    'receipt': "test_order",
    'notes':{
        'user': "user_name",
        }
    }
    order = client.order.create(data=data)
    print(order)

    return render(request, 'success.html')