from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
# from lxml import etree

from eulexistdb import db   

# load the 2014 and 2015 cve files on server launch
#cvestub = "static/data/nist.gov/nvd/cve/nvdcve-2.0-"
#tree2014 = etree.parse(cvestub+"2014"+".xml")
#tree2015 = etree.parse(cvestub+"2015"+".xml")

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

def cve_index(request, cveyear):
	if cveyear == None: return render(request, 'cvrf_index.html')	
	qrystr='''xquery version "3.0";
		declare namespace vuln = "http://scap.nist.gov/schema/vulnerability/0.4";
		declare namespace nvd = "http://scap.nist.gov/schema/feed/vulnerability/2.0";
		let $year := '''+cveyear+'''
		let $thisdoc := concat("/db/cve/nvdcve-2.0-",$year,".xml")
		for $v in doc($thisdoc)/nvd:nvd/nvd:entry
		let $last := substring($v/vuln:last-modified-datetime/text(),1,10)
		let $first := substring($v/vuln:published-datetime/text(),1,10)
		let $id := $v/vuln:cve-id/text()
		let $name := $v/vuln:summary/text()
		return <tr><td><a href="/cve/nist/xml/{$id}">{$id}</a></td><td>{$name}</td><td>{$first}</td><td>{$last}</td></tr>
		'''

	a = connExistDB()
	idx =a.get_data(qrystr)
	
	return render(request, 'cve_catalog.html', {'idx':idx, 'year':cveyear, 'qstr':qrystr})

def cvexml(request, cvenum):
	cveyear=cvenum.split('-')[1]
	if cveyear == None: return render(request, 'cvrf_index.html')	
	qrystr='''xquery version "3.0";
		declare namespace nvd = "http://scap.nist.gov/schema/feed/vulnerability/2.0";
		declare namespace cvss="http://scap.nist.gov/schema/cvss-v2/0.2"; 
		declare namespace cpe-lang="http://cpe.mitre.org/language/2.0" ;
		declare namespace vuln="http://scap.nist.gov/schema/vulnerability/0.4"; 
		declare namespace patch="http://scap.nist.gov/schema/patch/0.1" ;
		declare namespace scap-core="http://scap.nist.gov/schema/scap-core/0.1";
		let $year := "'''+cveyear+'''"
		let $thisdoc := concat("/db/cve/nvdcve-2.0-",$year,".xml")
		let $input := doc($thisdoc)/nvd:nvd/nvd:entry[@id="'''+cvenum+'''"]
		let $xsl := doc("/db/cyberxml/styles/xsl/cve.xsl")
		return
			transform:transform($input, $xsl, ())
		'''

	a = connExistDB()
	idx =a.get_data(qrystr)
	
	return render(request, 'cve_xml.html', {'idx':idx, 'cvenum':cvenum, 'qstr':qrystr})


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

