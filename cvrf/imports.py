import zipfile
import os
import shutil
from eulexistdb import db

root_src_dir = '/tmp/cvrf/'
root_dst_dir = '/opt/projects/django-cyberxml/static/data/microsoft.com/MSRC-CVRF/'

#------------------------------------------------------------------------------
# parse zip main def
#------------------------------------------------------------------------------
# filen=open("/tmp/iavms.zip","rb")
def parse_msrc_cvrf_zip(fn):
	flist=[]
	filen=open(fn,"rb")
	exdb = db.ExistDB()	  
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
			dst = root_dst_dir+f
			try:
				if f[-4:].lower()=='.xml':
					if os.path.exists(dst):
						os.remove(dst)
					shutil.move(src, dst)
					#logger.debug(': '.join(['move_iavm',src, dst]))
					#parse_xml(root+'/'+f) this is where I database boogie!
					fo = open(dst, 'rb')
					if exdb.load(fo, "/db/cvrf/microsoft.com/"+f, True):
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