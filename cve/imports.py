import urllib
import os.path
import os
from zipfile import ZipFile
from django.conf import settings
from eulexistdb import db

from datetime import date

thisyear = date.today().year

media_root = settings.MEDIA_ROOT
cve_data_dir = media_root+'/data/nist.gov/nvd/cve/'
db_cve_nist_collection = '/db/cyberxml/data/cve/nist.gov'

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


#------------------------------------------------------------------------------
# NIST NVD CVE
#------------------------------------------------------------------------------
def import_nist_cve():
	flist=[]
	exdb = db.ExistDB()	 
	validateCollection(exdb,db_cve_nist_collection)
		
	urls=[]
	for year in range(2002,thisyear+1):
		urls.append("http://static.nvd.nist.gov/feeds/xml/cve/nvdcve-2.0-"+str(year)+".xml.zip")

	# -----------------------------------------------------------------------------
	# download files even if they exist; NIST is constantly updating them
	# -----------------------------------------------------------------------------
	for u in urls:
		uname = u.split('/')[-1]
		# if file does not exist, download
		if (os.access(cve_data_dir, os.W_OK)):
			try:
				urllib.urlretrieve (u, cve_data_dir+uname)
				# unzip in place
				zip = ZipFile(cve_data_dir+uname)
				zip.extractall(cve_data_dir)
				zip.close()
				# remove zip file
				os.remove(cve_data_dir+uname)
				try:
					xname = uname.replace('.zip','')
					fo = open(cve_data_dir+xname, 'rb')
					if exdb.load(fo, db_cve_nist_collection+'/'+xname, True):
						flist.append(xname+": data import successful")
					else:
						flist.append(xname+": data import failed")
					fo.close()
				except:
					flist.append(uname+": file read failed")
			except:
				flist.append(uname+": file download failed")
		else:
			flist.append(uname+": file write failed")
	
	return flist
