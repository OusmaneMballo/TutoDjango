from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404

from .models import Question
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
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
