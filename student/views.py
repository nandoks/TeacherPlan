from django.shortcuts import render, redirect
from student.forms import StudentRegisterForms
from teacher.models import Teacher


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
