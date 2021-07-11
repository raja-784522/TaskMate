from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.todo, name='todolist'),
    path('delete/<task_id>',views.delete_task,name='delete_task'),
    path('edit/<task_id>',views.edit_task,name='edit_task'),
    path('complete/<task_id>',views.complete_task,name='complete_task'),

]