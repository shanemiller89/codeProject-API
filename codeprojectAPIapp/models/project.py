from django.db import models
from .coder import Coder

class Project(models.Model):

    title = models.CharField(max_length=100)
    repo = models.CharField(max_length=100)
    overview = models.TextField()
    project_image = models.CharField(max_length=150)
    erd_image = models.CharField(max_length=150)
    private = models.BooleanField()
    technologies = models.ManyToManyField("Technology", through="ProjectTechnology")
    wireframes = models.ManyToManyField("Wireframe", through="ProjectWireframe")
    tasks = models.ManyToManyField("Task", through="ProjectTask")
    supplementals = models.ManyToManyField("Supplemental", through="ProjectSupplemental")
    collaborators = models.ManyToManyField(Coder, through="ProjectCollaborator")
    owner = models.ForeignKey(Coder, on_delete=models.PROTECT, related_name="owner")

    class Meta:
        ordering = ["title"]
        verbose_name = ("project")
        verbose_name_plural = ("projects")

    def __str__(self):
        return f'{self.title}'