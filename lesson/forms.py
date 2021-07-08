from django import forms
from django.forms import DateInput, TimeInput
from tempus_dominus.widgets import TimePicker

from .models import Lesson
from .validation import *


class LessonRegisterForms(forms.ModelForm):
    date = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
    start = forms.TimeField(label='Lesson begins at:',
                            widget=TimePicker(
                                options={
                                    'format': 'HH:mm',
                                    'defaultDate': '2021-01-01T08:00:00',
                                    'stepping': '5',
                                },
                                attrs={
                                    'icon-toggle':True,
                                    'append': 'fa fa-clock',
                                },
                            ))
    end = forms.TimeField(label='Lesson ends at:',
                          widget=TimePicker(
                              options={
                                  'format':'HH:mm',
                                  'defaultDate': '2021-01-01T08:30:00',
                                  'stepping': '5',
                              },
                              attrs={
                                  'icon-toggle': True,
                                  'append': 'fa fa-clock',
                              },
                          ))

    class Meta:
        model = Lesson
        fields = [
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
