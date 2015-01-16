from django.conf.urls import patterns, include, url
from django.contrib import admin
from LiftTracker.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'LiftTracker.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # Admin page
    url(r'^admin/', include(admin.site.urls)),

    # Main Page
    (r'^$', main_page),

    # Login/ logout
    (r'^login/$', 'django.contrib.auth.views.login'), 
    (r'^logout/$', logout_page),

    # Registration page
    url(r'^register/', 'LiftTracker.views.register', name='register'),

    # Lift Portal
    url(r'^portal/', include('portal.urls')),

    # Serve static content
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', 
        {'document_root': 'static'}),
)
