from django.shortcuts import render
from .models import product
from django.http import HttpResponse
# Create your views here.

def product_list(req):
   products =  product.objects.all()
   return render(req, 'index.html', {'products':products})

def home(req):
   return HttpResponse('<h1> Hello, World! </h1> ')



