from django.contrib.postgres.fields import ArrayField
from django_countries.fields import CountryField
from django.db import models

from utilities.models import Level


class Student(models.Model):
    email = models.EmailField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    occupation = models.TextField(blank=True)
    age = models.IntegerField(blank=True)
    objective = models.TextField(blank=True)
    interests = models.TextField(blank=True)
    country = CountryField(blank=True, null=True)
    company = models.ForeignKey(to='utilities.Company', on_delete=models.CASCADE, null=True, blank=True)
    L1 = models.ForeignKey(to='utilities.Language', on_delete=models.CASCADE, related_name='l1_student', null=True,
                           blank=True)
    L2 = models.ManyToManyField(to='utilities.Language', related_name='l2_student1', blank=True)
    level = models.CharField(max_length=30, choices=Level.choices, default=Level.Un, null=True, blank=True)


