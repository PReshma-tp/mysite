from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Question, Choice

def index(request):
    question_list = Question.objects.all()
    context = {"question_list" : question_list}
    return render(request, "polls/index.html", context)

def details(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/details.html', {"question": question})

def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/result.html', {"question": question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
        
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            'polls/details.html',
            {"question": question,
             "error_message": "You didn't select a choice"
             }
        )
    else:
        selected_choice.vote =F('vote')+1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:result',args=(question_id,)))


   