from django.urls import path

from . import views

urlpatterns = [
    path('', views.todoList, name='todolist'),
    path('<int:taskview_id>/', views.taskView, name='task_view'),
    path('taskadd/', views.taskAdd, name="task_add"),
    path('taskremove/', views.taskRemove, name="task_remove"),
]
