from django.conf.urls import *
from . import views
from django.views.generic import TemplateView

# new CVE version allows for more digits in end
urlpatterns = patterns('iavm.views',
	url(r'^apply/$', views.get_iavm_apply),
)
