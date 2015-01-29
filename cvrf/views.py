from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from StringIO import StringIO
from . import cvrf

from eulexistdb import db   

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
        self.db = db.ExistDB(server_url="http://localhost:8080/exist")    
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
		rootObj = cvrf.parse("static/data/"+vdir+cvrfnum+".xml",0)
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
		rootObj = cvrf.parse("static/data/"+vdir+cvrfnum+".xml",0)
		xmlstr=StringIO()
		rootObj.export(xmlstr, 0)
		return render(request, 'cvrf_pretty.html', {'test':rootObj})
	except:
		raise Http404

def vendor_index(request, vendor):
	vendor = vendor.lower()
	vroot,vdir = getVendorDirectory(vendor)
	if vdir == None: return render(request, 'cvrf_index.html')	
	qrystr='''xquery version "3.0";
		declare namespace cvrf = "http://www.icasi.org/CVRF/schema/cvrf/1.1";
		let $vd := "'''+vendor+'''"
		for $v in reverse(collection("/db/cvrf/'''+vroot+'''/")/cvrf:cvrfdoc )
		let $id := $v/cvrf:DocumentTracking/cvrf:Identification/cvrf:ID/text()
		let $title := $v/cvrf:DocumentTitle/text()
		let $irdate := substring($v/cvrf:DocumentTracking/cvrf:InitialReleaseDate/text(),1,10)
		let $crdate := substring($v/cvrf:DocumentTracking/cvrf:CurrentReleaseDate/text(),1,10)
		let $fn := util:document-name($v)
		return <tr><td>{$id}</td>
			<td><a href="/cvrf/rawxml/{$vd}/{$fn}">{$title}</a></td>
			<td>{$irdate}</td>
			<td>{$crdate}</td></tr>'''

	a = connExistDB()
	idx =a.get_data(qrystr)
	
	return render(request, 'cvrf_catalog.html', {'idx':idx, 'vdir':vdir, 'vendor':vendor, 'qstr':qrystr})