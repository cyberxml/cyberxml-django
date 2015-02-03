import urllib
import os.path
import os
from zipfile import ZipFile

urls=[]
urls.append("http://static.nvd.nist.gov/feeds/xml/cpe/dictionary/official-cpe-dictionary_v2.3.xml")
urls.append("http://static.nvd.nist.gov/feeds/xml/cpe/dictionary/official-cpe-dictionary_v2.2.xml")
# -----------------------------------------------------------------------------
# download files even if they exist; NIST is constantly updating them
# -----------------------------------------------------------------------------
for u in urls:
	uname = u.split('/')[-1]
	# if file does not exist, download
	if os.access(".", os.W_OK):
		print ("downloading "+uname)
		urllib.urlretrieve (u, uname)
		# unzip in place
		zip = ZipFile(uname)
		zip.extractall()
		zip.close()
		# remove zip file
		os.remove(uname)