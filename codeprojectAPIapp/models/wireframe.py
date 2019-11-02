from django.db import models

class Wireframe(models.Model):

    wireframe_image = models.CharField(max_length=100)
    wireframe_title = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = ("wireframe")
        verbose_name_plural = ("wireframes")
