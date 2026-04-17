# WFD - River Basin Districts And Competent Authorities 4th cycle

Water Framework Directive – Electronic reporting data model review 
River Basin Districts & Competent Authorities 

**PROPOSAL - Version Version 2026.02.13** {download}`PDF <pdf/WFD_4rd_cycle_RiverBasinDistrictsAndCompetentAuthorities_v20260213.pdf>`

## Purpose and overview
The document revises the River Basin Districts, Subunits and Competent
Authorities classes used in the 3ʳᵈ cycle of reporting of the
Water Framework Directive River Basin Management Plans ({ref}`Figure 1 <Figure 1>`), as
well as the associated spatial data in the RiverBasinDistrict dataset
and SubUnit dataset ({ref}`Figure 2 <Figure 2>`).

*Figure 1. Class diagram for River Basin Districts, Subunits and Competent
Authorities schema - 3ʳᵈ cycle.*

(Figure 1)=
```{mermaid}
%%{init: {'theme': 'default'}}%%
classDiagram
direction TB

    class CompetentAuthority["«XSDcomplexType»
    CompetentAuthority"] {
        «XSDelement»
        +euCACode: FeatureUniqueEUCodeType
        +competentAuthorityName: String250Type
        +competentAuthorityNameNL: String250Type
        +competentAuthorityNameNLLanguage: LanguageCode_Enum
        +linkToCompetentAuthority: String1000Type
        +acronym: String100Type [0..1]
        +street: String100Type [0..1]
        +city: String100Type [0..1]
        +cityNL: String100Type [0..1]
        +country: String100Type [0..1]
        +postcode: String100Type [0..1]
        +mainRole: Roles_Enum [1..*]
        +otherRole: Roles_Enum [0..*]
    }

    class RBD["«XSDcomplexType»
    RBD"] {
        «XSDelement»
        +euRBDCode: FeatureUniqueEUCodeType
        +euSubUnitCode: FeatureUniqueEUCodeType [0..*]
        +internationalRBD: YesNoCode_Enum
        +internationalRBDName: String250Type [0..1]
        +primeCompetentAuthority: FeatureUniqueEUCodeType [1..*]
        +otherCompetentAuthority: FeatureUniqueEUCodeType [0..*]
        +subUnitsDefined: YesNoCode_Enum
    }

    class dcMetadata["WFDCommon_2022::dcMetadata"] {
        «XSDelement»
        +created: WiseDateTime [0..1]
        +creatorElectronicMailAddress: EmailType
        +creatorOrganisationName: String4000Type
        +description: String4000Type [0..1]
        +language: LanguageCode_Enum
        +license: URLType
        +title: String4000Type [0..1]
        +rights: String4000Type [0..1]
        +rightsHolder: String4000Type [0..1]
    }

    class RBDSUCA["«XSDcomplexType»
    RBDSUCA"] {
        «XSDelement»
        +countryCode: CountryCode_Enum
    }

  
    class RBDSUCATop["«XSDtopLev...
    RBDSUCA"] {
    }

    CompetentAuthority "1..*" <-- RBDSUCA : +CompetentAuthority
    RBD "1..*" <-- RBDSUCA : +RBD
    RBDSUCA "1..1" --> dcMetadata
    RBDSUCATop --|> RBDSUCA
    
```
Source: [https://cdr.eionet.europa.eu/help/WFD/WFD_715_2022/UML%20Data%20specification/WFD2022.EAP](https://cdr.eionet.europa.eu/help/WFD/WFD_715_2022/UML%20Data%20specification/WFD2022.EAP)


*Figure 2. Partial class diagram for RiverBasinDistrict and Subunit classes.*

(Figure 2)=
```{mermaid}
%%{init: {'theme': 'default'}}%%
classDiagram
direction TB

    class RiverBasinDistrict["«FeatureType»
    RiverBasinDistrict"] {
        +geometry: GM_MultiSurface
        +inspireIdLocalId: String254LeadingLetterOrNum
        +inspireIdNamespace: String254LeadingLetterOrNum
        +inspireIdVersionId: String25Type [0..1]
        +thematicIdIdentifier: FeatureUniqueEUCodeType
        +thematicIdIdentifierScheme: IdentifierScheme
        +beginLifespanVersion: WiseDateTimeType [0..1]
        +endLifespanVersion: WiseDateTimeType [0..1]
        +predecessorsIdentifier: String254LeadingLetterOrNum [0..1]
        +predecessorsIdentifierScheme: IdentifierScheme [0..1]
        +successorsIdentifier: String254LeadingLetterOrNum [0..1]
        +successorsIdentifierScheme: IdentifierScheme [0..1]
        +wiseEvolutionType: WiseEvolutionTypeValue
        +nameTextInternational: String254Latin
        +nameText: String254Type
        +nameLanguage: WiseLanguageCode_Enum
        +designationPeriodBegin: WiseDateTimeType
        +designationPeriodEnd: WiseDateTimeType [0..1]
        +zoneType: ZoneTypeCode
        +legalBasisName: String254LeadingLetterOrNum [0..1]
        +legalBasisLink: URLType [0..1]
        +legalBasisLevel: LegislationLevelValue [0..1]
        +relatedZoneTransboundaryIdentifier: String254LeadingLetterOrNum [0..1]
        +relatedZoneTransboundaryIdentifierScheme: IdentifierScheme [0..1]
        +sizeValue: PositiveDecimalType [0..1]
        +sizeUom: UomSize [0..1]
        +link: URLType [0..1]
    }

    class FeatureCollectionRBD["«FeatureType»
    FeatureCollection"] {
    }

    class SubUnit["«FeatureType»
    SubUnit"] {
        +geometry: GM_MultiSurface
        +inspireIdLocalId: String254LeadingLetterOrNum
        +inspireIdNamespace: String254LeadingLetterOrNum
        +inspireIdVersionId: String25Type [0..1]
        +thematicIdIdentifier: FeatureUniqueEUCodeType
        +thematicIdIdentifierScheme: IdentifierScheme
        +beginLifespanVersion: WiseDateTimeType [0..1]
        +endLifespanVersion: WiseDateTimeType [0..1]
        +predecessorsIdentifier: String254LeadingLetterOrNum [0..1]
        +predecessorsIdentifierScheme: IdentifierScheme [0..1]
        +successorsIdentifier: String254LeadingLetterOrNum [0..1]
        +successorsIdentifierScheme: IdentifierScheme [0..1]
        +wiseEvolutionType: WiseEvolutionTypeValue
        +nameTextInternational: String254Latin
        +nameText: String254Type
        +nameLanguage: WiseLanguageCode_Enum
        +designationPeriodBegin: WiseDateTimeType
        +designationPeriodEnd: WiseDateTimeType [0..1]
        +zoneType: ZoneTypeCode
        +specialisedZoneType: SpecialisedZoneTypeCode
        +legalBasisName: String254LeadingLetterOrNum [0..1]
        +legalBasisLink: URLType [0..1]
        +legalBasisLevel: LegislationLevelValue [0..1]
        +relatedZoneIdentifier: FeatureUniqueEUCodeType
        +relatedZoneIdentifierScheme: IdentifierScheme
        +relatedZoneTransboundaryIdentifier: String254LeadingLetterOrNum [0..1]
        +relatedZoneTransboundaryIdentifierScheme: IdentifierScheme [0..1]
        +sizeValue: PositiveDecimalType [0..1]
        +sizeUom: UomSize [0..1]
        +link: URLType [0..1]
    }

    class FeatureCollectionSU["«FeatureType»
    FeatureCollection"] {
    }

    RiverBasinDistrict "1..*" <-- FeatureCollectionRBD : +featureMember
    SubUnit "1..*" <-- FeatureCollectionSU : +featureMember
```

Source: [https://cdr.eionet.europa.eu/help/WFD/WFD_715_2022/UML%20Data%20specification/WFD2022.EAP ](https://cdr.eionet.europa.eu/help/WFD/WFD_715_2022/UML%20Data%20specification/WFD2022.EAP )

A proposal is presented for the electronic reporting in the 4ᵗʰ cycle (Figure 3).
The reporting of the units of management (i.e. the River Basin Districts) and of the competent authorities is combined into a single dataflow. The overall structure of the new **River Basin Districts and Competent Authorities** dataflow has been aligned with similar dataflows, e.g. under the Floods Directive [^floods-directive-footnote].

[^floods-directive-footnote]: See Floods Directive - Units of Management and Competent Authorities[2025] at https://reportnet.europa.eu/public/dataflow/1473

Reporting is only requested under the following conditions:

- If there are changes to the spatial delineation and/or the identifiers of one or more River Basin Districts (since the 3ʳᵈ cycle), the spatial dataset must be reported.

- If there are changes to the competent authorities or their roles, the descriptive data must be reported in accordance with Article 3(8) and 3(9) of the WFD.

Data providers can specify which datasets are being updated (spatial data, descriptive data, or both). Information about subunits is no longer requested. The reporting of metadata has also been simplified.

*Figure 3. River Basin Districts and Competent Authorities - 4ᵗʰ cycle*

(Figure 3)=
```{mermaid}
classDiagram
direction TB
namespace a. Documents {
class dcMetadata {
+ title: nvarchar(4000)
+ creatorOrganisationName: nvarchar(4000)
+ creatorElectronicMailAddress: Email - varchar(250)
+ description: nvarchar(4000) [0..1]
+ created: Date [0..1]
+ language: Language [1..n]
+ license: URL - varchar(2100)
+ rights: nvarchar(4000) [0..1]
+ rightsHolder: nvarchar(4000) [0..1]
+ licenseDocument: documentCode [0..*]
+ metadataDocument: documentCode [0..*]
+ updateCompetentAuthorities: YesNo
+ updateSpatialData: YesNo
}
class Document {
+ documentCode: WISEIdentifier - varchar(42)
+ documentName: nvarchar(250)
+ hyperlink: URL - varchar(2100) [0..1]
+ documentFile: Attachment [0..1]
}
}
namespace b.Descriptivedata {
class CompetentAuthority {
+ euCACode: WISEIdentifier - varchar(42)
+ competentAuthorityName: varchar(100)
+ competentAuthorityNameNL: nvarchar(100)
+ competentAuthorityNameNLLanguage: Language
+ acronym: nvarchar(100) [0..1]
+ street: nvarchar(100)
+ city: nvarchar(100)
+ country: nvarchar(100)
+ postCode: nvarchar(50) [0..1]
+ url: URL - varchar(2100)
}
class RiverBasinDistrictCompetentAuthority {
+ euRBDCode: WISEIdentifier - varchar(42)
+ euCACode: WISEIdentifier - varchar(42)
+ roleCode: Role [1..*]
}
}
namespace c.Spatialdata {
class RiverBasinDistrict {
+ geometry_polygon: geometry_multipolygon
+ inspireIdLocalId: String
+ inspireIdNamespace: String
+ inspireIdVersionId: String [0..1]
+ thematicIdIdentifier: WISEIdentifier
+ thematicIdIdentifierScheme: IdentifierScheme
+ beginLifespanVersion: Date
+ endLifespanVersion: Date [0..1]
+ predecessorsIdentifier: comma-separated list of WISEIdentifier [0..1]
+ predecessorsIdentifierScheme: IdentifierScheme [0..1]
+ successorsIdentifier: comma-separated list of WISEIdentifier [0..1]
+ successorsIdentifierScheme: IdentifierScheme [0..1]
+ wiseEvolutionType: WiseEvolutionType
+ nameTextInternational: String
+ nameText: String
+ nameLanguage: Language
+ designationPeriodBegin: Date
+ designationPeriodEnd: Date [0..1]
+ zoneType: ZoneType
+ specialisedZoneType: SpecialisedZoneType
+ legalBasisName: String [0..1]
+ legalBasisLink: url [0..1]
+ legalBasisLevel: LegislationLevelValue [0..1]
+ link: url [0..1]
}
}

dcMetadata --> "0..*" Document
CompetentAuthority --> "1..*" RiverBasinDistrictCompetentAuthority
```

## Documents dataset - 4ᵗʰ cycle

The Documents dataset ({ref}`Figure 3.a <Figure 3>`) follows the standard structure used in various WISE dataflows:

- The **dcMetadata** table is required and contains only one record per delivery (i.e. per country). It provides the basic Dublin Core metadata elements about the delivery.<br/>It also functions as a "manifest file" explaining if the delivery contains an update of the spatial data (updateSpatialData = 'Yes') and/or of the competent authorities (updateCompetentAuthorities= 'Yes'). If required by the data providers, and especially if spatial data is being reported, the licenseDocument and the metadataDocument attributes allow the provision of additional information.

- The structure of the **Document** table is standard in the WISE dataflows: it allows the upload of documents (for example, PDFs) or the provision of a link to a document stored in a publicly accessible national web site.


## Descriptive dataset - 4ᵗʰ cycle

The Descriptive dataset ({ref}`Figure 3.b <Figure 3>`) contains two tables:

- The **CompetentAuthority** table contains basic information about each Competent Authority.

- The **RiverBasinDistrictCompetentAuthority** table associates each Competent Authority with a River Basin District and specifies the role(s) of the competent authority in that specific RBD.


## Spatial dataset - 4ᵗʰ cycle

The Spatial dataset ({ref}`Figure 3.c <Figure 3>`) contains only the RiverBasinDistrict spatial table.
As stated before, Subunits are no longer requested in the 4ᵗʰ cycle of reporting.

The following changes have been made to the RiverBasinDistrict table (in comparison to version 7.06 used in the 3ʳᵈ cycle of reporting):

- Two attributes were removed, because they can be derived: sizeValue and sizeUom.

- Two attributes were removed, since they are not required at EU level: relatedTransboundaryIdentifier and relatedTransboundaryIdentifierScheme.

- The date values are now requested as simply as YYYY-MM-DD, because that is the format used by the data providers (beginLifespanVersion, endLifespanVersion, designationPeriodBegin, designationPeriodEnd).

- One attribute was moved from the descriptive data into the spatial data specialisedZoneType: {'internationalRiverBasinDistrict','nationalRiverBasinDistrict'}

- The attributes thematicIdIdentifierScheme and zoneType have been kept for clarity's sake, although all records in the national delivery will have the same fixed value.

- Likewise, the attributes successorsIdentifier and successorsIdentifierScheme have been kept for clarity's sake although their value will always be NULL - the appropriate value will be derived and included in the published WISE datasets that refer to the previous reporting cycles.
