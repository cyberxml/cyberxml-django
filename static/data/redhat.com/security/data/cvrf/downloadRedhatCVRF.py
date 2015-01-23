import urllib2
import urllib
import os.path
import os

# -----------------------------------------------------------------------------
# get list of cvrf urls
# -----------------------------------------------------------------------------
# need User-Agent or Red Hat blocks request
nurl="http://www.redhat.com/security/data/cvrf/index.txt"
headers = { 'User-Agent' : 'Mozilla/5.0' }
req = urllib2.Request(nurl, None, headers)
index = urllib2.urlopen(req).readlines()
urls = ['http://www.redhat.com/security/data/cvrf/'+i.replace('\n','') for i in index]

# -----------------------------------------------------------------------------
# download files if they don't exist
# TODO: check for revisions and download those as well (check hashes?)
# -----------------------------------------------------------------------------
for u in urls:
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
