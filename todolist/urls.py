from django.urls import path

from . import views

urlpatterns = [
    path('', views.mainPage, name='main_page'),
    path('tasks_view/', views.todoList, name='todolist'),
    path('task_view/<int:taskview_id>/', views.taskView, name='task_view'),
    path('task_add/', views.taskAdd, name='task_add'),
    path('task_edit/<int:taskedit_id>/', views.taskEdit, name='task_edit'),
    path('task_remove/<int:taskremove_id>/', views.taskRemove, name='task_remove'),
    path('task_done/<int:taskdone_id>/', views.taskDone, name='task_done'),
    path('tags_view/', views.tagsView, name='tags_view'),
    path('tag_view/<int:tagview_id>/', views.tagView, name='tag_view'),
    path('tag_add/', views.tagAdd, name='tag_add'),
    path('tag_edit/<int:tagedit_id>/', views.tagEdit, name='tag_edit'),
    path('tag_remove/<int:tagremove_id>/', views.tagRemove, name='tag_remove'),

]
