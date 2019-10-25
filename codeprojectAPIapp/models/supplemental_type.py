from django.db import models

class SupplementalType(models.Model):

    type = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("supplemental type")
        verbose_name_plural = ("supplemental types")

    def __str__(self):
        return f'{self.type}'