import urllib2
import os


# global variables
rhsa2cve={}
rhsa2cpe={}
cve2rhsa={}
cve2cpe={}
cpe2rhsa={}
cpe2cve={}

rhsamapcpe_text=[]

def import_rhsamapcpe(fn=None):
    global rhsamapcpe_text
    try:
        rhsamapcpe_text = open(fn,'r').readlines()
    except:
        try:
            headers = { 'User-Agent' : 'Mozilla/5.0' }
            req = urllib2.Request("https://www.redhat.com/security/data/metrics/rhsamapcpe.txt", None, headers)
            rhsamapcpe_text = urllib2.urlopen(req).read().split('\n')
        except:
            print("import_rhsamapcpe: failed to import file")
    return rhsamapcpe_text

def reset_dicts():
	global rhsa2cve
	global rhsa2cpe
	global cve2rhsa
	global cve2cpe
	global cpe2rhsa
	global cpe2cve
	rhsa2cve={}
	rhsa2cpe={}
	cve2rhsa={}
	cve2cpe={}
	cpe2rhsa={}
	cpe2cve={}

def add2dict(d,n,v):
    try:
        if d[n]:
            d[n]=d[n] + v
        else:
            d[n]=v
    except:
        try:
            d[n]=v
        except:
            print("add2dict: failed twice on "+n+" | "+v)
    return

def load_dicts():
    global rhsamapcpe_text
    for line in rhsamapcpe_text:
        try:
            line=line.replace('\n','')
            this=line.split(' ')
            rhsa=this[0]
            cves=[i for i in this[1].split(',')]
            cpes=[i for i in this[2].split(',')]
            add2dict(rhsa2cve,rhsa,cves)
            add2dict(rhsa2cpe,rhsa,cpes)
            for c in cves:
                add2dict(cve2rhsa,c,[rhsa])
                add2dict(cve2cpe,c,cpes)
            for c in cpes:
                add2dict(cpe2rhsa,c,[rhsa])
                add2dict(cpe2cve,c,cves)
        except:
            print("parsing rhsamapcpe bombed on line: "+line)

def getCpeFromRhsa(rhsa):
    global rhsa2cpe
    try:
        return rhsa2cpe[rhsa]
    except:
        return ([])

def getCveFromRhsa(rhsa):
	global rhsa2cve
	try:
		return rhsa2cve[rhsa]
	except:
		return ([])

def getRhsaFromCve(cve):
	global cve2rhsa
	try:
		return cve2rhsa[cve]
	except:
		return ([])

def getCpeFromCve(cve):
	global cve2cpe
	try:
		return cve2cpe[cve]
	except:
		return ([])

def getRhsaFromCpe(cpe):
	global cpe2rhsa
	try:
		return cpe2rhsa[cpe]
	except:
		return ([])

def getCveFromCpe(cpe):
	global cpe2cve
	try:
		return cpe2cve[cpe]
	except:
		return ([])

# this will initialize on import
reset_dicts()
rhsamapcpe_text=import_rhsamapcpe()
load_dicts()
