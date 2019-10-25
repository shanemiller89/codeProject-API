from django.db import models
from .task_type import TaskType

class Task(models.Model):

    task = models.TextField()
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("task")
        verbose_name_plural = ("tasks")

    def __str__(self):
        return f'{self.task}'
