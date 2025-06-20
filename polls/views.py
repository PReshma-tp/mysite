from django.http import HttpResponse 
from django.shortcuts import render
from .models import Question

def index(request):
    question_list = Question.objects.all()
    context = {"question_list" : question_list}
    return render(request, "polls/index.html", context)

def details(request, question_id):
    return HttpResponse("You are looking at the question %s " % question_id)

def result(request, question_id):
    return HttpResponse("You are looking at the results of question %s" % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s" % question_id)