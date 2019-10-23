from django.db import models

class TaskType(models.Model):

    type = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("task type")
        verbose_name_plural = ("task types")

    def __str__(self):
        return f'{self.type}'