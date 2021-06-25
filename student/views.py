from django.contrib.auth.decorators import login_required
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
            teacher = get_object_or_404(Teacher, user_id=request.user.id)
            student.teacher = teacher
            student.save()

            return redirect('dashboard')
        else:
            context = {
                'register_form': form
            }
            return render(request, 'student/student_form.html', context)

    register_form = StudentRegisterForms()

    context = {
        'register_form': register_form,
    }
    return render(request, 'student/register_student.html', context)


@login_required()
def student_detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    context = {
        'student': student,
    }
    return render(request, 'student/student_detail.html', context)


@login_required()
def modify_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        form = StudentModifyForms(instance=student, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_detail', student_id=student_id)
        else:
            for e in form.errors:
                print(e)
            context = {
                'modify_form': form,
            }
            return render(request, 'student/modify_student.html', context)

    modify_form = StudentModifyForms(instance=student)

    context = {
        'modify_form': modify_form,
    }
    return render(request, 'student/modify_student.html', context)
