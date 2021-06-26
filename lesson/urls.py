from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register_lesson, name='register_lesson'),
    path('list/', views.lesson_list, name='lesson_list'),
]