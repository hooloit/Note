from .models import Task
from .form import TaskForm
from django.shortcuts import render, redirect


def task(request):
    tasks = Task.objects.order_by("id")
    return render(request, 'task.html', {'title': 'Не главаня страница сайта', 'tasks': tasks})


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/create')
        else:
            error = 'Форма была не коректна'
    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'create.html', context)