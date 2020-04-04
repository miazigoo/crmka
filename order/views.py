from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import *
from .forms import PostForm
from Tasks.models import Task
from django.urls import reverse
from customer.models import Customer
from customer.forms import CustomerForm

from django.shortcuts import redirect


def post_list(request):
    posts = Post.objects.order_by('-pk')
    tasks = Task.objects.all()
    
    return render(request, 'order/post_list.html', {'posts':posts, 'tasks':tasks})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'order/post_detail.html', {'post':post})

def post_new(request):
	if request.method=="POST":
	    form = PostForm(request.POST)
	    if form.is_valid():
	        post = form.save(commit=False)
	        post.author = request.user
	        post.id=post.pk
	        post.published_date = timezone.now()
	        post.save()
	        return redirect('post_detail_url', pk=post.pk)                                                    
	else:
	    form = PostForm()
	return render(request, 'order/post_edit.html', {'form':form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail_url', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'order/post_edit.html', {'form':form})
