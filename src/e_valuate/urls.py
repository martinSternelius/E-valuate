# Main URLs file, delegates responsibility to individual applications.
from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()
from django.conf import settings

from e_valuate import evaluate
from e_valuate.evaluate.views import index as evaluateindex

urlpatterns = patterns('',
    
    (r'^$', evaluateindex),
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', 'e_valuate.evaluate.views.logout'),
    (r'^admin/', include(admin.site.urls)),
    (r'^index/$', evaluateindex),
    
    (r'^evaluation/', include('evaluate.urls')),
    
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )

