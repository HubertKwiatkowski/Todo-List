from django.shortcuts import render

from .models import ListItem, Tag


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

def taskAdd(request):
    return render(request, 'todolist/task_add.html')

def taskRemove(request):
    return render(request, 'todolist/task_remove.html')