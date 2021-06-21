from django import forms
from django.forms import Textarea, ChoiceField

from lesson_plan.models import LessonPlan
from utilities.models import Level


class CreateLessonPlanForms(forms.ModelForm):
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
        exclude = ['teacher']
        labels = {
            'pre_task': 'Pre-task',
        }
        widgets = {
            'lessons': ChoiceField,
            'title': Textarea(attrs={'rows': 1}),
            'lesson_link': Textarea(attrs={'rows': 1}),
            'pre_task': Textarea(attrs={'rows': 4}),
            'task': Textarea(attrs={'rows': 4}),
            'ccq': Textarea(attrs={'rows': 4}),
            'warmup': Textarea(attrs={'rows': 4}),
            'outline': Textarea(attrs={'rows': 4}),
        }

    def clean(self):
        return self.cleaned_data
