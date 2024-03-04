from django.urls import path
from . import views

urlpatterns = [
   #path('', views.home, name='home'),
   path('index/', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('orders/', views.orders, name='orders'),
    #path('products/', views.products, name='products'),
    path('deliveries/', views.deliveries, name='deliveries'),
    path('transfers/', views.transfers, name='transfers'),
    path('returns/', views.returns, name='returns'),
    path('disposals/', views.disposals, name='disposals'),
    path('customers/', views.customers, name='customers'),
    path('vehicles/', views.vehicles, name='vehicles'),
    path('users/', views.users, name='users'),
    path('routes/', views.routes, name='routes'),
    path('reports/', views.reports, name='reports'),
    path('settings/', views.settings, name='settings'),
    path('get_help/', views.get_help, name='get_help'),
    path('customers_index/', views.customers_index, name='customers_index'),
]