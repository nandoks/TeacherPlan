from django import forms
from django.forms import ChoiceField, Textarea, MultipleChoiceField
from django.contrib import auth

from utilities.models import Level
from lesson_plan.models import LessonPlan
from lesson.models import Lesson


class CreateLessonPlanForms(forms.ModelForm):
    lesson_link = forms.CharField()
    title = forms.CharField()
    levels = forms.MultipleChoiceField(choices=Level.to_tuple())

    class Meta:
        model = LessonPlan
        fields = '__all__'
        exclude = ['private', 'teacher']
        labels = {
            'pre_task': 'Pre-task'
        }
        widgets = {
            'lesson': ChoiceField,
            'title': Textarea(attrs={'rows':1}),
            'lesson_link': Textarea(attrs={'rows':1}),
            'pre_task': Textarea(attrs={'rows':4}),
            'task': Textarea(attrs={'rows': 4}),
            'ccq': Textarea(attrs={'rows': 4}),
            'warmup': Textarea(attrs={'rows': 4}),
            'outline': Textarea(attrs={'rows':4}),
        }

    # title = forms.CharField(label='Title')
    # lesson_link = forms.URLField(label='Lesson or resource link', required=False)
    # level = forms.MultipleChoiceField(label='Level(s)', choices=Level.choices)
    # pre_task = forms.CharField(label='Pre-Task', widget=forms.Textarea(), required=False)
    # task = forms.CharField(label='Task', widget=forms.Textarea(), required=False)
    # ccq = forms.CharField(label='Ccq', widget=forms.Textarea(), required=False)
    # warmup = forms.CharField(label='Warmup', widget=forms.Textarea(), required=False)
    # outline = forms.CharField(label='Outline', widget=forms.Textarea(), required=False)
    lessons = forms.ChoiceField(label='Session')

    def clean_title(self):
        title = self.cleaned_data.get('title')

