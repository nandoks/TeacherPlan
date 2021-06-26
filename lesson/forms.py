from django import forms
from django.forms import DateInput, TimeInput

from .models import Lesson
from .validation import *


class LessonRegisterForms(forms.ModelForm):
    date = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
    start = forms.TimeField(label='Lesson begins at:', widget=TimeInput(attrs={'type': 'time'}))
    end = forms.TimeField(label='Lesson ends at:', widget=TimeInput(attrs={'type': 'time'}))

    class Meta:
        model = Lesson
        fields = ['date',
                  'start',
                  'end',
                  'subject',
                  ]

    def clean(self):
        date = self.cleaned_data.get('date')
        start = self.cleaned_data.get('start')
        end = self.cleaned_data.get('end')
        error_list = {}
        is_start_before_end(start, end, error_list)
        is_date_today_or_after(date, error_list)

        if error_list is not None:
            for error in error_list:
                error_message = error_list[error]
                self.add_error(error, error_message)

        return self.cleaned_data
