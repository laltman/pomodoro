from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from todo.models import Task
from todo.forms import TaskForm
from django.template import RequestContext
from django.core.urlresolvers import reverse
import datetime

# Create your views here.
def task_list(request):  
    todo_listing = []  
    for todo_task in Task.objects.all():  
        todo_dict = {}
        todo_dict['pk'] = todo_task.pk
        todo_dict['priority'] = todo_task.get_priority_display()
        todo_dict['task_object'] = todo_task  
        todo_dict['pom_count'] = todo_task.pomnumber
        todo_listing.append(todo_dict)
    return render_to_response('todolist.html', { 'todo_listing': todo_listing }, RequestContext(request))

def task_new(request):
    if request.method == "POST":
        form =TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect('/tasklist')
    else:
        form = TaskForm()
    return render(request, 'task_new.html', {'form': form})

def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect('/tasklist', pk=task.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_edit.html', {'form': form})

def delete(request, pk):
    task = get_object_or_404(Task, pk=pk).delete()
    return HttpResponseRedirect(reverse('todo.views.task_list'))

def pom(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'timer.html', {'task': task}, context_instance = RequestContext(request))

def complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if task.pomnumber == 1:
        task = get_object_or_404(Task, pk=pk).delete()
    else:
        task.pomnumber = task.pomnumber - 1
        task.save()
    return render(request, 'task_complete.html', {'task': task})
