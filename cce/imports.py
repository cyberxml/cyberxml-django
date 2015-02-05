import urllib
import os
import os.path
from zipfile import ZipFile
from django.conf import settings
from eulexistdb import db

from datetime import date

thisyear = date.today().year

media_root = settings.MEDIA_ROOT
cce_data_dir = media_root+'/data/nist.gov/nvd/cce/'
db_cce_nist_collection = '/db/cyberxml/data/cce/nist.gov'

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
# NIST NVD CCE
#------------------------------------------------------------------------------
def import_nist_cce():
	flist=[]
	exdb = db.ExistDB()	 
	validateCollection(exdb,db_cce_nist_collection)
	validateDataPath(cce_data_dir)
		
	urls=[]
	urls.append("http://static.nvd.nist.gov/feeds/xml/cce/nvdcce-0.1-feed.xml.zip")

	# -----------------------------------------------------------------------------
	# download files even if they exist; NIST is constantly updating them
	# -----------------------------------------------------------------------------
	for u in urls:
		uname = u.split('/')[-1]
		# if file does not exist, download
		if (os.access(cce_data_dir, os.W_OK)):
			try:
				urllib.urlretrieve (u, cce_data_dir+uname)
				# unzip in place
				zip = ZipFile(cce_data_dir+uname)
				zip.extractall(cce_data_dir)
				zip.close()
				# remove zip file
				os.remove(cce_data_dir+uname)
				try:
					xname = uname.replace('.zip','')
					fo = open(cce_data_dir+xname, 'rb')
					try:
						if exdb.load(fo, db_cce_nist_collection+'/'+xname, True):
							flist.append(xname+": data import successful")
					except:
						flist.append(xname+": data import failed")
					fo.close()
				except:
					flist.append(uname+": file read failed")
			except:
				flist.append(uname+": file download failed")
		else:
			flist.append(uname+": file write failed")
	
	return flist
