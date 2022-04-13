from django.urls import path

from . import views

urlpatterns = [
    path('', views.mainPage, name='main_page'),
    path('register/', views.userRegistration, name='user_register'),
    path('login/', views.userLogin, name='user_login'),
    path('logout/', views.userLogout, name='user_logout'),
    path('tasks_view/', views.todoList, name='todolist'),
    path('task_view/<int:taskView_id>/', views.taskView, name='task_view'),
    path('task_add/', views.taskAdd, name='task_add'),
    path('task_edit/<int:taskEdit_id>/', views.taskEdit, name='task_edit'),
    path('task_remove/<int:taskRemove_id>/', views.taskRemove, name='task_remove'),
    path('task_undo_remove/<int:taskUndoRemove_id>/', views.taskUndoRemove, name='task_undo_remove'),
    path('task_perma_remove/<int:taskPermaRemove_id>/', views.taskPermaRemove, name='task_perma_remove'),
    path('task_done/<int:taskDone_id>/', views.taskDone, name='task_done'),
    path('tags_view/', views.tagsView, name='tags_view'),
    path('tag_view/<int:tagView_id>/', views.tagView, name='tag_view'),
    path('tag_add/', views.tagAdd, name='tag_add'),
    path('tag_edit/<int:tagEdit_id>/', views.tagEdit, name='tag_edit'),
    path('tag_remove/', views.tagRemove, name='tag_remove'),
]