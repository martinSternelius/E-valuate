from django.template import loader, Context, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from evaluate.models import *

def index(request):
  if request.user.is_authenticated():
    t = loader.get_template('index.html')
    c = RequestContext(request)
    return HttpResponse(t.render(c))
  else:
    return HttpResponseRedirect('/login')

def logout(request):
  auth.logout(request)
  return HttpResponseRedirect('/')
