import os
import os.path
import sys
import shutil
from datetime import date
from eulexistdb import db
from lxml import etree
from lxml.html import fromstring, tostring
import lxml
from django.conf import settings
from time import gmtime, strftime
import urllib2
import urllib
from StringIO import StringIO

media_root = settings.MEDIA_ROOT
adobe_data_dir = media_root+'/data/adobe.com/support/security/'
db_cvrf_adobe_collection = '/db/cyberxml/data/cvrf/adobe.com'

thisyear = date.today().year

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


class connExistDB:	  
	def __init__(self):
		self.db = db.ExistDB()	  
	def get_data(self, query):
		result = list()
		qresult = self.db.executeQuery(query)
		hits = self.db.getHits(qresult)
		for i in range(hits):
			result.append(str(self.db.retrieve(qresult, i)))
		return result
	
def get_qryAdobeCvrfCveCpe(cve):
	qry = '''xquery version "3.0";
	declare namespace cvrf = "http://www.icasi.org/CVRF/schema/cvrf/1.1";
	declare namespace prod = "http://www.icasi.org/CVRF/schema/prod/1.1";
	declare namespace vuln = "http://www.icasi.org/CVRF/schema/vuln/1.1";
	let $thiscve := "'''+cve+'''"
	for $pid in collection('/db/cyberxml/data/cvrf/oracle.com')//node()[vuln:CVE[.=$thiscve]]/vuln:ProductStatuses/vuln:Status[@Type="Known Affected"]/vuln:ProductID[starts-with(.,$cpe/ProductID/text())]
	return $cpe/CPE2.2/text()'''
	return qry


def getCpeFromCve(cve):
	try:
		qrystr=get_qryOracleCvrfCveCpe(cve)
		a = connExistDB()
		cpes =list(set(a.get_data(qrystr)))
	except:
		cpes=[]
	return(cpes)

def translateAdobeHtmlToCvrf(fullname):
	cvrf={}
	cvrf['DocumentTitle']=""
	cvrf['DocumentType']=""
	cvrf['DocumentTrackingID']=""
	cvrf['DocumentTrackingInitialReleaseDate']=""
	cvrf['DocumentTrackingCurrentReleaseDate']=""
	cvrf['DocumentNote']=""
	cvrf['ReferenceURL']=""
	cvrf['ReferenceDescription']=""
	#cvrf['ProductID']=""
	#cvrf['FullProductName']=""
	#cvrf['CVE']=""
	#cvrf['ProductID']=""
	
	uname=os.path.basename(fullname)
	parser = etree.HTMLParser()
	tree   = etree.parse(fullname, parser)
	root = tree.getroot()
	# DocumentType
	try:
		cvrf['DocumentType']=root.find(".//meta[@name='title']").get('content').strip()
	except:
		print("No title found")
	# DocumentTrackingInitialReleaseDate
	try:
		cvrf['DocumentTrackingInitialReleaseDate']=root.find(".//meta[@name='creationDate']").get('content').strip().replace(' @ ','T')+'Z'
	except:
		print("No InitialReleaseDate found; creating one")
		cvrf['DocumentTrackingInitialReleaseDate']=strftime("%Y-%m-%dT%H:%M:%SZ", gmtime())
	# DocumentTrackingCurrentReleaseDate
	try:
		cvrf['DocumentTrackingCurrentReleaseDate']=root.find(".//meta[@name='lastModifiedDate']").get('content').strip().replace(' @ ','T')+'Z'
	except:
		print("No CurrentReleaseDate found; creating one")
		cvrf['DocumentTrackingCurrentReleaseDate']=strftime("%Y-%m-%dT%H:%M:%SZ", gmtime())
	# DocumentTitle: Security update for Flash Player, released December 10 2013
	try:
		cvrf['DocumentTitle']=root.find(".//meta[@name='description']").get('content').strip()
	except:
		print("No description found; creating one")
		cvrf['DocumentTitle']= "Security update for Adobe Product, cvrf dated "+strftime("%Y-%m-%dT%H:%M:%SZ", gmtime())
	# DocumentTrackingCurrentReleaseDate
	try:
		cvrf['DocumentTrackingID']=''.join(tree.xpath('//node()[strong[.="Vulnerability identifier:"]]')[0].itertext()).split(':')[1].replace(' ','').strip()
	except:
		print("No vulnerability identifier found; creating one")
		cvrf['DocumentTrackingID']=uname.upper().replace('.html','')
	# DocumentTrackingCurrentReleaseDate
	try:
		cvrf['DocumentTrackingID']=''.join(tree.xpath('//node()[strong[.="Vulnerability identifier:"]]')[0].itertext()).split(':')[1].replace(' ','').strip()
	except:
		print("No vulnerability identifier found; creating one")
		cvrf['DocumentTrackingCurrentReleaseDate']=uname.upper().replace('.html','')
	# DocumentNote
	try:
		cvrf['DocumentNote']=''.join(tree.xpath('.//div[@class="text parbase section"]')[1].itertext()).replace('\r','').replace('\n','').replace('	 ',' ').strip()
	except:
		print("Document note not found; creating one")
		cvrf['DocumentNote']="CyberXML placeholder. HTML security notice not in current format."
	# DocumentNote
	try:
		cvrf['ReferenceURL']=tree.xpath('.//link[contains(@href,"'+uname+'")]')[0].get('href')
	except:
		print("ReferenceURL note not found; creating one")
		cvrf['DocumentNote']="https://helpx.adobe.com/security.html"
	# ReferenceDescription
	cvrf['ReferenceDescription']=cvrf['DocumentTitle']
	
	# -----------------------------------------------------------------------------
	# create cpe for productID and keep FullProductName as in Affected Software
	# -----------------------------------------------------------------------------
	try:
		d=tree.xpath('.//div[@class="text parbase section"]')[2]
		li=d.findall("./div/ul/li")
	except:
		print("Cannot read 'Affected Software'; aborting")
		quit(-1)
	
	sw=[]
	for l in li:
		sw.append(''.join(l.itertext()).strip().replace(u'\xa0', ' ').strip().encode())
	
	products=[]
	for i in range(len(sw)):
		this = sw[i].replace('Adobe Flash Player','cpe:/a:adobe:flash-player:')
		this = this.replace('Adobe Reader','cpe:/a:adobe:reader:')
		this = this.replace('Adobe Acrobat','cpe:/a:adobe:acrobat:')
		# 14-09
		# Adobe AIR 4.0.0.1628 SDK and earlier versions
		# Adobe AIR 4.0.0.1628 SDK &amp; Compiler 
		if 'Adobe AIR' in this:
			if 'SDK &amp; Compiler' in this:
				this = this.replace('SDK &amp; Compiler ','').replace('AIR', 'AIR SDK and Compiler')
			elif 'SDK & Compiler' in this:
				this = this.replace('SDK & Compiler ','').replace('AIR', 'AIR SDK and Compiler')
			elif 'SDK and Compiler' in this:
				this = this.replace('SDK and Compiler ','').replace('AIR' , 'AIR SDK and Compiler')
			elif 'SDK' in this:
				this = this.replace('SDK ','').replace('AIR' , 'AIR SDK')
		# 15-01
		# Adobe AIR desktop runtime 15.0.0.356 and earlier versions
		# Adobe AIR SDK and Compiler 15.0.0.356 and earlier versions
		# Adobe AIR SDK &amp; Compiler 15.0.0.302 and earlier versions
		# <vuln:ProductID>cpe:/a:adobe:air:desktopruntime15.0.0.356</vuln:ProductID>
		this = this.replace('Adobe AIR desktop runtime','cpe:/a:adobe:air_desktop_runtime:')
		this = this.replace('Adobe AIR SDK and Compiler','cpe:/a:adobe:air_sdk_compiler:')
		this = this.replace('Adobe AIR SDK &amp; Compiler','cpe:/a:adobe:air_sdk_compiler:')
		this = this.replace('Adobe AIR SDK','cpe:/a:adobe:air_sdk:')
		this = this.replace('Adobe AIR','cpe:/a:adobe:air:')
		
		this = this.replace('X','')
		this = this.replace('I','')
		this = this.replace('V','')
		this = this.replace(')','')
		this = this.replace('(','')
		these = this.split('and')
		cpe = these[0].replace(' ','')
		print cpe
		if 'for' in sw[i]:
			for x in sw[i].split('for')[1].split():
				x=x.replace(',','').lower()
				if x=='windows':
					products.append([sw[i],cpe+'::~~~windows~~'])
				if x=='macintosh':
					products.append([sw[i],cpe+'::~~~macintosh~~'])
				if x=='linux':
					products.append([sw[i],cpe+'::~~~linux~~'])
		else:
			products.append([sw[i],cpe])
	
	# import cvrf template
	mincvrf=etree.parse('minimumCvrfTemplate.xml')
	mincvrf.find("//{http://www.icasi.org/CVRF/schema/cvrf/1.1}DocumentTitle").text=cvrf['DocumentTitle']
	mincvrf.find("//{http://www.icasi.org/CVRF/schema/cvrf/1.1}DocumentType").text=cvrf['DocumentType']
	mincvrf.find("//{http://www.icasi.org/CVRF/schema/cvrf/1.1}InitialReleaseDate").text=cvrf['DocumentTrackingInitialReleaseDate']
	mincvrf.find("//{http://www.icasi.org/CVRF/schema/cvrf/1.1}CurrentReleaseDate").text=cvrf['DocumentTrackingCurrentReleaseDate']
	mincvrf.find("//{http://www.icasi.org/CVRF/schema/cvrf/1.1}Date").text=strftime("%Y-%m-%dT%H:%M:%SZ", gmtime())
	mincvrf.find("//{http://www.icasi.org/CVRF/schema/cvrf/1.1}ID").text=cvrf['DocumentTrackingID']
	mincvrf.find('//{http://www.icasi.org/CVRF/schema/cvrf/1.1}Note[@Ordinal="3"]').text=cvrf['DocumentNote']
	mincvrf.find("//{http://www.icasi.org/CVRF/schema/cvrf/1.1}URL").text=cvrf['ReferenceURL']
	mincvrf.find('//{http://www.icasi.org/CVRF/schema/cvrf/1.1}Description').text=cvrf['ReferenceDescription']
	
	'''
	  <prod:FullProductName ProductID="%ProductID%">%FullProductName%</prod:FullProductName>
	'''
	try:
		pt=mincvrf.find('//{http://www.icasi.org/CVRF/schema/prod/1.1}ProductTree')
		for p in products:
			fpn=etree.Element('{http://www.icasi.org/CVRF/schema/prod/1.1}FullProductName',ProductID=p[1])
			cpe=etree.Element('{http://www.icasi.org/CVRF/schema/prod/1.1}CPE')
			cpe.text=p[1]
			cpe.tail='\n'
			fpn.append(cpe)
			fpn.text=p[0]
			fpn.tail='\n'
			pt.append(fpn)
	except:
		print("No Software/CPEs found")
	
	'''
	<vuln:Vulnerability Ordinal="1">
	  <vuln:Title xml:lang="en">%VulnerabilityTitle%</vuln:Title>
		<CVE>%CVE%</CVE>
		<vuln:ProductStatuses>
		  <vuln:Status Type="Known Affected">
			<vuln:ProductID>%ProductID%</vuln:ProductID>
		  </vuln:Status>
		</vuln:ProductStatuses>
	</vuln:Vulnerability>
	'''
	# cves translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')
	try:
		cves=''.join(tree.xpath('//node()[strong[contains(translate((.), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"),"cve number")]]')[0].itertext()).split(':')[1].strip().split(',')
		for i in range(len(cves)):
			vuln=etree.Element('{http://www.icasi.org/CVRF/schema/vuln/1.1}Vulnerability',Ordinal=str(i+1))
			vuln.tail='\n'
			cve=etree.Element('{http://www.icasi.org/CVRF/schema/vuln/1.1}CVE')
			cve.text=cves[i].replace(' ','').strip()
			cve.tail='\n'
			vuln.append(cve)
			ps=etree.Element('{http://www.icasi.org/CVRF/schema/vuln/1.1}ProductStatuses')
			ps.tail='\n'
			stat=etree.Element('{http://www.icasi.org/CVRF/schema/vuln/1.1}Status',Type="Known Affected")
			stat.tail='\n'
			for p in products:
				pid = etree.Element('{http://www.icasi.org/CVRF/schema/vuln/1.1}ProductID')
				pid.text=p[1]
				pid.tail='\n'
				stat.append(pid)
			ps.append(stat)
			vuln.append(ps)
			mincvrf.getroot().append(vuln)
	except:
		print("No CVEs found")
	
	mincvrf.write(outfile,pretty_print=True,xml_declaration=True, encoding='utf-8')

def importAdobeHtml():
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
			#cvrfhtml = urllib2.urlopen(req).read()
			urllib.urlretrieve (u, adobe_data_dir+uname)
			#f = open(uname,'w')
			#f.write(cvrfhtml)
			#f.close()
			try:
				if int(uname[4:6])>13:
					translateAdobeHtmlToCvrf(adobe_data_dir+uname)
			except:
				pass
