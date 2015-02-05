from django.conf.urls import *
from . import views
from django.views.generic import TemplateView

# new cpe version allows for more digits in end
urlpatterns = patterns('stig.views',
	url(r'.*', TemplateView.as_view(template_name='stig_index.html')),
)
