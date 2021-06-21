from django.db import models
from datetime import datetime


class Lesson(models.Model):
    date = models.DateField()
    start = models.TimeField()
    end = models.TimeField()
    lesson_plan = models.ForeignKey(to='lesson_plan.LessonPlan', on_delete=models.DO_NOTHING, null=True, blank=True)
    subject = models.ManyToManyField(to='utilities.Subject', blank=True)
    teacher = models.ForeignKey(to='teacher.Teacher', on_delete=models.DO_NOTHING)
    student = models.OneToOneField(to='student.Student', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.date.strftime("%d/%m/%Y - %H:%M")} - {self.student.first_name} {self.student.last_name}'
