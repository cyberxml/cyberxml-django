import urllib2
import urllib
import os.path
import os
import lxml
from lxml import etree
from StringIO import StringIO


# -----------------------------------------------------------------------------
# get list of security advisory by product
# -----------------------------------------------------------------------------

import urllib
from lxml.html import fromstring

produrls = [
	"https://helpx.adobe.com/security/products/reader.html",
	"https://helpx.adobe.com/security/products/flash-player.html",
	]

apslinks=[]
for pu in produrls:
	content = urllib.urlopen(pu).read()
	doc = fromstring(content)
	doc.make_links_absolute("https://helpx.adobe.com")
	for a in doc.xpath('//a[contains(@href,"/aps")]'):
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
		cvrfxml = urllib2.urlopen(req).read()
		urllib.urlretrieve (u, uname)
		f = open(uname,'w')
		f.write(cvrfxml)
		f.close()
