from django.db import models
from django.utils import timezone

class Tasks(models.Model):
    task_name = models.CharField(max_length = 100)
    date_set = models.DateTimeField()
    due_date = models.DateTimeField()

    def __str__(self):
        return self.task_name