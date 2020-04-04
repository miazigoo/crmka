from django.urls import path,include
from . import views

urlpatterns = [
    path('order', views.post_list, name='order_url'),                                
    path('post/<int:pk>/', views.post_detail, name='post_detail_url'), 
    path('post/new/', views.post_new, name='post_new_url'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit_url'),                                          
]