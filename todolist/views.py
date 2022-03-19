from django.http import HttpResponseRedirect
from django.shortcuts import render

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

# def taskAdd(request):
#     if request.method == 'POST':
#         form = ItemForm(request.POST)
#         if form.is_valid():
#             tnav = form.cleaned_data("taskName")
#             tddv = form.cleaned_data("taslDone")
#             tnov = form.cleaned_data["taskNote"]
#             tsdv = form.cleaned_data["taskStartDate"]
#             tdlv = form.cleaned_data["taskDeadline"]
#             newItem = ItemForm(
#                 taskName = tnav,
#                 taskDone = tddv,
#                 taskNote = tnov,
#                 taskStartDate = tsdv,
#                 taskDeadline = tdlv)
#             newItem.save()
#             return HttpResponseRedirect('/')

#     else:
#         form = ItemForm()

#     context = {
#         'form': form,
#         }

#     return render(request, 'todolist/task_add.html', context)

# def taskAdd(request):
#     taskNameValue = ''
#     taskNoteValue = ''
#     taskStartDateValue = ''
#     taskDeadlineValue = ''

#     if request.method == 'POST':
#         form = ItemForm(request.POST)
#         if form.is_valid():
#             taskNameValue = form.cleaned_data.get("taskName")
#             taskNoteValue = form.cleaned_data.get("taskNote")
#             taskStartDateValue = form.cleaned_data.get("taskStartDate")
#             taskDeadlineValue = form.cleaned_data.get("taskDeadline")
#             return HttpResponseRedirect('/')

#     else:
#         form = ItemForm()

#     context = {
#         'form': form,
#         'taskNameValue': taskNameValue,
#         'taskNoteValue': taskNoteValue,
#         'taskStartDateValue': taskStartDateValue,
#         'taskDeadlineValue': taskDeadlineValue,
#         }

#     return render(request, 'todolist/task_add.html', context)

def taskRemove(request):
    return render(request, 'todolist/task_remove.html')