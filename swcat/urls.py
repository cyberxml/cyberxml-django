from django.conf.urls import *
from . import views
from django.views.generic import TemplateView

# new cpe version allows for more digits in end
urlpatterns = patterns('swcat.views',
	url(r'.*', TemplateView.as_view(template_name='swcat_index.html')),
)
