﻿from copy import deepcopy
from django.template import loader, Context, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from evaluate.models import Evaluation, EvaluationForm, Question

def index(request):
  t = loader.get_template('index.html')
  c = RequestContext(request)
  return HttpResponse(t.render(c))

def logout(request):
  auth.logout(request)
  return HttpResponseRedirect('/')

def new(request):
  if request.method == "POST":
    newEvaluation = EvaluationForm(request.POST).save()
    
    try: 
      int(request.POST['templateId'])
    except:
      pass
    else:
      if int(request.POST['templateId']):
        # kopiera alla questions ifrån templaten man valde och adda dom till vår nya evaluation
        selectedTemplateId = request.POST['templateId']
        selectedTemplate = Evaluation.objects.get(id=selectedTemplateId)
        
        templateQuestions = Question.objects.filter(evaluation=selectedTemplate.id)
        
        for templateQuestion in templateQuestions:
          newQuestion = deepcopy(templateQuestion)
          newQuestion.id = None
          newQuestion.evaluation = newEvaluation
          newQuestion.save()

    return HttpResponseRedirect("/evaluation/"+ str(newEvaluation.id) +"/add_question")
    
  templates = Evaluation().getAllTemplates()
  t = loader.get_template('new_evaluation.html')
  c = RequestContext(request, {"templates" : templates, "evaluationForm" : EvaluationForm()})
  return HttpResponse(t.render(c))