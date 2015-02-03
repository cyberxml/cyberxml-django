from django.shortcuts import render
#from django.http import HttpResponse
#from django.http import Http404
import imports
# from lxml import etree

from eulexistdb import db   


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

'''
xquery version "3.0";
declare namespace cpe-23 = "http://scap.nist.gov/schema/cpe-extension/2.3";
declare namespace cpe = "http://cpe.mitre.org/dictionary/2.0";
let $ver :="2.2"
let $thisdoc := concat("/db/cyberxml/data/cpe/nist.gov/official-cpe-dictionary_v",$ver,".xml")
for $v in doc($thisdoc)/cpe:cpe-list/cpe:cpe-item[contains(@name, "cpe:/a:1024cms:1024_cms:0.7")]
return $v
'''
def search_nist_cpe(request):
	try:
		if request.method == 'POST':
			# Redisplay the iavm upload form, with error message
			try:
				deprecated = request.POST['deprecated']
				deprecated = True
			except:
				deprecated = False
			version = request.POST['version']
			part = request.POST['part']
			if version == "cpe":
				part='/'+part
			vendor = request.POST['vendor']
			product = request.POST['product']
			#reqstr=':'.join([version,part])
			reqstr = ':'.join([version,part,vendor,product])
			#deprecated = True
			return render(request, 'cpe_nist_search.html', {'reqstr':reqstr,'deprecated':deprecated})
		else:
			return render(request, 'cpe_nist_search.html')
	except:
		return render(request, 'cpe_nist_search.html', {'error_message': "post failed.",})


def redhat_cpe_catalog(request):
	qrystr='''xquery version "3.0";
		declare namespace cpe_dict = "http://cpe.mitre.org/dictionary/2.0";
		let $cpedoc := "/db/cyberxml/data/cpe/redhat.com/cpe-dictionary.xml"
		for $iavcve in doc($cpedoc)/cpe_dict:cpe-list/cpe_dict:cpe-item
		return <tr><td>{string($iavcve/@name)}</td><td>{$iavcve/cpe_dict:title/text()}</td></tr>
		'''
	
	a = connExistDB()
	idx =a.get_data(qrystr)
	
	return render(request, 'cpe_redhat_catalog.html', {'idx':idx, 'vdir':'redhat.com', 'vendor':'redhat', 'qstr':qrystr})

#@login_required
def import_nist_cpe(request):
	if request.method == 'POST':
		try:
			files=imports.import_nist_cpe()
			return render(request, 'cpe_nist_import.html', {'files':files,})			
		except:
			return render(request, 'cpe_nist_import.html', {'error_message': "request failed",})
	else:
			return render(request, 'cpe_nist_import.html')

def import_redhat_cpe(request):
	if request.method == 'POST':
		try:
			files=imports.import_redhat_cpe()
			return render(request, 'cpe_redhat_import.html', {'files':files,})			
		except:
			return render(request, 'cpe_redhat_import.html', {'error_message': "request failed",})
	else:
			return render(request, 'cpe_redhat_import.html')
