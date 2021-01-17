from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse

from .models import Question, Choice
from django.template import loader


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    '''template = loader.get_template('sondages/questions/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))'''

    '''context = {'latest_question_list': latest_question_list}
    return render(request, 'sondages/questions/index.html', context)'''
    return render(request, 'sondages/questions/index.html', {'latest_question_list': latest_question_list})


def detail(request, question_id):
    '''
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    '''
    question = get_object_or_404(Question, pk=question_id)
    choices = question.choice_set.all
    return render(request, 'sondages/questions/detail.html', {'question': question, 'choices': choices})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'sondages/questions/resultat.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'sondages/questions/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('sondages:resultat', args=(question.id,)))

