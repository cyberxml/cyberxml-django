from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from . import cvrf
from cStringIO import StringIO
import re

#remsnum = re.compile("^[mM][sS]\d{2}-\d{3}$")

# Create your views here.
def rawxml(request,vendor,cvrfnum):
	cvrfnum = cvrfnum.lower()
	vendor = vendor.lower()
	if vendor == "ms":
		vdir = "microsoft.com/MSRC-CVRF/"
	elif vendor == "redhat":
		vdir = "redhat.com/security/data/cvrf/"
	elif vendor == "cisco":
		vdir = "cisco.com/security/center/cvrfListing.x/"
	elif vendor == "oracle":
		vdir = "oracle.com/documents/webcontent/cvrf/"
	else:
		raise Http404
	try:
		rootObj = cvrf.parse("static/data/"+vdir+cvrfnum+".xml",0)
		xmlstr=StringIO()
		rootObj.export(xmlstr, 0)
		return HttpResponse(xmlstr.getvalue(), content_type="application/xml")
	except:
		raise Http404

# Create your views here.
def prettyxml(request,vendor,cvrfnum):
	cvrfnum = cvrfnum.lower()
	vendor = vendor.lower()
	if vendor == "ms":
		vdir = "microsoft.com/MSRC-CVRF/"
	elif vendor == "redhat":
		vdir = "redhat.com/security/data/cvrf/"
	elif vendor == "cisco":
		vdir = "cisco.com/security/center/cvrfListing.x/"
	elif vendor == "oracle":
		vdir = "oracle.com/documents/webcontent/cvrf/"
	else:
		raise Http404
	try:
		rootObj = cvrf.parse("static/data/"+vdir+cvrfnum+".xml",0)
		xmlstr=StringIO()
		rootObj.export(xmlstr, 0)
		#return render(request, 'cvrf_pretty.html', {'test':msnum})
		return render(request, 'cvrf_test.html', {'test':rootObj})
	except:
		raise Http404

'''
#from django.views.generic import View
from . import models
def prettyxmltest(request,vendor,cvrfnum):
	cvrfnum = cvrfnum.lower()
	if vendor == "ms":
		vdir = "microsoft.com/MSRC-CVRF/"
	elif vendor == "redhat":
		vdir = "redhat.com/security/data/cvrf/"
	else:
		raise Http404
	rootObj = cvrf.parse("static/data/"+vdir+cvrfnum+".xml",0)
	cd = models.cvrfdoc_model()
	
	# ---------------------------------------------------------------------	
	cd.DocumentTitle = models.DocumentTitleType_model(rootObj.DocumentTitle.get_valueOf_())
	# ---------------------------------------------------------------------	
	
	# ---------------------------------------------------------------------	
	cd.DocumentType = models.DocumentTypeType_model(rootObj.DocumentType.get_valueOf_())
	# ---------------------------------------------------------------------	
	
	# ---------------------------------------------------------------------	
	cd.DocumentPublisher = models.DocumentPublisherType_model()
	# ---------------------------------------------------------------------	
	cd.DocumentPublisher.VendorID = rootObj.DocumentPublisher.VendorID
	cd.DocumentPublisher.Type = rootObj.DocumentPublisher.Type
	cd.DocumentPublisher.ContactDetails = models.ContactDetailsType_model(rootObj.DocumentPublisher.ContactDetails.get_valueOf_())
	cd.DocumentPublisher.IssuingAuthority = models.IssuingAuthorityType_model(rootObj.DocumentPublisher.IssuingAuthority.get_valueOf_())
	
	# ---------------------------------------------------------------------	
	cd.DocumentTracking = models.DocumentTrackingType_model()
	# ---------------------------------------------------------------------	
	cd.DocumentTracking.Identification = models.IdentificationType_model()
	cd.DocumentTracking.Identification.ID = models.IDType_model(rootObj.DocumentTracking.Identification.get_ID().get_valueOf_()) 
	# there is a list of Aliasess for Identification
	cd.DocumentTracking.Identification.Alias = models.AliasType_model(rootObj.DocumentTracking.Identification.get_Alias()[0].get_valueOf_())
	
	cd.DocumentTracking.Status = rootObj.DocumentTracking.Status
	cd.DocumentTracking.Version = rootObj.DocumentTracking.Version
	
	cd.DocumentTracking.RevisionHistory = models.RevisionHistoryType_model()
	cd.DocumentTracking.RevisionHistory.Revision = models.RevisionType_model()
	# there is a list of Revisions for RevisionHistory
	cd.DocumentTracking.RevisionHistory.Revision.Number = rootObj.DocumentTracking.RevisionHistory.get_Revision()[0].get_Number()
	cd.DocumentTracking.RevisionHistory.Revision.Date = rootObj.DocumentTracking.RevisionHistory.get_Revision()[0].get_Date()
	cd.DocumentTracking.RevisionHistory.Revision.Description = models.DescriptionType_model(rootObj.DocumentTracking.RevisionHistory.get_Revision()[0].get_Description().get_valueOf_())
	
	cd.DocumentTracking.InitialReleaseDate = rootObj.DocumentTracking.InitialReleaseDate
	cd.DocumentTracking.CurrentReleaseDate = rootObj.DocumentTracking.CurrentReleaseDate
	
	#cd.DocumentTracking.Generator = models.GeneratorType_model(rootObj.DocumentTracking.Generator)
	# Engine
	# Date
	
	# ---------------------------------------------------------------------	
	cd.DocumentNotes = models.DocumentNotesType_model()
	# ---------------------------------------------------------------------	
	# there is a list of Notes for DocumentNotes
        cd.DocumentNotes.Note = models.NoteType_model(rootObj.DocumentNotes.get_Note()[0].get_valueOf_()) 
	cd.DocumentNotes.Note.Ordinal = rootObj.DocumentNotes.get_Note()[0].get_Ordinal() 
	cd.DocumentNotes.Note.Audience = rootObj.DocumentNotes.get_Note()[0].get_Audience() 
	cd.DocumentNotes.Note.Type = rootObj.DocumentNotes.get_Note()[0].get_Type() 
	cd.DocumentNotes.Note.Title = rootObj.DocumentNotes.get_Note()[0].get_Title() 
	
	# ---------------------------------------------------------------------	
	cd.AggregateSeverity = models.AggregateSeverityType_model(rootObj.AggregateSeverity.get_valueOf_())
	# ---------------------------------------------------------------------	
	
	# ---------------------------------------------------------------------	
	cd.DocumentReferences = models.DocumentReferencesType_model()
	# ---------------------------------------------------------------------	
	# there is a list of References for DocumentReferences
	cd.DocumentReferences.Reference = models.ReferenceType_model()
        cd.DocumentReferences.Reference.URL = rootObj.DocumentReferences.get_Reference()[0].get_URL() 
        cd.DocumentReferences.Reference.Type = rootObj.DocumentReferences.get_Reference()[0].get_Type() 
	cd.DocumentReferences.Reference.Description  = models.DescriptionType1_model(rootObj.DocumentReferences.get_Reference()[0].get_Description().get_valueOf_())
	
	# ---------------------------------------------------------------------	
	#cd.Acknowledgments = models.AcknowledgmentsType_model()
	# ---------------------------------------------------------------------	
	# there is a list of Acknowledgements  for Acknowledgements
	#cd.Acknowledgments.Acknowledgement = models.AcknowledgmentType_model()
	#cd.Acknowledgments.Acknowledgement.URL = rootObj.Acknowledgements.get_Acknowledgement()[0].get_URL() 
	#cd.Acknowledgments.Acknowledgement = models.AcknowledgmentType_model()
	
	# ---------------------------------------------------------------------	
	cd.ProductTree = models.ProductTree_model()
	# ---------------------------------------------------------------------	
	# If tree is flat, # branches = 0
	# Branches can be nested to a depth of ?
	#cd.ProductTree.Branch = models.BranchType_model()
	#cd.ProductTree.Branch.Type = rootObj.ProductTree.get_Branch()[0].get_Type() 
	#cd.ProductTree.Branch.Name = rootObj.ProductTree.get_Branch()[0].get_Name() 
	# there is a list of FullProductNames  for ProductTree
	pt = rootObj.ProductTree.get_FullProductName()
	fpn=[]
	for i in range(len(pt)):
		this = models.FullProductName_model(rootObj.ProductTree.get_FullProductName()[i].get_valueOf_())
		this.CPE = rootObj.ProductTree.get_FullProductName()[i].get_CPE()
		this.ProductID = rootObj.ProductTree.get_FullProductName()[i].get_ProductID()
		fpn.append(this)
	cd.ProductTree = models.ProductTree_model(fpn)
	cd.ProductTree.Relationship = models.RelationshipType_model()
	# more
	cd.ProductTree.ProductGroups = models.ProductGroupsType_model()
	# more
	
	return render(request, 'cvrf_table.html', {'cvrfdoc':cd})
'''	
