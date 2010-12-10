from django.conf.urls.defaults import *

urlpatterns = patterns('',
  (r'^new/'                                         , 'e_valuate.evaluate.views.new'),
  (r'^new/template'                                 , 'e_valuate.evaluate.views.new', {"isTemplate":True}),
  (r'^list/unsent'                                  , 'e_valuate.evaluate.views.list', {"sent":False}),
  (r'^list/sent'                                    , 'e_valuate.evaluate.views.list', {"sent":True}),
  (r'^(?P<evaluationId>\d+)/questions$'             , 'e_valuate.evaluate.views.questions'),
  (r'^(?P<evaluationId>\d+)/addQuestion$'           , 'e_valuate.evaluate.views.addQuestion'),
  (r'^(?P<evaluationId>\d+)$'                       , 'e_valuate.evaluate.views.viewSingle'),
  (r'^(?P<evaluationId>\d+)/(?P<activeSubView>\w+)' , 'e_valuate.evaluate.views.viewSingle'),
)
