from cvrf.libs import redhat
from cvrf.libs import microsoft
from cvrf.libs import oracle
from cvrf.libs import adobe
from cvrf.libs import cisco
from cvrf.libs import vmware
from cve.libs import nist

from lxml import etree

from django.conf import settings
from eulexistdb import db

from datetime import date
thisyear = date.today().year


media_root = settings.MEDIA_ROOT
disa_pki_flag = settings.USE_DISA_PKI
root_src_dir = '/tmp/iavms/'
iavm_cve_data_dir = media_root+'/data/disa.mil/iavm/cve/'
iavm_data_dir = media_root+'/data/disa.mil/iavm/'
db_iavm_cve_disa_collection = '/db/cyberxml/data/iavm/cve/disa.mil'
db_iavm_disa_collection = '/db/cyberxml/data/iavm/disa.mil'
iavm_to_cve_path = '/db/cyberxml/data/iavm/cve/disa.mil/u_iavm-to-cve.xml'
iavm_to_cpe_coll = '/db/cyberxml/apps/iavm/cve/disa.mil'
iavm_to_cpe_path = '/db/cyberxml/apps/iavm/cve/disa.mil/u_iavm-to-cpe.xml'

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

def get_qryDisaIavmCve(iavm):
    if disa_pki_flag:
        qry='''
            xquery version "3.0";
            declare namespace iavmNotice = "http://iavm.csd.disa.mil/schemas/IavmNoticeSchema/1.2";
            let $thisiavm := "'''+iavm+'''"
            let $thisdoc := concat('/db/cyberxml/data/iavm/disa.mil/',$thisiavm,'.xml')
            let $cves := doc($thisdoc)/iavmNotice:iavmNotice/iavmNotice:techOverview/iavmNotice:entry/iavmNotice:title/text()
            return $cves'''
    else:
        qry='''
            xquery version "3.0";
            let $thisiavm := "'''+iavm+'''"
            let $thisdoc := '/db/cyberxml/data/iavm/cve/disa.mil/u_iavm-to-cve.xml'
            for $cves in doc($thisdoc)//node()[S[@IAVM=$thisiavm]]/CVEs/CVENumber/text()
            return $cves'''
    return qry
            

def getCveFromIavm(iavm):
    try:
        qrystr=get_qryDisaIavmCve(iavm)
        a = connExistDB()
        cves =a.get_data(qrystr)
    except:
        cves=[]
    return(cves)

def getCpeFromIavm(iavm):
    cves=getCveFromIavm(iavm)
    cpes=[]
    for cve in cves:
        cpes=cpes+redhat.getCpeFromCve(cve)
        cpes=cpes+microsoft.getCpeFromCve(cve)
        cpes=cpes+oracle.getCpeFromCve(cve)
        cpes=cpes+adobe.getCpeFromCve(cve)
        cpes=cpes+vmware.getCpeFromCve(cve)
        cpes=cpes+cisco.getCpeFromCve(cve)
        cpes=cpes+nist.getCpeFromCve(cve)
    return(cpes)

def getCpeFromCve(cve):
    cpes=[]
    try:
        vendor_cpes=microsoft.getCpeFromCve(cve)
        if len(vendor_cpes)>0:
            cpes=cpes+[["microsoft.com",vendor_cpes]]
    except:
        pass
    try:
        vendor_cpes=oracle.getCpeFromCve(cve)
        if len(vendor_cpes)>0:
            cpes=cpes+[["oracle.com",vendor_cpes]]
    except:
        pass
    try:
        vendor_cpes=redhat.getCpeFromCve(cve)
        if len(vendor_cpes)>0:
            cpes=cpes+[["redhat.com",vendor_cpes]]
    except:
        pass
    try:
        vendor_cpes=adobe.getCpeFromCve(cve)
        if len(vendor_cpes)>0:
            cpes=cpes+[["adobe.com",vendor_cpes]]
    except:
        pass
    try:
        vendor_cpes=vmware.getCpeFromCve(cve)
        if len(vendor_cpes)>0:
            cpes=cpes+[["vmware.com",vendor_cpes]]
    except:
        pass
    try:
        vendor_cpes=cisco.getCpeFromCve(cve)
        if len(vendor_cpes)>0:
            cpes=cpes+[["cisco.com",vendor_cpes]]
    except:
        pass
    try:
        vendor_cpes=nist.getCpeFromCve(cve)
        if len(vendor_cpes)>0:
            cpes=cpes+[["nist.gov",vendor_cpes]]
    except:
        pass
    return(cpes)

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

# first pass on this is to vet cpe against IAVM title
# this is targeted at the granular VMware IAVM written against bulk VMSA
def filter_iavm_title(cpe, title):
    if "ESXi 3.0.3" in title and not ":esxi:3.0.3" in cpe:
        return False
    if "ESXi 3.5" in title and not ":esxi:3.5" in cpe:
        return False
    if "ESXi 4.0" in title and not ":esxi:4.0" in cpe:
        return False
    if "ESXi 4.1" in title and not ":esxi:4.1" in cpe:
        return False
    if "ESXi 5.0" in title and not ":esxi:5.0" in cpe:
        return False
    if "ESXi 5.1" in title and not ":esxi:5.1" in cpe:
        return False
    if "ESXi 5.5" in title and not ":esxi:5.5" in cpe:
        return False
    if "Horizon View" in title and not "cpe:/a:vmware:horizon_view" in cpe:
        return False
    if "vCenter Converter Standalone 5.0" in title and not "cpe:/a:vmware:vcenter_converter_standalone:5.0" in cpe:
        return False
    if "vCenter Converter Standalone 5.1" in title and not "cpe:/a:vmware:vcenter_converter_standalone:5.1" in cpe:
        return False
    if "vCenter Converter Standalone 5.5" in title and not "cpe:/a:vmware:vcenter_converter_standalone:5.5" in cpe:
        return False
    if "vCenter Operation" in title and not "cpe:/a:vmware:vcenter_operations_manager" in cpe:
        return False
    if "vCenter Orchestrator" in title and not "cpe:/a:vmware:vcenter_orchestrator" in cpe:
        return False        
    if "vCenter Server Appliance 5.0" in title and not "cpe:/a:vmware:vcenter_server_appliance:5.0" in cpe:
        return False
    if "vCenter Server Appliance 5.1" in title and not "cpe:/a:vmware:vcenter_server_appliance:5.1" in cpe:
        return False
    if "vCenter Server Appliance 5.5" in title and not "cpe:/a:vmware:vcenter_server_appliance:5.0" in cpe:
        return False
    if "vCenter Server 5.0" in title and not "cpe:/a:vmware:vcenter_server:5.0" in cpe:
        return False
    if "vCenter Server 5.1" in title and not "cpe:/a:vmware:vcenter_server:5.1" in cpe:
        return False
    if "vCenter Server 5.5" in title and not "cpe:/a:vmware:vcenter_server:5.5" in cpe:
        return False
    if "VMware Fusion" in title and not "cpe:/a:vmware:fusion" in cpe:
        return False
    if "VMware Player" in title and not "cpe:/a:vmware:player" in cpe:
        return False
    if "VMware Workstation" in title and not "cpe:/a:vmware:workstation" in cpe:
        return False
    if "vSphere Client" in title and not "cpe:/a:vmware:vsphere_client" in cpe:
        return False
    if "Update Manager" in title and not "cpe:/a:vmware:update_manager:" in cpe:
        return False
    if "Solaris" in title and not "cpe:/o:oracle:solaris" in cpe:
        return False
    if "Oracle" in title and "Sun" in title not "cpe:/o:oracle:solaris" in cpe:
        return False
    if "Oracle" in title and "Java" in title and not ("cpe:/o:oracle:jre" in cpe or "cpe:/o:oracle:jdk" in cpe):
        return False
    if "Oracle" in title and "Database" in title and not "cpe:/a:oracle:database" in cpe:
        return False
    if "Oracle" in title and "Fusion" in title and not "cpe:/a:oracle:fusion_middleware" in cpe:
        return False
    if "Oracle" in title and "Enterprise Manager" in title and not "cpe:/a:oracle:enterprise_manager" in cpe:
        return False
    if "Oracle" in title and "E-Business" in title and not "cpe:/a:oracle:e-business_suite" in cpe:
        return False
    if "Apple" in title and not ("cpe:/a:apple" in cpe or "cpe:/o:apple" in cpe):
        return False
	# misplaced NIST OS CPEs from OVAL logic
    if "McAfee" in title and not ":mcafee:" in cpe:
        return False
    if "Blue Coat" in title and not ":blue_coat:" in cpe:
        return False
    if "IBM" in title and not ":ibm:" in cpe:
        return False
    if "HP" in title and not ":hp" in cpe:
        return False
    if "Chrome" in title and "cpe:/o:" in cpe:
        return False
    return True


def filter_iavm_references(vendor, references):
    # vendor is a string
    # references is an etree element
    # not sure how best to combine nist with vendor
    if vendor == 'nist.gov': return True
    
    refs = references.findall('./Reference')
    for ref in refs:
        try:
            if 'microsoft.com' in ref.get('URL') and vendor == 'microsoft.com': return True
            if 'redhat.com' in ref.get('URL') and vendor == 'redhat.com': return True
            if 'adobe.com' in ref.get('URL') and vendor == 'adobe.com': return True
            # note that Red Hat redistributes Adobe Flash
            if 'adobe.com' in ref.get('URL') and vendor == 'redhat.com': return True
            if 'vmware.com' in ref.get('URL') and vendor == 'vmware.com': return True
            if 'asterisk.org' in ref.get('URL') and vendor == 'asterisk.org': return True
            if 'hp.com' in ref.get('URL') and vendor == 'hp.com': return True
            if 'symantec.com' in ref.get('URL') and vendor == 'symantec.com': return True
            if 'mcafee.com' in ref.get('URL') and vendor == 'mcafee.com': return True
            if 'apple.com' in ref.get('URL') and vendor == 'apple.com': return True
            if 'siemens.com' in ref.get('URL') and vendor == 'siemens.com': return True
            if 'juniper.net' in ref.get('URL') and vendor == 'juniper.net': return True
            if 'oracle.com' in ref.get('URL') and vendor == 'oracle.com': return True
            if 'google.com' in ref.get('URL') and vendor == 'google.com': return True
        except:
            pass
        
        # still here?
        try:
            if 'Microsoft' in ref.get('RefName') and vendor == 'microsoft.com': return True
            if 'Red Hat' in ref.get('RefName') and vendor == 'redhat.com': return True
            if 'Adobe' in ref.get('RefName') and vendor == 'adobe.com': return True
            # note that Red Hat redistributes Adobe Flash
            if 'Adobe Flash' in ref.get('RefName') and vendor == 'redhat.com': return True
            if 'VMware' in ref.get('RefName') and vendor == 'vmware.com': return True
            if 'Asterisk' in ref.get('RefName') and vendor == 'asterisk.org': return True
            if 'HP' in ref.get('RefName') and vendor == 'hp.com': return True
            if 'Symantec' in ref.get('RefName') and vendor == 'symantec.com': return True
            if 'McAfee' in ref.get('RefName') and vendor == 'mcafee.com': return True
            if 'Apple' in ref.get('RefName') and vendor == 'apple.com': return True
            if 'Siemens' in ref.get('RefName') and vendor == 'siemens.com': return True
            if 'Juniper' in ref.get('RefName') and vendor == 'juniper.net': return True
            if 'Oracle' in ref.get('RefName') and vendor == 'oracle.com': return True
            if 'Google' in ref.get('RefName') and vendor == 'google.com': return True
        except:
            pass
        
        
    return False

def iavm_to_cpe_doc():
    exdb = db.ExistDB()
    validateCollection(exdb, iavm_to_cpe_coll)
    
    thisdoc=exdb.getDocument(iavm_to_cve_path)
    
    root = etree.fromstring(thisdoc)
    
    # get all IAVMs
    find = etree.XPath('//IAVM')
    iavms = find(root)
    
    for i in range(len(iavms)):
        print(iavms[i].find('./S').get('IAVM'))
        iav_title = iavms[i].find('./S').get('Title')
        cves = iavms[i].findall('./CVEs/CVENumber')
        for j in range(len(cves)):
            cpes = getCpeFromCve(cves[j].text)
            if len(cpes) > 0:
                cves[j].append(etree.Element('CPEs'))
                cpes_elem=cves[j].find('./CPEs')
                for v in cpes:
                    # apply vendor/reference filter
                    if filter_iavm_references(v[0],iavms[i].find("./References")):
                        cpes_elem.append(etree.Element('Vendor',id=v[0]))
                        v_elem=cpes_elem.findall('./Vendor')[-1]
                        for cpe in v[1]:
                            # apply cpe/title filter
                            if filter_iavm_title(cpe,iav_title):
                                v_elem.append(etree.Element('CPE'))
                                this = v_elem.findall('./CPE')[-1]
                                this.text = cpe
    

    # rewrite the above loop to just query once for each cve in the IAVMs
    # create a dict for each cve with cpe values
    # get all IAVMs
    # this is 1800 CVEs at roughly 1.5 seconds = 45 minutes.
    '''
    find = etree.XPath('//CVENumber')
    cvenodes = find(root)
    cves=[]
    for j in range(len(cvenodes)):
        cves.append(cvenodes[j].text)
    
    cves = list(set(cves)) # create unique list
    cves.sort()
    cve2cpe = {} # dictionary
    for cve in cves:
        print cve
        cve2cpe[cve]=getCpeFromCve(cve)
    '''
    
    # print(etree.tostring(iavms[0],pretty_print=True))
    
    # write xml doc to database
    exdb.load(etree.tostring(root,pretty_print=True),iavm_to_cpe_path,True)

# fn is file handle
def export_iavm_to_cpe_doc(fn):
    exdb = db.ExistDB()
    thisdoc=exdb.getDocument(iavm_to_cpe_path)
    #f=open(fn,'w')
    fn.write(thisdoc)
    fn.close()

    
