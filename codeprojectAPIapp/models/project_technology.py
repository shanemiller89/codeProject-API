from django.db import models
from .project import Project
from .technology import Technology


class ProjectTechnology(models.Model):

    technology = models.ForeignKey(Technology, on_delete=models.CASCADE, related_name="projecttechnology")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="projecttechnology")

    class Meta:
        verbose_name = ("project technology")
        verbose_name_plural = ("project technologies")
