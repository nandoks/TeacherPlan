from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=150)
    area = models.ForeignKey(to='utilities.Area', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'Company: {self.name} - {self.area}'
