from django.shortcuts import render

# Create your views here.
from feedback.models import Feedback


def list_feedbacks(request):

    feedbacks = Feedback.objects.all()
    context = {
        'feedbacks': feedbacks,
    }
    return render(request, 'feedback/feedback_list.html', context)
