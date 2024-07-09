from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=200)
    task_description = models.TextField(blank=True)
    task_date = models.DateField()
    task_time = models.TimeField(default=timezone.now)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task_name