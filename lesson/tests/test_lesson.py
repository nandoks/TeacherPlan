import datetime as dt

import pytest
from django.core.exceptions import ValidationError
from django.test import TestCase
from faker import factory

from lesson.tests.factories import LessonFactory
from teacher.tests.factories import TeacherFactory


class OverlapingLessonForTeacher(Exception):
    '''Teacher already has another class on this time frame'''


@pytest.mark.django_db
class TestLessonCase(TestCase):
    def test_no_creation_overlap_teacher(self):
        """Test that two lessons can't overlap on time if they have same 
           teacher
        """
        lesson1 = LessonFactory()

        with pytest.raises(ValidationError):
            lesson2 = LessonFactory(teacher=lesson1.teacher)

    def test_no_creation_overlap_student(self):
        """Test that two lessons can't overlap on time if they have same
           student
        """
        lesson1 = LessonFactory()
        teacher2 = TeacherFactory(email='teacher2@factory.com')
        with pytest.raises(ValidationError):
            # lesson2 at the same time as lesson1
            lesson2 = LessonFactory(teacher=teacher2, student=lesson1.student)

