from django.contrib import admin

# Register your models here.
from lesson.models import Lesson

admin.site.register({
    Lesson,
})
