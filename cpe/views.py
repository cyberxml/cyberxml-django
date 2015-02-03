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
