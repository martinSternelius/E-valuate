from django.conf.urls.defaults import *

urlpatterns = patterns('',
  (r'^new/', 'e_valuate.evaluate.views.new'),
  (r'^new/template', 'e_valuate.evaluate.views.new', True),
  (r'^(?P<evaluationId>\d+)/questions$'    , 'e_valuate.evaluate.views.questions'),
  (r'^(?P<evaluationId>\d+)/add_question$'  , 'e_valuate.evaluate.views.addQuestion'),
  (r'^(?P<evaluationId>\d+)/questions/(?P<questionOrder>\d+)/add_alternatives$'  , 'e_valuate.evaluate.views.addAlternatives'),
)
