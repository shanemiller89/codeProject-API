from django.db import models

class TechnologyType(models.Model):

    type = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("technology type")
        verbose_name_plural = ("technology types")

    def __str__(self):
        return f'{self.type}'