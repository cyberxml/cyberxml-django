from django.conf.urls import *
from . import views
from django.views.generic import TemplateView

# new CVE version allows for more digits in end
urlpatterns = patterns('cvrf.views',
	#url(r'^rawxml/([cC][vV][eE]-\d{4}-\d{4})', views.rawxml),
	url(r'^nist/catalog/(\d{4})', views.cve_index),
	url(r'^nist/catalog', TemplateView.as_view(template_name='cve_catalog.html')),
	url(r'^nist/import', views.import_nist_cve),
	url(r'^nist/xml/([cC][vV][eE]-\d{4}-\d{3}\d+)', views.cvexml),
	#url(r'^rawxml/([cC][vV][eE]-\d{4}-\d{3}\d+)', views.rawxml),
	url(r'.*', TemplateView.as_view(template_name='cve_catalog.html')),
)
