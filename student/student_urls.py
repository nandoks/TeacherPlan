from django.urls import path
from . import student_views

urlpatterns = [
    path('register/', student_views.register_student, name='register_student'),
    path('detail/<int:student_id>/', student_views.student_detail, name='student_detail'),
    path('modify/<int:student_id>/', student_views.modify_student, name='modify_student'),
]