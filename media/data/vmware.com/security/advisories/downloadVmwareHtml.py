import os
import os.path
import sys
import shutil
from lxml import etree
from lxml.html import fromstring, tostring
import lxml
import urllib2
import urllib
from StringIO import StringIO


produrls = [
	"http://www.vmware.com/security/advisories",
	]

apslinks=[]
for pu in produrls:
	content = urllib.urlopen(pu).read()
	doc = fromstring(content)
	doc.make_links_absolute("https://www.vmware.com")
	for a in doc.xpath('//a[contains(@class,"l-reg")]'):
		apslinks.append(a.get('href'))

apslinks = list(set(list(apslinks)))
apslinks.sort()

# -----------------------------------------------------------------------------
# download files if they don't exist
# TODO: check for revisions and download those as well (check hashes?)
# -----------------------------------------------------------------------------
for u in apslinks:
	uname = u.split('/')[-1]
	# if file does not exist, download
	if (not os.path.isfile(uname) and os.access(".", os.W_OK)):
		print ("downloading "+uname)
		headers = { 'User-Agent' : 'Mozilla/5.0' }
		req = urllib2.Request(u, None, headers)
		urllib.urlretrieve (u, uname)

