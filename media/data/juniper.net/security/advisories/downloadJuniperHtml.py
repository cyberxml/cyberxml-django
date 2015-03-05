import os
import os.path
import sys
import shutil
import urllib2
import urllib
from lxml.html import fromstring, tostring

produrls = [
	"http://kb.juniper.net/InfoCenter/index?page=content&channel=SECURITY_ADVISORIES&cat=SIRT_ADVISORY&&actp=&sort=datemodified&dir=descending&max=1000&batch=1000&rss=true&itData.offset=0",
	]

apslinks=[]
for pu in produrls:
	content = urllib.urlopen(pu).read()
	doc = fromstring(content)
	doc.make_links_absolute("http://kb.juniper.net/InfoCenter/")
	for a in doc.xpath('//a[contains(@href,"id=JSA") and contains(@href,"showDraft")]'):
		apslinks.append(a.get('href'))

apslinks = list(set(list(apslinks)))
apslinks.sort()

# -----------------------------------------------------------------------------
# download files if they don't exist
# TODO: check for revisions and download those as well (check hashes?)
# -----------------------------------------------------------------------------
for u in apslinks:
	uname = u.split('id=')[1].split('&')[0]+'.html'
	# if file does not exist, download
	if (not os.path.isfile(uname) and os.access(".", os.W_OK)):
		print ("downloading "+uname)
		headers = { 'User-Agent' : 'Mozilla/5.0' }
		req = urllib2.Request(u, None, headers)
		urllib.urlretrieve (u, uname)
