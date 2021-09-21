from django.contrib.postgres.fields import ArrayField
from django_countries.fields import CountryField
from django.db import models

from utilities.models import Level


class Student(models.Model):
    teacher = models.ForeignKey(to='teacher.Teacher', on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(max_length=150)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    occupation = models.CharField(max_length=150, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    objective = models.TextField(blank=True, null=True)
    interests = models.TextField(blank=True, null=True)
    country = CountryField(blank=True, null=True)
    company = models.ForeignKey(to='Company', on_delete=models.CASCADE, null=True, blank=True)
    L1 = models.ForeignKey(to='utilities.Language', on_delete=models.CASCADE, related_name='l1_student', null=True,
                           blank=True)
    L2 = models.ManyToManyField(to='utilities.Language', related_name='l2_student1', blank=True)
    level = models.CharField(max_length=30, choices=Level.choices, default=Level.Un, null=True, blank=True)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['first_name', 'last_name',]