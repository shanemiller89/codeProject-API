from django.db import models
from .project import Project
from .wireframe import Wireframe

class ProjectWireframe(models.Model):

    wireframe = models.ForeignKey(Wireframe, on_delete=models.CASCADE, related_name="wireframe")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="project")

    class Meta:
        verbose_name = ("project wireframe")
        verbose_name_plural = ("project wireframes")
