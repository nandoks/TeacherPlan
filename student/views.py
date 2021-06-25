from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from student.forms import StudentRegisterForms
from student.models import Student
from teacher.models import Teacher

@login_required(login_url='login')
def register_student(request):
    if request.method == 'POST':
        form = StudentRegisterForms(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            teacher = Teacher.objects.get(user_id=request.user.id)
            student.teacher = teacher
            student.save()

            return redirect('dashboard')
        else:
            context = {
                'register_form' : form
            }
            return render(request, 'student/student_form.html',context)

    register_form = StudentRegisterForms()

    context = {
        'register_form': register_form,
    }
    return render(request, 'student/register_student.html', context)


@login_required()
def student_detail(request, student_id):
    student = Student.objects.get(pk=student_id)

    context = {
        'student': student,
    }
    return render(request, 'student/student_detail.html', context)

@login_required()
def modify_student(request, student_id):
    return render(request, 'student/modify_student.html')