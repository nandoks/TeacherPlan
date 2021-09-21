from datetime import date

from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404

from lesson.models import Lesson
from lesson_plan.models import LessonPlan
from student.models import Student
from .teacher_forms import TeacherRegisterForms, LoginForms, TeacherUpdateForms

# Create your views here.
from .models import Teacher


def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = TeacherRegisterForms(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password']

            Teacher.objects.create_user(email=email, first_name=first_name,
                                        last_name=last_name, password=password)

            return redirect('login')
        else:
            context = {'register_form': form}
            return render(request, 'teacher/register.html', context)

    register_form = TeacherRegisterForms()

    context = {
        'register_form': register_form,
    }

    return render(request, 'teacher/register.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                auth.login(request, user)
            return redirect('dashboard')
        else:
            return redirect('login')
    login_form = LoginForms()

    context = {
        'login_form': login_form,
    }
    return render(request, 'teacher/login.html', context)


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')


@login_required(login_url='login')
def dashboard(request):
    next_lessons = Lesson.objects.filter(teacher_id=request.user.id, date__gt=date.today())

    context = {
        'next_lessons': next_lessons,
    }
    return render(request, 'teacher/dashboard.html', context)


@login_required(login_url='login')
def teacher_students(request):
    students = Student.objects.filter(teacher_id=request.user.id)

    context = {
        'students': students,
    }
    return render(request, 'teacher/students.html', context)


@login_required(login_url='login')
def teacher_profile(request):
    teacher = get_object_or_404(Teacher, pk=request.user.id)

    context = {
        'teacher': teacher,
    }
    return render(request, 'teacher/profile.html', context)


@login_required(login_url='login')
def teacher_update(request):
    teacher = get_object_or_404(Teacher, pk=request.user.id)
    if request.method == 'POST':
        form = TeacherUpdateForms(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_profile')
        else:
            context = {
                'update_form': form,
            }
            return render(request, 'teacher/update.html', context)

    update_form = TeacherUpdateForms(instance=teacher)

    context = {
        'update_form': update_form,
    }
    return render(request, 'teacher/update.html', context)
