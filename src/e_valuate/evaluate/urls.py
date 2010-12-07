from django.conf.urls.defaults import *
from e_valuate.evaluate.views import *

urlpatterns = patterns('',
  (r'^new/'                                 , new),
  (r'^new/template'                         , new, True),
  (r'^(?P<evaluationId>\d+)/questions$'    , 'e_valuate.evaluate.views.questions'),
  (r'^(?P<evaluationId>\d+)/addQuestion$'  , 'e_valuate.evaluate.views.addQuestion'),
)
