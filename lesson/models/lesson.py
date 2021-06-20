from django.db import models


class Lesson(models.Model):
    date = models.DateTimeField()
    lesson_plan = models.ForeignKey(to='lesson_plan.LessonPlan', on_delete=models.DO_NOTHING)
    subject = models.ManyToManyField(to='utilities.Subject')
    teacher = models.ForeignKey(to='teacher.Teacher', on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.date)
