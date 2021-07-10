from factory.django import DjangoModelFactory

from student.models import Student


class StudentFactory(DjangoModelFactory):
    class Meta:
        model = Student

    email = 'student@factory.com'
    first_name = 'student'
    last_name = 'factory-boy'