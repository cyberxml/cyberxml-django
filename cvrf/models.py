from django.db import models


class AcknowledgmentType_model(models.Model):
    Name = models.ForeignKey("NameType_model",related_name="23778751")
    Organization = models.ForeignKey("OrganizationType_model",related_name="29106573")
    Description = models.ForeignKey("DescriptionType2_model",related_name="84581385")
    URL = models.CharField(max_length=1000, blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )

class AcknowledgmentType11_model(models.Model):
    Name = models.ForeignKey("NameType12_model",related_name="15220829")
    Organization = models.ForeignKey("OrganizationType13_model",related_name="58553734")
    Description = models.ForeignKey("DescriptionType14_model",related_name="19347538")
    URL = models.CharField(max_length=1000, blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )

class AcknowledgmentsType_model(models.Model):
    Acknowledgment = models.ForeignKey("AcknowledgmentType_model",related_name="81062270")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class AcknowledgmentsType10_model(models.Model):
    Acknowledgment = models.ForeignKey("AcknowledgmentType11_model",related_name="17353068")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class AggregateSeverityType_model(models.Model):
    localizedString = models.ForeignKey("localizedString_model",related_name="48498321")
    Namespace = models.CharField(max_length=1000, blank=True)
    valueOf_x = models.ForeignKey("localizedString_model",related_name="15186262")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class AliasType_model(models.Model):
    localizedString = models.ForeignKey("localizedString_model",related_name="36695705")
    valueOf_x = models.ForeignKey("localizedString_model",related_name="49173647")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class BranchType_model(models.Model):
    Type = models.CharField(max_length=1000, blank=True)
    Name = models.CharField(max_length=1000, blank=True)
    FullProductName = models.ForeignKey("FullProductName_model",related_name="91009411")
    Branch = models.ForeignKey("BranchType_model",related_name="26525690")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class CVSSScoreSetsType_model(models.Model):
    ScoreSet = models.ForeignKey("ScoreSetType_model",related_name="89318755")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class CWEType_model(models.Model):
    row = models.AutoField(primary_key=True)
    localizedString = models.ForeignKey("localizedString_model",related_name="22035095")
    ID = models.CharField(max_length=1000, blank=True)
    valueOf_x = models.ForeignKey("localizedString_model",related_name="63179837")
    def __unicode__(self):
        return "id: %s" % (self.row, )

class ContactDetailsType_model(models.Model):
    localizedString = models.ForeignKey("localizedString_model",related_name="57107715")
    valueOf_x = models.ForeignKey("localizedString_model",related_name="33215757")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class DescriptionType_model(models.Model):
    localizedString = models.ForeignKey("localizedString_model",related_name="10445476")
    valueOf_x = models.ForeignKey("localizedString_model",related_name="50293082")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class DescriptionType1_model(models.Model):
    localizedString = models.ForeignKey("localizedString_model",related_name="56739448")
    valueOf_x = models.ForeignKey("localizedString_model",related_name="85416464")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class DescriptionType14_model(models.Model):
    localizedString = models.ForeignKey("localizedString_model",related_name="4014086")
    valueOf_x = models.ForeignKey("localizedString_model",related_name="10802240")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class DescriptionType15_model(models.Model):
    localizedString = models.ForeignKey("localizedString_model",related_name="63939589")
    valueOf_x = models.ForeignKey("localizedString_model",related_name="1311101")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class DescriptionType2_model(models.Model):
    localizedString = models.ForeignKey("localizedString_model",related_name="72018445")
    valueOf_x = models.ForeignKey("localizedString_model",related_name="10181425")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class DescriptionType5_model(models.Model):
    localizedString = models.ForeignKey("localizedString_model",related_name="48294500")
    valueOf_x = models.ForeignKey("localizedString_model",related_name="25435540")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class DescriptionType6_model(models.Model):
    localizedString = models.ForeignKey("localizedString_model",related_name="67669742")
    valueOf_x = models.ForeignKey("localizedString_model",related_name="89678213")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class DescriptionType7_model(models.Model):
    localizedString = models.ForeignKey("localizedString_model",related_name="75989568")
    valueOf_x = models.ForeignKey("localizedString_model",related_name="72029223")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class DescriptionType9_model(models.Model):
    localizedString = models.ForeignKey("localizedString_model",related_name="90762299")
    valueOf_x = models.ForeignKey("localizedString_model",related_name="92861057")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class DocumentDistributionType_model(models.Model):
    localizedString = models.ForeignKey("localizedString_model",related_name="37766298")
    valueOf_x = models.ForeignKey("localizedString_model",related_name="89975589")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class DocumentNotesType_model(models.Model):
    Note = models.ForeignKey("NoteType_model",related_name="77887992")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class DocumentPublisherType_model(models.Model):
    VendorID = models.CharField(max_length=1000, blank=True)
    Type = models.CharField(max_length=1000, blank=True)
    ContactDetails = models.ForeignKey("ContactDetailsType_model",related_name="32425456")
    IssuingAuthority = models.ForeignKey("IssuingAuthorityType_model",related_name="19423114")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class DocumentReferencesType_model(models.Model):
    Reference = models.ForeignKey("ReferenceType_model",related_name="99555286")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class DocumentTitleType_model(models.Model):
    localizedNormalizedString = models.ForeignKey("localizedNormalizedString_model",related_name="16129639")
    valueOf_x = models.ForeignKey("localizedNormalizedString_model",related_name="70803439")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class DocumentTrackingType_model(models.Model):
    Identification = models.ForeignKey("IdentificationType_model",related_name="50151905")
    Status = models.CharField(max_length=1000, blank=True)
    Version = models.CharField(max_length=1000, blank=True)
    RevisionHistory = models.ForeignKey("RevisionHistoryType_model",related_name="93630080")
    InitialReleaseDate = models.DateTimeField(blank=True)
    CurrentReleaseDate = models.DateTimeField(blank=True)
    Generator = models.ForeignKey("GeneratorType_model",related_name="71632325")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class DocumentTypeType_model(models.Model):
    localizedNormalizedString = models.ForeignKey("localizedNormalizedString_model",related_name="10519035")
    valueOf_x = models.ForeignKey("localizedNormalizedString_model",related_name="20920472")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class EngineType_model(models.Model):
    localizedString = models.ForeignKey("localizedString_model",related_name="55939654")
    valueOf_x = models.ForeignKey("localizedString_model",related_name="70543210")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class EntitlementType_model(models.Model):
    localizedString = models.ForeignKey("localizedString_model",related_name="7823366")
    valueOf_x = models.ForeignKey("localizedString_model",related_name="51052982")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class FactRefType_model(models.Model):
    name = models.CharField(max_length=1000, blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )

class FullProductName_model(models.Model):
    CPE = models.CharField(max_length=1000, blank=True)
    ProductID = models.CharField(max_length=1000, blank=True)
    valueOf_x = models.CharField(max_length=1000, blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )

class GeneratorType_model(models.Model):
    Engine = models.ForeignKey("EngineType_model",related_name="19619745")
    Date = models.DateTimeField(blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )

class GroupType_model(models.Model):
    GroupID = models.CharField(max_length=1000, blank=True)
    Description = models.ForeignKey("DescriptionType15_model",related_name="27421079")
    ProductID = models.CharField(max_length=1000, blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )

class IDType_model(models.Model):
    localizedString = models.ForeignKey("localizedString_model",related_name="63860227")
    valueOf_x = models.ForeignKey("localizedString_model",related_name="44820788")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class IDType3_model(models.Model):
    SystemName = models.CharField(max_length=1000, blank=True)
    valueOf_x = models.CharField(max_length=1000, blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )

class IdentificationType_model(models.Model):
    row = models.AutoField(primary_key=True)
    ID = models.ForeignKey("IDType_model",related_name="3987182")
    Alias = models.ForeignKey("AliasType_model",related_name="46725133")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class InvolvementType_model(models.Model):
    Status = models.CharField(max_length=1000, blank=True)
    Party = models.CharField(max_length=1000, blank=True)
    Description = models.ForeignKey("DescriptionType5_model",related_name="7775653")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class InvolvementsType_model(models.Model):
    Involvement = models.ForeignKey("InvolvementType_model",related_name="3810037")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class IssuingAuthorityType_model(models.Model):
    localizedString = models.ForeignKey("localizedString_model",related_name="16004445")
    valueOf_x = models.ForeignKey("localizedString_model",related_name="39783196")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class LogicalTestType_model(models.Model):
    operator = models.CharField(max_length=1000, blank=True)
    negate = models.BooleanField(blank=True)
    logical_test = models.ForeignKey("LogicalTestType_model",related_name="68889770")
    fact_ref = models.ForeignKey("fact_ref_model",related_name="53471155")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class NameType_model(models.Model):
    localizedString = models.ForeignKey("localizedString_model",related_name="68691984")
    valueOf_x = models.ForeignKey("localizedString_model",related_name="27245719")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class NameType12_model(models.Model):
    localizedString = models.ForeignKey("localizedString_model",related_name="46593257")
    valueOf_x = models.ForeignKey("localizedString_model",related_name="27655527")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class NoteType_model(models.Model):
    localizedString = models.ForeignKey("localizedString_model",related_name="45008596")
    Ordinal = models.IntegerField(blank=True)
    Audience = models.CharField(max_length=1000, blank=True)
    Type = models.CharField(max_length=1000, blank=True)
    Title = models.CharField(max_length=1000, blank=True)
    valueOf_x = models.ForeignKey("localizedString_model",related_name="93506918")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class NoteType4_model(models.Model):
    localizedString = models.ForeignKey("localizedString_model",related_name="8693180")
    Ordinal = models.IntegerField(blank=True)
    Audience = models.CharField(max_length=1000, blank=True)
    Type = models.CharField(max_length=1000, blank=True)
    Title = models.CharField(max_length=1000, blank=True)
    valueOf_x = models.ForeignKey("localizedString_model",related_name="45388885")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class NotesType_model(models.Model):
    Note = models.ForeignKey("NoteType4_model",related_name="94562533")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class OrganizationType_model(models.Model):
    localizedString = models.ForeignKey("localizedString_model",related_name="85571945")
    valueOf_x = models.ForeignKey("localizedString_model",related_name="12097636")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class OrganizationType13_model(models.Model):
    localizedString = models.ForeignKey("localizedString_model",related_name="1416391")
    valueOf_x = models.ForeignKey("localizedString_model",related_name="23451486")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class PlatformBaseType_model(models.Model):
    title = models.ForeignKey("title_model",related_name="86631324")
    remark = models.ForeignKey("TextType_model",related_name="43739039")
    logical_test = models.ForeignKey("logical_test_model",related_name="76954797")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class PlatformType_model(models.Model):
    PlatformBaseType = models.ForeignKey("PlatformBaseType_model",related_name="87400274")
    idx = models.CharField(max_length=1000, blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )

class ProductGroupsType_model(models.Model):
    Group = models.ForeignKey("GroupType_model",related_name="37693356")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class ProductStatusesType_model(models.Model):
    Status = models.ForeignKey("StatusType_model",related_name="94432805")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class ProductTree_model(models.Model):
    Branch = models.ForeignKey("BranchType_model",related_name="79849269")
    FullProductName = models.ForeignKey("FullProductName_model",related_name="83863355")
    Relationship = models.ForeignKey("RelationshipType_model",related_name="94665596")
    ProductGroups = models.ForeignKey("ProductGroupsType_model",related_name="58605186")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class ReferenceType_model(models.Model):
    Type = models.CharField(max_length=1000, blank=True)
    URL = models.CharField(max_length=1000, blank=True)
    Description = models.ForeignKey("DescriptionType1_model",related_name="59916287")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class ReferenceType8_model(models.Model):
    Type = models.CharField(max_length=1000, blank=True)
    URL = models.CharField(max_length=1000, blank=True)
    Description = models.ForeignKey("DescriptionType9_model",related_name="31934733")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class ReferencesType_model(models.Model):
    Reference = models.ForeignKey("ReferenceType8_model",related_name="42116158")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class RelationshipType_model(models.Model):
    RelationType = models.CharField(max_length=1000, blank=True)
    RelatesToProductReference = models.CharField(max_length=1000, blank=True)
    ProductReference = models.CharField(max_length=1000, blank=True)
    FullProductName = models.ForeignKey("FullProductName_model",related_name="90410658")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class RemediationType_model(models.Model):
    Date = models.DateTimeField(blank=True)
    Type = models.CharField(max_length=1000, blank=True)
    Description = models.ForeignKey("DescriptionType7_model",related_name="15846199")
    Entitlement = models.ForeignKey("EntitlementType_model",related_name="83515942")
    URL = models.CharField(max_length=1000, blank=True)
    ProductID = models.CharField(max_length=1000, blank=True)
    GroupID = models.CharField(max_length=1000, blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )

class RemediationsType_model(models.Model):
    Remediation = models.ForeignKey("RemediationType_model",related_name="73194155")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class RevisionHistoryType_model(models.Model):
    Revision = models.ForeignKey("RevisionType_model",related_name="49183724")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class RevisionType_model(models.Model):
    Number = models.CharField(max_length=1000, blank=True)
    Date = models.DateTimeField(blank=True)
    Description = models.ForeignKey("DescriptionType_model",related_name="21212948")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class ScoreSetType_model(models.Model):
    BaseScore = models.FloatField(blank=True)
    TemporalScore = models.FloatField(blank=True)
    EnvironmentalScore = models.FloatField(blank=True)
    Vector = models.CharField(max_length=1000, blank=True)
    ProductID = models.CharField(max_length=1000, blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )

class SimpleLiteral_model(models.Model):
    lang = models.CharField(max_length=1000, blank=True)
    valueOf_x = models.CharField(max_length=1000, blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )

class StatusType_model(models.Model):
    Type = models.CharField(max_length=1000, blank=True)
    ProductID = models.CharField(max_length=1000, blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )

class TextType_model(models.Model):
    lang = models.CharField(max_length=1000, blank=True)
    valueOf_x = models.CharField(max_length=1000, blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )

class ThreatType_model(models.Model):
    Date = models.DateTimeField(blank=True)
    Type = models.CharField(max_length=1000, blank=True)
    Description = models.ForeignKey("DescriptionType6_model",related_name="11975247")
    ProductID = models.CharField(max_length=1000, blank=True)
    GroupID = models.CharField(max_length=1000, blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )

class ThreatsType_model(models.Model):
    Threat = models.ForeignKey("ThreatType_model",related_name="4836305")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class TitleType_model(models.Model):
    localizedString = models.ForeignKey("localizedString_model",related_name="42602604")
    valueOf_x = models.ForeignKey("localizedString_model",related_name="32578194")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class Vulnerability_model(models.Model):
    row = models.AutoField(primary_key=True)
    Ordinal = models.IntegerField(blank=True)
    Title = models.ForeignKey("TitleType_model",related_name="10466186")
    ID = models.ForeignKey("IDType3_model",related_name="42891643")
    Notes = models.ForeignKey("NotesType_model",related_name="62314757")
    DiscoveryDate = models.DateTimeField(blank=True)
    ReleaseDate = models.DateTimeField(blank=True)
    Involvements = models.ForeignKey("InvolvementsType_model",related_name="61870044")
    CVE = models.CharField(max_length=1000, blank=True)
    CWE = models.ForeignKey("CWEType_model",related_name="77999684")
    ProductStatuses = models.ForeignKey("ProductStatusesType_model",related_name="48803124")
    Threats = models.ForeignKey("ThreatsType_model",related_name="98955030")
    CVSSScoreSets = models.ForeignKey("CVSSScoreSetsType_model",related_name="92585110")
    Remediations = models.ForeignKey("RemediationsType_model",related_name="64217436")
    References = models.ForeignKey("ReferencesType_model",related_name="74736471")
    Acknowledgments = models.ForeignKey("AcknowledgmentsType10_model",related_name="95656944")
    def __unicode__(self):
        return "id: %s" % (self.row, )

class accessComplexityType_model(models.Model):
    approximated = models.BooleanField(blank=True)
    valueOf_x = models.CharField(max_length=1000, blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )

class accessVectorType_model(models.Model):
    approximated = models.BooleanField(blank=True)
    valueOf_x = models.CharField(max_length=1000, blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )

class assessmentMethodType_model(models.Model):
    assessment_check = models.ForeignKey("checkReferenceType_model",related_name="51596598")
    assessment_engine = models.CharField(max_length=1000, blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )

class authenticationType_model(models.Model):
    approximated = models.BooleanField(blank=True)
    valueOf_x = models.CharField(max_length=1000, blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )

class baseMetricsType_model(models.Model):
    metricsType = models.ForeignKey("metricsType_model",related_name="22139808")
    score = models.FloatField(blank=True)
    exploit_subscore = models.FloatField(blank=True)
    impact_subscore = models.FloatField(blank=True)
    access_vector = models.ForeignKey("accessVectorType_model",related_name="29963174")
    access_complexity = models.ForeignKey("accessComplexityType_model",related_name="81016157")
    authentication = models.ForeignKey("authenticationType_model",related_name="635902")
    confidentiality_impact = models.ForeignKey("ciaType_model",related_name="28056982")
    integrity_impact = models.ForeignKey("ciaType_model",related_name="91917209")
    availability_impact = models.ForeignKey("ciaType_model",related_name="36737998")
    source = models.ForeignKey("source_model",related_name="40725180")
    generated_on_datetime = models.CharField(max_length=1000, blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )

class checkReferenceType_model(models.Model):
    checkSearchType = models.ForeignKey("checkSearchType_model",related_name="87450313")
    href = models.CharField(max_length=1000, blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )

class checkSearchType_model(models.Model):
    system = models.CharField(max_length=1000, blank=True)
    name = models.CharField(max_length=1000, blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )

class ciaRequirementType_model(models.Model):
    approximated = models.BooleanField(blank=True)
    valueOf_x = models.CharField(max_length=1000, blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )

class ciaType_model(models.Model):
    approximated = models.BooleanField(blank=True)
    valueOf_x = models.CharField(max_length=1000, blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )

class collateralDamagePotentialType_model(models.Model):
    approximated = models.BooleanField(blank=True)
    valueOf_x = models.CharField(max_length=1000, blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )

class confidenceType_model(models.Model):
    approximated = models.BooleanField(blank=True)
    valueOf_x = models.CharField(max_length=1000, blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )

class contributor_model(models.Model):
    def __unicode__(self):
        return "id: %s" % (self.id, )

class controlMappingType_model(models.Model):
    source = models.CharField(max_length=1000, blank=True)
    system_id = models.CharField(max_length=1000, blank=True)
    last_modified = models.DateTimeField(blank=True)
    mapping = models.ForeignKey("mappingInstanceType_model",related_name="95225967")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class controlMappingsType_model(models.Model):
    control_mapping = models.ForeignKey("controlMappingType_model",related_name="99036004")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class coverage_model(models.Model):
    def __unicode__(self):
        return "id: %s" % (self.id, )

class creator_model(models.Model):
    def __unicode__(self):
        return "id: %s" % (self.id, )

class cvrfdoc_model(models.Model):
    DocumentTitle = models.ForeignKey("DocumentTitleType_model",related_name="15040449")
    DocumentType = models.ForeignKey("DocumentTypeType_model",related_name="54823646")
    DocumentPublisher = models.ForeignKey("DocumentPublisherType_model",related_name="23713416")
    DocumentTracking = models.ForeignKey("DocumentTrackingType_model",related_name="77184572")
    DocumentNotes = models.ForeignKey("DocumentNotesType_model",related_name="45876557")
    DocumentDistribution = models.ForeignKey("DocumentDistributionType_model",related_name="73122276")
    AggregateSeverity = models.ForeignKey("AggregateSeverityType_model",related_name="19715534")
    DocumentReferences = models.ForeignKey("DocumentReferencesType_model",related_name="47371062")
    Acknowledgments = models.ForeignKey("AcknowledgmentsType_model",related_name="92379658")
    ProductTree = models.ForeignKey("ProductTree_model",related_name="85886576")
    Vulnerability = models.ForeignKey("Vulnerability_model",related_name="94579757")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class cvssImpactBaseType_model(models.Model):
    base_metrics = models.ForeignKey("baseMetricsType_model",related_name="39968643")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class cvssImpactEnvironmentalType_model(models.Model):
    cvssImpactTemporalType = models.ForeignKey("cvssImpactTemporalType_model",related_name="34531176")
    environmental_metrics = models.ForeignKey("environmentalMetricsType_model",related_name="20103121")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class cvssImpactTemporalType_model(models.Model):
    cvssImpactBaseType = models.ForeignKey("cvssImpactBaseType_model",related_name="32200757")
    temporal_metrics = models.ForeignKey("temporalMetricsType_model",related_name="33617149")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class cvssImpactType_model(models.Model):
    cvssType = models.ForeignKey("cvssType_model",related_name="57068635")
    base_metrics = models.ForeignKey("baseMetricsType_model",related_name="43699960")
    environmental_metrics = models.ForeignKey("environmentalMetricsType_model",related_name="87438999")
    temporal_metrics = models.ForeignKey("temporalMetricsType_model",related_name="64393797")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class cvssType_model(models.Model):
    base_metrics = models.ForeignKey("baseMetricsType_model",related_name="51794071")
    environmental_metrics = models.ForeignKey("environmentalMetricsType_model",related_name="89487428")
    temporal_metrics = models.ForeignKey("temporalMetricsType_model",related_name="83920233")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class date_model(models.Model):
    def __unicode__(self):
        return "id: %s" % (self.id, )

class description_model(models.Model):
    def __unicode__(self):
        return "id: %s" % (self.id, )

class elementContainer_model(models.Model):
    any = models.ForeignKey("SimpleLiteral_model",related_name="63769503")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class environmentalMetricsType_model(models.Model):
    metricsType = models.ForeignKey("metricsType_model",related_name="47632858")
    score = models.FloatField(blank=True)
    collateral_damage_potential = models.ForeignKey("collateralDamagePotentialType_model",related_name="42298455")
    target_distribution = models.ForeignKey("targetDistributionType_model",related_name="903641")
    confidentiality_requirement = models.ForeignKey("ciaRequirementType_model",related_name="60819929")
    integrity_requirement = models.ForeignKey("ciaRequirementType_model",related_name="92754663")
    availability_requirement = models.ForeignKey("ciaRequirementType_model",related_name="34870821")
    source = models.ForeignKey("source_model",related_name="25281480")
    generated_on_datetime = models.CharField(max_length=1000, blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )

class exploitabilityType_model(models.Model):
    approximated = models.BooleanField(blank=True)
    valueOf_x = models.CharField(max_length=1000, blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )

class fact_ref_model(models.Model):
    def __unicode__(self):
        return "id: %s" % (self.id, )

class format_model(models.Model):
    def __unicode__(self):
        return "id: %s" % (self.id, )

class identifier_model(models.Model):
    def __unicode__(self):
        return "id: %s" % (self.id, )

class identifyableAssessmentMethodType_model(models.Model):
    assessmentMethodType = models.ForeignKey("assessmentMethodType_model",related_name="41127680")
    idx = models.IntegerField(blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )

class language_model(models.Model):
    def __unicode__(self):
        return "id: %s" % (self.id, )

class localizedNormalizedString_model(models.Model):
    lang = models.CharField(max_length=1000, blank=True)
    valueOf_x = models.CharField(max_length=1000, blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )

class localizedString_model(models.Model):
    lang = models.CharField(max_length=1000, blank=True)
    valueOf_x = models.CharField(max_length=1000, blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )

class logical_test_model(models.Model):
    def __unicode__(self):
        return "id: %s" % (self.id, )

class mappingInstanceType_model(models.Model):
    published = models.DateTimeField(blank=True)
    valueOf_x = models.CharField(max_length=1000, blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )

class metricsType_model(models.Model):
    upgraded_from_version = models.FloatField(blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )

class platformSpecificationType_model(models.Model):
    platform = models.ForeignKey("PlatformType_model",related_name="24643622")
    def __unicode__(self):
        return "id: %s" % (self.id, )

class publisher_model(models.Model):
    def __unicode__(self):
        return "id: %s" % (self.id, )

class relation_model(models.Model):
    def __unicode__(self):
        return "id: %s" % (self.id, )

class remediationLevelType_model(models.Model):
    approximated = models.BooleanField(blank=True)
    valueOf_x = models.CharField(max_length=1000, blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )

class rights_model(models.Model):
    def __unicode__(self):
        return "id: %s" % (self.id, )

class searchableCpeReferencesType_model(models.Model):
    cpe_name = models.CharField(max_length=1000, blank=True)
    cpe_searchable_name = models.CharField(max_length=1000, blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )

class source_model(models.Model):
    def __unicode__(self):
        return "id: %s" % (self.id, )

class subject_model(models.Model):
    def __unicode__(self):
        return "id: %s" % (self.id, )

class targetDistributionType_model(models.Model):
    approximated = models.BooleanField(blank=True)
    valueOf_x = models.CharField(max_length=1000, blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )

class temporalMetricsType_model(models.Model):
    metricsType = models.ForeignKey("metricsType_model",related_name="97837778")
    score = models.FloatField(blank=True)
    temporal_multiplier = models.CharField(max_length=1000, blank=True)
    exploitability = models.ForeignKey("exploitabilityType_model",related_name="47021503")
    remediation_level = models.ForeignKey("remediationLevelType_model",related_name="68234451")
    report_confidence = models.ForeignKey("confidenceType_model",related_name="80209699")
    source = models.ForeignKey("source_model",related_name="85046005")
    generated_on_datetime = models.CharField(max_length=1000, blank=True)
    def __unicode__(self):
        return "id: %s" % (self.id, )

class title_model(models.Model):
    def __unicode__(self):
        return "id: %s" % (self.id, )

class type__model(models.Model):
    def __unicode__(self):
        return "id: %s" % (self.id, )
