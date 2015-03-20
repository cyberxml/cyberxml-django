from django.conf import settings
from eulexistdb import db

from datetime import date

thisyear = date.today().year

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
	
def get_qryNistCveCpe(cve):
	year = cve.split('-')[1]
	qry = '''xquery version "3.0";
	declare namespace vuln = "http://scap.nist.gov/schema/vulnerability/0.4";
	declare namespace nvd = "http://scap.nist.gov/schema/feed/vulnerability/2.0";
	let $thiscve := "'''+cve+'''"
	let $thisyear := "'''+year+'''"
	let $thisdoc := concat("/db/cyberxml/data/cve/nist.gov/nvdcve-2.0-",$thisyear,".xml")
	for $cpe in doc($thisdoc)//nvd:entry[@id=$thiscve]/vuln:vulnerable-software-list/vuln:product/text()
	return $cpe'''
	return qry


def getCpeFromCve(cve):
	try:
		qrystr=get_qryNistCveCpe(cve)
		a = connExistDB()
		cpes =a.get_data(qrystr)
		cpes.sort()
	except:
		cpes=[]
	return(cpes)
