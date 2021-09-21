from django.contrib.postgres.fields import ArrayField
from django.db import models

from utilities.models import Level


class LessonPlan(models.Model):
    db_table = 'lesson_plan'
    title = models.TextField(blank=True, null=True)
    lesson_link = models.TextField(blank=True, null=True)
    levels = ArrayField(models.CharField(max_length=30, choices=Level.choices, default=Level.Un), null=True, blank=True)
    private = models.BooleanField(default=True)
    teacher = models.ForeignKey(to='teacher.Teacher', on_delete=models.DO_NOTHING, null=True, blank=True)
    stages = ArrayField(models.TextField(null=True, blank=True), null=True,
                        blank=True)
