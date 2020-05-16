from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

def index(request):
	products = Product.objects.all()
	return render(request,'index.html', {'products':products})



def new(request):
	return HttpResponse('New products')


def sales(request):
	return HttpResponse('Products on sales!')


def details(request):
	return HttpResponse('Products details ...')
