# Main URLs file, delegates responsibility to individual applications.
from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

from e_valuate import evaluate
from e_valuate.evaluate.views import index as evaluateindex
import e_valuate.evaluate.views

urlpatterns = patterns('',    
    (r'^$', evaluateindex),
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', 'e_valuate.evaluate.views.logout'),
    (r'^admin/', include(admin.site.urls)),
    (r'^index/$', evaluateindex),
    (r'^evaluation/(?P<evaluation_id>\d+)/questions$', 'e_valuate.evaluate.views.questions'),
)
