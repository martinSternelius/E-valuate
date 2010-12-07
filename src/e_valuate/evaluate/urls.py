from django.conf.urls.defaults import *

urlpatterns = patterns('',
  (r'^new/', 'e_valuate.evaluate.views.new'),
)
