from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from .forms import TaskForm
from .models import *


def task_list(request):
    posts = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'posts':posts})


def task_detail(request, pk):
    post = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/task_detail.html', {'post': post})


def task_new(request):
    form = TaskForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print (request.POST)
        print (form.cleaned_data)
        data = form.cleaned_data
        print (data["title"])
        post = form.save(commit=False)

        new_form = form.save()
        return redirect('task_detail', pk=post.pk)
    else:
        form = TaskForm()
    return render(request, 'tasks/task_new.html', {'form': form})



def task_edit(request, pk):
    post = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('task_detail', pk=post.pk)
    else:
        form = TaskForm(instance=post)
    return render(request, 'tasks/task_new.html', {'form': form})


def task_remove(request, pk):
    post = get_object_or_404(Task, pk=pk)
    post.delete()
    return redirect('task_list_url')    