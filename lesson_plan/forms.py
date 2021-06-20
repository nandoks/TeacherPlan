from django import forms
from django.contrib import auth

from utilities.models import Level
from lesson.models import Lesson


class CreateLessonPlanForms(forms.Form):

    title = forms.CharField(label='Title')
    lesson_link = forms.URLField(label='Lesson or resource link', required=False)
    level = forms.MultipleChoiceField(label='Level(s)', choices=Level.choices)
    pre_task = forms.CharField(label='Pre-Task', widget=forms.Textarea(), required=False)
    task = forms.CharField(label='Task', widget=forms.Textarea(), required=False)
    ccq = forms.CharField(label='Ccq', widget=forms.Textarea(), required=False)
    warmup = forms.CharField(label='Warmup', widget=forms.Textarea(), required=False)
    outline = forms.CharField(label='Outline', widget=forms.Textarea(), required=False)
    lessons = forms.ChoiceField(label='Session')

    def clean_title(self):
        title = self.cleaned_data.get('title')

