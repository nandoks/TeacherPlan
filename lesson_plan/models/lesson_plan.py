from django.contrib.postgres.fields import ArrayField
from django.db import models

from utilities.models import Level


class LessonPlan(models.Model):
    db_table = 'lesson_plan'
    title = models.TextField(blank=True)
    lesson_link = models.TextField(blank=True)
    levels = ArrayField(models.CharField(max_length=30, choices=Level.choices, default=Level.Un))
    pre_task = models.TextField(blank=True)
    task = models.TextField(blank=True)
    ccq = models.TextField(blank=True)
    warmup = models.TextField(blank=True)
    outline = models.TextField(blank=True)
    private = models.BooleanField(default=True)
    teacher = models.ForeignKey(to='teacher.Teacher', on_delete=models.DO_NOTHING, null=True, blank=True)
