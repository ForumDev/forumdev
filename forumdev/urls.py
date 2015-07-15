from django.conf.urls import *  # NOQA
#from django.conf.urls.i18n import i18n_patterns
from django.conf.urls import patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf import settings
from cms.sitemaps import CMSSitemap
from myauth.forms import AuthLoginForm 

admin.site.login_form = AuthLoginForm 
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/publications/publication/import_bibtex/$', 'publications.admin_views.import_bibtex'),
    url(r'^admin/', include(admin.site.urls)),  # NOQA
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': {'cmspages': CMSSitemap}}),
    url(r'^publications/', include('publications.urls')),
    url(r'^auth/', include('myauth.urls')),
    url(r'^select2/', include('django_select2.urls')),
    url(r'^', include('cms.urls')),
)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',  # NOQA
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ) + staticfiles_urlpatterns() + urlpatterns  # NOQA
