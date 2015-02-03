from django.conf.urls import *
from . import views
from django.views.generic import TemplateView

# new cpe version allows for more digits in end
urlpatterns = patterns('cpe.views',
	#url(r'^rawxml/([cC][vV][eE]-\d{4}-\d{4})', views.rawxml),
	#url(r'^nist/catalog/(\d{4})', views.cpe_index),
	#url(r'^nist/catalog', TemplateView.as_view(template_name='cpe_catalog.html')),
	url(r'^redhat/catalog',  views.redhat_cpe_catalog),
	url(r'^nist/import', views.import_nist_cpe),
	url(r'^redhat/import', views.import_redhat_cpe),
	url(r'^nist/search', views.search_nist_cpe),
	#url(r'^nist/xml/([cC][vV][eE]-\d{4}-\d{3}\d+)', views.cpexml),
	#url(r'^rawxml/([cC][vV][eE]-\d{4}-\d{3}\d+)', views.rawxml),
	url(r'.*', TemplateView.as_view(template_name='cpe_index.html')),
)
