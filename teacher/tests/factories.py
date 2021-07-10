from factory.django import DjangoModelFactory

from teacher.models import Teacher


class TeacherFactory(DjangoModelFactory):
    class Meta:
        model = Teacher

    email = 'teacher@factory.com'
    first_name = 'teacher'
    last_name = 'factory-boy'
