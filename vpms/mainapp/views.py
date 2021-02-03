from django.shortcuts import render,get_object_or_404, redirect
from .models import *
# Create your views here.
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
            data.order_price = (c_info.card_selling_price*data.quantity)
            data.save()
            form.save_m2m()
            return redirect('success')
    else:
        form = customer_input_form()
        return render(request, 'process.html', {"c_info":c_info,"form":form })

# from . forms import customer_input
def success(request):
    key_id="rzp_test_sSj3DF8kI97bSo" 
    key_secret="UtzDhOevixD28yF1DyrakRv1"

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