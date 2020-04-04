from django.urls import path,include
from . import views

urlpatterns = [
    path('task_new', views.task_new, name='task_new_url'),                                
    path('task/<int:pk>', views.task_detail, name='task_detail'),
    path('task', views.task_list, name='task_list_url'),
    path('task/<int:pk>/edit', views.task_edit, name='task_edit_url'),
    path('task/<pk>/remove/', views.task_remove, name='task_remove_url'),                                        
]