from django.db import models
from .project import Project
from .coder import Coder

class ProjectCollaborator(models.Model):

    collaborator = models.ForeignKey(Coder, on_delete=models.CASCADE, related_name="projectcollaborator")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="projectcollaborator")

    class Meta:
        verbose_name = ("project collaborator")
        verbose_name_plural = ("project collaborator")
