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

# list of prouduct ids and names
qry_product='''xquery version "3.0";
declare namespace cvrf = "http://www.icasi.org/CVRF/schema/cvrf/1.1";
declare namespace prod = "http://www.icasi.org/CVRF/schema/prod/1.1";
declare namespace vuln = "http://www.icasi.org/CVRF/schema/vuln/1.1";
for $fpn in collection('/db/cyberxml/data/cvrf/cisco.com')//prod:FullProductName
return <entry><id>{string($fpn/@ProductID)}</id><name>{$fpn/text()}</name><cpe2_2></cpe2_2><cpe2_3></cpe2_3></entry>
'''

qry_cpe='''xquery version "3.0";
declare namespace cpe = "http://cpe.mitre.org/dictionary/2.0";
declare namespace cpe-23 = "http://scap.nist.gov/schema/cpe-extension/2.3";
for $cpe in doc('/db/cyberxml/data/cpe/nist.gov/official-cpe-dictionary_v2.3.xml')//cpe:cpe-item[starts-with(@name, "cpe:/h:cisco:") and not (@deprecated=True)]
return <entry><title>{$cpe/cpe:title/text()}</title><cpe>{string($cpe/@name)}</cpe></entry>
'''

# probably faster if I reverse order of for loops
def get_qryCiscoCvrfCveCpe(cve):
	qry = '''xquery version "3.0";
	declare namespace cvrf = "http://www.icasi.org/CVRF/schema/cvrf/1.1";
	declare namespace prod = "http://www.icasi.org/CVRF/schema/prod/1.1";
	declare namespace vuln = "http://www.icasi.org/CVRF/schema/vuln/1.1";
	let $thiscve := "'''+cve+'''"
	for $pid in distinct-values(collection('/db/cyberxml/data/cvrf/cisco.com')//node()[vuln:CVE[.=$thiscve]]/vuln:ProductStatuses/vuln:Status[@Type="Known Affected"]/vuln:ProductID/text())
	for $cpe in distinct-values(doc('/db/cyberxml/apps/cvrf/cisco.com/cisco_productid2cpe.xml')//node()[id[.=$pid]]/cpe2_2/text())
	return $cpe'''
	return qry


def getCpeFromCve(cve):
	try:
		qrystr=get_qryCiscoCvrfCveCpe(cve)
		a = connExistDB()
		cpes =list(set(a.get_data(qrystr)))
		cpes.sort()
	except:
		cpes=[]
	return(cpes)
