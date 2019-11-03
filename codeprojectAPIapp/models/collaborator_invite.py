from django.db import models
from .project import Project
from .coder import Coder

class CollaboratorInvite(models.Model):

    collaborator = models.ForeignKey(Coder, on_delete=models.CASCADE, related_name="collaboratorinvite")
    owner = models.ForeignKey(Coder, on_delete=models.CASCADE, related_name="ownerinvite")
    message = models.TextField()
    accept = models.BooleanField(null=True)

    class Meta:
        verbose_name = ("invite")
        verbose_name_plural = ("invites")
