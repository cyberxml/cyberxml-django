from django.conf.urls import *
from . import views
from django.views.generic import TemplateView

# new cpe version allows for more digits in end
urlpatterns = patterns('cce.views',
	url(r'^nist/import', views.import_nist_cce),
	url(r'^nist/view', views.view_nist_cce),
	url(r'.*', TemplateView.as_view(template_name='cce_index.html')),
)
