from django.conf.urls import *
from . import views
from django.views.generic import TemplateView

# new CVE version allows for more digits in end
urlpatterns = patterns('cvrf.views',
	url(r'^rawxml/([cC][vV][eE]-\d{4}-\d{4})', views.rawxml),
)
