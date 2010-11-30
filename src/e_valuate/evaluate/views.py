from django.template import loader, Context, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from evaluate.models import *

def index(request):
  t = loader.get_template('index.html')
  c = RequestContext(request)
  return HttpResponse(t.render(c))
