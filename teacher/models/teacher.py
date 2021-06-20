from django.contrib.auth.models import User
from django.db import models
from TeacherPlan import settings


class Teacher(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    L1 = models.ForeignKey(to='utilities.Language', on_delete=models.CASCADE, related_name='student_l1', null=True,
                           blank=True)
    L2 = models.ManyToManyField(to='utilities.Language', related_name='l2_teacher', blank=True)

    def __str__(self):
        return f'{self.user}'
