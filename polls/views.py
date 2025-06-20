from django.http import HttpResponse 

def index(request):
    return HttpResponse("Hello User:)) You are at Polls Index...")

def details(request, question_id):
    return HttpResponse("You are looking at the question %s " % question_id)

def result(request, question_id):
    return HttpResponse("You are looking at the results of question %s" % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s" % question_id)