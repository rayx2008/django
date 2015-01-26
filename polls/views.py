
# Create your views here.
from django.shortcuts import get_object_or_404, render

from polls.models import Question
# ...
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
def index(request,question_id):
    return render()

def vote(request,question_id):
    return render()

def results(request,question_id):
    return render()
    