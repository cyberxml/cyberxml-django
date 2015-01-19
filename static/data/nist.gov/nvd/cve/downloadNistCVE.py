import urllib
import os.path
import os
from zipfile import ZipFile

#TODO: make the endpoint 'this' year
urls=[]
for year in range(2002,2016):
	urls.append("http://static.nvd.nist.gov/feeds/xml/cve/nvdcve-2.0-"+str(year)+".xml.zip")

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
		# remove zip file
		os.remove(uname)