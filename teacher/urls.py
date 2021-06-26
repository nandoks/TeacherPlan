from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register_teacher'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('', views.dashboard, name='dashboard'),
    path('students/', views.teacher_students, name='teacher_students'),
    path('profile/', views.teacher_profile, name='teacher_profile'),
    path('profile/update/', views.teacher_update, name='teacher_update'),
]
