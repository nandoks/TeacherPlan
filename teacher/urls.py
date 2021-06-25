from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register_teacher'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('', views.dashboard, name='dashboard'),
    path('teacher/students/', views.teacher_students, name='teacher_students')
]
