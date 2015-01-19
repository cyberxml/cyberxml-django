from lxml import etree
from lxml.html import fromstring, tostring
import urllib2
import urllib
import os.path
import os

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

# -----------------------------------------------------------------------------
# download files if they don't exist
# -----------------------------------------------------------------------------
for u in urls:
	uname = u.split('/')[-1]
	# if file does not exist, download
	if (not os.path.isfile(uname) and os.access(".", os.W_OK)):
		urllib.urlretrieve (u, uname)