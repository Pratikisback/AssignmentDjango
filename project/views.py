from django.shortcuts import render, redirect
from .models import Users,projects,task
from .forms import TaskForm

# Create your views here.
def get_all_project(request):
    obj_project = projects.objects.all()
    context = {"projects":obj_project}
    return render(request,"project_list.html",context)

def get_single_project_details(request,pk):
    object_project = projects.objects.filter(id = pk)
    obj_task = task.objects.filter(project_name = pk)
    context = {"projects":object_project, "tasks":obj_task}
    return render(request,"single_project.html",context)

#This is for list of task
def get_all_task(request):
    obj_task = task.objects.all()
    context = {"tasks":obj_task}
    return render(request,"task_list.html",context)

def create_task(request):
    tasks = TaskForm()

    if request.method == "POST":
        tasks = TaskForm(request.POST)
        if tasks.is_valid():
            tasks.save()
            return redirect("all-task")

    context = {"tasks":tasks}
    return render(request,"task_form.html",context)

def update_task(request,pk):
    task_obj = task.objects.get(id=pk)
    print("This is line 37",task_obj)
    tasks = TaskForm(instance=task_obj)

    if request.method == "POST":
        tasks = TaskForm(request.POST,instance=task_obj)
        if tasks.is_valid():
            tasks.save()
            return redirect("all-task")

    context = {"tasks":tasks}
    return render(request,"task_form.html",context)

def dashboard(request):
    proj = projects.objects.filter(task__status ="Complete").distinct()
    context = {"proj":proj}
    return render(request,"dashboard.html",context)
