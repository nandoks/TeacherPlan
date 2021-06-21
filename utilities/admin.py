from django.contrib import admin

from .models import Subject, Language

# Register your models here.

admin.site.register(
    {
        Language,
        Subject,
    },

)


