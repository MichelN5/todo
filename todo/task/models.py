from django.db import models

# Create your models here.
class Task(models.Model):
    TODO= 'todo'
    DONE= 'done'
    status_choices= (
        (TODO, 'Todo'),
        (DONE, 'Done')
    )
    task_desc= models.CharField(max_length=255)
    status= models.CharField(max_length=10, choices=status_choices,default=TODO)

