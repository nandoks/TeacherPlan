from django.urls import path
from . import teacher_views

urlpatterns = [
    path('register', teacher_views.register, name='register_teacher'),
    path('login', teacher_views.login, name='login'),
    path('logout', teacher_views.logout, name='logout'),
    path('', teacher_views.dashboard, name='dashboard'),
    path('students/', teacher_views.teacher_students, name='teacher_students'),
    path('profile/', teacher_views.teacher_profile, name='teacher_profile'),
    path('profile/update/', teacher_views.teacher_update, name='teacher_update'),
]
