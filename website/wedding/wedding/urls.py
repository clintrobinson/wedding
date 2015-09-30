from django.conf import settings
from django.conf.urls import patterns, include, url, static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

from wagtail.wagtailcore import urls as wagtail_urls
from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailsearch import urls as wagtailsearch_urls
from wagtail.contrib.wagtailsitemaps.views import sitemap

import adminactions.actions as actions


actions.add_to_site(admin.site)

urlpatterns = [
    url(r'^admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    url(r'^clientadmin/', include(admin.site.urls)),
    url(r'^robots\.txt/$', TemplateView.as_view(template_name='robots.txt',
        content_type='text/plain')),
    url(r'^cmsadmin/', include(wagtailadmin_urls)),
    url(r'^search/', include(wagtailsearch_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url('^sitemap\.xml$', sitemap),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static.static(
      settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += (
      url(r'^404/$', 'django.views.defaults.page_not_found'),
      url(r'^500/$', 'django.views.defaults.server_error')
    )

urlpatterns += (
    url(r'', include(wagtail_urls)),
)
