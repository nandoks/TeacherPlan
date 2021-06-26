from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.create, name='create_lesson_plan'),
    path('lp_detail/<int:lp_id>', views.lp_detail, name="lp_detail"),
    path('lp_update/<int:lp_id>', views.lp_update, name='lp_update'),
    path('lesson_plans/', views.lp_list, name='lp_list'),
]
