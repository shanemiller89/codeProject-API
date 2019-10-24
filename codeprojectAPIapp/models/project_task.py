from django.db import models
from .project import Project
from .task import Task


class ProjectTask(models.Model):

    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="projecttask")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="projecttask")

    class Meta:
        verbose_name = ("project task")
        verbose_name_plural = ("project tasks")
