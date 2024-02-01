from django.db import models
import uuid
# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=200)
    id = models.UUIDField(default = uuid.uuid4, primary_key= True, 
                          unique = True ,editable=False)

    def __str__(self):
        return self.name
class projects(models.Model):
    project_name = models.CharField(max_length = 200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    id = models.UUIDField(default = uuid.uuid4, primary_key= True, 
                          unique = True ,editable=False)
    def __str__(self):
        return self.project_name

class task(models.Model):
    title = models.CharField(max_length= 200)
    project_name = models.ForeignKey(projects, on_delete = models.CASCADE)
    description = models.TextField()
    deadline = models.DateField()
    user = models.OneToOneField(Users,on_delete = models.CASCADE,null=True)   
    status_progress = (
        ("Complete","complete"),("in-progress","progress")
    )
    status = models.CharField(max_length = 2000,choices= status_progress, default ="progress")
   
