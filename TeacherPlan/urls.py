from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('teacher.urls')),
    path('lesson_plan/', include('lesson_plan.urls')),
    path('admin/', admin.site.urls),
    path('student/', include('student.urls')),
    path('lesson/',include('lesson.urls')),
    path('feedback/', include('feedback.urls')),

]
