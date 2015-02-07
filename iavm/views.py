from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.utils.datastructures import MultiValueDictKeyError
from django.conf import settings
from . import imports
from eulexistdb import db	

disa_pki_flag = settings.USE_DISA_PKI

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

# could use the IAVM-to-CVE spreadsheet 
# if it was accurately based on the IAVM XML
# instead of being based on the IAVM HTML
def get_iavm_apply(request):
	iavm='1899-Z-0001'
	smrs=[]
	xqr=[]
	try:
		iavm=request.GET['iavm']
		if disa_pki_flag:
			qryIavmApply='''
				xquery version "3.0";
				declare namespace iavmNotice = "http://iavm.csd.disa.mil/schemas/IavmNoticeSchema/1.2";
				declare namespace cvrf = "http://www.icasi.org/CVRF/schema/cvrf/1.1";
				declare namespace vuln = "http://www.icasi.org/CVRF/schema/vuln/1.1";
				declare namespace pt = "http://www.icasi.org/CVRF/schema/prod/1.1";
				let $iavnum := "'''+iavm+'''"
				let $iavdoc := concat("/db/cyberxml/data/iavm/disa.mil/",$iavnum,".xml")
				for $iavcve in doc($iavdoc)/iavmNotice:iavmNotice/iavmNotice:techOverview/iavmNotice:entry/iavmNotice:title/text()
				for $iavcvrf in collection("/db/cyberxml/data/cvrf")//cvrf:cvrfdoc/vuln:Vulnerability[vuln:CVE=$iavcve]
				let $cvrfdoc := base-uri($iavcvrf)
				let $fn := tokenize($cvrfdoc,'/')[last()]
				for $prod in $iavcvrf/vuln:ProductStatuses/vuln:Status[not(contains(@Type, 'Not Affected'))]/vuln:ProductID/text()
				for $name in doc($cvrfdoc)//pt:FullProductName[@ProductID=$prod]/text()
				return <tr id="{$iavnum}"><td>{$iavcve}</td><td>{$fn}</td><td>{$prod}</td><td>{$name}</td></tr>'''
		else:
			qryIavmApply='''
				xquery version "3.0";
				declare namespace cvrf = "http://www.icasi.org/CVRF/schema/cvrf/1.1";
				declare namespace vuln = "http://www.icasi.org/CVRF/schema/vuln/1.1";
				declare namespace pt = "http://www.icasi.org/CVRF/schema/prod/1.1";
				let $iavnum := "'''+iavm+'''"
				let $iavdoc := "/db/cyberxml/data/iavm/cve/disa.mil/u_iavm-to-cve.xml"
				for $iavcve in doc($iavdoc)//node()[S/@IAVM=$iavnum]/CVEs/CVENumber/text()
				for $iavcvrf in collection("/db/cyberxml/data/cvrf")//cvrf:cvrfdoc/vuln:Vulnerability[vuln:CVE=$iavcve]
				let $cvrfdoc := base-uri($iavcvrf)
				let $fn := tokenize($cvrfdoc,'/')[last()]
				for $prod in $iavcvrf/vuln:ProductStatuses/vuln:Status[not(contains(@Type, 'Not Affected'))]/vuln:ProductID/text()
				for $name in doc($cvrfdoc)//pt:FullProductName[@ProductID=$prod]/text()
				return <tr id="{$iavnum}"><td>{$iavcve}</td><td>{$fn}</td><td>{$prod}</td><td>{$name}</td></tr>'''
		
		a = connExistDB()
		xqr =a.get_data(qryIavmApply)
	
	except MultiValueDictKeyError:
		pass
	return render(request,'iavm_apply.html',{'xqr':xqr, 'iavm':iavm, 'disa_pki_flag':disa_pki_flag})

def get_iavm_view(request):
	iavm='1899-Z-0001'
	smrs=[]
	xqr=[]
	try:
		iavm=request.GET['iavm']
		qryIavmApply='''
			xquery version "3.0";
			declare namespace iavmNotice = "http://iavm.csd.disa.mil/schemas/IavmNoticeSchema/1.2";
			let $thisiavm := "'''+iavm+'''"
			let $thisdoc := concat('/db/cyberxml/data/iavm/disa.mil/',$thisiavm,'.xml')
			let $iav := doc($thisdoc)
			let $xsl := doc("/db/cyberxml/styles/xsl/iavm.xsl")
			return transform:transform($iav,$xsl,())
			'''
		a = connExistDB()
		xqr =a.get_data(qryIavmApply)
	except MultiValueDictKeyError:
		pass
	return render(request,'iavm_view.html',{'iavxml':xqr, 'iavm':iavm,'disa_pki_flag':disa_pki_flag})

#@login_required
def iavm_index(request, iavyear):
	if iavyear == None: return render(request, 'iavm_catalog.html')	
	qrystr='''xquery version "3.0";
		declare namespace iav = "http://iavm.csd.disa.mil/schemas/IavmNoticeSchema/1.2";
		let $year := "'''+iavyear+'''"
		let $thiscollection := "/db/cyberxml/data/iavm/disa.mil"
		for $v in collection($thiscollection)/iav:iavmNotice/iav:iavmNoticeNumber[starts-with(text(),$year)]
		let $iavstr := base-uri($v)
		let $iavdoc := doc($iavstr)
		let $id := $v/text()
		let $last := substring($iavdoc/iav:iavmNotice/iav:lastSaved/text(),1,10)
		let $first := substring($iavdoc/iav:iavmNotice/iav:releaseDate/text(),1,10)
		let $name := $iavdoc/iav:iavmNotice/iav:title/text()
		return <tr><td><a href="/iavm/disa/xml/{$id}">{$id}</a></td><td>{$name}</td><td>{$first}</td><td>{$last}</td></tr>
		'''

	a = connExistDB()
	idx =a.get_data(qrystr)
	
	return render(request, 'iavm_catalog.html', {'idx':idx, 'year':iavyear, 'qstr':qrystr,'disa_pki_flag':disa_pki_flag})


#@login_required
def import_disa_iavm_request(request):
	try:
		i = request.FILES['disaiavm']
		if (i == ""):
			# Redisplay the iavm upload form, with error message
			return render(request, 'iavm_disa_import.html', {'error_message': "file not found.",'disa_pki_flag':disa_pki_flag})
		else:
			fn = "/tmp/disa_iavm.zip"
			#logger.info('saving uploaded file as '+fn)
			with open(fn, 'wb+') as destination:
				for chunk in i.chunks():
					destination.write(chunk)
			destination.close()
			#logger.info('starting DISA IAVM parse_disa_iavm_zip function')
			files=imports.parse_disa_iavm_zip(fn)
			#logger.info('finished DISA IAVM parse_disa_iavm_zip function')
			return render(request, 'iavm_disa_import.html', {'files':files,'disa_pki_flag':disa_pki_flag})
			
	except:
		return render(request, 'iavm_disa_import.html', {'error_message': "no file provided.",'disa_pki_flag':disa_pki_flag})

#@login_required
def import_disa_iavm_cve_request(request):
	if request.method == 'POST':
		try:
			files=imports.import_disa_iavm_cve()
			return render(request, 'iavm_disa_import.html', {'files':files,'disa_pki_flag':disa_pki_flag})			
		except:
			return render(request, 'iavm_disa_import.html', {'error_message': "request failed",'disa_pki_flag':disa_pki_flag})
	else:
			return render(request, 'iavm_disa_import.html', {'disa_pki_flag':disa_pki_flag})
