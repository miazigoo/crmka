from django.urls import path,include
from . import views

urlpatterns = [
    path('customer/', views.customer_list, name='customer_list_url'),                                
    path('customer/<int:pk>/', views.customer_detail, name='customer_detail'), 
    path('customer/new/', views.customer_new, name='customer_new_url'),
    path('customer/<int:pk>/edit/', views.customer_edit, name='customer_edit_url'),                                          
]