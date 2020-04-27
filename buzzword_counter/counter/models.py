from django.db import models


class Buzzword(models.Model):
    word = models.CharField(max_length=127, unique=True)
    count = models.PositiveSmallIntegerField(blank=True, default=0)

    class Meta:
        ordering = ['word']

    def __str__(self):
        return f'Buzzword "{self.word}"'
