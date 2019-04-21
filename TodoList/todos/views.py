from django.shortcuts import render
from django.views.generic.edit import FormView
from .models import Tasks
from .forms import TasksForm

def index(request):
    tasks = Tasks.objects.all

    if request == 'POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            pass
        else:
            form = TasksForm()


    return render(request, 'todos/index.html', {'tasks':tasks, 'form':form  })