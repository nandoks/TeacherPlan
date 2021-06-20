from django.contrib import admin

from .models import Company, Area, Subject, Language

# Register your models here.

admin.site.register(
    {
        Language,
        Company,
        Area,
        Subject,
    },

)


