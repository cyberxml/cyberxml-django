from django.conf.urls import *
from . import views
from django.views.generic import TemplateView

# new CVE version allows for more digits in end
urlpatterns = patterns('iavm.views',
	url(r'^disa/apply', views.get_iavm_apply),
	url(r'^disa/catalog/(\d{4})', views.iavm_index),
	url(r'^disa/catalog', TemplateView.as_view(template_name='iavm_catalog.html')),
	url(r'^disa/import', views.import_disa_iavm_request),
	url(r'.*', TemplateView.as_view(template_name='iavm_index.html')),
)
