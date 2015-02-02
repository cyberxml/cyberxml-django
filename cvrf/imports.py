import urllib2
import urllib
import os
import os.path
import zipfile
import shutil
from eulexistdb import db
from lxml import etree
from lxml.html import fromstring, tostring
from django.conf import settings


media_root = settings.MEDIA_ROOT
root_src_dir = '/tmp/cvrf/'
ms_data_dir = media_root+'/data/microsoft.com/MSRC-CVRF/'
redhat_data_dir = media_root+'/data/redhat.com/security/data/cvrf/'
oracle_data_dir = media_root+'/data/oracle.com/documents/webcontent/cvrf/'
cisco_data_dir = media_root+'/data/cisco.com/security/center/cvrfListing.x/'

db_cvrf_cisco_collection = '/db/cyberxml/data/cvrf/cisco.com'
db_cvrf_microsoft_collection = '/db/cyberxml/data/cvrf/microsoft.com'
db_cvrf_oracle_collection = '/db/cyberxml/data/cvrf/oracle.com'
db_cvrf_redhat_collection = '/db/cyberxml/data/cvrf/redhat.com'

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
# Microsoft MSRC-CVRF
#------------------------------------------------------------------------------
# filen=open("/tmp/msrc_cvrf.zip","rb")
def parse_msrc_cvrf_zip(fn):
	flist=[]
	filen=open(fn,"rb")
	exdb = db.ExistDB()
	validateCollection(exdb,db_cvrf_microsoft_collection)
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

	#walk files in dir and add to database
	#20140709rb: this is an awkward construction
	for root, dirs, files in os.walk(tmp_dir):
		for f in files:			
			#move tmp files to permanent location
			#TODO: use static definition
			src = root+'/'+f
			dst = ms_data_dir+f
			try:
				if f[-4:].lower()=='.xml':
					if os.path.exists(dst):
						os.remove(dst)
					shutil.move(src, dst)
					#logger.debug(': '.join(['move_iavm',src, dst]))
					#parse_xml(root+'/'+f) this is where I database boogie!
					fo = open(dst, 'rb')
					if exdb.load(fo, db_cvrf_microsoft_collection+'/'+f, True):
						flist.append(f+": data import successful")
					else:
						flist.append(f+": data import failed")
					fo.close()
			except:
				#logger.debug(': '.join(['move_iavm', 'FAILED',src, dst]))
				flist.append(f+": file upload failed")
				pass


	flist.reverse()
	return flist

#------------------------------------------------------------------------------
# Redhat CVRF
#------------------------------------------------------------------------------
def import_redhat_cvrf():
	flist=[]
	exdb = db.ExistDB()	 
	validateCollection(exdb,db_cvrf_redhat_collection)
	# -----------------------------------------------------------------------------
	# get list of cvrf urls
	# -----------------------------------------------------------------------------
	# need User-Agent or Red Hat blocks request
	nurl="http://www.redhat.com/security/data/cvrf/index.txt"
	headers = { 'User-Agent' : 'Mozilla/5.0' }
	req = urllib2.Request(nurl, None, headers)
	index = urllib2.urlopen(req).readlines()
	urls = ['http://www.redhat.com/security/data/cvrf/'+i.replace('\n','') for i in index]
	
	# -----------------------------------------------------------------------------
	# download files if they don't exist
	# TODO: check for revisions and download those as well (check hashes?)
	# -----------------------------------------------------------------------------
	for u in urls:
		uname = u.split('/')[-1]
		# if file does not exist, download
		#if (not os.path.isfile(redhat_data_dir+uname) and os.access(redhat_data_dir, os.W_OK)):
		if (os.access(redhat_data_dir, os.W_OK)):
			try:
				headers = { 'User-Agent' : 'Mozilla/5.0' }
				req = urllib2.Request(u, None, headers)
				cvrfxml = urllib2.urlopen(req).read()
				urllib.urlretrieve (u, redhat_data_dir+uname)
				f = open(redhat_data_dir+uname,'w')
				f.write(cvrfxml)
				f.close()
				try:
					fo = open(redhat_data_dir+uname, 'rb')
					if exdb.load(fo, db_cvrf_redhat_collection+'/'+uname, True):
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
# Oracle CVRF
#------------------------------------------------------------------------------
def import_oracle_cvrf():
	flist=[]
	exdb = db.ExistDB()
	validateCollection(exdb,db_cvrf_oracle_collection)
	# -----------------------------------------------------------------------------
	# get list of cvrf urls
	# -----------------------------------------------------------------------------
	nurl="http://www.oracle.com/ocom/groups/public/@otn/documents/webcontent/1932662.xml"
	request = urllib2.Request(nurl)
	rawPage = urllib2.urlopen(request)
	read = rawPage.read()
	#print read
	root = etree.fromstring(read)	 
	arefs=root.xpath("//link/text()")
	
	urls=[]
	for a in arefs:
		if "@otn" in a:
			urls.append(a.replace('\t','').replace('\n','').replace(' ',''))
    
	# -----------------------------------------------------------------------------
	# download files if they don't exist
	# -----------------------------------------------------------------------------
	for u in urls:
		uname = u.split('/')[-1]			
		# if file does not exist, download
		#if (not os.path.isfile(oracle_data_dir+uname) and os.access(oracle_data_dir, os.W_OK)):
		if (os.access(oracle_data_dir, os.W_OK)):
			try:
				urllib.urlretrieve (u, oracle_data_dir+uname)
				try:
					fo = open(oracle_data_dir+uname)
					if exdb.load(fo, db_cvrf_oracle_collection+'/'+uname, True):
						flist.append(uname+": data import successful")
					else:
						flist.append(uname+": data import failed")
					fo.close()
				except:
					flist.append(uname+": file read failed : "+oracle_data_dir+uname)
			except:
				flist.append(uname+": file download failed : " +u)
		else:
			flist.append(uname+": file write failed : "+oracle_data_dir+uname)
    
	return flist

#------------------------------------------------------------------------------
# Cisco CVRF
#------------------------------------------------------------------------------
def import_cisco_cvrf():
	flist=[]
	exdb = db.ExistDB()	 
	validateCollection(exdb,db_cvrf_cisco_collection)
	
	# -----------------------------------------------------------------------------
	# get list of cvrf urls
	# -----------------------------------------------------------------------------
	nurl="http://tools.cisco.com/security/center/cvrfListing.x"
	request = urllib2.Request(nurl)
	rawPage = urllib2.urlopen(request)
	read = rawPage.read()
	#print read
	tree = etree.HTML(read)	   
	tpath="//a[contains(@href,'cvrf.xml')]"
	findall = etree.ETXPath(tpath)
	arefs=findall(tree)
	
	urls=[]
	for a in arefs:
		urls.append(a.get('href').replace('\t','').replace('\n',''))
	
	# just for tracking for now, need to get cisco to fix or apply a fix
	# i might ignore if it wasn't for poodle
	badfiles=["/cisco-sa-20040420-tcp-nonios_cvrf.xml",
		"cisco-sa-20120328-msdp_cvrf.xml",
		"cisco-sa-20141015-poodle_cvrf.xml",]
	
	# -----------------------------------------------------------------------------
	# download files if they don't exist
	# -----------------------------------------------------------------------------
	for u in urls:
		uname = u.split('/')[-1]
		# if file does not exist, download
		#if (not os.path.isfile(cisco_data_dir+uname) and os.access(".", os.W_OK)):
		if (os.access(".", os.W_OK)):
			try:
				print ("downloading "+uname)
				urllib.urlretrieve (u, cisco_data_dir+uname)
				try:
					fo = open(cisco_data_dir+uname, 'rb')
					if exdb.load(fo, db_cvrf_cisco_collection+'/'+uname, True):
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
