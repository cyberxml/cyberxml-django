from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.utils.datastructures import MultiValueDictKeyError
# from lxml import etree

from eulexistdb import db	

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

# could use the IAVM-to-CVE spreadsheet 
# if it was accurately based on the IAVM XML
# instead of being based on the IAVM HTML
def get_iavm_apply(request):
	iavm='1899-Z-0001'
	smrs=[]
	xqr=[]
	try:
		iavm=request.GET['iavm']
		qryIavmApply='''
			xquery version "3.0";
			declare namespace iavmNotice = "http://iavm.csd.disa.mil/schemas/IavmNoticeSchema/1.2";
			declare namespace cvrf = "http://www.icasi.org/CVRF/schema/cvrf/1.1";
			declare namespace vuln = "http://www.icasi.org/CVRF/schema/vuln/1.1";
			declare namespace pt = "http://www.icasi.org/CVRF/schema/prod/1.1";
			let $iavnum := "'''+iavm+'''"
			let $iavdoc := concat("/db/iavm/",$iavnum,".xml")
			for $iavcve in doc($iavdoc)/iavmNotice:iavmNotice/iavmNotice:techOverview/iavmNotice:entry/iavmNotice:title/text()
			for $iavcvrf in collection("/db/cvrf")//cvrf:cvrfdoc/vuln:Vulnerability[vuln:CVE=$iavcve]
			let $cvrfdoc := base-uri($iavcvrf)
			let $fn := tokenize($cvrfdoc,'/')[last()]
			for $prod in $iavcvrf/vuln:ProductStatuses/vuln:Status[not(contains(@Type, 'Not Affected'))]/vuln:ProductID/text()
			for $name in doc($cvrfdoc)//pt:FullProductName[@ProductID=$prod]/text()
			return <tr id="{$iavnum}"><td>{$iavcve}</td><td>{$fn}</td><td>{$prod}</td><td>{$name}</td></tr>'''
		
		a = connExistDB()
		xqr =a.get_data(qryIavmApply)
	
	except MultiValueDictKeyError:
		pass
	return render(request,'iavm_apply.html',{'xqr':xqr, 'iavm':iavm})

