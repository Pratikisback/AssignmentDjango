from django.urls import path
from .views import get_all_project,get_single_project_details,get_all_task,\
    create_task,update_task,dashboard
urlpatterns = [
    path("",get_all_project,name="all-projects"),
    path("single-project/<str:pk>/",get_single_project_details,name="single-project"),
    path("all-task/",get_all_task,name="all-task"),
    path("create-task/",create_task,name="create-task"),
    path("update-task/<str:pk>/",update_task,name = "update-task"),
    path("dashboard/", dashboard,name= "dashboard"),
]
