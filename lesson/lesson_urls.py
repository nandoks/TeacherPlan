from django.urls import path

from . import lesson_views

urlpatterns = [
    path('register/', lesson_views.register_lesson, name='register_lesson'),
    path('list/', lesson_views.lesson_list, name='lesson_list'),
]