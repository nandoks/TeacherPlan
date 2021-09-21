from django.urls import path

from . import lesson_plan_views

urlpatterns = [
    path('create/', lesson_plan_views.create, name='create_lesson_plan'),
    path('lp_detail/<int:lp_id>', lesson_plan_views.lp_detail, name="lp_detail"),
    path('lp_update/<int:lp_id>', lesson_plan_views.lp_update, name='lp_update'),
    path('lesson_plans/', lesson_plan_views.lp_list, name='lp_list'),
]
