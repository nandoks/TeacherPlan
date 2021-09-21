from django.db import models


class Feedback(models.Model):
    next_steps = models.TextField(blank=True)
    homework_link = models.TextField(blank=True)
    greeting = models.TextField(blank=True)
    lexis = models.TextField(blank=True)
    corrections = models.TextField(blank=True)
    summary = models.TextField(blank=True)
    praise = models.TextField(blank=True)
    teacher_only = models.TextField(blank=True)
    lesson = models.OneToOneField(to='lesson.Lesson', on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey(to='student.Student', on_delete=models.SET_NULL, null=True, blank=True)
