from django import forms

from student.models import Student
from teacher.validation import is_characters_only
from utilities.models import Level


class StudentModifyForms(forms.ModelForm):
    level = forms.ChoiceField(choices=Level.to_tuple(), required=False)
    age = forms.IntegerField(min_value=1, max_value=150)

    class Meta:
        model = Student
        exclude = ('teacher',)

    def clean(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        error_list = {}
        is_characters_only(first_name, 'first_name', error_list)
        is_characters_only(last_name, 'last_name', error_list)

        if error_list is not None:
            for error in error_list:
                error_message = error_list[error]
                self.add_error(error, error_message)

        return self.cleaned_data


class StudentRegisterForms(forms.ModelForm):
    level = forms.ChoiceField(choices=Level.to_tuple(), required=False)

    class Meta:
        model = Student
        fields = ['email',
                  'first_name',
                  'last_name',
                  'company',
                  'level',
                  ]

    def clean(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        error_list = {}
        is_characters_only(first_name, 'first_name', error_list)
        is_characters_only(last_name, 'last_name', error_list)

        if error_list is not None:
            for error in error_list:
                error_message = error_list[error]
                self.add_error(error, error_message)

        return self.cleaned_data