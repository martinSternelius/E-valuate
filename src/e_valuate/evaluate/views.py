from django.template import loader, Context, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib import auth
<<<<<<< HEAD
from evaluate.models import *
from e_valuate.evaluate.models import Evaluation
from e_valuate import evaluate
=======
from evaluate.models import Evaluation

def index(request):
    t = loader.get_template('index.html')
    c = RequestContext(request)
    return HttpResponse(t.render(c))

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def questions(request, evaluation_id):
    evaluation = get_object_or_404(Evaluation, pk=evaluation_id)
    print evaluation.name
    return render_to_response('evaluation/questions.html', {'evaluation': evaluation})

def create(request):
    if request.method == "POST":
        Evaluation.save(request.POST)

    t = loader.get_template('evaluation_create.html')
    c = RequestContext(request)
    return HttpResponse(t.render(c))
