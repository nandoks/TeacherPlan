from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_student, name='register_student'),
    path('detail/<int:student_id>/', views.student_detail, name='student_detail'),
    path('modify/<int:student_id>/', views.modify_student, name='modify_student'),
]