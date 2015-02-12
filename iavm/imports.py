import urllib
import os.path
import os
import shutil
import zipfile
import glob
from django.conf import settings
from eulexistdb import db

from datetime import date

thisyear = date.today().year

media_root = settings.MEDIA_ROOT
disa_pki_flag = settings.USE_DISA_PKI
root_src_dir = '/tmp/iavms/'
iavm_cve_data_dir = media_root+'/data/disa.mil/iavm/cve/'
iavm_data_dir = media_root+'/data/disa.mil/iavm/'
db_iavm_cve_disa_collection = '/db/cyberxml/data/iavm/cve/disa.mil'
db_iavm_disa_collection = '/db/cyberxml/data/iavm/disa.mil'

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
# DISA IAVM to CVE
#------------------------------------------------------------------------------
def import_disa_iavm_cve():
	flist=[]
	exdb = db.ExistDB()	 
	validateCollection(exdb,db_iavm_cve_disa_collection)
	validateDataPath(iavm_cve_data_dir)
		
	urls=[]
	urls.append(("http://iasecontent.disa.mil/stigs/xml/iavm-to-cve%28u%29.xml","u_iavm-to-cve.xml"))
	
	# -----------------------------------------------------------------------------
	# download files even if they exist; NIST is constantly updating them
	# -----------------------------------------------------------------------------
	for url in urls:
		u = url[0]
		uname = url[1]
		# if file does not exist, download
		if (os.access(iavm_cve_data_dir, os.W_OK)):
			try:
				urllib.urlretrieve (u, iavm_cve_data_dir+uname)
				try:
					fo = open(iavm_cve_data_dir+uname, 'rb')
					try:
						if exdb.load(fo, db_iavm_cve_disa_collection+'/'+uname, True):
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

#------------------------------------------------------------------------------
# DISA IAVM
#------------------------------------------------------------------------------
# fn="/tmp/disa_iavm.zip"
def parse_disa_iavm_zip(fn):
	if not disa_pki_flag:
		return []
	flist=[]
	filen=open(fn,"rb")
	exdb = db.ExistDB()
	validateCollection(exdb,db_iavm_disa_collection)
	#logger.debug(': '.join(['parse_zip',filen.name]))

	#create zipfile object from passed in zip file object
	z_file = zipfile.ZipFile(filen)

	#create temporary directory
	f_name = filen.name.split('/')[-1]
	dir_name = f_name.replace('.zip', '')

	tmp_dir = root_src_dir + dir_name + '/'

	#logger.info(tmp_dir)

	if not os.path.exists(tmp_dir):
		os.makedirs(tmp_dir)

	#extract files to tmp dir
	z_file.extractall(tmp_dir)

	# walk files in dir and add to database
	# ValueError: too many values to unpack
	# for root, dirs, files in os.walk(tmp_dir):
	for src in glob.glob(tmp_dir+'/*/*.xml'):
		print src
		f =  src.split(os.sep)[-1].split()[0]+'.xml'
		#move tmp files to permanent location
		#TODO: use static definition
		dst = iavm_data_dir+f
		try:
			if os.path.exists(dst):
				os.remove(dst)
			shutil.move(src, dst)
			#logger.debug(': '.join(['move_iavm',src, dst]))
			#parse_xml(root+'/'+f) this is where I database boogie!
			fo = open(dst, 'rb')
			try:
				if exdb.load(fo, db_iavm_disa_collection+'/'+f, True):
					flist.append(f+": data import successful")
			except:
				flist.append(f+": data import failed")
			fo.close()
		except:
			#logger.debug(': '.join(['move_iavm', 'FAILED',src, dst]))
			flist.append(f+": file upload failed")
			pass


	flist.reverse()
	return flist
