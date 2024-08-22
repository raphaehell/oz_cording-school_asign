from django.shortcuts import render
from .models import Todo


def todo_list(request):
    todos = Todo.objects.all()

    return render(request, "todo_list.html", {"todos": todos})


def todo_detail(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)

    return render(request, "todo_info.html", {"todo": todo})
