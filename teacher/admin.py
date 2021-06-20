from django.contrib import admin

# Register your models here.
from .models import Teacher, CustomUser

admin.site.register(
    {
        Teacher,
        CustomUser,
    },
)
