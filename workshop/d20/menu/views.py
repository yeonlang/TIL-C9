from django.shortcuts import render
from .models import Question, Choice
# Create your views here.

def test(request):
    question = Question.objects.first()
    choices = question.choice_set.all()
    
    return render(request, 'test.html', {'question': question, 'choices':choices})