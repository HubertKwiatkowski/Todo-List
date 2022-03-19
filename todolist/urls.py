from django.urls import path

from . import views

urlpatterns = [
    path('', views.todoList, name='todolist'),
    path('<int:taskview_id>/', views.taskView, name='task_view'),
    path('task_add/', views.taskAdd, name="task_add"),
    path('tag_add/', views.tagAdd, name="tag_add"),
    path('task_remove/', views.taskRemove, name="task_remove"),
]
