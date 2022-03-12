from django.urls import path

from . import views

urlpatterns = [
    path('', views.todoList, name='todolist'),
    path('<int:taskview_id>/', views.taskView, name='taskview'),
    # path('taskadd/', views.)
]
