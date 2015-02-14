from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cyberxml.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^cce/', include('cce.urls')),
	url(r'^cpe/', include('cpe.urls')),
    url(r'^cvrf/', include('cvrf.urls')),
    url(r'^cve/', include('cve.urls')),
	url(r'^iavm/', include('iavm.urls')),
	url(r'^stig/', include('stig.urls')),
	url(r'^swcat/', include('swcat.urls')),
	url(r'^usgcb/', include('usgcb.urls')),
	(r'^asset/import', TemplateView.as_view(template_name='asset_import.html')),
	(r'^asset/catalog', TemplateView.as_view(template_name='asset_catalog.html')),
	(r'^asset', TemplateView.as_view(template_name='asset_index.html')),
	(r'^config', TemplateView.as_view(template_name='config_index.html')),
	(r'^vuln/apply', TemplateView.as_view(template_name='vuln_apply.html')),
	(r'^vuln/catalog', TemplateView.as_view(template_name='vuln_catalog.html')),
	(r'^vuln/import', TemplateView.as_view(template_name='vuln_import.html')),
	(r'^vuln', TemplateView.as_view(template_name='vuln_index.html')),
	(r'^robots.txt', TemplateView.as_view(template_name='robots.txt',content_type='text/plain')),
	(r'^$', TemplateView.as_view(template_name='index.html')),
)

#urlpatterns += staticfiles_urlpatterns()
