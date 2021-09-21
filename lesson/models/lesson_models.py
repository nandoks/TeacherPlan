from django.core.exceptions import ValidationError
from django.db import models
from datetime import datetime

from django.db.models import Q


class Lesson(models.Model):
    date = models.DateField()
    start = models.TimeField()
    end = models.TimeField()
    lesson_plan = models.ForeignKey(to='lesson_plan.LessonPlan', on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name='lesson')
    subject = models.ManyToManyField(to='utilities.Subject', blank=True)
    teacher = models.ForeignKey(to='teacher.Teacher', on_delete=models.DO_NOTHING)
    student = models.ForeignKey(to='student.Student', on_delete=models.CASCADE)
    canceled = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.date.strftime("%d/%m/%Y")} {self.start.strftime("%H:%M")} - {self.end.strftime("%H:%M")} - {self.student.first_name} {self.student.last_name}'

    class Meta:
        ordering = ['date']

    def save(self, *args, **kwargs):
        if self.is_teacher_overlaping():
            raise ValidationError('Teacher lesson overlaping with an existing lesson')
        if self.is_student_overlaping():
            raise ValidationError('Student lesson overlaping with an existing lesson')

        super().save(*args, **kwargs)

    def is_teacher_overlaping(self):
        lesson = Lesson.objects.filter(
            Q(teacher=self.teacher) & Q(date=self.date)
            & (Q(start__gte=self.start) & Q(start__lt=self.end))
            | (Q(end__gt=self.start) & Q(end__lte=self.end)))
        return len(lesson) > 0

    def is_student_overlaping(self):
        lesson = Lesson.objects.filter(
            Q(student=self.student) & Q(date=self.date)
            & (Q(start__gte=self.start) & Q(start__lt=self.end))
            | (Q(end__gt=self.start) & Q(end__lte=self.end)))
        return len(lesson) > 0
