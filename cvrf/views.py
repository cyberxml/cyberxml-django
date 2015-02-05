from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.http import Http404
from StringIO import StringIO
from . import cvrf
from . import imports

from eulexistdb import db	
from django.conf import settings

#import logging
#logger = logging.getLogger(__name__)

def getVendorDirectory(vendor):
	vendor = vendor.lower()
	vdir = None
	if vendor == "ms":
		vdir = "microsoft.com/MSRC-CVRF/"
		vroot ="microsoft.com"
	if vendor == "microsoft":
		vdir = "microsoft.com/MSRC-CVRF/"
		vroot ="microsoft.com"
	elif vendor == "redhat":
		vdir = "redhat.com/security/data/cvrf/"
		vroot ="redhat.com"
	elif vendor == "rhel":
		vdir = "redhat.com/security/data/cvrf/"
		vroot ="redhat.com"
	elif vendor == "cisco":
		vdir = "cisco.com/security/center/cvrfListing.x/"
		vroot ="cisco.com"
	elif vendor == "oracle":
		vdir = "oracle.com/documents/webcontent/cvrf/"
		vroot ="oracle.com"
	return (vroot,vdir)

class connExistDB:	  
	def __init__(self):
		self.db = db.ExistDB()	  
	def get_data(self, query):
		result = list()
		qresult = self.db.executeQuery(query)
		hits = self.db.getHits(qresult)
		for i in range(hits):
			result.append(str(self.db.retrieve(qresult, i)))
		return result

# Create your views here.
def rawxml(request,vendor,cvrfnum):
	cvrfnum = cvrfnum.lower().replace('.xml','')
	vroot,vdir = getVendorDirectory(vendor)
	if vdir == None: raise Http404
	try:
		rootObj = cvrf.parse("media/data/"+vdir+cvrfnum+".xml",0)
		xmlstr=StringIO()
		rootObj.export(xmlstr, 0)
		return HttpResponse(xmlstr.getvalue(), content_type="application/xml")
	except:
		#raise Http404
		pass

# Create your views here.
def prettyxml(request,vendor,cvrfnum):
	cvrfnum = cvrfnum.lower().replace('.xml','')
	vroot,vdir = getVendorDirectory(vendor)
	if vdir == None: raise Http404
	try:
		rootObj = cvrf.parse("media/data/"+vdir+cvrfnum+".xml",0)
		xmlstr=StringIO()
		rootObj.export(xmlstr, 0)
		return render(request, 'cvrf_pretty.html', {'test':rootObj})
	except:
		raise Http404

def index_cvrf(request, vendor):
	vendor = vendor.lower()
	return render(request, 'cvrf_index.html', {'vendor':vendor,})
	
def vendor_index(request, vendor):
	vendor = vendor.lower()
	vroot,vdir = getVendorDirectory(vendor)
	if vdir == None: return render(request, 'cvrf_index.html')	
	qrystr='''xquery version "3.0";
		declare namespace cvrf = "http://www.icasi.org/CVRF/schema/cvrf/1.1";
		let $vd := "'''+vendor+'''"
		for $v in reverse(collection("/db/cyberxml/data/cvrf/'''+vroot+'''/")/cvrf:cvrfdoc )
		let $id := $v/cvrf:DocumentTracking/cvrf:Identification/cvrf:ID/text()
		let $title := $v/cvrf:DocumentTitle/text()
		let $irdate := substring($v/cvrf:DocumentTracking/cvrf:InitialReleaseDate/text(),1,10)
		let $crdate := substring($v/cvrf:DocumentTracking/cvrf:CurrentReleaseDate/text(),1,10)
		let $fn := util:document-name($v)
		return <tr><td>{$id}</td>
			<td><a href="/cvrf/{$vd}/xml/{$fn}">{$title}</a></td>
			<td>{$irdate}</td>
			<td>{$crdate}</td></tr>'''

	a = connExistDB()
	idx =a.get_data(qrystr)
	
	return render(request, 'cvrf_catalog.html', {'idx':idx, 'vdir':vdir, 'vendor':vendor, 'qstr':qrystr})

def cvrfxml(request,vendor,cvrfnum):
	vendor = vendor.lower()
	vroot,vdir = getVendorDirectory(vendor)
	qrystr='''xquery version "3.0";
		declare namespace cvrf = "http://www.icasi.org/CVRF/schema/cvrf/1.1";
		let $cvrf := "'''+cvrfnum+'''"
		let $vendor := "'''+vroot+'''"
		let $thisdoc := concat("/db/cyberxml/data/cvrf/",$vendor,"/",$cvrf,".xml")
		let $input := doc($thisdoc)
		let $xsl := doc("/db/cyberxml/styles/xsl/cvrf.xsl")
		return
			transform:transform($input, $xsl, ())
		'''

	a = connExistDB()
	idx =a.get_data(qrystr)
	
	return render(request, 'cvrf_xml.html', {'idx':idx, 'vendor':vendor, 'cvrfnum':cvrfnum, 'qstr':qrystr})

#@login_required
def import_msrc_cvrf(request):
	try:
		i = request.FILES['mscvrf']
		if (i == ""):
			# Redisplay the iavm upload form, with error message
			return render(request, 'cvrf_ms_import.html', {'error_message': "file not found.",})
		else:
			fn = "/tmp/msrc_cvrf.zip"
			#logger.info('saving uploaded file as '+fn)
			with open(fn, 'wb+') as destination:
				for chunk in i.chunks():
					destination.write(chunk)
			destination.close()
			#logger.info('starting MSRC CVRF parse_msrc_cvrf_zip function')
			files=imports.parse_msrc_cvrf_zip(fn)
			#logger.info('finished MSRC CVRF parse_msrc_cvrf_zip function')
			return render(request, 'cvrf_ms_import.html', {'files':files,})
			
	except:
		return render(request, 'cvrf_ms_import.html', {'error_message': "no file provided.",})

#@login_required
def import_redhat_cvrf(request):
	if request.method == 'POST':
		try:
			files=imports.import_redhat_cvrf()
			return render(request, 'cvrf_redhat_import.html', {'files':files,})			
		except:
			return render(request, 'cvrf_redhat_import.html', {'error_message': "request failed",})
	else:
			return render(request, 'cvrf_redhat_import.html')
	
#@login_required
def import_oracle_cvrf(request):
	if request.method == 'POST':
		try:
			files=imports.import_oracle_cvrf()
			return render(request, 'cvrf_oracle_import.html', {'files':files,})			
		except:
			return render(request, 'cvrf_oracle_import.html', {'error_message': "request failed",})
	else:
			return render(request, 'cvrf_oracle_import.html')

#@login_required
def import_cisco_cvrf(request):
	if request.method == 'POST':
		try:
			files=imports.import_cisco_cvrf()
			return render(request, 'cvrf_cisco_import.html', {'files':files,})			
		except:
			return render(request, 'cvrf_cisco_import.html', {'error_message': "request failed",})
	else:
			return render(request, 'cvrf_cisco_import.html')
	


