from django import forms


class AcknowledgmentType_form(forms.Form):
    Name = forms.MultipleChoiceField(NameType_model.objects.all())
    Organization = forms.MultipleChoiceField(OrganizationType_model.objects.all())
    Description = forms.MultipleChoiceField(DescriptionType2_model.objects.all())
    URL = forms.CharField(max_length=1000, blank=True)

class AcknowledgmentType11_form(forms.Form):
    Name = forms.MultipleChoiceField(NameType12_model.objects.all())
    Organization = forms.MultipleChoiceField(OrganizationType13_model.objects.all())
    Description = forms.MultipleChoiceField(DescriptionType14_model.objects.all())
    URL = forms.CharField(max_length=1000, blank=True)

class AcknowledgmentsType_form(forms.Form):
    Acknowledgment = forms.MultipleChoiceField(AcknowledgmentType_model.objects.all())

class AcknowledgmentsType10_form(forms.Form):
    Acknowledgment = forms.MultipleChoiceField(AcknowledgmentType11_model.objects.all())

class AggregateSeverityType_form(forms.Form):
    Namespace = forms.CharField(max_length=1000, blank=True)
    valueOf_x = forms.MultipleChoiceField(localizedString_model.objects.all())

class AliasType_form(forms.Form):
    valueOf_x = forms.MultipleChoiceField(localizedString_model.objects.all())

class BranchType_form(forms.Form):
    Type = forms.CharField(max_length=1000, blank=True)
    Name = forms.CharField(max_length=1000, blank=True)
    FullProductName = forms.MultipleChoiceField(FullProductName_model.objects.all())
    Branch = forms.MultipleChoiceField(BranchType_model.objects.all())

class CVSSScoreSetsType_form(forms.Form):
    ScoreSet = forms.MultipleChoiceField(ScoreSetType_model.objects.all())

class CWEType_form(forms.Form):
    ID = forms.CharField(max_length=1000, blank=True)
    valueOf_x = forms.MultipleChoiceField(localizedString_model.objects.all())

class ContactDetailsType_form(forms.Form):
    valueOf_x = forms.MultipleChoiceField(localizedString_model.objects.all())

class DescriptionType_form(forms.Form):
    valueOf_x = forms.MultipleChoiceField(localizedString_model.objects.all())

class DescriptionType1_form(forms.Form):
    valueOf_x = forms.MultipleChoiceField(localizedString_model.objects.all())

class DescriptionType14_form(forms.Form):
    valueOf_x = forms.MultipleChoiceField(localizedString_model.objects.all())

class DescriptionType15_form(forms.Form):
    valueOf_x = forms.MultipleChoiceField(localizedString_model.objects.all())

class DescriptionType2_form(forms.Form):
    valueOf_x = forms.MultipleChoiceField(localizedString_model.objects.all())

class DescriptionType5_form(forms.Form):
    valueOf_x = forms.MultipleChoiceField(localizedString_model.objects.all())

class DescriptionType6_form(forms.Form):
    valueOf_x = forms.MultipleChoiceField(localizedString_model.objects.all())

class DescriptionType7_form(forms.Form):
    valueOf_x = forms.MultipleChoiceField(localizedString_model.objects.all())

class DescriptionType9_form(forms.Form):
    valueOf_x = forms.MultipleChoiceField(localizedString_model.objects.all())

class DocumentDistributionType_form(forms.Form):
    valueOf_x = forms.MultipleChoiceField(localizedString_model.objects.all())

class DocumentNotesType_form(forms.Form):
    Note = forms.MultipleChoiceField(NoteType_model.objects.all())

class DocumentPublisherType_form(forms.Form):
    VendorID = forms.CharField(max_length=1000, blank=True)
    Type = forms.CharField(max_length=1000, blank=True)
    ContactDetails = forms.MultipleChoiceField(ContactDetailsType_model.objects.all())
    IssuingAuthority = forms.MultipleChoiceField(IssuingAuthorityType_model.objects.all())

class DocumentReferencesType_form(forms.Form):
    Reference = forms.MultipleChoiceField(ReferenceType_model.objects.all())

class DocumentTitleType_form(forms.Form):
    valueOf_x = forms.MultipleChoiceField(localizedNormalizedString_model.objects.all())

class DocumentTrackingType_form(forms.Form):
    Identification = forms.MultipleChoiceField(IdentificationType_model.objects.all())
    Status = forms.CharField(max_length=1000, blank=True)
    Version = forms.CharField(max_length=1000, blank=True)
    RevisionHistory = forms.MultipleChoiceField(RevisionHistoryType_model.objects.all())
    InitialReleaseDate = forms.DateTimeField(blank=True)
    CurrentReleaseDate = forms.DateTimeField(blank=True)
    Generator = forms.MultipleChoiceField(GeneratorType_model.objects.all())

class DocumentTypeType_form(forms.Form):
    valueOf_x = forms.MultipleChoiceField(localizedNormalizedString_model.objects.all())

class EngineType_form(forms.Form):
    valueOf_x = forms.MultipleChoiceField(localizedString_model.objects.all())

class EntitlementType_form(forms.Form):
    valueOf_x = forms.MultipleChoiceField(localizedString_model.objects.all())

class FactRefType_form(forms.Form):
    name = forms.CharField(max_length=1000, blank=True)

class FullProductName_form(forms.Form):
    CPE = forms.CharField(max_length=1000, blank=True)
    ProductID = forms.CharField(max_length=1000, blank=True)
    valueOf_x = forms.CharField(max_length=1000, blank=True)

class GeneratorType_form(forms.Form):
    Engine = forms.MultipleChoiceField(EngineType_model.objects.all())
    Date = forms.DateTimeField(blank=True)

class GroupType_form(forms.Form):
    GroupID = forms.CharField(max_length=1000, blank=True)
    Description = forms.MultipleChoiceField(DescriptionType15_model.objects.all())
    ProductID = forms.CharField(max_length=1000, blank=True)

class IDType_form(forms.Form):
    valueOf_x = forms.MultipleChoiceField(localizedString_model.objects.all())

class IDType3_form(forms.Form):
    SystemName = forms.CharField(max_length=1000, blank=True)
    valueOf_x = forms.CharField(max_length=1000, blank=True)

class IdentificationType_form(forms.Form):
    ID = forms.MultipleChoiceField(IDType_model.objects.all())
    Alias = forms.MultipleChoiceField(AliasType_model.objects.all())

class InvolvementType_form(forms.Form):
    Status = forms.CharField(max_length=1000, blank=True)
    Party = forms.CharField(max_length=1000, blank=True)
    Description = forms.MultipleChoiceField(DescriptionType5_model.objects.all())

class InvolvementsType_form(forms.Form):
    Involvement = forms.MultipleChoiceField(InvolvementType_model.objects.all())

class IssuingAuthorityType_form(forms.Form):
    valueOf_x = forms.MultipleChoiceField(localizedString_model.objects.all())

class LogicalTestType_form(forms.Form):
    operator = forms.CharField(max_length=1000, blank=True)
    negate = forms.BooleanField(blank=True)
    logical_test = forms.MultipleChoiceField(LogicalTestType_model.objects.all())
    fact_ref = forms.MultipleChoiceField(fact_ref_model.objects.all())

class NameType_form(forms.Form):
    valueOf_x = forms.MultipleChoiceField(localizedString_model.objects.all())

class NameType12_form(forms.Form):
    valueOf_x = forms.MultipleChoiceField(localizedString_model.objects.all())

class NoteType_form(forms.Form):
    Ordinal = forms.IntegerField(blank=True)
    Audience = forms.CharField(max_length=1000, blank=True)
    Type = forms.CharField(max_length=1000, blank=True)
    Title = forms.CharField(max_length=1000, blank=True)
    valueOf_x = forms.MultipleChoiceField(localizedString_model.objects.all())

class NoteType4_form(forms.Form):
    Ordinal = forms.IntegerField(blank=True)
    Audience = forms.CharField(max_length=1000, blank=True)
    Type = forms.CharField(max_length=1000, blank=True)
    Title = forms.CharField(max_length=1000, blank=True)
    valueOf_x = forms.MultipleChoiceField(localizedString_model.objects.all())

class NotesType_form(forms.Form):
    Note = forms.MultipleChoiceField(NoteType4_model.objects.all())

class OrganizationType_form(forms.Form):
    valueOf_x = forms.MultipleChoiceField(localizedString_model.objects.all())

class OrganizationType13_form(forms.Form):
    valueOf_x = forms.MultipleChoiceField(localizedString_model.objects.all())

class PlatformBaseType_form(forms.Form):
    title = forms.MultipleChoiceField(title_model.objects.all())
    remark = forms.MultipleChoiceField(TextType_model.objects.all())
    logical_test = forms.MultipleChoiceField(logical_test_model.objects.all())

class PlatformType_form(forms.Form):
    idx = forms.CharField(max_length=1000, blank=True)

class ProductGroupsType_form(forms.Form):
    Group = forms.MultipleChoiceField(GroupType_model.objects.all())

class ProductStatusesType_form(forms.Form):
    Status = forms.MultipleChoiceField(StatusType_model.objects.all())

class ProductTree_form(forms.Form):
    Branch = forms.MultipleChoiceField(BranchType_model.objects.all())
    FullProductName = forms.MultipleChoiceField(FullProductName_model.objects.all())
    Relationship = forms.MultipleChoiceField(RelationshipType_model.objects.all())
    ProductGroups = forms.MultipleChoiceField(ProductGroupsType_model.objects.all())

class ReferenceType_form(forms.Form):
    Type = forms.CharField(max_length=1000, blank=True)
    URL = forms.CharField(max_length=1000, blank=True)
    Description = forms.MultipleChoiceField(DescriptionType1_model.objects.all())

class ReferenceType8_form(forms.Form):
    Type = forms.CharField(max_length=1000, blank=True)
    URL = forms.CharField(max_length=1000, blank=True)
    Description = forms.MultipleChoiceField(DescriptionType9_model.objects.all())

class ReferencesType_form(forms.Form):
    Reference = forms.MultipleChoiceField(ReferenceType8_model.objects.all())

class RelationshipType_form(forms.Form):
    RelationType = forms.CharField(max_length=1000, blank=True)
    RelatesToProductReference = forms.CharField(max_length=1000, blank=True)
    ProductReference = forms.CharField(max_length=1000, blank=True)
    FullProductName = forms.MultipleChoiceField(FullProductName_model.objects.all())

class RemediationType_form(forms.Form):
    Date = forms.DateTimeField(blank=True)
    Type = forms.CharField(max_length=1000, blank=True)
    Description = forms.MultipleChoiceField(DescriptionType7_model.objects.all())
    Entitlement = forms.MultipleChoiceField(EntitlementType_model.objects.all())
    URL = forms.CharField(max_length=1000, blank=True)
    ProductID = forms.CharField(max_length=1000, blank=True)
    GroupID = forms.CharField(max_length=1000, blank=True)

class RemediationsType_form(forms.Form):
    Remediation = forms.MultipleChoiceField(RemediationType_model.objects.all())

class RevisionHistoryType_form(forms.Form):
    Revision = forms.MultipleChoiceField(RevisionType_model.objects.all())

class RevisionType_form(forms.Form):
    Number = forms.CharField(max_length=1000, blank=True)
    Date = forms.DateTimeField(blank=True)
    Description = forms.MultipleChoiceField(DescriptionType_model.objects.all())

class ScoreSetType_form(forms.Form):
    BaseScore = forms.FloatField(blank=True)
    TemporalScore = forms.FloatField(blank=True)
    EnvironmentalScore = forms.FloatField(blank=True)
    Vector = forms.CharField(max_length=1000, blank=True)
    ProductID = forms.CharField(max_length=1000, blank=True)

class SimpleLiteral_form(forms.Form):
    lang = forms.CharField(max_length=1000, blank=True)
     = forms.CharField(max_length=1000, blank=True)

class StatusType_form(forms.Form):
    Type = forms.CharField(max_length=1000, blank=True)
    ProductID = forms.CharField(max_length=1000, blank=True)

class TextType_form(forms.Form):
    lang = forms.CharField(max_length=1000, blank=True)
    valueOf_x = forms.CharField(max_length=1000, blank=True)

class ThreatType_form(forms.Form):
    Date = forms.DateTimeField(blank=True)
    Type = forms.CharField(max_length=1000, blank=True)
    Description = forms.MultipleChoiceField(DescriptionType6_model.objects.all())
    ProductID = forms.CharField(max_length=1000, blank=True)
    GroupID = forms.CharField(max_length=1000, blank=True)

class ThreatsType_form(forms.Form):
    Threat = forms.MultipleChoiceField(ThreatType_model.objects.all())

class TitleType_form(forms.Form):
    valueOf_x = forms.MultipleChoiceField(localizedString_model.objects.all())

class Vulnerability_form(forms.Form):
    Ordinal = forms.IntegerField(blank=True)
    Title = forms.MultipleChoiceField(TitleType_model.objects.all())
    ID = forms.MultipleChoiceField(IDType3_model.objects.all())
    Notes = forms.MultipleChoiceField(NotesType_model.objects.all())
    DiscoveryDate = forms.DateTimeField(blank=True)
    ReleaseDate = forms.DateTimeField(blank=True)
    Involvements = forms.MultipleChoiceField(InvolvementsType_model.objects.all())
    CVE = forms.CharField(max_length=1000, blank=True)
    CWE = forms.MultipleChoiceField(CWEType_model.objects.all())
    ProductStatuses = forms.MultipleChoiceField(ProductStatusesType_model.objects.all())
    Threats = forms.MultipleChoiceField(ThreatsType_model.objects.all())
    CVSSScoreSets = forms.MultipleChoiceField(CVSSScoreSetsType_model.objects.all())
    Remediations = forms.MultipleChoiceField(RemediationsType_model.objects.all())
    References = forms.MultipleChoiceField(ReferencesType_model.objects.all())
    Acknowledgments = forms.MultipleChoiceField(AcknowledgmentsType10_model.objects.all())

class accessComplexityType_form(forms.Form):
    approximated = forms.BooleanField(blank=True)
    valueOf_x = forms.CharField(max_length=1000, blank=True)

class accessVectorType_form(forms.Form):
    approximated = forms.BooleanField(blank=True)
    valueOf_x = forms.CharField(max_length=1000, blank=True)

class assessmentMethodType_form(forms.Form):
    assessment_check = forms.MultipleChoiceField(checkReferenceType_model.objects.all())
    assessment_engine = forms.CharField(max_length=1000, blank=True)

class authenticationType_form(forms.Form):
    approximated = forms.BooleanField(blank=True)
    valueOf_x = forms.CharField(max_length=1000, blank=True)

class baseMetricsType_form(forms.Form):
    score = forms.FloatField(blank=True)
    exploit_subscore = forms.FloatField(blank=True)
    impact_subscore = forms.FloatField(blank=True)
    access_vector = forms.MultipleChoiceField(accessVectorType_model.objects.all())
    access_complexity = forms.MultipleChoiceField(accessComplexityType_model.objects.all())
    authentication = forms.MultipleChoiceField(authenticationType_model.objects.all())
    confidentiality_impact = forms.MultipleChoiceField(ciaType_model.objects.all())
    integrity_impact = forms.MultipleChoiceField(ciaType_model.objects.all())
    availability_impact = forms.MultipleChoiceField(ciaType_model.objects.all())
    source = forms.MultipleChoiceField(source_model.objects.all())
    generated_on_datetime = forms.CharField(max_length=1000, blank=True)

class checkReferenceType_form(forms.Form):
    href = forms.CharField(max_length=1000, blank=True)

class checkSearchType_form(forms.Form):
    system = forms.CharField(max_length=1000, blank=True)
    name = forms.CharField(max_length=1000, blank=True)

class ciaRequirementType_form(forms.Form):
    approximated = forms.BooleanField(blank=True)
    valueOf_x = forms.CharField(max_length=1000, blank=True)

class ciaType_form(forms.Form):
    approximated = forms.BooleanField(blank=True)
    valueOf_x = forms.CharField(max_length=1000, blank=True)

class collateralDamagePotentialType_form(forms.Form):
    approximated = forms.BooleanField(blank=True)
    valueOf_x = forms.CharField(max_length=1000, blank=True)

class confidenceType_form(forms.Form):
    approximated = forms.BooleanField(blank=True)
    valueOf_x = forms.CharField(max_length=1000, blank=True)

class contributor_form(forms.Form):

class controlMappingType_form(forms.Form):
    source = forms.CharField(max_length=1000, blank=True)
    system_id = forms.CharField(max_length=1000, blank=True)
    last_modified = forms.DateTimeField(blank=True)
    mapping = forms.MultipleChoiceField(mappingInstanceType_model.objects.all())

class controlMappingsType_form(forms.Form):
    control_mapping = forms.MultipleChoiceField(controlMappingType_model.objects.all())

class coverage_form(forms.Form):

class creator_form(forms.Form):

class cvrfdoc_form(forms.Form):
    DocumentTitle = forms.MultipleChoiceField(DocumentTitleType_model.objects.all())
    DocumentType = forms.MultipleChoiceField(DocumentTypeType_model.objects.all())
    DocumentPublisher = forms.MultipleChoiceField(DocumentPublisherType_model.objects.all())
    DocumentTracking = forms.MultipleChoiceField(DocumentTrackingType_model.objects.all())
    DocumentNotes = forms.MultipleChoiceField(DocumentNotesType_model.objects.all())
    DocumentDistribution = forms.MultipleChoiceField(DocumentDistributionType_model.objects.all())
    AggregateSeverity = forms.MultipleChoiceField(AggregateSeverityType_model.objects.all())
    DocumentReferences = forms.MultipleChoiceField(DocumentReferencesType_model.objects.all())
    Acknowledgments = forms.MultipleChoiceField(AcknowledgmentsType_model.objects.all())
    ProductTree = forms.MultipleChoiceField(ProductTree_model.objects.all())
    Vulnerability = forms.MultipleChoiceField(Vulnerability_model.objects.all())

class cvssImpactBaseType_form(forms.Form):
    base_metrics = forms.MultipleChoiceField(baseMetricsType_model.objects.all())

class cvssImpactEnvironmentalType_form(forms.Form):
    environmental_metrics = forms.MultipleChoiceField(environmentalMetricsType_model.objects.all())

class cvssImpactTemporalType_form(forms.Form):
    temporal_metrics = forms.MultipleChoiceField(temporalMetricsType_model.objects.all())

class cvssImpactType_form(forms.Form):
    base_metrics = forms.MultipleChoiceField(baseMetricsType_model.objects.all())
    environmental_metrics = forms.MultipleChoiceField(environmentalMetricsType_model.objects.all())
    temporal_metrics = forms.MultipleChoiceField(temporalMetricsType_model.objects.all())

class cvssType_form(forms.Form):
    base_metrics = forms.MultipleChoiceField(baseMetricsType_model.objects.all())
    environmental_metrics = forms.MultipleChoiceField(environmentalMetricsType_model.objects.all())
    temporal_metrics = forms.MultipleChoiceField(temporalMetricsType_model.objects.all())

class date_form(forms.Form):

class description_form(forms.Form):

class elementContainer_form(forms.Form):
    any = forms.MultipleChoiceField(SimpleLiteral_model.objects.all())

class environmentalMetricsType_form(forms.Form):
    score = forms.FloatField(blank=True)
    collateral_damage_potential = forms.MultipleChoiceField(collateralDamagePotentialType_model.objects.all())
    target_distribution = forms.MultipleChoiceField(targetDistributionType_model.objects.all())
    confidentiality_requirement = forms.MultipleChoiceField(ciaRequirementType_model.objects.all())
    integrity_requirement = forms.MultipleChoiceField(ciaRequirementType_model.objects.all())
    availability_requirement = forms.MultipleChoiceField(ciaRequirementType_model.objects.all())
    source = forms.MultipleChoiceField(source_model.objects.all())
    generated_on_datetime = forms.CharField(max_length=1000, blank=True)

class exploitabilityType_form(forms.Form):
    approximated = forms.BooleanField(blank=True)
    valueOf_x = forms.CharField(max_length=1000, blank=True)

class format_form(forms.Form):

class identifier_form(forms.Form):

class identifyableAssessmentMethodType_form(forms.Form):
    idx = forms.IntegerField(blank=True)

class language_form(forms.Form):

class localizedNormalizedString_form(forms.Form):
    lang = forms.CharField(max_length=1000, blank=True)
    valueOf_x = forms.CharField(max_length=1000, blank=True)

class localizedString_form(forms.Form):
    lang = forms.CharField(max_length=1000, blank=True)
    valueOf_x = forms.CharField(max_length=1000, blank=True)

class mappingInstanceType_form(forms.Form):
    published = forms.DateTimeField(blank=True)
    valueOf_x = forms.CharField(max_length=1000, blank=True)

class metricsType_form(forms.Form):
    upgraded_from_version = forms.FloatField(blank=True)

class platformSpecificationType_form(forms.Form):
    platform = forms.MultipleChoiceField(PlatformType_model.objects.all())

class publisher_form(forms.Form):

class relation_form(forms.Form):

class remediationLevelType_form(forms.Form):
    approximated = forms.BooleanField(blank=True)
    valueOf_x = forms.CharField(max_length=1000, blank=True)

class rights_form(forms.Form):

class searchableCpeReferencesType_form(forms.Form):
    cpe_name = forms.CharField(max_length=1000, blank=True)
    cpe_searchable_name = forms.CharField(max_length=1000, blank=True)

class source_form(forms.Form):

class subject_form(forms.Form):

class targetDistributionType_form(forms.Form):
    approximated = forms.BooleanField(blank=True)
    valueOf_x = forms.CharField(max_length=1000, blank=True)

class temporalMetricsType_form(forms.Form):
    score = forms.FloatField(blank=True)
    temporal_multiplier = forms.CharField(max_length=1000, blank=True)
    exploitability = forms.MultipleChoiceField(exploitabilityType_model.objects.all())
    remediation_level = forms.MultipleChoiceField(remediationLevelType_model.objects.all())
    report_confidence = forms.MultipleChoiceField(confidenceType_model.objects.all())
    source = forms.MultipleChoiceField(source_model.objects.all())
    generated_on_datetime = forms.CharField(max_length=1000, blank=True)

class title_form(forms.Form):

class type__form(forms.Form):
