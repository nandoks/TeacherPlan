from django.contrib import admin

# Register your models here.
from lesson.models import Student, Lesson

admin.site.register({
    Student,
    Lesson,
})
