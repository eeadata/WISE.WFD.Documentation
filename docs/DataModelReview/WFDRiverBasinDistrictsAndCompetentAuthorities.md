# WFD - River Basin Districts And Competent Authorities 4th cycle

Water Framework Directive – Electronic reporting data model review 
River Basin Districts & Competent Authorities 

**PROPOSAL - Version Version 2026.02.13** {download}`PDF <pdf/WFD_4rd_cycle_RiverBasinDistrictsAndCompetentAuthorities_v20260213.pdf>`


**WFD Data Model and Dataflow**


```{mermaid}
%%{init: {'theme': 'neutral'}}%%

flowchart 

%% 
title@{ shape: braces, label: "WISE Dataflow XPTO \n Status update: 2026-03-26" }

%% Defining the nodes and overall flow
        
initial([start])
final([end])

%% DATAFLOW for DATA COLLECTION

subgraph P4["DATA COLLECTION - Opening the dataflow"]
    direction LR
    
    %% activities
    P41["Update and publish documentation \n (release v1.0)"]
    P42["Create collections"]
    P43["Grant permissions \n (by data stewards)"]
    P44["Open data collection"]
    P45["Provide user support \n (by data stewards)"]
    P46["Provide final feedback \n (by data stewards)"]
    P47["Close data collection"]

    %% workflow
    P41 --> P42 --> P43 --> P44 
    P44 --- P45 --- P47
    P44 --- P46 --- P47

end

%% EXTERNAL TESTING

subgraph P3["EXTERNAL TESTING - Opening the dataflow for beta testing by Member States"]
    direction LR

    %% activities
    P31["Update and publish documentation \n (release v0.2)"]
    P32["Create collections"]
    P33["Grant permissions \n (by data stewards)"]
    P34["Open for testing"]
    P35["Provide user support \n (also by data stewards)"]
    
    %% workflow
    P31 --> P32 --> P33 --> P34 --> P35
end

%% INTERNAL TESTING
    
subgraph P2["INTERNAL TESTING - Opening the dataflow for alpha testing by Data Stewards and Data Steward Support roles"]
    direction LR

    %% activities
    P21["Update and publish documentation \n (release v0.1)"]
    P22["Create collections"]
    P23["Grant permissions"]
    P24["Open for testing"]

    %% workflow
    P21 --> P22 --> P23 --> P24
end

%% design and build

subgraph P1["Design and build the MASTER dataflow"]
    direction TB

    subgraph QC["Quality control"]
        direction TB

        %% activities
        QC1["Define and document"]
        QC2["Implement in \n SQL Server database"]
        QC3["Test in SQL Server"]
        QC4["Implement in RN3"]
        QC5["Test in RN3"]

        %% workflow
        QC1 --- QC2 --- QC3 --- QC4 --- QC5
    end

    subgraph TF["Template FILE(S)"]
        direction TB

        %% activities
        TF1["Define and document"]
        TF2["Generate TEMPLATE file(s)"]
        TF3["Create TEST file(s)"]   
        TF4["Test the RN3 import \n into the reporting dataset(s)"]
        TF5["Create PREFILLED file(s)"]   

        %% workflow 
        TF1 --- TF2 --- TF3 --- TF4 
        TF3 --- TF5 --- TF4
    end

    subgraph RefD["Reference DATASET"]
        direction TB

        %% activities
        RefD1["Define and document"]
        RefD2["Generate in \n SQL Server database"]
        RefD3["Implement in RN3"]
        RefD4["Create or configure \n RN3 import process"]
        RefD5["Populate in RN3"]
        RefD6["Create or configure automation \n (if required & possible)"]

        %% workflow
        RefD1 --- RefD2 --- RefD3 --- RefD4 --- RefD5
        RefD3 --- RefD6 --- RefD5
    end     
    
    subgraph CL["Codelist DATASET"]
        direction TB

        %% activities
        CL1["Define and document"]
        CL2["Generate in \n SQL Server database"]
        CL3["Implement in RN3"]
        CL4["Create or configure \n RN3 import process"]
        CL5["Populate in RN3"]

        %% workflow
        CL1 --- CL2 --- CL3 --- CL4 --- CL5 
    end

    subgraph RepD["Reporting DATASET(S)"]
        direction TB

        %% activities
        RepD1["Define and document"]
        RepD2["Generate in \n SQL Server database"]
        RepD3["Implement in RN3"]
        RepD4["Create or configure \n RN3 import process"]
        RepD5["Configure the metadata and data harvesting process"]

        %% workflow
        RepD1 --- RepD2 --- RepD3 --- RepD4 --- RepD5
    end

    subgraph MD["Modelling and documentation"]
        direction TB

        %% activities
        MD1["Define conceptual model"]
        MD2["Describe datasets, tables, columns and domains"]
        MD3["Create Enterprise Architect project"]
        MD4["Generate DRAFT reporting guidance"]
        MD5["Generate WISE documentation"]

        %% workflow
        MD1 --- MD2 --- MD3 --- MD4 --- MD5
    end
end

%% Main workflow
    
initial-->P1

P1 ==>|clone MASTER dataflow| P2 
P1 ==>|clone MASTER dataflow| P3
P1 ==>|clone MASTER dataflow| P4
P2 -->|revise and correct| P1
P3 -->|revise and correct| P1
P4 <-->|correct or optimise \n Quality Control| P1

P2 .->|after approval \n by data steward \n and data custodian| P3
P3 .->|after testing period| P4

P4-->final

%% JUST VISUALISATION 

final ~~~ Legend

subgraph Legend
    direction LR
    planned
    inProgress:::inProgress
    implemented:::implemented
    validated:::validated
    forFixing:::forFixing

    planned ~~~ forFixing ~~~ inProgress ~~~ implemented ~~~ validated
end

%% Define status styles

classDef inProgress stroke-width:3px, fill:transparent

classDef forFixing stroke-width:3px, stroke:red, fill:transparent
classDef implemented stroke-width:3px, stroke:orange, fill:transparent
classDef validated stroke-width:3px, stroke:green, fill:transparent
classDef initial fill:#000,stroke:#000,stroke-width:2px
classDef final fill:#000,stroke:#aaa,stroke-width:4px

%% STATUS UPDATES
%% 2026-03-26
class P1 inProgress
class MD inProgress

class MD1 validated;
class MD2 inProgress;
class MD3 implemented;
```
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
%%{init: {'theme': 'default'}}%%
flowchart LR

    subgraph A["a) Documents"]
        direction TB
        dcMetadata["dcMetadata<br/>―――――――――――<br/>+ title: nvarchar(4000)<br/>+ creatorOrganisationName: nvarchar(4000)<br/>+ creatorElectronicMailAddress: Email - varchar(250)<br/>+ description: nvarchar(4000) [0..1]<br/>+ created: Date [0..1]<br/>+ language: Language [1..n]<br/>+ license: URL - varchar(2100)<br/>+ rights: nvarchar(4000) [0..1]<br/>+ rightsHolder: nvarchar(4000) [0..1]<br/>+ licenseDocument: documentCode [0..*]<br/>+ metadataDocument: documentCode [0..*]<br/>+ updateCompetentAuthorities: YesNo<br/>+ updateSpatialData: YesNo"]
        Document["Document<br/>―――――――――――<br/>+ documentCode: WISEIdentifier - varchar(42)<br/>+ documentName: nvarchar(250)<br/>+ hyperlink: URL - varchar(2100) [0..1]<br/>+ documentFile: Attachment [0..1]"]
        dcMetadata -->|"0..*"| Document
    end

    subgraph B["b) Descriptive data"]
        direction TB
        CompetentAuthority["CompetentAuthority<br/>―――――――――――<br/>+ euCACode: WISEIdentifier - varchar(42)<br/>+ competentAuthorityName: varchar(100)<br/>+ competentAuthorityNameNL: nvarchar(100)<br/>+ competentAuthorityNameNLLanguage: Language<br/>+ acronym: nvarchar(100) [0..1]<br/>+ street: nvarchar(100)<br/>+ city: nvarchar(100)<br/>+ country: nvarchar(100)<br/>+ postCode: nvarchar(50) [0..1]<br/>+ url: URL - varchar(2100)"]
        RBDCA["RiverBasinDistrictCompetentAuthority<br/>―――――――――――<br/>+ euRBDCode: WISEIdentifier - varchar(42)<br/>+ euCACode: WISEIdentifier - varchar(42)<br/>+ roleCode: Role [1..*]"]
        CompetentAuthority -->|"1..*"| RBDCA
    end

    subgraph C["c) Spatial data"]
        direction TB
        RiverBasinDistrict["RiverBasinDistrict<br/>―――――――――――<br/>+ geometry_polygon: geometry_multipolygon<br/>+ inspireIdLocalId: String<br/>+ inspireIdNamespace: String<br/>+ inspireIdVersionId: String [0..1]<br/>+ thematicIdIdentifier: WISEIdentifier<br/>+ thematicIdIdentifierScheme: IdentifierScheme<br/>+ beginLifespanVersion: Date<br/>+ endLifespanVersion: Date [0..1]<br/>+ predecessorsIdentifier: comma-separated list of WISEIdentifier [0..1]<br/>+ predecessorsIdentifierScheme: IdentifierScheme [0..1]<br/>- successorsIdentifier: comma-separated list of WISEIdentifier [0..1]<br/>- successorsIdentifierScheme: IdentifierScheme [0..1]<br/>+ wiseEvolutionType: WiseEvolutionType<br/>+ nameTextInternational: String<br/>+ nameText: String<br/>+ nameLanguage: Language<br/>+ designationPeriodBegin: Date<br/>+ designationPeriodEnd: Date [0..1]<br/>+ zoneType: ZoneType<br/>+ specialisedZoneType: SpecialisedZoneType<br/>+ legalBasisName: String [0..1]<br/>+ legalBasisLink: url [0..1]<br/>+ legalBasisLevel: LegislationLevelValue [0..1]<br/>+ link: url [0..1]"]
    end

    A ~~~ B ~~~ C
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
