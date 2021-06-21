from django.shortcuts import render, redirect

from lesson.models import Lesson
from teacher.models import Teacher
from .forms import CreateLessonPlanForms


# Create your views here.

def create(request):
    teacher_id = Teacher.objects.values_list('id', flat=True).filter(user_id=request.user.id)[0]
    lesson = Lesson.objects.filter(teacher_id=teacher_id)

    if request.method == 'POST':
        form = CreateLessonPlanForms(request.POST)
        if form.is_valid():
            teacher = Teacher.objects.get(id=teacher_id)
            lesson_plan = form.save(commit=False)
            lesson_plan.teacher = teacher
            lesson_plan.save()

            lesson_id = request.POST['lesson_id']
            if lesson_id is None:
                lesson = Lesson.objects.get(pk=lesson_id)
                lesson.lesson_plan = lesson_plan
                lesson.save()

            return redirect('dashboard')
        else:
            context = context = {
                'create_form': form,
                'lessons': lesson
            }
            return render(request, 'lesson_plan/create.html', context)

    create_form = CreateLessonPlanForms()
    context = {
        'create_form': create_form,
        'lessons': lesson,
    }

    return render(request, 'lesson_plan/create.html', context)