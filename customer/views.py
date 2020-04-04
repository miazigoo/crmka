from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from .forms import CustomerForm
from .models import *


def customer_list(request):
    posts = Customer.objects.all()
    return render(request, 'customer/customer_list.html', {'posts':posts})


def customer_detail(request, pk):
    post = get_object_or_404(Customer, pk=pk)
    return render(request, 'customer/customer_detail.html', {'post': post})  


def customer_new(request):
    if request.method=="POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('customer_detail', pk=post.pk)                                                    
    else:
        form = CustomerForm()
    return render(request, 'customer/customer_new.html', {'form': form})



def customer_edit(request, pk):
    post = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('customer_detail', pk=post.pk)
    else:
        form = CustomerForm(instance=post)
    return render(request, 'customer/customer_new.html', {'form': form})