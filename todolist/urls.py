from django.urls import path

from . import views

urlpatterns = [
    path('', views.todoList, name='todolist'),
    path('tasksview/<int:taskview_id>/', views.taskView, name='task_view'),
    path('task_add/', views.taskAdd, name="task_add"),
    path('task_remove/', views.taskRemove, name="task_remove"),
    path('tags_view/', views.tagsView, name='tags_view'),
    path('tag_view/<int:tagview_id>/', views.tagView, name='tag_view'),
    path('tag_add/', views.tagAdd, name="tag_add"),
    path('tag_edit/<int:tagedit_id>/', views.tagEdit, name="tag_edit"),

]
