from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

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
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in as {username}.')
                return redirect('main_page')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'main/login.html', context)


def userLogout(request):
    logout(request)
    return redirect('main_page')

""" TASKS management """

def todoList(request):
    tagList = Tag.objects.all()
    itemList = ListItem.objects.all()
    itemCount = ListItem.objects.filter(task_done=False).filter(task_trash=False)
    doneCount = ListItem.objects.filter(task_done=True).filter(task_trash=False)
    trashCount = ListItem.objects.filter(task_trash=True)
    context = {
        'itemList': itemList,
        'tagList': tagList,
        'itemCount': itemCount,
        'doneCount': doneCount,
        'trashCount': trashCount,
    }
    return render(request, 'todolist/tasks_view.html', context)

def taskView(request, taskView_id):
    item = ListItem.objects.get(id=taskView_id)
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

def taskEdit(request, taskEdit_id):
    task = ListItem.objects.get(id=taskEdit_id)
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

def taskRemove(request, taskRemove_id):
    task = ListItem.objects.get(id=taskRemove_id)
    if task.task_trash == False:
        task.task_trash = True
    else:
        task.trash = False
    task.save()
    return HttpResponseRedirect('/tasks_view/')

def taskUndoRemove(request, taskUndoRemove_id):
    task = ListItem.objects.get(id=taskUndoRemove_id)
    task.task_trash = False
    task.save()
    return HttpResponseRedirect('/tasks_view/')

def taskPermaRemove(request, taskPermaRemove_id):
    task = ListItem.objects.get(id=taskPermaRemove_id)
    if task.task_trash == True:
        task.delete()
    return HttpResponseRedirect('/tasks_view/')

def taskDone(request, taskDone_id):
    task = ListItem.objects.get(id=taskDone_id)
    if task.task_done == False:
        task.task_done = True
    else:
        task.task_done = False
    task.save()
    return HttpResponseRedirect('/tasks_view/')

""" TAGS management """

def tagsView(request):
    tagList = Tag.objects.all()
    context = {
        'tagList': tagList,
    }
    return render(request, 'todolist/tags_view.html', context)

def tagView(request, tagView_id):
    tag = Tag.objects.get(id=tagView_id)
    context = {
        'tag': tag,
    }
    return render(request, 'todolist/tag_view.html', context)

def tagEdit(request, tagEdit_id):
    tag = Tag.objects.get(id=tagEdit_id)
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

def tagRemove(request, tagRemove_id):
    tag = Tag.objects.get(id=tagRemove_id)
    tag.delete()
    return HttpResponseRedirect('/tags_view/')