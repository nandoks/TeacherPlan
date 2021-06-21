from django import forms

from .models import Lesson


class LessonRegisterForms(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'
