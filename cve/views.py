from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from lxml import etree

# load the 2014 and 2015 cve files on server launch
cvestub = "static/data/nist.gov/nvd/cve/nvdcve-2.0-"
tree2014 = etree.parse(cvestub+"2014"+".xml")
tree2015 = etree.parse(cvestub+"2015"+".xml")

# Create your views here.
def rawxml(request,cvenum):
	cvenum = cvenum.upper()
	try:
		cveyear = cvenum.split('-')[1]
		tpath=('//{http://scap.nist.gov/schema/feed/vulnerability/2.0}entry[contains(@id,"'+cvenum+'")]')
		findall = etree.ETXPath(tpath)
		if cveyear == '2015':
			return HttpResponse(etree.tostring(findall(tree2015)[0]), content_type="application/xml")
		elif cveyear == '2014':
			return HttpResponse(etree.tostring(findall(tree2014)[0]), content_type="application/xml")
		else:
			raise Http404
	except:
		raise Http404

