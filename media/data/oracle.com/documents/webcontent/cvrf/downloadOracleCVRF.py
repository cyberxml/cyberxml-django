from lxml import etree
from lxml.html import fromstring, tostring
import urllib2
import urllib
import os.path
import os

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
		urls.append(a.replace('\t','').replace('\n',''))

# -----------------------------------------------------------------------------
# download files if they don't exist
# -----------------------------------------------------------------------------
for u in urls:
	uname = u.split('/')[-1]
	# if file does not exist, download
	if (not os.path.isfile(uname) and os.access(".", os.W_OK)):
		print ("downloading "+uname)
		urllib.urlretrieve (u, uname)