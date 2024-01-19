from django.shortcuts import redirect, render
from .models import *
from .forms import *

# Create your views here.
def index(request):
    if request.method == 'POST':
        task = request.POST['task']
        priority = request.POST['priority']
        date = request.POST['date']
        desc = request.POST['desc']
        todo = Todo(task=task, priority=priority ,date=date, desc=desc)
        todo.save()
        return redirect('/')
    todo_task = Todo.objects.all()
    context = {
        'todo_task':todo_task
    }
    return render(request,'home.html',context)

def update(request,id):
    data = Todo.objects.get(id=id)
    form = UpdateForm(request.POST,request.FILES,instance=data)
    if form.is_valid():
        form.save()
        return redirect('/')
    form = UpdateForm(instance=data)
    return render(request,'update.html',{'form':form})

def delete(request,id):
    data = Todo.objects.get(id=id)
    data.delete()
    return redirect('/')