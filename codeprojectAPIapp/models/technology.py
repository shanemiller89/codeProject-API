from django.db import models
from .technology_type import TechnologyType

class Technology(models.Model):

    technology = models.CharField(max_length=100)
    technology_type = models.ForeignKey(TechnologyType, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("technology")
        verbose_name_plural = ("technologies")

    def __str__(self):
        return f'{self.technology}'
