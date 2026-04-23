# WFD - River Basin Districts And Competent Authorities

Last revised: 2026-03-24

## Purpose and overview
The document revises the River Basin Districts, Subunits and Competent
Authorities classes used in the 3ʳᵈ cycle of reporting of the
Water Framework Directive River Basin Management Plans ({numref}`RBDSUCA_3rdCycle`), as
well as the associated spatial data in the RiverBasinDistrict dataset
and SubUnit dataset ({numref}`RBDSU_3rdCycle_Spatial`).  
The full reporting schemas for the 3ʳᵈ cycle of reporting can be found in the [WFD2022 EAP file](https://cdr.eionet.europa.eu/help/WFD/WFD_715_2022/UML%20Data%20specification/WFD2022.EAP).


```{mermaid}  /DataModelReview/mmd/RBDSUCA_3rdCycle_ClassDiagram.mmd
:name: RBDSUCA_3rdCycle
:caption: River Basin Districts, Subunits and Competent Authorities schema - 3ʳᵈ cycle - OBSOLETE
:align: center    
```

```{mermaid}  /DataModelReview/mmd/RBDSUCA_3rdCycle_Spatial_ClassDiagram.mmd
:name: RBDSU_3rdCycle_Spatial
:caption: RiverBasinDistrict and Subunit spatial datasets - 3ʳᵈ cycle - OBSOLETE
:align: center
```

A proposal is presented for the electronic reporting in the 4ᵗʰ cycle (Figure 3).  
The reporting of the units of management (i.e. the River Basin Districts) and of the competent authorities is combined into a single dataflow.  
The overall structure of the new **River Basin Districts and Competent Authorities** dataflow is aligned with similar dataflows, e.g. under the Floods Directive [^floods-directive-footnote].

[^floods-directive-footnote]: See [Floods Directive - Units of Management and Competent Authorities[2025]](https://reportnet.europa.eu/public/dataflow/1473).

Reporting is only requested under the following conditions:

*   If there are changes to the spatial delineation and/or the identifiers of one or more River Basin Districts (since the 3ʳᵈ cycle), the spatial dataset must be reported.

*   If there are changes to the competent authorities or their roles, the descriptive data must be reported in accordance with Article 3(8) and 3(9) of the WFD.

Data providers can specify which datasets are being updated (spatial data, descriptive data, or both).  
Information about subunits is no longer requested.  
The reporting of metadata has also been simplified.


## Documents dataset - 4ᵗʰ cycle

```{mermaid}
:name: RBDCA_4thCycle_Documents
:caption:  River Basin Districts and Competent Authorities - 4ᵗʰ cycle - Documents
:align: center
:zoom:
%%{init: {'theme': 'neutral'}}%%
classDiagram
direction LR
namespace Documents {
class dcMetadata {
+ title : String4000
+ creatorOrganisationName : String4000
+ creatorElectronicMailAddress : Email
+ description : String4000 [0..1]
+ created : Date [0..1]
+ language : Language [1..n]
+ license : URL
+ rights : String4000 [0..1]
+ rightsHolder : String4000 [0..1]
+ licenseDocument : documentCode [0..*]
+ metadataDocument : documentCode [0..*]
+ updateCompetentAuthorities : YesNo
+ updateSpatialData : YesNo
}
class Document {
+ documentCode : wiseIdentifier
+ documentName : String250
+ hyperlink : URL [0..1]
+ documentFile : Attachment [0..1]
}
}
dcMetadata -- "0..*" Document
```

The Documents dataset ({numref}`RBDCA_4thCycle_Documents`) follows the standard structure used in various WISE dataflows:

- The **dcMetadata** table is required and contains only one record per delivery (i.e. per country). It provides the basic Dublin Core metadata elements about the delivery.<br/>It also functions as a "manifest file" explaining if the delivery contains an update of the spatial data (updateSpatialData = 'Yes') and/or of the competent authorities (updateCompetentAuthorities= 'Yes'). If required by the data providers, and especially if spatial data is being reported, the licenseDocument and the metadataDocument attributes allow the provision of additional information.

- The structure of the **Document** table is standard in the WISE dataflows: it allows the upload of documents (for example, PDFs) or the provision of a link to a document stored in a publicly accessible national web site.


## Descriptive dataset - 4ᵗʰ cycle

The Descriptive dataset ({numref}`RBDCA_4thCycle_Descriptive`) contains two tables:

- The **CompetentAuthority** table contains basic information about each Competent Authority.

- The **RiverBasinDistrictCompetentAuthority** table associates each Competent Authority with a River Basin District and specifies the role(s) of the competent authority in that specific RBD.

```{mermaid}
:name: RBDCA_4thCycle_Descriptive
:caption:  River Basin Districts and Competent Authorities - 4ᵗʰ cycle - Descriptive Data
:align: center
:zoom:
%%{init: {'theme': 'neutral'}}%%
classDiagram
direction LR
namespace DescriptiveData {
class CompetentAuthority {
+ euCACode : wiseIdentifier
+ competentAuthorityName : String250
+ competentAuthorityNameNL : String250
+ competentAuthorityNameNLLanguage : Language
+ acronym : String100 [0..1]
+ street : String100
+ city : String100
+ country : String100
+ postCode : String100 [0..1]
+ url : URL
}
class RiverBasinDistrictCompetentAuthority {
+ euRBDCode: wiseIdentifier
+ euCACode: wiseIdentifier
+ roleCode: Role [1..*]
}
}
CompetentAuthority -- "1..*" RiverBasinDistrictCompetentAuthority
```

```{mermaid}
:name: RBDCA_4thCycle_RoleCodelist
:caption:  River Basin Districts and Competent Authorities - 4ᵗʰ cycle - Descriptive Data - Codelist
:align: center
:zoom:
%%{init: {'theme': 'neutral'}}%%
classDiagram
direction LR
namespace Codelist{
class Role{
    <<enumeration>>
pressureAndImpactAnalysis
economicAnalysis
monitoringOfSurfaceWater
monitoringOfGroundwater
assessmentOfStatusOfSurfaceWater
assessmentOfStatusOfGroundwater
preparationOfRBMP
preparationOfProgrammeOfMeasures
implementationOfMeasures
publicParticipation
enforcementOfRegulations
coordinationOfImplementation
reportingToTheEuropeanCommission
}
}
```

## Spatial dataset - 4ᵗʰ cycle

```{mermaid}
:name: RBDCA_4thCycle_Spatial
:caption:  River Basin Districts and Competent Authorities - 4ᵗʰ cycle - Spatial Data
:align: center
:zoom:
%%{init: {'theme': 'neutral'}}%%
classDiagram
direction LR
namespace Spatialdata {
class RiverBasinDistrict {
+ geometry_polygon: geometry_multipolygon
+ inspireIdLocalId: String
+ inspireIdNamespace: String
+ inspireIdVersionId: String [0..1]
+ thematicIdIdentifier: wiseIdentifier
+ thematicIdIdentifierScheme: IdentifierScheme
+ beginLifespanVersion: Date
+ endLifespanVersion: Date [0..1]
+ predecessorsIdentifier: comma-separated list of wiseIdentifier [0..1]
+ predecessorsIdentifierScheme: IdentifierScheme [0..1]
+ successorsIdentifier: comma-separated list of wiseIdentifier [0..1]
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
+ legalBasisLink: URL [0..1]
+ legalBasisLevel: LegislationLevelValue [0..1]
+ link: URL [0..1]
}
}
```

The Spatial dataset ({numref}`RBDCA_4thCycle_Spatial`)  contains only the RiverBasinDistrict spatial table.  
As stated before, Subunits are no longer requested in the 4ᵗʰ cycle of reporting.

The following changes have been made to the RiverBasinDistrict table (in comparison to the 3ʳᵈ cycle of reporting):

*   Two attributes were removed, because they can be derived from the reported geometry: **sizeValue** and **sizeUom**.

*   Two attributes were removed, because they are not required at EU level: **relatedTransboundaryIdentifier** and **relatedTransboundaryIdentifierScheme**.

*   The date values are now requested as simply as YYYY-MM-DD, because that was the format used by the data providers during the previous cycles, and therefore it is not necessary to mantain more variants. This applies to **beginLifespanVersion**, **endLifespanVersion**, **designationPeriodBegin**, **designationPeriodEnd**.

*   One attribute was moved from the descriptive dataset into the spatial dataset.
    The **specialisedZoneType** now accepts the options **{'internationalRiverBasinDistrict','nationalRiverBasinDistrict'}**.

*  The attributes **thematicIdIdentifierScheme** and **zoneType** have been kept for clarity's sake. 
   However, all records in the **RiverBasinDistrict** dataset have a fixed value for these attributes.

*  Likewise, the attributes **successorsIdentifier** and **successorsIdentifierScheme** have been kept for clarity's sake. *In the reported datasets*, the values of these attributes will always be NULL. The appropriate value will be derived and included in the published WISE datasets (for the 1st cycle, 2nd cycle and 3rd cycle RiverBasinDistrict datasets).

## Annex - Exploratory analysis of data reported in the 3rd cycle

### National and International River Basins Districts - 3rd cycle

The query below retrieves the information reporting during the 3rd cycle.  
If the information is correct, and the delineation of the River Basin Districts did not change,
then it is not necessary to report the RiverBasinDistrict dataset again.

<details>
<summary>Show code</summary>
	
```sql
  
  --   https://discodata.eea.europa.eu/

SELECT [countryCode]
	  ,[euRBDCode] AS [thematicIdIdentifier]
	  ,'euRBDCode' AS [thematicIdIdentifierScheme]
	  ,IIF([internationalRBD] = 'Yes', 'internationalRiverBasionDistrict', 'nationalRiverBasionDistrict') AS [specialisedZoneType]
  FROM [WISE_WFD].[latest].[RBDSUCA_RBD]
  WHERE [cYear] = 2022

```
</details><br/>
	
### Competent Authorities and their roles - 3rd cycle

The query below retrieves the information reporting during the 3rd cycle.  
If the information is correct, and the competent authorities and their roles have not changed,
then it is not necessary to report the information again.

<details>
<summary>Show code</summary>
	
```sql

SELECT [countryCode],
       [euRBDCode], 
       [primeCompetentAuthority] AS [euCACode], 
       [roleCode]
FROM [WISE_WFD]. [latest]. [RBDSUCA_RBD_primeCompetentAuthority] vBase

JOIN 

    ( SELECT [euCACode],STRING_AGG(b.[roleCode], ',') AS [roleCode]
       FROM

        (SELECT [euCACode], [otherRole] AS [roleCode] 
         FROM [WISE_WFD]. [latest]. [RBDSUCA_CompetentAuthority_otherRole] 
         WHERE [cYear] = 2022 AND [otherRole] IS NOT NULL

         UNION

         SELECT [euCACode], [mainRole] AS [roleCode] 
         FROM [WISE_WFD]. [latest]. [RBDSUCA_CompetentAuthority_mainRole] 
         WHERE [cYear] = 2022 AND [mainRole] IS NOT NULL ) 
        
        AS vUnion
 
        JOIN 
    
        (SELECT *
        FROM (VALUES
        ('1 - Pressure and impact analysis',  'pressureAndImpactAnalysis'),
        ('2 - Economic analysis',  'economicAnalysis'),
        ('3 - Monitoring of surface water',  'monitoringOfSurfaceWater'),
        ('4 - Monitoring of groundwater',  'monitoringOfGroundwater'),
        ('5 - Assessment of status of surface water',  'assessmentOfStatusOfSurfaceWater'),
        ('6 - Assessment of status of groundwater',  'assessmentOfStatusOfGroundwater'),
        ('7 - Preparation of RBMP',  'preparationOfRBMP'),
        ('8 - Preparation of PoM',  'preparationOfPoM'),
        ('9 - Implementation of measures',  'implementationOfMeasures'),
        ('10 - Public participation', 'publicParticipation'),
        ('11 - Enforcement of regulations', 'enforcementOfRegulations'),
        ('12 - Co-ordination of implementation', 'coordinationOfImplementation'),
        ('13 - Reporting to the European Commission', 'reportingToTheEuropeanCommission')
        ) AS t(originalValue, roleCode)) AS b

        ON vUnion.roleCode = b.originalValue

    GROUP BY [euCACode] ) AS vRoles
    ON vBase.primeCompetentAuthority = vRoles.euCACode
    WHERE [cYear] = 2022

```

</details><br/>

## References

Note: The original document can still be downloaded but should no longer be used.  
See **PROPOSAL - Version 2026.02.13** {download}`PDF <pdf/WFD_4th_cycle_RiverBasinDistrictsAndCompetentAuthorities_v20260213.pdf>`
