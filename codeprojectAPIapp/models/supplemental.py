from django.db import models
from .supplemental_type import SupplementalType

class Supplemental(models.Model):

    title = models.CharField(max_length=100)
    text = models.TextField()
    language = models.CharField(max_length=100, blank=True)
    supplemental_image = models.CharField(max_length=150, blank=True)
    pinned = models.BooleanField(default=False)
    supplemental_type = models.ForeignKey(SupplementalType, on_delete=models.CASCADE)


    class Meta:
        verbose_name = ("extra")
        verbose_name_plural = ("extras")

    def __str__(self):
        return f'{self.title}'
