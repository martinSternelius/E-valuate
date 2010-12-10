from django.conf.urls.defaults import *

urlpatterns = patterns('',
  (r'^new/?$'                                          , 'e_valuate.evaluate.views.new'),
  (r'^new/template/?$'                                 , 'e_valuate.evaluate.views.new', {"isTemplate":True}),
  (r'^list/unsent/?$'                                  , 'e_valuate.evaluate.views.list', {"sent":False}),
  (r'^list/sent/?$'                                    , 'e_valuate.evaluate.views.list', {"sent":True}),
  (r'^(?P<evaluationId>\d+)/questions/?$'              , 'e_valuate.evaluate.views.questions'),
  (r'^(?P<evaluationId>\d+)/add_question/?$'           , 'e_valuate.evaluate.views.addQuestion'),
  (r'^(?P<evaluationId>\d+)/add_question/(?P<questionId>\w+)$'                    , 'e_valuate.evaluate.views.addQuestion'),
  (r'^(?P<evaluationId>\d+)/remove_question/(?P<questionId>\w+)/?$'         , 'e_valuate.evaluate.views.removeQuestion'),
  (r'^(?P<evaluationId>\d+)/questions/(?P<questionOrder>\d+)/add_alternatives/?$'   , 'e_valuate.evaluate.views.addAlternatives'),
  (r'^(?P<evaluationId>\d+)/?$'                       , 'e_valuate.evaluate.views.viewSingle'),
  (r'^(?P<evaluationId>\d+)/(?P<activeSubView>\w+)/?$' , 'e_valuate.evaluate.views.viewSingle'),
)
