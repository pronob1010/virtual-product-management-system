from django.shortcuts import render,get_object_or_404
from .models import *
# Create your views here.
def index(request):
    cardlist = card.objects.all()
    return render(request, 'index.html', {"cardlist":cardlist})

def process(request, id):
    c_info = get_object_or_404(card, id=id)
    print(c_info)
    return render(request, 'process.html', {"c_info":c_info})