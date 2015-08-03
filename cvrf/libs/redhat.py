import urllib2
import os
from eulexistdb import db
from django.conf import settings
#import bz2
#from bz2 import decompress
import tarfile
import glob

media_root = settings.MEDIA_ROOT
root_src_dir = '/tmp/cvrf/'
redhat_data_dir = media_root+'/data/redhat.com/security/data/cvrf/'
redhat_oval_dir = media_root+'/data/redhat.com/security/data/oval/'

db_cvrf_redhat_collection = '/db/cyberxml/data/cvrf/redhat.com'
db_oval_redhat_collection = '/db/cyberxml/data/oval/redhat.com'

# converting oval criterion to cpe fields
platdict={
'Red Hat Enterprise Linux 3 is installed':'cpe:/o:redhat:rhel_els:3::es/',
'Red Hat Enterprise Linux 4 is installed':'cpe:/o:redhat:rhel_els:4::es/',
'Red Hat Enterprise Linux 5 is installed':'cpe:/o:redhat:enterprise_linux::3:server/',
'Red Hat Enterprise Linux 6 Client is installed':'cpe:/o:redhat:enterprise_linux:6::client/',
'Red Hat Enterprise Linux 6 ComputeNode is installed':'cpe:/o:redhat:enterprise_linux:6::computernode/',
'Red Hat Enterprise Linux 6 Server is installed':'cpe:/o:redhat:enterprise_linux:6::server/',
'Red Hat Enterprise Linux 6 Workstation is installed':'cpe:/o:redhat:enterprise_linux:6::workstation/',
'Red Hat Enterprise Linux 7 Client is installed':'cpe:/o:redhat:enterprise_linux:7::client/',
'Red Hat Enterprise Linux 7 ComputeNode is installed':'cpe:/o:redhat:enterprise_linux:7::computernode/',
'Red Hat Enterprise Linux 7 Server is installed':'cpe:/o:redhat:enterprise_linux:7::server/',
'Red Hat Enterprise Linux 7 Workstation is installed':'cpe:/o:redhat:enterprise_linux:7::workstation/'
}
 
# global variables
rhsa2cve={}
rhsa2cpe={}
cve2rhsa={}
cve2cpe={}
cpe2rhsa={}
cpe2cve={}

rhsamapcpe_text=[]

def validateCollection(xdb, path):
	p = path.split('/')
	flag =0
	for i in range(len(p)):
		if not xdb.hasCollection('/'.join(p[0:i+1])):
			try:
				xdb.createCollection('/'.join(p[0:i+1]))
			except:
				flag=-1
	return flag

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

def get_qryRedhatOvalCvePlatform(cve):
	qry = '''xquery version "3.0";
	declare namespace unix-def = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix";
	declare namespace oval-def = "http://oval.mitre.org/XMLSchema/oval-definitions-5";
	declare namespace oval = "http://oval.mitre.org/XMLSchema/oval-common-5";
	declare namespace red-def = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux";
	let $thiscve := "'''+cve+'''"
	for $platform in collection('/db/cyberxml/data/oval/redhat.com')//node()[node()[node()[oval-def:cve[contains(.,$thiscve)]]]]//oval-def:criterion[contains(@comment,' is installed')]/@comment/string()
	return $platform'''
	return qry



def get_qryRedhatOvalCveComponent(cve):
	qry = '''xquery version "3.0";
	declare namespace unix-def = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix";
	declare namespace oval-def = "http://oval.mitre.org/XMLSchema/oval-definitions-5";
	declare namespace oval = "http://oval.mitre.org/XMLSchema/oval-common-5";
	declare namespace red-def = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux";
	let $thiscve := "'''+cve+'''"
	for $component in collection('/db/cyberxml/data/oval/redhat.com')//node()[node()[node()[oval-def:cve[contains(.,$thiscve)]]]]//oval-def:criterion[contains(@comment,' is earlier')]/@comment/string()
	return $component'''
	return qry

def import_rhsamapcpe(fn=None):
	global rhsamapcpe_text
	try:
		rhsamapcpe_text = open(fn,'r').readlines()
	except:
		try:
			headers = { 'User-Agent' : 'Mozilla/5.0' }
			req = urllib2.Request("https://www.redhat.com/security/data/metrics/rhsamapcpe.txt", None, headers)
			rhsamapcpe_text = urllib2.urlopen(req).read().split('\n')
		except:
			print("import_rhsamapcpe: failed to import file")
	return rhsamapcpe_text


#------------------------------------------------------------------------------
# Redhat OVAL
#------------------------------------------------------------------------------
def download_redhat_oval():
	exdb = db.ExistDB()	 
	validateCollection(exdb,db_oval_redhat_collection)
	
	try:
		dlurl="https://www.redhat.com/security/data/oval/rhsa.tar.bz2"
		headers = { 'User-Agent' : 'Mozilla/5.0' }
		req = urllib2.Request(dlurl, None, headers)
		dlreq = urllib2.urlopen(req)
		CHUNK = 16 * 1024
		with open(redhat_oval_dir+'rhsa.tar.bz2', 'wb') as fp:
		  while True:
			chunk = dlreq.read(CHUNK)
			if not chunk: break
			fp.write(chunk)
		try:
			tar = tarfile.open(redhat_oval_dir+'rhsa.tar.bz2', 'r:bz2')
			tar.extractall(redhat_oval_dir)
		except:
			print("import_redhat_oval: failed to uncompress tar.bz2 file")
	except:
		print("import_redhat_oval: failed to download file")
	return

def import_redhat_oval():
	flist=[]
	exdb = db.ExistDB()
	# download
	download_redhat_oval()
	# get list of file names
	for fname in glob.glob(redhat_oval_dir+"com.redhat.rhsa-*.xml"):
		uname = fname.split(os.sep)[-1]
		try:
			fo = open(redhat_oval_dir+uname, 'rb')
			if exdb.load(fo, db_oval_redhat_collection+'/'+uname, True):
				flist.append(uname+": data import successful")
			else:
				flist.append(uname+": data import failed")
			fo.close()
		except:
			flist.append(uname+": file read failed")
	return flist
	

def reset_dicts():
	global rhsa2cve
	global rhsa2cpe
	global cve2rhsa
	global cve2cpe
	global cpe2rhsa
	global cpe2cve
	rhsa2cve={}
	rhsa2cpe={}
	cve2rhsa={}
	cve2cpe={}
	cpe2rhsa={}
	cpe2cve={}

def add2dict(d,n,v):
	try:
		if d[n]:
			d[n]=d[n] + v
		else:
			d[n]=v
	except:
		try:
			d[n]=v
		except:
			print("add2dict: failed twice on "+n+" | "+v)
	return

def load_dicts():
	global rhsamapcpe_text
	for line in rhsamapcpe_text:
		try:
			line=line.replace('\n','')
			this=line.split(' ')
			rhsa=this[0]
			cves=[i for i in this[1].split(',')]
			cpes=[i for i in this[2].split(',')]
			add2dict(rhsa2cve,rhsa,cves)
			add2dict(rhsa2cpe,rhsa,cpes)
			for c in cves:
				add2dict(cve2rhsa,c,[rhsa])
				add2dict(cve2cpe,c,cpes)
			for c in cpes:
				add2dict(cpe2rhsa,c,[rhsa])
				add2dict(cpe2cve,c,cves)
		except:
			print("parsing rhsamapcpe bombed on line: "+line)

def getCpeFromRhsa(rhsa):
	global rhsa2cpe
	try:
		return rhsa2cpe[rhsa]
	except:
		return ([])

def getCveFromRhsa(rhsa):
	global rhsa2cve
	try:
		return rhsa2cve[rhsa]
	except:
		return ([])

def getRhsaFromCve(cve):
	global cve2rhsa
	try:
		return cve2rhsa[cve]
	except:
		return ([])

def getCpeFromCve(cve):
	global cve2cpe
	try:
		return cve2cpe[cve]
	except:
		return ([])

def getRhsaFromCpe(cpe):
	global cpe2rhsa
	try:
		return cpe2rhsa[cpe]
	except:
		return ([])

def getCveFromCpe(cpe):
	global cpe2cve
	try:
		return cpe2cve[cpe]
	except:
		return ([])

def getCpeFromCveOval(cve):
	try:
		qrystr_platform=get_qryRedhatOvalCvePlatform(cve)
		a = connExistDB()
		plats = a.get_data(qrystr_platform)
		plats = list(set(plats))
		plats.sort()
		for i in range(len(plats)):
			plats[i]=platdict[plats[i]]
		qrystr_component=get_qryRedhatOvalCveComponent(cve)
		a = connExistDB()
		comps = a.get_data(qrystr_component)
		comps = list(set(comps))
		comps.sort()
		for i in range(len(comps)):
			comps[i]=comps[i].split(' ')[0]
		cpes=[]
		for p in plats:
			for c in comps:
				cpes.append(''.join([p,c]))
	except:
		cpes=[]
	return(cpes)

# this will initialize on import
reset_dicts()
rhsamapcpe_text=import_rhsamapcpe()
load_dicts()
