from django.template import loader, Context, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib import auth
from evaluate.models import *
from e_valuate.evaluate.models import Evaluation, QuestionForm
from e_valuate import evaluate

def index(request):
    t = loader.get_template('index.html')
    c = RequestContext(request)
    return HttpResponse(t.render(c))

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def questions(request, evaluation_id):
    evaluation = get_object_or_404(Evaluation, pk=evaluation_id)
    return render_to_response('evaluation/questions.html', {'evaluation': evaluation})

def create(request):
    if request.method == "POST":
        Evaluation.save(request.POST)

    t = loader.get_template('evaluation_create.html')
    c = RequestContext(request)
    return HttpResponse(t.render(c))

def addQuestion(request, evaluation_id):
    #evaluation = get_object_or_404(Evaluation, pk=evaluation_id)
    evaluation = Evaluation.objects.get(pk=evaluation_id)
    if request.method == "POST":
        print request.POST
    else:
        questionForm = QuestionForm()
        return render_to_response('evaluation/addQuestion.html', {'questionForm':questionForm, 'evaluation':evaluation})
