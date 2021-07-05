from datetime import date

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404

from lesson.models import Lesson
from teacher.models import Teacher
from .forms import LessonPlanForms
from .models import LessonPlan


@login_required(login_url='login')
def create(request):
    lesson = Lesson.objects.filter(teacher_id=request.user.id, date__gt=date.today(), lesson_plan_id__isnull=True)

    if request.method == 'POST':
        form = LessonPlanForms(request.POST)
        stages = [s for s in request.POST.getlist('stages[]') if s != '']
        print(stages)
        if form.is_valid():
            teacher = Teacher.objects.get(id=request.user.id)
            lesson_plan = form.save(commit=False)
            lesson_plan.teacher = teacher

            lesson_plan.stages = stages
            lesson_plan.save()

            lesson_id = request.POST['lesson_id']

            if lesson_id.isnumeric():
                lesson = Lesson.objects.get(pk=lesson_id)
                lesson.lesson_plan = lesson_plan
                lesson.save()

            return redirect('dashboard')
        else:
            context = context = {
                'create_form': form,
                'lessons': lesson,
                'stages': stages,
            }
            return render(request, 'lesson_plan/create.html', context)

    create_form = LessonPlanForms()
    context = {
        'create_form': create_form,
        'lessons': lesson,
        'stages': [''] * 6
    }

    return render(request, 'lesson_plan/create.html', context)


@login_required(login_url='login')
def lp_detail(request, lp_id):
    lp = get_object_or_404(LessonPlan, pk=lp_id)
    is_permission_denied(lp.teacher.id, request.user.id)

    context = {
        'lesson_plan': lp,
    }
    return render(request, 'lesson_plan/detail.html', context)


@login_required(login_url='login')
def lp_update(request, lp_id):
    lesson_plan = get_object_or_404(LessonPlan, id=lp_id)
    update_form = LessonPlanForms(instance=lesson_plan)
    lesson = Lesson.objects.filter(teacher_id=request.user.id, date__gte=date.today(), lesson_plan_id__isnull=True)

    if request.method == 'POST':
        form = LessonPlanForms(data=request.POST, instance=lesson_plan)
        if form.is_valid():
            form.save()

            return redirect('teacher_lesson_plans')
        context = {
            'update_form': form,
            'lessons': lesson,
        }
        return render(request, 'lesson_plan/update.html', context)

    context = {
        'update_form': update_form,
        'lessons': lesson,
    }
    return render(request, 'lesson_plan/update.html', context)


@login_required(login_url='login')
def lp_list(request):
    lesson_plans = LessonPlan.objects.filter(teacher_id=request.user.id)

    context = {
        'lesson_plans': lesson_plans,
    }
    return render(request, 'lesson_plan/lp_list.html', context)


def is_permission_denied(lp_id, user_id):
    if lp_id != user_id:
        raise PermissionDenied
