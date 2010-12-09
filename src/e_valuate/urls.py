# Main URLs file, delegates responsibility to individual applications.
from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

from e_valuate import evaluate
import e_valuate.evaluate.views

urlpatterns = patterns('',    
  (r'^$', 'e_valuate.evaluate.views.index'),
  (r'^login/$', 'django.contrib.auth.views.login'),
  (r'^logout/$', 'e_valuate.evaluate.views.logout'),
  (r'^admin/', include(admin.site.urls)),
  (r'^index/$', 'e_valuate.evaluate.views.index'),
  (r'^evaluation/', include('evaluate.urls')),
)

if settings.DEBUG:
  urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
  )
