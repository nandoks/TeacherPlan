from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from student.models import Student
from teacher.models import Teacher
from .forms import LessonRegisterForms
from .models import Lesson


@login_required(login_url='login')
def register_lesson(request):
    students = Student.objects.filter(teacher_id=request.user.id)

    if request.method == 'POST':
        form = LessonRegisterForms(request.POST)
        if form.is_valid():
            student_id = request.POST['student_id']
            lesson = form.save(commit=False)
            student = Student.objects.get(pk=student_id)
            lesson.student = student
            teacher = Teacher.objects.get(pk=request.user.id)
            lesson.teacher = teacher
            lesson.save()
            form.save_m2m()
            return redirect('dashboard')
        else:
            context = {
                'register_form': form,
                'students': students,
            }
            return render(request, 'lesson/register.html', context)

    lesson_form = LessonRegisterForms()

    context = {
        'register_form': lesson_form,
        'students': students,
    }

    return render(request, 'lesson/register.html', context)


def lesson_list(request):
    lessons = Lesson.objects.filter(teacher_id=request.user.id)

    context = {
        'lessons': lessons,
    }

    return render(request, 'lesson/lesson_list.html', context)