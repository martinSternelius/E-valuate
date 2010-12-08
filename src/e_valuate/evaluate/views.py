#coding: utf-8
from copy import deepcopy
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import loader, Context, RequestContext
from e_valuate.evaluate.models import Evaluation, EvaluationForm, Question, \
  QuestionForm, QuestionType
from evaluate.models import *

def index(request):
  t = loader.get_template('index.html')
  c = Context(request)
  return HttpResponse(t.render(c))

def logout(request):
  auth.logout(request)
  return HttpResponseRedirect('/')

def questions(request, evaluationId):
  evaluation = get_object_or_404(Evaluation, pk=evaluationId)
  return render_to_response('evaluation/questions.html', {'evaluation': evaluation})

def new(request, isTemplate=False):
  if request.method == "POST":
    newEvaluation = Evaluation()
    if isTemplate:
      newEvaluation.name = request.POST['name']
      newEvaluation.isTemplate = True
      newEvaluation.save()
    else:
      newEvaluation = EvaluationForm(request.POST).save()
      try: 
        int(request.POST['templateId'])
      except:
        # If we can't convert templateId to an integer we assume the user 
        # doesn't want to generate an evaluation from an evaluation template
        # and so we just sends him through to the template.
        pass
      else:
        # assures that templateId isnt below 1
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
  if isTemplate:
    t = loader.get_template('new_template.html')
    c = RequestContext(request, {"evaluationForm" : EvaluationForm()})      
  else:
    templates = Evaluation().getAllTemplates()
    t = loader.get_template('new_evaluation.html')
    c = RequestContext(request, {"templates" : templates, "evaluationForm" : EvaluationForm()})
  return HttpResponse(t.render(c))

def addQuestion(request, evaluationId):
  evaluation = Evaluation.objects.get(pk=evaluationId)
  if request.method == "POST":
    question = QuestionForm(request.POST).save(commit=False)
    question.order = evaluation.getNextQuestionOrder()
    question.evaluation = evaluation
    question.save()
    
  questionForm = QuestionForm()
  template = loader.get_template('evaluation/addQuestion.html')
  context = RequestContext(request, {'questionForm':questionForm, 'evaluation':evaluation})
  return HttpResponse(template.render(context))

def addIntegerAlternatives(request, questionId, low, high):
  question = Question.objects.get(pk=questionId)