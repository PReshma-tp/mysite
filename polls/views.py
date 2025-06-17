from django.http import HttpResponse 

def index(request):
    return HttpResponse("Hello User:)) You are at Polls Index...")
