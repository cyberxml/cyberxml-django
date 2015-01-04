import glob
from lxml import etree

# get product id / product name map from cvrf
datdir="/projects/rhinohide.org/cybersec/draft/data/MSRC-CVRF/"
xmldir=datdir+"*xml"
fxml=glob.glob(xmldir)
fxml.sort()

for fn in fxml:
	f=open(fn)
	xml=f.readlines()
	f.close()
	
	# fixed on 20141230
	#if xml[0].find('cvrf:cvrfdoc') == -1 and xml[1].find('cvrf:cvrfdoc') == -1 :
	#	xml[0]=cvrfhead+xml[0]
	
	#if xml[-1].find('cvrf:cvrfdoc') == -1 and xml[-2].find('cvrf:cvrfdoc') == -1 :
	#	xml[-1]=xml[-1]+cvrftail
	
	try:
		strxml=' '.join(xml)
		root=etree.fromstring(strxml)
	except:
		print ('xml parsing failed on file: '+fn+'\n')
