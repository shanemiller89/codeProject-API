from django.db import models
from .project import Project
from .wireframe import Wireframe

class ProjectWireframe(models.Model):

    wireframe = models.ForeignKey(Wireframe, on_delete=models.CASCADE, related_name="projectwireframe")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="projectwireframe")

    class Meta:
        verbose_name = ("project wireframe")
        verbose_name_plural = ("project wireframes")
