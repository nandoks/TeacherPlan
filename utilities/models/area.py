from django.db import models


class Area(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return f'Area: {self.name}'
