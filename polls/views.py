# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'views/index.html', context)


def detail(request, question_id):
    return HttpResponse('You are looking at question %s' % question_id)


def results(request, question_id):
    return HttpResponse('You are looking for the result of question %s' % question_id)


def vote(request, question_id):
    return HttpResponse('You are voting for question %s' % question_id)