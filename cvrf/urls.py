from django.conf.urls import *
from . import views
from django.views.generic import TemplateView

urlpatterns = patterns('cvrf.views',
	(r'^hello', TemplateView.as_view(template_name='cvrf_hello.html')),
	#url(r'^rawxml/([mM][sS]\d{2}-\d{3})', views.rawxml),
	url(r'^rawxml/([mM][sS])/([mM][sS]\d{2}-\d{3})', views.rawxml),
	url(r'^rawxml/([rR][eE][dD][hH][aA][tT])/(cvrf-rhsa-\d{4}-\d{4})', views.rawxml),
	url(r'^rawxml/([cC][iI][sS][cC][oO])/(cisco-s[aArR]-\d{8}-.*_cvrf)', views.rawxml),
	url(r'^prettyxml/([mM][sS])/([mM][sS]\d{2}-\d{3})', views.prettyxmltest),
	url(r'^prettyxml/([rR][eE][dD][hH][aA][tT])/(cvrf-rhsa-\d{4}-\d{4})', views.prettyxmltest),
	url(r'^prettyxml/([cC][iI][sS][cC][oO])/(cisco-s[aArR]-\d{8}-.*_cvrf)', views.prettyxmltest),
	#url(r'^pretty/([mM][sS])/([mM][sS]\d{2}-\d{3})', views.prettyxml),
	#url(r'^pretty/([rR][eE][dD][hH][aA][tT])/(cvrf-rhsa-\d{4}-\d{4})', views.prettyxml),
)
