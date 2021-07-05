from django import forms
from django.contrib.postgres.forms import SplitArrayField
from django.db.models import TextField
from django.forms import Textarea, ChoiceField

from lesson_plan.models import LessonPlan
from utilities.models import Level


class LessonPlanForms(forms.ModelForm):
    lesson_link = forms.CharField()
    title = forms.CharField()
    levels = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=Level.to_tuple(), required=False)
    private = forms.BooleanField(
        label='Make this lesson plan public?',
        required=False,
        initial=False
    )

    class Meta:
        model = LessonPlan
        exclude = ['teacher', 'stages']
        labels = {
            'pre_task': 'Pre-task',
        }
        widgets = {
            'lessons': ChoiceField,
            'title': Textarea(attrs={'rows': 1}),
            'lesson_link': Textarea(attrs={'rows': 1}),
        }

    def clean(self):
        return self.cleaned_data