from django.shortcuts import render,HttpResponseRedirect,get_object_or_404
from .forms import TaskForm
from .models import Task
from django.urls import reverse

# Create your views here.
def createTask(request):
    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('viewTask'))
    else:
        form = TaskForm()
    return render(request,"homePage.html",{"form":form})

def viewTask(request):
    tasks = Task.objects.all()
    return render(request,"viewTask.html",{"tasks":tasks})

def deleteTask(request,id):
    task = get_object_or_404(Task,pk=id)
    task.delete()
    return HttpResponseRedirect(reverse('viewTask'))