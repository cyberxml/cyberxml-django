from django.conf.urls import *
from . import views
from django.views.generic import TemplateView

urlpatterns = patterns('cvrf.views',
	(r'^hello', TemplateView.as_view(template_name='cvrf_hello.html')),
	url(r'^rawxml/([mM][sS]\d{2}-\d{3})', views.rawxml),
	url(r'^pretty/([mM][sS]\d{2}-\d{3})', views.prettyxml),
)
