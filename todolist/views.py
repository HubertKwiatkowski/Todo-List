from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .models import *
from .forms import *

""" MAIN APP"""
def mainPage(request):
    return render(request, 'main/index.html')


""" USERS management """

def userRegistration(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registraton successful.")
            return redirect('main_page')
        messages.error(request, "Unsuccessful registration.")
    form = NewUserForm()
    context = {
        'form': form
    }
    return render(request, 'main/register.html', context)


def userLogin(request):
    pass


def userLogout(request):
    pass


""" TASKS management """

def todoList(request):
    tagList = Tag.objects.all()
    itemList = ListItem.objects.all()
    context = {
        'itemList': itemList,
        'tagList': tagList,
    }
    return render(request, 'todolist/tasks_view.html', context)

def taskView(request, taskview_id):
    item = ListItem.objects.get(id=taskview_id)
    context = {
        'item': item,
    }
    return render(request, 'todolist/task_view.html', context)

def taskAdd(response):
    if response.method == 'POST':
        form = ItemForm(response.POST)
        if form.is_valid():
            tnav = form.cleaned_data["task_name"]
            tsv = form.cleaned_data["task_status"]
            tddv = form.cleaned_data["task_done"]
            tnov = form.cleaned_data["task_note"]
            tsdv = form.cleaned_data["task_start_date"]
            tstv = form.cleaned_data["task_start_time"]
            tedv = form.cleaned_data["task_end_date"]
            tetv = form.cleaned_data["task_end_time"]
            ttv = form.cleaned_data["task_tags"]
            newItem = ListItem(
                task_name = tnav,
                task_status = tsv,
                task_done = tddv, 
                task_note = tnov, 
                task_start_date = tsdv, 
                task_start_time = tstv, 
                task_end_date = tedv,
                task_end_time = tetv,
                task_tags = ttv
                )
            newItem.save()
            return HttpResponseRedirect('/tasks_view/')
    else:
        form = ItemForm()
    context = {
        'form': form,
        }
    return render(response, 'todolist/task_add.html', context)

def taskEdit(request, taskedit_id):
    task = ListItem.objects.get(id=taskedit_id)
    if request.method == 'GET':
        form = ItemForm(instance=task)
    else:
        form = ItemForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/tasks_view/')
    context = {
        'form': form,
    }
    return render(request, 'todolist/task_edit.html', context)

def taskRemove(request, taskremove_id):
    task = ListItem.objects.get(id=taskremove_id)
    task.delete()
    context = {
        'task': task,
    }
    return render(request, 'todolist/task_remove.html', context)

def taskDone(request, taskdone_id):
    task = ListItem.objects.get(id=taskdone_id)
    if task.task_done == False:
        task.task_done = True
    else:
        task.task_done = False
    task.save()
    context = {
        'task': task,
    }
    return render(request, 'todolist/task_done.html', context)

""" TAGS management """

def tagsView(request):
    tagList = Tag.objects.all()
    context = {
        'tagList': tagList,
    }
    return render(request, 'todolist/tags_view.html', context)

def tagView(request, tagview_id):
    tag = Tag.objects.get(id=tagview_id)
    context = {
        'tag': tag,
    }
    return render(request, 'todolist/tag_view.html', context)

def tagEdit(request, tagedit_id):
    tag = Tag.objects.get(id=tagedit_id)
    if request.method == 'GET':
        form = TagForm(instance=tag)
    else:
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            return redirect('tags_view')
    context = {
        'form': form,
    }
    return render(request, 'todolist/tag_edit.html', context)

def tagAdd(response):
    if response.method == 'POST':
        form = TagForm(response.POST)
        if form.is_valid():
            n = form.cleaned_data["tag_name"]
            c = form.cleaned_data["tag_color"]
            newTag = Tag(
                tag_name=n, 
                tag_color=c
            )
            newTag.save()
            return HttpResponseRedirect('/tasks_view/')
    else:
        form = TagForm()
    context = {
        'form': form,
        }
    return render(response, 'todolist/tag_add.html', context)

def tagRemove(request, tagremove_id):
    tag = Tag.objects.get(id=tagremove_id)
    tag.delete()
    context = {
        'tag': tag,
    }
    return render(request, 'todolist/tag_remove.html', context)