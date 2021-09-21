from django import forms
from django.contrib.auth.password_validation import validate_password

from teacher.teacher_validation import *


class TeacherRegisterForms(forms.Form):
    email = forms.EmailField(label='E-mail', max_length=100)
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirmation = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')
        email = self.cleaned_data.get('email')
        error_list = {}
        is_characters_only(first_name, 'first_name', error_list)
        is_characters_only(last_name, 'last_name', error_list)
        password_match(password, password_confirmation, error_list)
        email_is_unique(email, 'email', error_list)
        validate_password(password)

        if error_list is not None:
            for error in error_list:
                error_message = error_list[error]
                self.add_error(error, error_message)

        return self.cleaned_data


class LoginForms(forms.Form):
    email = forms.EmailField(label='E-mail', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class TeacherUpdateForms(forms.ModelForm):

    class Meta:
        model = Teacher
        fields = [
            'email',
            'first_name',
            'last_name',
            'L1',
            'L2',

        ]
