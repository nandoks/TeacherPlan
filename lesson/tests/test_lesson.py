import pytest
from django.test import TestCase

from lesson.tests.factories import LessonFactory

@pytest.mark.django_db
class TestLessonCase(TestCase):
    def test_no_creation_overlap_teacher(self):
        """Test that two lessons can't overlap on time if they have same 
           teacher
        """
        lesson1 = LessonFactory()
        # To be continued :
        # Try create two lessons with same teacher that overlap in time : 
        # second lesson should not be created (raise exception on creation 
        # or check that condition in LessonRegisterForms to make the form invalid)
        
    def test_no_creation_overlap_student(self):
        """Test that two lessons can't overlap on time if they have same 
           teacher
        """
        lesson1 = LessonFactory()
        # To be continued :
        # Try create two lessons with same student that overlap in time : 
        # second lesson should not be created (raise exception on creation 
        # or check that condition in LessonRegisterForms to make the form invalid)
