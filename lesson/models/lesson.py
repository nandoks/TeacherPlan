from django.db import models
from datetime import datetime


class Lesson(models.Model):
    date = models.DateField()
    start = models.TimeField()
    end = models.TimeField()
    lesson_plan = models.ForeignKey(to='lesson_plan.LessonPlan', on_delete=models.DO_NOTHING, null=True, blank=True,
                                    related_name='lesson')
    subject = models.ManyToManyField(to='utilities.Subject', blank=True)
    teacher = models.ForeignKey(to='teacher.Teacher', on_delete=models.DO_NOTHING)
    student = models.ForeignKey(to='student.Student', on_delete=models.CASCADE)
    canceled = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.date.strftime("%d/%m/%Y")} {self.start.strftime("%H:%M")} - {self.end.strftime("%H:%M")} - {self.student.first_name} {self.student.last_name}'

    class Meta:
        ordering = ['date']
