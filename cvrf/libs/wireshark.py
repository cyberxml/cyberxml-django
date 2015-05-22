import os
import os.path
import sys
import shutil
from datetime import date
from datetime import datetime
from dateutil import parser as dtparser
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
static_root = settings.STATIC_ROOT
wireshark_data_dir = media_root+'/data/wireshark.org/security/'
db_cvrf_wireshark_collection = '/db/cyberxml/data/cvrf/wireshark.org'

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

def validateMediaPath(path):
    flag =0
    try:
        if not os.path.exists(path):
            os.makedirs(path)
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
    
def get_qryWiresharkCvrfCveCpe(cve):
    qry = '''xquery version "3.0";
    declare namespace cvrf = "http://www.icasi.org/CVRF/schema/cvrf/1.1";
    declare namespace prod = "http://www.icasi.org/CVRF/schema/prod/1.1";
    declare namespace vuln = "http://www.icasi.org/CVRF/schema/vuln/1.1";
    let $thiscve := "'''+cve+'''"
    for $cpe in collection('/db/cyberxml/data/cvrf/wireshark.org')//node()[vuln:CVE[.=$thiscve]]/vuln:ProductStatuses/vuln:Status[@Type="Known Affected"]/vuln:ProductID/text()
    return $cpe'''
    return qry


def getCpeFromCve(cve):
    try:
        qrystr=get_qryWiresharkCvrfCveCpe(cve)
        a = connExistDB()
        cpes =list(set(a.get_data(qrystr)))
        cpes.sort()
    except:
        cpes=[]
    return(cpes)

def translateWiresharkHtmlToCvrf(fullname):
    cvrf={}
    cvrf['DocumentTitle']=""
    cvrf['DocumentType']="Security Advisory"
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
    print("wireshark::translateWiresharkHtmlToCvrf::"+fullname)
    parser = etree.HTMLParser()
    tree   = etree.parse(fullname, parser)
    root = tree.getroot()
    
    # DocumentTitle
    try:
        cvrf['DocumentTitle']=root.find(".//title").text.encode('utf-8').replace('\xb7','-').replace('\xc2','').strip()
    except:
        print("No description found; creating one")
        vmsa=root.find(".//meta[@name='title']").get('content').strip()
        cvrf['DocumentTitle']= "Security Advisory for "+vmsa
    
    # DocumentType
    '''
    try:
        cvrf['DocumentType']=root.find(".//meta[@name='title']").get('content').strip()
    except:
        print("No title found")
    '''
    
    # DocumentTrackingInitialReleaseDate
    try:
        d=root.xpath('.//p/strong[contains(text(),"Date")]')[0].getparent()
        dt=''.join(d.itertext()).replace('Date:','').strip()
        dto=dtparser.parse(dt)
        cvrf['DocumentTrackingInitialReleaseDate']=dto.strftime('%Y-%m-%d')+"T00:00:00Z"
    except:
        print("No InitialReleaseDate found; creating one")
        cvrf['DocumentTrackingInitialReleaseDate']=strftime("%Y-%m-%dT%H:%M:%SZ", gmtime())
    
    # DocumentTrackingCurrentReleaseDate
    try:
        d=root.xpath('.//p/strong[contains(text(),"Date")]')[0].getparent()
        dt=''.join(d.itertext()).replace('Date:','').strip()
        dto=dtparser.parse(dt)
        cvrf['DocumentTrackingCurrentReleaseDate']=dto.strftime('%Y-%m-%d')+"T00:00:00Z"
    except:
        print("No CurrentReleaseDate found; creating one")
        cvrf['DocumentTrackingCurrentReleaseDate']=strftime("%Y-%m-%dT%H:%M:%SZ", gmtime())
    
    # DocumentTrackingID
    try:
        i=root.xpath('.//p/strong[contains(text(),"Docid:")]')[0].getparent()
        id=''.join(i.itertext()).replace('Docid:','').strip()
        cvrf['DocumentTrackingID']=id
    except:
        print("No vulnerability identifier found; creating one")
        cvrf['DocumentTrackingID']=uname.upper().replace('.HTML','')
    
    # DocumentNote
    # only retrieves first such content note
    try:
        n=root.xpath('.//p/strong[contains(text(),"Name")]')[0].getparent()
        note=''.join(n.itertext()).replace('Name:','').strip()
        cvrf['DocumentNote']=note
    except:
        print("Document note not found; creating one")
        cvrf['DocumentNote']="CyberXML placeholder. HTML security notice not in current format."
    
    # ReferenceURL
    try:
        n=root.xpath('.//p/strong[contains(text(),"Name")]')[0].getparent()
        note=''.join(n.itertext()).replace('Name:','').strip()
        cvrf['ReferenceURL']="https://www.wireshark.org/security/"+note+'.html'
    except:
        cvrf['ReferenceURL']='https://www.wireshark.org/security/'+uname
    
    # ReferenceDescription
    cvrf['ReferenceDescription']=cvrf['DocumentTitle']
    
    # -----------------------------------------------------------------------------
    # create cpe for productID
    # -----------------------------------------------------------------------------
    # advanced versions of this would handle wireshark version numbers
    
    # use black list to filter product candidates
    prod=['cpe:/a:wireshark:wireshark']
    
    # create ProductFullName
    products=[]
    for p in prod:
        products.append(['Wireshark',p])
        
    # import cvrf template
    try:
        mincvrf=etree.parse(static_root+'/templates/minimumCvrfTemplate.xml')
    except:
        try:
            mincvrf=etree.parse('minimumCvrfTemplate.xml')
        except:
            print("translateWiresharkHtmlToCvrf: cannot find minimumCvrfTemplate.xml")
            # throw exception
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
        cves=[]
        cv = tree.xpath('//a[contains(@href,"name=CVE-")]')
        for c in cv:
            cves.append(c.get('href').split('=')[1])
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
    
    outfile=fullname.replace(".html","-cvrf.xml")
    print("Saving Wireshark CVRF: "+outfile)
    mincvrf.write(outfile,pretty_print=True,xml_declaration=True, encoding='utf-8')

def importWiresharkHtml():
    exdb = db.ExistDB()  
    validateCollection(exdb,db_cvrf_wireshark_collection)
    validateMediaPath(wireshark_data_dir.replace('/',os.sep))
    flist=[]
    produrls = [
        "http://www.wireshark.org/security/",
        ]
    
    apslinks=[]
    for pu in produrls:
        content = urllib.urlopen(pu).read()
        doc = fromstring(content)
        doc.make_links_absolute("https://www.wireshark.org/security/")
        for a in doc.xpath('//a[contains(@href,"wnpa")]'):
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
            urllib.urlretrieve (u, wireshark_data_dir+uname)
            #f = open(uname,'w')
            #f.write(cvrfhtml)
            #f.close()
            try:
                #if int(uname[9:13])>2010:
                try:
                    translateWiresharkHtmlToCvrf(wireshark_data_dir+uname)
                    try:
                        cvrfname=uname.replace(".html","-cvrf.xml")
                        fo = open(wireshark_data_dir+cvrfname, 'rb')
                        if exdb.load(fo, db_cvrf_wireshark_collection+'/'+cvrfname, True):
                            flist.append(cvrfname+": data import successful")
                        else:
                            flist.append(cvrfname+": data import failed")
                        fo.close()
                    except:
                        flist.append(uname+": file read failed")
                except:
                    print("failed to translate: "+uname)
            except:
                pass
