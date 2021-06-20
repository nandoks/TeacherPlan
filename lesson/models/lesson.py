from django.db import models


class Lesson(models.Model):
    date = models.DateTimeField()
    lesson_plan = models.ForeignKey(to='lesson_plan.LessonPlan', on_delete=models.DO_NOTHING)
    subject = models.ManyToManyField(to='utilities.Subject')
    teacher = models.ForeignKey(to='teacher.Teacher', on_delete=models.DO_NOTHING)
    student = models.OneToOneField(to='lesson.Student', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{str(self.date)} - {self.student.first_name} {self.student.last_name} - {self.subject}'
