import urllib
import urllib2
import os.path
import os
from zipfile import ZipFile
from django.conf import settings
from eulexistdb import db

from datetime import date

thisyear = date.today().year

media_root = settings.MEDIA_ROOT
cpe_nist_data_dir = media_root+'/data/nist.gov/nvd/cpe/'
cpe_redhat_data_dir = media_root+'/data/redhat.com/security/data/cpe/'
db_cpe_nist_collection = '/db/cyberxml/data/cpe/nist.gov'
db_cpe_redhat_collection = '/db/cyberxml/data/cpe/redhat.com'

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


def validateDataPath(path):
	p = path.split('/')
	flag =0
	for i in range(len(p)):
		if not os.path.exists('/'.join(p[0:i+1])):
			try:
				os.mkdir('/'.join(p[0:i+1]))
			except:
				flag=-1
	return flag


#------------------------------------------------------------------------------
# NIST NVD cpe
#------------------------------------------------------------------------------
def import_nist_cpe():
	flist=[]
	exdb = db.ExistDB()	 
	validateCollection(exdb,db_cpe_nist_collection)
	validateDataPath(cpe_nist_data_dir)
		
	urls=[]
	urls.append("http://static.nvd.nist.gov/feeds/xml/cpe/dictionary/official-cpe-dictionary_v2.3.xml")
	urls.append("http://static.nvd.nist.gov/feeds/xml/cpe/dictionary/official-cpe-dictionary_v2.2.xml")

	# -----------------------------------------------------------------------------
	# download files even if they exist; NIST is constantly updating them
	# -----------------------------------------------------------------------------
	for u in urls:
		uname = u.split('/')[-1]
		# if file does not exist, download
		if (os.access(cpe_nist_data_dir, os.W_OK)):
			try:
				urllib.urlretrieve (u, cpe_nist_data_dir+uname)
				try:
					fo = open(cpe_nist_data_dir+uname, 'rb')
					if exdb.load(fo, db_cpe_nist_collection+'/'+uname, True):
						flist.append(uname+": data import successful")
					else:
						flist.append(uname+": data import failed")
					fo.close()
				except:
					flist.append(uname+": file read failed")
			except:
				flist.append(uname+": file download failed")
		else:
			flist.append(uname+": file write failed")
	
	return flist

#------------------------------------------------------------------------------
# NIST NVD CVE
#------------------------------------------------------------------------------
def import_redhat_cpe():
	flist=[]
	exdb = db.ExistDB()	 
	validateCollection(exdb,db_cpe_redhat_collection)
	validateDataPath(cpe_redhat_data_dir)
	
	urls=[]
	urls.append("https://www.redhat.com/security/data/metrics/cpe-dictionary.xml")
	
	# -----------------------------------------------------------------------------
	# download files even if they exist; NIST is constantly updating them
	# -----------------------------------------------------------------------------
	for u in urls:
		uname = u.split('/')[-1]
		# if file does not exist, download
		if (os.access(cpe_nist_data_dir, os.W_OK)):
			try:
				urllib.urlretrieve (u, cpe_redhat_data_dir+uname)
				headers = { 'User-Agent' : 'Mozilla/5.0' }
				req = urllib2.Request(u, None, headers)
				cpexml = urllib2.urlopen(req).read()
				#urllib.urlretrieve (u, cpe_redhat_data_dir+uname)
				f = open(cpe_redhat_data_dir+uname,'w')
				f.write(cpexml)
				f.close()
				try:
					fo = open(cpe_redhat_data_dir+uname, 'rb')
					try:
						if exdb.load(fo, db_cpe_redhat_collection+'/'+uname, True):
							flist.append(uname+": data import successful")
					except:
						flist.append(uname+": data import failed")
					fo.close()
				except:
					flist.append(uname+": file read failed")
			except:
				flist.append(uname+": file download failed")
		else:
			flist.append(uname+": file write failed")
	
	return flist
