from django.contrib import auth
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from .forms import TeacherRegisterForms, LoginForms

# Create your views here.
from .models import Teacher, CustomUser


def register(request):
    if request.method == 'POST':
        form = TeacherRegisterForms(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password']
            if CustomUser.objects.filter(email=email).exists():
                return redirect('register')

            user = CustomUser.objects.create_user(email=email, password=password, first_name=first_name,
                                                  last_name=last_name)
            user.save()

            teacher = Teacher(user_id=user.id)
            teacher.save()

            return redirect('login')
        else:
            context = {'register_form': form}
            return render(request, 'teacher/register.html', context)
    else:
        register_form = TeacherRegisterForms()

        context = {
            'register_form': register_form,
        }

        return render(request, 'teacher/register.html', context)


def login(request):
    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print(email, password)
            user = authenticate(email=email, password=password)
            print(user)
            if user is not None:
                auth.login(request, user)
                print('user loged in')
            return redirect('dashboard')
        else:
            return redirect('login')
    login_form = LoginForms()

    context = {
        'login_form': login_form,
    }
    return render(request, 'teacher/login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('login')


def dashboard(request):
    return render(request, 'teacher/dashboard.html')
