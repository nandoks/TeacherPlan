from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from student.models import Student
from teacher.models import Teacher
from .forms import LessonRegisterForms


@login_required(login_url='login')
def register_lesson(request):
    teacher_id = Teacher.objects.values_list('id', flat=True).filter(user_id=request.user.id)[0]
    students = Student.objects.filter(teacher_id=teacher_id)

    if request.method == 'POST':
        form = LessonRegisterForms(request.POST)
        if form.is_valid():
            student_id = request.POST['student_id']
            lesson = form.save(commit=False)
            student = Student.objects.get(pk=student_id)
            lesson.student = student
            teacher = Teacher.objects.get(pk=teacher_id)
            lesson.teacher = teacher
            lesson.save()
            form.save_m2m()
        else:
            context = {
                'register_form': form,
                'students': students,
            }
            return render(request, 'lesson/register_lesson.html', context)

    lesson_form = LessonRegisterForms()

    context = {
        'register_form': lesson_form,
        'students': students,
    }

    return render(request, 'lesson/register_lesson.html', context)
