from django.db import models

class Archive(models.Model):

    title = models.CharField(max_length=100)
    repo = models.CharField(max_length=100)
    overview = models.TextField()
    libraries = models.ManyToManyField(Library)
    logs = models.ManyToManyField(Log)

    class Meta:
        ordering = ["title"]
        verbose_name = ("archive")
        verbose_name_plural = ("archives")

    def __str__(self):
        return f'{self.title}'