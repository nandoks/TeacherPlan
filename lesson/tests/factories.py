import datetime as dt

import factory

from lesson.models import Lesson


class LessonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Lesson
        
    date = factory.LazyFunction(lambda: dt.datetime.now().date())
    start = factory.LazyFunction(lambda: dt.datetime.now().time())
    end = factory.LazyFunction(lambda: (dt.datetime.now() + dt.timedelta(hours=1)).time())
