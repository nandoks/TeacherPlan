from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404

from student.forms import StudentRegisterForms, StudentModifyForms
from student.models import Student
from teacher.models import Teacher


@login_required(login_url='login')
def register_student(request):
    if request.method == 'POST':
        form = StudentRegisterForms(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            teacher = get_object_or_404(Teacher, pk=request.user.id)
            student.teacher = teacher
            student.save()

            return redirect('teacher_students')
        else:
            context = {
                'register_form': form
            }
            return render(request, 'student/student_form.html', context)

    register_form = StudentRegisterForms()

    context = {
        'register_form': register_form,
    }
    return render(request, 'student/register.html', context)


@login_required(login_url='login')
def student_detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    is_permission_denied(student.teacher.id, request.user.id)

    context = {
        'student': student,
    }
    return render(request, 'student/detail.html', context)


@login_required(login_url='login')
def modify_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    is_permission_denied(student.teacher.id, request.user.id)
    if request.method == 'POST':
        form = StudentModifyForms(instance=student, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_detail', student_id=student_id)
        else:

            context = {
                'modify_form': form,
            }
            return render(request, 'student/update.html', context)

    modify_form = StudentModifyForms(instance=student)

    context = {
        'modify_form': modify_form,
    }
    return render(request, 'student/update.html', context)


def is_permission_denied(teacher_id, user_id):
    if teacher_id != user_id:
        raise PermissionDenied
