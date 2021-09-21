from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('teacher.teacher_urls')),
    path('lesson_plan/', include('lesson_plan.lesson_plan_urls')),
    path('admin/', admin.site.urls),
    path('student/', include('student.student_urls')),
    path('lesson/', include('lesson.lesson_urls')),
    path('feedback/', include('feedback.feedback_urls')),

]
