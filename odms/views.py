from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# from .models import Product

@login_required
def index(request):
    return render(request, 'index.html', {})

@login_required
def home(request):
    return render(request, 'home.html', {})

@login_required
def orders(request):
    return render(request, 'orders.html', {})

@login_required
def deliveries(request):
    return render(request, 'deliveries.html', {})

@login_required
def transfers(request):
    return render(request, 'transfers.html', {})

@login_required
def returns(request):
    return render(request, 'returns.html', {})

@login_required
def disposals(request):
    return render(request, 'disposals.html', {})

@login_required
def customers(request):
    return render(request, 'customers.html', {})

#@login_required
#def products(request):
 #   product_list = Product.objects.all()
           
    return render(request, 'products.html', {'product_list': product_list})

@login_required
def vehicles(request):
    return render(request, 'vehicles.html', {})

@login_required
def users(request):
    return render(request, 'users.html', {})

@login_required
def routes(request):
    return render(request, 'routes.html', {})

@login_required
def reports(request):
    return render(request, 'reports.html', {})

@login_required
def settings(request):
    return render(request, 'settings.html', {})

@login_required
def get_help(request):
    return render(request, 'get_help.html', {})

@login_required
def customers_index(request):
    return render(request, 'customers_index.html', {})

@login_required
def index(request):
    return render(request, 'index.html', {})