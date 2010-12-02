from django.conf.urls.defaults import *
from e_valuate.evaluate.views import *

urlpatterns = patterns('',
  (r'^create/', create),
)
