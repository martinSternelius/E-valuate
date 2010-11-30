# Main URLs file, delegates responsibility to individual applications.
from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

from e_valuate import evaluate
from e_valuate.evaluate.views import index as evaluateindex

urlpatterns = patterns('',
    
    (r'^$', evaluateindex),

    (r'^login/$', 'django.contrib.auth.views.login'),
        
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    
    (r'^index/$', evaluateindex),
    
)
