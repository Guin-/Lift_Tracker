from django.conf.urls import url, patterns, include
from portal.views import *

urlpatterns = patterns('',

    # Main portal entrance page
    url(r'^$', portal_main_page),

    url(r'^profile/', user_profile) 
    
    )
