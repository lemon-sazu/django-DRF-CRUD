from django.urls import path

from .views import *

urlpatterns = [
    path('',apiOverView),
    path('task-list/', taskList, name="task-list"),
    path('task-details/<str:pk>/', taskDetails, name="task-details"),
    path('task-create', taskCreate, name='task-create'),
    path('task-update/<str:pk>/', taskUpdate, name='task-update'),
    path('task-delete/<str:pk>/', taskDelete, name='task-delete'),
]