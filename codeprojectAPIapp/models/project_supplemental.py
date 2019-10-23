from django.db import models
from .project import Project
from .supplemental import Supplemental

class ProjectSupplemental(models.Model):

    supplemental = models.ForeignKey(Supplemental, on_delete=models.CASCADE, related_name="supplemental")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="project")

    class Meta:
        verbose_name = ("project supplemental")
        verbose_name_plural = ("project supplemental")
