from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .models import ListItem, Tag
from .forms import ItemForm, TagForm


def todoList(request):
    tagList = Tag.objects.all()
    itemList = ListItem.objects.all()
    context = {
        'itemList': itemList,
        'tagList': tagList,
    }
    return render(request, 'todolist/index.html', context)

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
            tnav = form.cleaned_data["taskName"]
            tddv = form.cleaned_data["taskDone"]
            tnov = form.cleaned_data["taskNote"]
            tsdv = form.cleaned_data["taskStartDate"]
            tstv = form.cleaned_data["taskStartTime"]
            tedv = form.cleaned_data["taskEndDate"]
            tetv = form.cleaned_data["taskEndTime"]
            # ttv = form.cleaned_data["taskTag"]
            newItem = ListItem(
                taskName = tnav, 
                taskDone = tddv, 
                taskNote = tnov, 
                taskStartDate = tsdv, 
                taskStartTime = tstv, 
                taskEndDate = tedv,
                taskEndTime = tetv)
            newItem.save()
            return HttpResponseRedirect('/')

    else:
        form = ItemForm()

    context = {
        'form': form,
        }

    return render(response, 'todolist/task_add.html', context)

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
            return redirect('tagEdit')
    context = {
        'form': form,
    }
    return render (request, 'todolist/tag_edit.html', context)

def tagAdd(response):
    if response.method == 'POST':
        form = TagForm(response.POST)
        if form.is_valid():
            n = form.cleaned_data["tagName"]
            c = form.cleaned_data["tagColor"]
            newTag = Tag(tagName=n, tagColor=c)
            newTag.save()
            return HttpResponseRedirect('/')

    else:
        form = TagForm()

    context = {
        'form': form,
        }

    return render(response, 'todolist/tag_add.html', context)

def taskRemove(request):
    return render(request, 'todolist/task_remove.html')