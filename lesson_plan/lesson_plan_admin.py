from django.contrib import admin

# Register your models here.
from lesson_plan.models import LessonPlan

admin.site.register(
    {
        LessonPlan,
    },
)
