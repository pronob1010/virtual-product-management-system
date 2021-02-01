from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.models import User
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
            data.save()
            form.save_m2m()
            return redirect('success')
    else:
        form = customer_input_form()
         
        return render(request, 'process.html', {"c_info":c_info,"form":form })

def success(request):
    return render(request, 'success.html')