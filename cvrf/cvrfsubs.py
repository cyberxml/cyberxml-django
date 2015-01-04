#!/usr/bin/env python

#
# Generated Wed Dec 31 18:45:04 2014 by generateDS.py version 2.14a.
#
# Command line options:
#   ('-o', 'cvrf.py')
#   ('-s', 'cvrfsubs.py')
#
# Command line arguments:
#   ./schemata/cvrf/1.1/cvrf.xsd
#
# Command line:
#   /home/action/.parts/packages/python2/2.7.6/bin/generateDS.py -o "cvrf.py" -s "cvrfsubs.py" ./schemata/cvrf/1.1/cvrf.xsd
#
# Current working directory (os.getcwd()):
#   tmp
#

import sys

import ??? as supermod

etree_ = None
Verbose_import_ = False
(
    XMLParser_import_none, XMLParser_import_lxml,
    XMLParser_import_elementtree
) = range(3)
XMLParser_import_library = None
try:
    # lxml
    from lxml import etree as etree_
    XMLParser_import_library = XMLParser_import_lxml
    if Verbose_import_:
        print("running with lxml.etree")
except ImportError:
    try:
        # cElementTree from Python 2.5+
        import xml.etree.cElementTree as etree_
        XMLParser_import_library = XMLParser_import_elementtree
        if Verbose_import_:
            print("running with cElementTree on Python 2.5+")
    except ImportError:
        try:
            # ElementTree from Python 2.5+
            import xml.etree.ElementTree as etree_
            XMLParser_import_library = XMLParser_import_elementtree
            if Verbose_import_:
                print("running with ElementTree on Python 2.5+")
        except ImportError:
            try:
                # normal cElementTree install
                import cElementTree as etree_
                XMLParser_import_library = XMLParser_import_elementtree
                if Verbose_import_:
                    print("running with cElementTree")
            except ImportError:
                try:
                    # normal ElementTree install
                    import elementtree.ElementTree as etree_
                    XMLParser_import_library = XMLParser_import_elementtree
                    if Verbose_import_:
                        print("running with ElementTree")
                except ImportError:
                    raise ImportError(
                        "Failed to import ElementTree from any known place")


def parsexml_(*args, **kwargs):
    if (XMLParser_import_library == XMLParser_import_lxml and
            'parser' not in kwargs):
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        kwargs['parser'] = etree_.ETCompatXMLParser()
    doc = etree_.parse(*args, **kwargs)
    return doc

#
# Globals
#

ExternalEncoding = 'utf-8'

#
# Data representation classes
#


class cvrfdocSub(supermod.cvrfdoc):
    def __init__(self, DocumentTitle=None, DocumentType=None, DocumentPublisher=None, DocumentTracking=None, DocumentNotes=None, DocumentDistribution=None, AggregateSeverity=None, DocumentReferences=None, Acknowledgments=None, ProductTree=None, Vulnerability=None):
        super(cvrfdocSub, self).__init__(DocumentTitle, DocumentType, DocumentPublisher, DocumentTracking, DocumentNotes, DocumentDistribution, AggregateSeverity, DocumentReferences, Acknowledgments, ProductTree, Vulnerability, )
supermod.cvrfdoc.subclass = cvrfdocSub
# end class cvrfdocSub


class SimpleLiteralSub(supermod.SimpleLiteral):
    def __init__(self, lang=None, anytypeobjs_=None):
        super(SimpleLiteralSub, self).__init__(lang, anytypeobjs_, )
supermod.SimpleLiteral.subclass = SimpleLiteralSub
# end class SimpleLiteralSub


class titleSub(supermod.title):
    def __init__(self):
        super(titleSub, self).__init__()
supermod.title.subclass = titleSub
# end class titleSub


class creatorSub(supermod.creator):
    def __init__(self):
        super(creatorSub, self).__init__()
supermod.creator.subclass = creatorSub
# end class creatorSub


class subjectSub(supermod.subject):
    def __init__(self):
        super(subjectSub, self).__init__()
supermod.subject.subclass = subjectSub
# end class subjectSub


class descriptionSub(supermod.description):
    def __init__(self):
        super(descriptionSub, self).__init__()
supermod.description.subclass = descriptionSub
# end class descriptionSub


class publisherSub(supermod.publisher):
    def __init__(self):
        super(publisherSub, self).__init__()
supermod.publisher.subclass = publisherSub
# end class publisherSub


class contributorSub(supermod.contributor):
    def __init__(self):
        super(contributorSub, self).__init__()
supermod.contributor.subclass = contributorSub
# end class contributorSub


class dateSub(supermod.date):
    def __init__(self, valueOf_=None):
        super(dateSub, self).__init__()
supermod.date.subclass = dateSub
# end class dateSub


class type_Sub(supermod.type_):
    def __init__(self):
        super(type_Sub, self).__init__()
supermod.type_.subclass = type_Sub
# end class type_Sub


class formatSub(supermod.format):
    def __init__(self):
        super(formatSub, self).__init__()
supermod.format.subclass = formatSub
# end class formatSub


class identifierSub(supermod.identifier):
    def __init__(self):
        super(identifierSub, self).__init__()
supermod.identifier.subclass = identifierSub
# end class identifierSub


class sourceSub(supermod.source):
    def __init__(self):
        super(sourceSub, self).__init__()
supermod.source.subclass = sourceSub
# end class sourceSub


class languageSub(supermod.language):
    def __init__(self, valueOf_=None):
        super(languageSub, self).__init__()
supermod.language.subclass = languageSub
# end class languageSub


class relationSub(supermod.relation):
    def __init__(self):
        super(relationSub, self).__init__()
supermod.relation.subclass = relationSub
# end class relationSub


class coverageSub(supermod.coverage):
    def __init__(self):
        super(coverageSub, self).__init__()
supermod.coverage.subclass = coverageSub
# end class coverageSub


class rightsSub(supermod.rights):
    def __init__(self):
        super(rightsSub, self).__init__()
supermod.rights.subclass = rightsSub
# end class rightsSub


class elementContainerSub(supermod.elementContainer):
    def __init__(self, any=None):
        super(elementContainerSub, self).__init__(any, )
supermod.elementContainer.subclass = elementContainerSub
# end class elementContainerSub


class VulnerabilitySub(supermod.Vulnerability):
    def __init__(self, Ordinal=None, Title=None, ID=None, Notes=None, DiscoveryDate=None, ReleaseDate=None, Involvements=None, CVE=None, CWE=None, ProductStatuses=None, Threats=None, CVSSScoreSets=None, Remediations=None, References=None, Acknowledgments=None):
        super(VulnerabilitySub, self).__init__(Ordinal, Title, ID, Notes, DiscoveryDate, ReleaseDate, Involvements, CVE, CWE, ProductStatuses, Threats, CVSSScoreSets, Remediations, References, Acknowledgments, )
supermod.Vulnerability.subclass = VulnerabilitySub
# end class VulnerabilitySub


class platformSpecificationTypeSub(supermod.platformSpecificationType):
    def __init__(self, platform=None):
        super(platformSpecificationTypeSub, self).__init__(platform, )
supermod.platformSpecificationType.subclass = platformSpecificationTypeSub
# end class platformSpecificationTypeSub


class PlatformBaseTypeSub(supermod.PlatformBaseType):
    def __init__(self, title=None, remark=None, logical_test=None, extensiontype_=None):
        super(PlatformBaseTypeSub, self).__init__(title, remark, logical_test, extensiontype_, )
supermod.PlatformBaseType.subclass = PlatformBaseTypeSub
# end class PlatformBaseTypeSub


class PlatformTypeSub(supermod.PlatformType):
    def __init__(self, title=None, remark=None, logical_test=None, id=None):
        super(PlatformTypeSub, self).__init__(title, remark, logical_test, id, )
supermod.PlatformType.subclass = PlatformTypeSub
# end class PlatformTypeSub


class LogicalTestTypeSub(supermod.LogicalTestType):
    def __init__(self, operator=None, negate=None, logical_test=None, fact_ref=None):
        super(LogicalTestTypeSub, self).__init__(operator, negate, logical_test, fact_ref, )
supermod.LogicalTestType.subclass = LogicalTestTypeSub
# end class LogicalTestTypeSub


class FactRefTypeSub(supermod.FactRefType):
    def __init__(self, name=None):
        super(FactRefTypeSub, self).__init__(name, )
supermod.FactRefType.subclass = FactRefTypeSub
# end class FactRefTypeSub


class TextTypeSub(supermod.TextType):
    def __init__(self, lang=None, valueOf_=None):
        super(TextTypeSub, self).__init__(lang, valueOf_, )
supermod.TextType.subclass = TextTypeSub
# end class TextTypeSub


class checkSearchTypeSub(supermod.checkSearchType):
    def __init__(self, system=None, name=None, extensiontype_=None):
        super(checkSearchTypeSub, self).__init__(system, name, extensiontype_, )
supermod.checkSearchType.subclass = checkSearchTypeSub
# end class checkSearchTypeSub


class searchableCpeReferencesTypeSub(supermod.searchableCpeReferencesType):
    def __init__(self, cpe_name=None, cpe_searchable_name=None):
        super(searchableCpeReferencesTypeSub, self).__init__(cpe_name, cpe_searchable_name, )
supermod.searchableCpeReferencesType.subclass = searchableCpeReferencesTypeSub
# end class searchableCpeReferencesTypeSub


class controlMappingsTypeSub(supermod.controlMappingsType):
    def __init__(self, control_mapping=None):
        super(controlMappingsTypeSub, self).__init__(control_mapping, )
supermod.controlMappingsType.subclass = controlMappingsTypeSub
# end class controlMappingsTypeSub


class controlMappingTypeSub(supermod.controlMappingType):
    def __init__(self, source=None, system_id=None, last_modified=None, mapping=None):
        super(controlMappingTypeSub, self).__init__(source, system_id, last_modified, mapping, )
supermod.controlMappingType.subclass = controlMappingTypeSub
# end class controlMappingTypeSub


class mappingInstanceTypeSub(supermod.mappingInstanceType):
    def __init__(self, published=None, valueOf_=None):
        super(mappingInstanceTypeSub, self).__init__(published, valueOf_, )
supermod.mappingInstanceType.subclass = mappingInstanceTypeSub
# end class mappingInstanceTypeSub


class assessmentMethodTypeSub(supermod.assessmentMethodType):
    def __init__(self, assessment_check=None, assessment_engine=None, extensiontype_=None):
        super(assessmentMethodTypeSub, self).__init__(assessment_check, assessment_engine, extensiontype_, )
supermod.assessmentMethodType.subclass = assessmentMethodTypeSub
# end class assessmentMethodTypeSub


class identifyableAssessmentMethodTypeSub(supermod.identifyableAssessmentMethodType):
    def __init__(self, assessment_check=None, assessment_engine=None, id=None):
        super(identifyableAssessmentMethodTypeSub, self).__init__(assessment_check, assessment_engine, id, )
supermod.identifyableAssessmentMethodType.subclass = identifyableAssessmentMethodTypeSub
# end class identifyableAssessmentMethodTypeSub


class accessComplexityTypeSub(supermod.accessComplexityType):
    def __init__(self, approximated='false', valueOf_=None):
        super(accessComplexityTypeSub, self).__init__(approximated, valueOf_, )
supermod.accessComplexityType.subclass = accessComplexityTypeSub
# end class accessComplexityTypeSub


class accessVectorTypeSub(supermod.accessVectorType):
    def __init__(self, approximated='false', valueOf_=None):
        super(accessVectorTypeSub, self).__init__(approximated, valueOf_, )
supermod.accessVectorType.subclass = accessVectorTypeSub
# end class accessVectorTypeSub


class ciaRequirementTypeSub(supermod.ciaRequirementType):
    def __init__(self, approximated='false', valueOf_=None):
        super(ciaRequirementTypeSub, self).__init__(approximated, valueOf_, )
supermod.ciaRequirementType.subclass = ciaRequirementTypeSub
# end class ciaRequirementTypeSub


class collateralDamagePotentialTypeSub(supermod.collateralDamagePotentialType):
    def __init__(self, approximated='false', valueOf_=None):
        super(collateralDamagePotentialTypeSub, self).__init__(approximated, valueOf_, )
supermod.collateralDamagePotentialType.subclass = collateralDamagePotentialTypeSub
# end class collateralDamagePotentialTypeSub


class targetDistributionTypeSub(supermod.targetDistributionType):
    def __init__(self, approximated='false', valueOf_=None):
        super(targetDistributionTypeSub, self).__init__(approximated, valueOf_, )
supermod.targetDistributionType.subclass = targetDistributionTypeSub
# end class targetDistributionTypeSub


class ciaTypeSub(supermod.ciaType):
    def __init__(self, approximated='false', valueOf_=None):
        super(ciaTypeSub, self).__init__(approximated, valueOf_, )
supermod.ciaType.subclass = ciaTypeSub
# end class ciaTypeSub


class authenticationTypeSub(supermod.authenticationType):
    def __init__(self, approximated='false', valueOf_=None):
        super(authenticationTypeSub, self).__init__(approximated, valueOf_, )
supermod.authenticationType.subclass = authenticationTypeSub
# end class authenticationTypeSub


class remediationLevelTypeSub(supermod.remediationLevelType):
    def __init__(self, approximated='false', valueOf_=None):
        super(remediationLevelTypeSub, self).__init__(approximated, valueOf_, )
supermod.remediationLevelType.subclass = remediationLevelTypeSub
# end class remediationLevelTypeSub


class confidenceTypeSub(supermod.confidenceType):
    def __init__(self, approximated='false', valueOf_=None):
        super(confidenceTypeSub, self).__init__(approximated, valueOf_, )
supermod.confidenceType.subclass = confidenceTypeSub
# end class confidenceTypeSub


class exploitabilityTypeSub(supermod.exploitabilityType):
    def __init__(self, approximated='false', valueOf_=None):
        super(exploitabilityTypeSub, self).__init__(approximated, valueOf_, )
supermod.exploitabilityType.subclass = exploitabilityTypeSub
# end class exploitabilityTypeSub


class cvssTypeSub(supermod.cvssType):
    def __init__(self, base_metrics=None, environmental_metrics=None, temporal_metrics=None):
        super(cvssTypeSub, self).__init__(base_metrics, environmental_metrics, temporal_metrics, )
supermod.cvssType.subclass = cvssTypeSub
# end class cvssTypeSub


class cvssImpactTypeSub(supermod.cvssImpactType):
    def __init__(self, base_metrics=None, environmental_metrics=None, temporal_metrics=None):
        super(cvssImpactTypeSub, self).__init__(base_metrics, environmental_metrics, temporal_metrics, )
supermod.cvssImpactType.subclass = cvssImpactTypeSub
# end class cvssImpactTypeSub


class cvssImpactBaseTypeSub(supermod.cvssImpactBaseType):
    def __init__(self, base_metrics=None, extensiontype_=None):
        super(cvssImpactBaseTypeSub, self).__init__(base_metrics, extensiontype_, )
supermod.cvssImpactBaseType.subclass = cvssImpactBaseTypeSub
# end class cvssImpactBaseTypeSub


class cvssImpactTemporalTypeSub(supermod.cvssImpactTemporalType):
    def __init__(self, base_metrics=None, temporal_metrics=None, extensiontype_=None):
        super(cvssImpactTemporalTypeSub, self).__init__(base_metrics, temporal_metrics, extensiontype_, )
supermod.cvssImpactTemporalType.subclass = cvssImpactTemporalTypeSub
# end class cvssImpactTemporalTypeSub


class cvssImpactEnvironmentalTypeSub(supermod.cvssImpactEnvironmentalType):
    def __init__(self, base_metrics=None, temporal_metrics=None, environmental_metrics=None):
        super(cvssImpactEnvironmentalTypeSub, self).__init__(base_metrics, temporal_metrics, environmental_metrics, )
supermod.cvssImpactEnvironmentalType.subclass = cvssImpactEnvironmentalTypeSub
# end class cvssImpactEnvironmentalTypeSub


class metricsTypeSub(supermod.metricsType):
    def __init__(self, upgraded_from_version=None, extensiontype_=None):
        super(metricsTypeSub, self).__init__(upgraded_from_version, extensiontype_, )
supermod.metricsType.subclass = metricsTypeSub
# end class metricsTypeSub


class baseMetricsTypeSub(supermod.baseMetricsType):
    def __init__(self, upgraded_from_version=None, score=None, exploit_subscore=None, impact_subscore=None, access_vector=None, access_complexity=None, authentication=None, confidentiality_impact=None, integrity_impact=None, availability_impact=None, source=None, generated_on_datetime=None):
        super(baseMetricsTypeSub, self).__init__(upgraded_from_version, score, exploit_subscore, impact_subscore, access_vector, access_complexity, authentication, confidentiality_impact, integrity_impact, availability_impact, source, generated_on_datetime, )
supermod.baseMetricsType.subclass = baseMetricsTypeSub
# end class baseMetricsTypeSub


class environmentalMetricsTypeSub(supermod.environmentalMetricsType):
    def __init__(self, upgraded_from_version=None, score=None, collateral_damage_potential=None, target_distribution=None, confidentiality_requirement=None, integrity_requirement=None, availability_requirement=None, source=None, generated_on_datetime=None):
        super(environmentalMetricsTypeSub, self).__init__(upgraded_from_version, score, collateral_damage_potential, target_distribution, confidentiality_requirement, integrity_requirement, availability_requirement, source, generated_on_datetime, )
supermod.environmentalMetricsType.subclass = environmentalMetricsTypeSub
# end class environmentalMetricsTypeSub


class temporalMetricsTypeSub(supermod.temporalMetricsType):
    def __init__(self, upgraded_from_version=None, score=None, temporal_multiplier=None, exploitability=None, remediation_level=None, report_confidence=None, source=None, generated_on_datetime=None):
        super(temporalMetricsTypeSub, self).__init__(upgraded_from_version, score, temporal_multiplier, exploitability, remediation_level, report_confidence, source, generated_on_datetime, )
supermod.temporalMetricsType.subclass = temporalMetricsTypeSub
# end class temporalMetricsTypeSub


class localizedStringSub(supermod.localizedString):
    def __init__(self, lang='en', valueOf_=None, extensiontype_=None):
        super(localizedStringSub, self).__init__(lang, valueOf_, extensiontype_, )
supermod.localizedString.subclass = localizedStringSub
# end class localizedStringSub


class localizedNormalizedStringSub(supermod.localizedNormalizedString):
    def __init__(self, lang='en', valueOf_=None, extensiontype_=None):
        super(localizedNormalizedStringSub, self).__init__(lang, valueOf_, extensiontype_, )
supermod.localizedNormalizedString.subclass = localizedNormalizedStringSub
# end class localizedNormalizedStringSub


class BranchTypeSub(supermod.BranchType):
    def __init__(self, Type=None, Name=None, FullProductName=None, Branch=None):
        super(BranchTypeSub, self).__init__(Type, Name, FullProductName, Branch, )
supermod.BranchType.subclass = BranchTypeSub
# end class BranchTypeSub


class ProductTreeSub(supermod.ProductTree):
    def __init__(self, Branch=None, FullProductName=None, Relationship=None, ProductGroups=None):
        super(ProductTreeSub, self).__init__(Branch, FullProductName, Relationship, ProductGroups, )
supermod.ProductTree.subclass = ProductTreeSub
# end class ProductTreeSub


class FullProductNameSub(supermod.FullProductName):
    def __init__(self, CPE=None, ProductID=None, valueOf_=None):
        super(FullProductNameSub, self).__init__(CPE, ProductID, valueOf_, )
supermod.FullProductName.subclass = FullProductNameSub
# end class FullProductNameSub


class DocumentTitleTypeSub(supermod.DocumentTitleType):
    def __init__(self, lang='en', valueOf_=None):
        super(DocumentTitleTypeSub, self).__init__(lang, valueOf_, )
supermod.DocumentTitleType.subclass = DocumentTitleTypeSub
# end class DocumentTitleTypeSub


class DocumentTypeTypeSub(supermod.DocumentTypeType):
    def __init__(self, lang='en', valueOf_=None):
        super(DocumentTypeTypeSub, self).__init__(lang, valueOf_, )
supermod.DocumentTypeType.subclass = DocumentTypeTypeSub
# end class DocumentTypeTypeSub


class DocumentPublisherTypeSub(supermod.DocumentPublisherType):
    def __init__(self, VendorID=None, Type=None, ContactDetails=None, IssuingAuthority=None):
        super(DocumentPublisherTypeSub, self).__init__(VendorID, Type, ContactDetails, IssuingAuthority, )
supermod.DocumentPublisherType.subclass = DocumentPublisherTypeSub
# end class DocumentPublisherTypeSub


class ContactDetailsTypeSub(supermod.ContactDetailsType):
    def __init__(self, lang='en', valueOf_=None):
        super(ContactDetailsTypeSub, self).__init__(lang, valueOf_, )
supermod.ContactDetailsType.subclass = ContactDetailsTypeSub
# end class ContactDetailsTypeSub


class IssuingAuthorityTypeSub(supermod.IssuingAuthorityType):
    def __init__(self, lang='en', valueOf_=None):
        super(IssuingAuthorityTypeSub, self).__init__(lang, valueOf_, )
supermod.IssuingAuthorityType.subclass = IssuingAuthorityTypeSub
# end class IssuingAuthorityTypeSub


class DocumentTrackingTypeSub(supermod.DocumentTrackingType):
    def __init__(self, Identification=None, Status=None, Version=None, RevisionHistory=None, InitialReleaseDate=None, CurrentReleaseDate=None, Generator=None):
        super(DocumentTrackingTypeSub, self).__init__(Identification, Status, Version, RevisionHistory, InitialReleaseDate, CurrentReleaseDate, Generator, )
supermod.DocumentTrackingType.subclass = DocumentTrackingTypeSub
# end class DocumentTrackingTypeSub


class IdentificationTypeSub(supermod.IdentificationType):
    def __init__(self, ID=None, Alias=None):
        super(IdentificationTypeSub, self).__init__(ID, Alias, )
supermod.IdentificationType.subclass = IdentificationTypeSub
# end class IdentificationTypeSub


class IDTypeSub(supermod.IDType):
    def __init__(self, lang='en', valueOf_=None):
        super(IDTypeSub, self).__init__(lang, valueOf_, )
supermod.IDType.subclass = IDTypeSub
# end class IDTypeSub


class AliasTypeSub(supermod.AliasType):
    def __init__(self, lang='en', valueOf_=None):
        super(AliasTypeSub, self).__init__(lang, valueOf_, )
supermod.AliasType.subclass = AliasTypeSub
# end class AliasTypeSub


class RevisionHistoryTypeSub(supermod.RevisionHistoryType):
    def __init__(self, Revision=None):
        super(RevisionHistoryTypeSub, self).__init__(Revision, )
supermod.RevisionHistoryType.subclass = RevisionHistoryTypeSub
# end class RevisionHistoryTypeSub


class RevisionTypeSub(supermod.RevisionType):
    def __init__(self, Number=None, Date=None, Description=None):
        super(RevisionTypeSub, self).__init__(Number, Date, Description, )
supermod.RevisionType.subclass = RevisionTypeSub
# end class RevisionTypeSub


class DescriptionTypeSub(supermod.DescriptionType):
    def __init__(self, lang='en', valueOf_=None):
        super(DescriptionTypeSub, self).__init__(lang, valueOf_, )
supermod.DescriptionType.subclass = DescriptionTypeSub
# end class DescriptionTypeSub


class GeneratorTypeSub(supermod.GeneratorType):
    def __init__(self, Engine=None, Date=None):
        super(GeneratorTypeSub, self).__init__(Engine, Date, )
supermod.GeneratorType.subclass = GeneratorTypeSub
# end class GeneratorTypeSub


class EngineTypeSub(supermod.EngineType):
    def __init__(self, lang='en', valueOf_=None):
        super(EngineTypeSub, self).__init__(lang, valueOf_, )
supermod.EngineType.subclass = EngineTypeSub
# end class EngineTypeSub


class DocumentNotesTypeSub(supermod.DocumentNotesType):
    def __init__(self, Note=None):
        super(DocumentNotesTypeSub, self).__init__(Note, )
supermod.DocumentNotesType.subclass = DocumentNotesTypeSub
# end class DocumentNotesTypeSub


class NoteTypeSub(supermod.NoteType):
    def __init__(self, lang='en', Ordinal=None, Audience=None, Type=None, Title=None, valueOf_=None):
        super(NoteTypeSub, self).__init__(lang, Ordinal, Audience, Type, Title, valueOf_, )
supermod.NoteType.subclass = NoteTypeSub
# end class NoteTypeSub


class DocumentDistributionTypeSub(supermod.DocumentDistributionType):
    def __init__(self, lang='en', valueOf_=None):
        super(DocumentDistributionTypeSub, self).__init__(lang, valueOf_, )
supermod.DocumentDistributionType.subclass = DocumentDistributionTypeSub
# end class DocumentDistributionTypeSub


class AggregateSeverityTypeSub(supermod.AggregateSeverityType):
    def __init__(self, lang='en', Namespace=None, valueOf_=None):
        super(AggregateSeverityTypeSub, self).__init__(lang, Namespace, valueOf_, )
supermod.AggregateSeverityType.subclass = AggregateSeverityTypeSub
# end class AggregateSeverityTypeSub


class DocumentReferencesTypeSub(supermod.DocumentReferencesType):
    def __init__(self, Reference=None):
        super(DocumentReferencesTypeSub, self).__init__(Reference, )
supermod.DocumentReferencesType.subclass = DocumentReferencesTypeSub
# end class DocumentReferencesTypeSub


class ReferenceTypeSub(supermod.ReferenceType):
    def __init__(self, Type='External', URL=None, Description=None):
        super(ReferenceTypeSub, self).__init__(Type, URL, Description, )
supermod.ReferenceType.subclass = ReferenceTypeSub
# end class ReferenceTypeSub


class DescriptionType1Sub(supermod.DescriptionType1):
    def __init__(self, lang='en', valueOf_=None):
        super(DescriptionType1Sub, self).__init__(lang, valueOf_, )
supermod.DescriptionType1.subclass = DescriptionType1Sub
# end class DescriptionType1Sub


class AcknowledgmentsTypeSub(supermod.AcknowledgmentsType):
    def __init__(self, Acknowledgment=None):
        super(AcknowledgmentsTypeSub, self).__init__(Acknowledgment, )
supermod.AcknowledgmentsType.subclass = AcknowledgmentsTypeSub
# end class AcknowledgmentsTypeSub


class AcknowledgmentTypeSub(supermod.AcknowledgmentType):
    def __init__(self, Name=None, Organization=None, Description=None, URL=None):
        super(AcknowledgmentTypeSub, self).__init__(Name, Organization, Description, URL, )
supermod.AcknowledgmentType.subclass = AcknowledgmentTypeSub
# end class AcknowledgmentTypeSub


class NameTypeSub(supermod.NameType):
    def __init__(self, lang='en', valueOf_=None):
        super(NameTypeSub, self).__init__(lang, valueOf_, )
supermod.NameType.subclass = NameTypeSub
# end class NameTypeSub


class OrganizationTypeSub(supermod.OrganizationType):
    def __init__(self, lang='en', valueOf_=None):
        super(OrganizationTypeSub, self).__init__(lang, valueOf_, )
supermod.OrganizationType.subclass = OrganizationTypeSub
# end class OrganizationTypeSub


class DescriptionType2Sub(supermod.DescriptionType2):
    def __init__(self, lang='en', valueOf_=None):
        super(DescriptionType2Sub, self).__init__(lang, valueOf_, )
supermod.DescriptionType2.subclass = DescriptionType2Sub
# end class DescriptionType2Sub


class TitleTypeSub(supermod.TitleType):
    def __init__(self, lang='en', valueOf_=None):
        super(TitleTypeSub, self).__init__(lang, valueOf_, )
supermod.TitleType.subclass = TitleTypeSub
# end class TitleTypeSub


class IDType3Sub(supermod.IDType3):
    def __init__(self, SystemName=None, valueOf_=None):
        super(IDType3Sub, self).__init__(SystemName, valueOf_, )
supermod.IDType3.subclass = IDType3Sub
# end class IDType3Sub


class NotesTypeSub(supermod.NotesType):
    def __init__(self, Note=None):
        super(NotesTypeSub, self).__init__(Note, )
supermod.NotesType.subclass = NotesTypeSub
# end class NotesTypeSub


class NoteType4Sub(supermod.NoteType4):
    def __init__(self, lang='en', Ordinal=None, Audience=None, Type=None, Title=None, valueOf_=None):
        super(NoteType4Sub, self).__init__(lang, Ordinal, Audience, Type, Title, valueOf_, )
supermod.NoteType4.subclass = NoteType4Sub
# end class NoteType4Sub


class InvolvementsTypeSub(supermod.InvolvementsType):
    def __init__(self, Involvement=None):
        super(InvolvementsTypeSub, self).__init__(Involvement, )
supermod.InvolvementsType.subclass = InvolvementsTypeSub
# end class InvolvementsTypeSub


class InvolvementTypeSub(supermod.InvolvementType):
    def __init__(self, Status=None, Party=None, Description=None):
        super(InvolvementTypeSub, self).__init__(Status, Party, Description, )
supermod.InvolvementType.subclass = InvolvementTypeSub
# end class InvolvementTypeSub


class DescriptionType5Sub(supermod.DescriptionType5):
    def __init__(self, lang='en', valueOf_=None):
        super(DescriptionType5Sub, self).__init__(lang, valueOf_, )
supermod.DescriptionType5.subclass = DescriptionType5Sub
# end class DescriptionType5Sub


class CWETypeSub(supermod.CWEType):
    def __init__(self, lang='en', ID=None, valueOf_=None):
        super(CWETypeSub, self).__init__(lang, ID, valueOf_, )
supermod.CWEType.subclass = CWETypeSub
# end class CWETypeSub


class ProductStatusesTypeSub(supermod.ProductStatusesType):
    def __init__(self, Status=None):
        super(ProductStatusesTypeSub, self).__init__(Status, )
supermod.ProductStatusesType.subclass = ProductStatusesTypeSub
# end class ProductStatusesTypeSub


class StatusTypeSub(supermod.StatusType):
    def __init__(self, Type=None, ProductID=None):
        super(StatusTypeSub, self).__init__(Type, ProductID, )
supermod.StatusType.subclass = StatusTypeSub
# end class StatusTypeSub


class ThreatsTypeSub(supermod.ThreatsType):
    def __init__(self, Threat=None):
        super(ThreatsTypeSub, self).__init__(Threat, )
supermod.ThreatsType.subclass = ThreatsTypeSub
# end class ThreatsTypeSub


class ThreatTypeSub(supermod.ThreatType):
    def __init__(self, Date=None, Type=None, Description=None, ProductID=None, GroupID=None):
        super(ThreatTypeSub, self).__init__(Date, Type, Description, ProductID, GroupID, )
supermod.ThreatType.subclass = ThreatTypeSub
# end class ThreatTypeSub


class DescriptionType6Sub(supermod.DescriptionType6):
    def __init__(self, lang='en', valueOf_=None):
        super(DescriptionType6Sub, self).__init__(lang, valueOf_, )
supermod.DescriptionType6.subclass = DescriptionType6Sub
# end class DescriptionType6Sub


class CVSSScoreSetsTypeSub(supermod.CVSSScoreSetsType):
    def __init__(self, ScoreSet=None):
        super(CVSSScoreSetsTypeSub, self).__init__(ScoreSet, )
supermod.CVSSScoreSetsType.subclass = CVSSScoreSetsTypeSub
# end class CVSSScoreSetsTypeSub


class ScoreSetTypeSub(supermod.ScoreSetType):
    def __init__(self, BaseScore=None, TemporalScore=None, EnvironmentalScore=None, Vector=None, ProductID=None):
        super(ScoreSetTypeSub, self).__init__(BaseScore, TemporalScore, EnvironmentalScore, Vector, ProductID, )
supermod.ScoreSetType.subclass = ScoreSetTypeSub
# end class ScoreSetTypeSub


class RemediationsTypeSub(supermod.RemediationsType):
    def __init__(self, Remediation=None):
        super(RemediationsTypeSub, self).__init__(Remediation, )
supermod.RemediationsType.subclass = RemediationsTypeSub
# end class RemediationsTypeSub


class RemediationTypeSub(supermod.RemediationType):
    def __init__(self, Date=None, Type=None, Description=None, Entitlement=None, URL=None, ProductID=None, GroupID=None):
        super(RemediationTypeSub, self).__init__(Date, Type, Description, Entitlement, URL, ProductID, GroupID, )
supermod.RemediationType.subclass = RemediationTypeSub
# end class RemediationTypeSub


class DescriptionType7Sub(supermod.DescriptionType7):
    def __init__(self, lang='en', valueOf_=None):
        super(DescriptionType7Sub, self).__init__(lang, valueOf_, )
supermod.DescriptionType7.subclass = DescriptionType7Sub
# end class DescriptionType7Sub


class EntitlementTypeSub(supermod.EntitlementType):
    def __init__(self, lang='en', valueOf_=None):
        super(EntitlementTypeSub, self).__init__(lang, valueOf_, )
supermod.EntitlementType.subclass = EntitlementTypeSub
# end class EntitlementTypeSub


class ReferencesTypeSub(supermod.ReferencesType):
    def __init__(self, Reference=None):
        super(ReferencesTypeSub, self).__init__(Reference, )
supermod.ReferencesType.subclass = ReferencesTypeSub
# end class ReferencesTypeSub


class ReferenceType8Sub(supermod.ReferenceType8):
    def __init__(self, Type='External', URL=None, Description=None):
        super(ReferenceType8Sub, self).__init__(Type, URL, Description, )
supermod.ReferenceType8.subclass = ReferenceType8Sub
# end class ReferenceType8Sub


class DescriptionType9Sub(supermod.DescriptionType9):
    def __init__(self, lang='en', valueOf_=None):
        super(DescriptionType9Sub, self).__init__(lang, valueOf_, )
supermod.DescriptionType9.subclass = DescriptionType9Sub
# end class DescriptionType9Sub


class AcknowledgmentsType10Sub(supermod.AcknowledgmentsType10):
    def __init__(self, Acknowledgment=None):
        super(AcknowledgmentsType10Sub, self).__init__(Acknowledgment, )
supermod.AcknowledgmentsType10.subclass = AcknowledgmentsType10Sub
# end class AcknowledgmentsType10Sub


class AcknowledgmentType11Sub(supermod.AcknowledgmentType11):
    def __init__(self, Name=None, Organization=None, Description=None, URL=None):
        super(AcknowledgmentType11Sub, self).__init__(Name, Organization, Description, URL, )
supermod.AcknowledgmentType11.subclass = AcknowledgmentType11Sub
# end class AcknowledgmentType11Sub


class NameType12Sub(supermod.NameType12):
    def __init__(self, lang='en', valueOf_=None):
        super(NameType12Sub, self).__init__(lang, valueOf_, )
supermod.NameType12.subclass = NameType12Sub
# end class NameType12Sub


class OrganizationType13Sub(supermod.OrganizationType13):
    def __init__(self, lang='en', valueOf_=None):
        super(OrganizationType13Sub, self).__init__(lang, valueOf_, )
supermod.OrganizationType13.subclass = OrganizationType13Sub
# end class OrganizationType13Sub


class DescriptionType14Sub(supermod.DescriptionType14):
    def __init__(self, lang='en', valueOf_=None):
        super(DescriptionType14Sub, self).__init__(lang, valueOf_, )
supermod.DescriptionType14.subclass = DescriptionType14Sub
# end class DescriptionType14Sub


class RelationshipTypeSub(supermod.RelationshipType):
    def __init__(self, RelationType=None, RelatesToProductReference=None, ProductReference=None, FullProductName=None):
        super(RelationshipTypeSub, self).__init__(RelationType, RelatesToProductReference, ProductReference, FullProductName, )
supermod.RelationshipType.subclass = RelationshipTypeSub
# end class RelationshipTypeSub


class ProductGroupsTypeSub(supermod.ProductGroupsType):
    def __init__(self, Group=None):
        super(ProductGroupsTypeSub, self).__init__(Group, )
supermod.ProductGroupsType.subclass = ProductGroupsTypeSub
# end class ProductGroupsTypeSub


class GroupTypeSub(supermod.GroupType):
    def __init__(self, GroupID=None, Description=None, ProductID=None):
        super(GroupTypeSub, self).__init__(GroupID, Description, ProductID, )
supermod.GroupType.subclass = GroupTypeSub
# end class GroupTypeSub


class DescriptionType15Sub(supermod.DescriptionType15):
    def __init__(self, lang='en', valueOf_=None):
        super(DescriptionType15Sub, self).__init__(lang, valueOf_, )
supermod.DescriptionType15.subclass = DescriptionType15Sub
# end class DescriptionType15Sub


class checkReferenceTypeSub(supermod.checkReferenceType):
    def __init__(self, system=None, name=None, href=None):
        super(checkReferenceTypeSub, self).__init__(system, name, href, )
supermod.checkReferenceType.subclass = checkReferenceTypeSub
# end class checkReferenceTypeSub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'cvrfdoc'
        rootClass = supermod.cvrfdoc
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='xmlns:cvrf="http://www.icasi.org/CVRF/schema/cvrf/1.1"',
            pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'cvrfdoc'
        rootClass = supermod.cvrfdoc
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(content)
        sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    from StringIO import StringIO
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'cvrfdoc'
        rootClass = supermod.cvrfdoc
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='xmlns:cvrf="http://www.icasi.org/CVRF/schema/cvrf/1.1"')
    return rootObj


def parseLiteral(inFilename, silence=False):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'cvrfdoc'
        rootClass = supermod.cvrfdoc
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('#from ??? import *\n\n')
        sys.stdout.write('import ??? as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print USAGE_TEXT
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
