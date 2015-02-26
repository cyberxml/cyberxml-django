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
	doc.make_links_absolute(url)
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

# -----------------------------------------------------------------------------
# convert from HTML to CVRF XML
# -----------------------------------------------------------------------------
xslt_root = etree.XML('''
<xsl:styleshversion="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:templmatch="/">
     <foo><xsl:valueselect="/a/b/text/></foo>
  </xsl:template>
</xsl:stylesheet>''')

html2cvrf={}
html2cvrf['title']=''
html2cvrf['description']=''
html2cvrf['creationdate']=''
html2cvrf['lastmodifieddate']=''
html2cvrf['release date']=''
html2cvrf['vulnerability identifier']=''
html2cvrf['cve nubmers']=''
html2cvrf['platform']=''
html2cvrf['swlist']=''

parser = etree.HTMLParser()
tree   = etree.parse(uname, parser)
root=tree.getroot()
# Title: Adobe Security Bulletin
html2cvrf['title']=root.findall(".//meta[@name='title']")[0].get('content')
# Description: Security update for Flash Player, released December 10 2013
html2cvrf['description']=root.findall(".//meta[@name='description']")[0].get('content')
# creationDate: 2015-02-19 @ 13:09:35
html2cvrf['creationdate']=root.findall(".//meta[@name='creationDate']")[0].get('content')
# lastModifiedDate: 2015-02-19 @ 13:09:35
html2cvrf['lastmodifieddate']=root.findall(".//meta[@name='lastModifiedDate']")[0].get('content')
#
'''
<p><strong>Release date:</strong>&nbsp;February 5, 2015</p>
<p><strong>Last updated:</strong> February 19, 2015</p>
<p><strong>Vulnerability identifier:</strong> APSB15-04</p>
<p><strong>Priority:&nbsp;</strong><a href="#table">See table below</a></p>
<p><strong>CVE number</strong>:&nbsp;CVE-2015-0313, CVE-2015-0314, CVE-2015-0315, CVE-2015-0316, CVE-2015-0317,&nbsp;CVE-2015-0318,&nbsp;CVE-2015-0319, CVE-2015-0320, CVE-2015-0321, CVE-2015-0322, CVE-2015-0323, CVE-2015-0324, CVE-2015-0325, CVE-2015-0326, CVE-2015-0327, CVE-2015-0328, CVE-2015-0329, CVE-2015-0330, CVE-2015-0331</p>
<p><strong>Platform:</strong> All Platforms</p>
'''
div0=root.findall(".//div/[@class='text parbase section']")[0]
paras = div0.findall(".//div/p")
etree.tostring(paras[1])


for p in paras:
	try:
		html2cvrf[p.find("./strong").text.split(':')[0].lower()]=etree.tostring(p).split('</strong>')[1].split('<')[0]
	except:
		print "No key for: "+p.find("./strong").text.split(':')[0].lower()



div2=root.findall(".//div/[@class='text parbase section']")[2]
swlist=div2.findall(".//div/ul/li")
slist=[]
for sw in swlist:
	try:
		slist.append(sw.find("./p").text.split(' and ')[0])
	except:
		try:
			slist.append(sw.text.split(' and ')[0])
		except:
			print "failed to parse sw from: "+etree.tostring(sw)
		

html2cvrf['swlist']=slist


