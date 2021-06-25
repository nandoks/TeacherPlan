from django import forms

from student.models import Student
from utilities.models import Level

class StudentModifyForms(forms.ModelForm):
    level = forms.ChoiceField(choices=Level.to_tuple(), required=False)

    class Meta:
        model = Student
        exclude = ('teacher',)


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
