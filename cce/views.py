from django.shortcuts import render
#from django.http import HttpResponse
#from django.http import Http404
#from lxml import etree
import imports

from eulexistdb import db   

# load the 2014 and 2015 cce files on server launch
#ccestub = "static/data/nist.gov/nvd/cce/nvdcce-2.0-"
#tree2014 = etree.parse(ccestub+"2014"+".xml")
#tree2015 = etree.parse(ccestub+"2015"+".xml")

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

def cce_index(request, cceyear):
	if cceyear == None: return render(request, 'cvrf_index.html')	
	qrystr='''xquery version "3.0";
		declare namespace vuln = "http://scap.nist.gov/schema/vulnerability/0.4";
		declare namespace nvd = "http://scap.nist.gov/schema/feed/vulnerability/2.0";
		let $year := '''+cceyear+'''
		let $thisdoc := concat("/db/cyberxml/data/cce/nist.gov/nvdcce-2.0-",$year,".xml")
		for $v in doc($thisdoc)/nvd:nvd/nvd:entry
		let $last := substring($v/vuln:last-modified-datetime/text(),1,10)
		let $first := substring($v/vuln:published-datetime/text(),1,10)
		let $id := $v/vuln:cce-id/text()
		let $name := $v/vuln:summary/text()
		return <tr><td><a href="/cce/nist/xml/{$id}">{$id}</a></td><td>{$name}</td><td>{$first}</td><td>{$last}</td></tr>
		'''

	a = connExistDB()
	idx =a.get_data(qrystr)
	
	return render(request, 'cce_catalog.html', {'idx':idx, 'year':cceyear, 'qstr':qrystr})

def ccexml(request, ccenum):
	cceyear=ccenum.split('-')[1]
	if cceyear == None: return render(request, 'cvrf_index.html')	
	qrystr='''xquery version "3.0";
		declare namespace nvd = "http://scap.nist.gov/schema/feed/vulnerability/2.0";
		declare namespace cvss="http://scap.nist.gov/schema/cvss-v2/0.2"; 
		declare namespace cpe-lang="http://cpe.mitre.org/language/2.0" ;
		declare namespace vuln="http://scap.nist.gov/schema/vulnerability/0.4"; 
		declare namespace patch="http://scap.nist.gov/schema/patch/0.1" ;
		declare namespace scap-core="http://scap.nist.gov/schema/scap-core/0.1";
		let $year := "'''+cceyear+'''"
		let $thisdoc := concat("/db/cyberxml/data/cce/nist.gov/nvdcce-2.0-",$year,".xml")
		let $input := doc($thisdoc)/nvd:nvd/nvd:entry[@id="'''+ccenum+'''"]
		let $xsl := doc("/db/cyberxml/styles/xsl/cce.xsl")
		return
			transform:transform($input, $xsl, ())
		'''

	a = connExistDB()
	idx =a.get_data(qrystr)
	
	return render(request, 'cce_xml.html', {'idx':idx, 'ccenum':ccenum, 'qstr':qrystr})

#@login_required
def import_nist_cce(request):
	if request.method == 'POST':
		try:
			files=imports.import_nist_cce()
			return render(request, 'cce_import.html', {'files':files,})			
		except:
			return render(request, 'cce_import.html', {'error_message': "request failed",})
	else:
			return render(request, 'cce_import.html')
# Create your views here.
