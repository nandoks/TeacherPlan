from django.shortcuts import render

from lesson.models import Lesson
from .forms import CreateLessonPlanForms
# Create your views here.

def create(request):

    data = {
        'lessons': Lesson.objects.filter(teacher_id=request.user.id)
    }

    create_form = CreateLessonPlanForms(data)

    context = {
        'create_form': create_form,
    }

    return render(request, 'lesson_plan/create.html', context)
