from django.shortcuts import render
from .models import Question


# Create your views here.
def index(request):
    question = Question.objects.all()
    context = {
        "questions": question
    }
    return render(request, "index.html", context=context)
