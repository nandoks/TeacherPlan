from django.urls import path
from . import feedback_views

urlpatterns = [
    path('list/', feedback_views.list_feedbacks, name="feedback_list"),

]