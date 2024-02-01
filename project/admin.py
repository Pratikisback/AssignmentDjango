from django.contrib import admin
from .models import projects,task,Users
# Register your models here.
@admin.register(projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ["project_name","start_date","end_date","id"]

@admin.register(task)
class TaskAdmin(admin.ModelAdmin):
    list_display  =["title","project_name","deadline","status","id"]

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ["name"]
    