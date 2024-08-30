from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo, name='todo'),
    path('<int:todo_id>/', views.todo_info, name='todo_info'),
    path('create/',views.todo_create, name='todo_create'),
    path('<int:todo_id>/update', views.todo_update, name='todo_update'),
    path('<int:todo_id>/delete', views.todo_delete, name='todo_delete'),
]