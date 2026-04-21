# WFD - Protected Areas

**PROPOSAL - Version 2026.02.13** {download}`PDF <pdf/WFD_4rd_cycle_ProtectedAreas_v20260220.pdf>`

## Purpose and overview

"According to Article 6 and Annex IV of the WFD, Member States shall ensure the establishment of a register or registers of all areas lying within each River Basin District which have been designated as requiring special protection under specific Community legislation for the protection of their surface water and groundwater, or for the conservation of habitats and species directly depending on water, including the protection of Natura 2000 sites and economically significant aquatic species (e.g. shellfish)."[^1].

The document revises the reporting of WFD Protected Areas in the 2ⁿᵈ and 3ʳᵈ cycle of reporting of the Water Framework Directive River Basin Management Plans (Figure 1), as well as the associated spatial data (Figure 2). A proposal is presented for the electronic reporting in the 4ᵗʰ cycle. Aspects related to exemptions are addressed in a later document.

*Figure 1. Partial class diagram for Protected Areas related data in the 3ʳᵈ cycle of reporting.*

(Figure 1)=

```{mermaid}
%%{init: {'theme': 'default', 'flowchart': {'rankDir': 'TB'}}}%%
classDiagram
    class SWB_2022 SWAssociatedProtectedArea["«XSDcomplexType»
    SWB_2022::SWAssociatedProtectedArea"]  {
        XSDcomplexType SWB_2022
        +euProtectedAreaCode: FeatureUniqueEUCodeType
        +protectedAreaType: ProtectedAreaType_Enum
        +protectedAreaObjectivesSet: ProtectedAreaObjective_Enum [0..1]
        +protectedAreaObjectivesMet: YesNoNoInformation_Union_Enum [0..1]
        +protectedAreaComment: String1000Type [0..1]
        +protectedAreaExemption: ExemptionType_Enum [1..*]
    }
    class SurfaceWaterBody {
        XSDcomplexType SWB_2022
    }
    class GWB_2022 GWAssociatedProtectedArea["«XSDcomplexType»
    GWB_2022::GWAssociatedProtectedArea"] {
        XSDcomplexType GWB_2022
        +euProtectedAreaCode: FeatureUniqueEUCodeType
        +protectedAreaType: ProtectedGWAreaType_Enum
        +protectedAreaObjectivesSet: ProtectedAreaObjective_Enum [0..1]
        +protectedAreaObjectivesMet: YesNoNoInformation_Union_Enum [0..1]
        +protectedAreaComment: String1000Type [0..1]
        +protectedAreaExemption: ExemptionType_Enum [1..*]
    }
    class GroundWaterBody {
        XSDcomplexType GWB_2022
    }

   SWB_2022 SWAssociatedProtectedArea "0..*" --> "1" SurfaceWaterBody : +SWAssociatedProtectedArea
   GWB_2022 GWAssociatedProtectedArea "0..*" --> "1" GroundWaterBody : +GWAssociatedProtectedArea
```

Source: [https://cdr.eionet.europa.eu/help/WFD/WFD_715_2022/UML%20Data%20specification/WFD2022.EAP](https://cdr.eionet.europa.eu/help/WFD/WFD_715_2022/UML%20Data%20specification/WFD2022.EAP)

---

*Figure 2. Partial class diagram for the ProtectedArea class – 3ʳᵈ cycle of reporting.*

```{mermaid}
classDiagram
    class ProtectedArea["«FeatureType»
    ProtectedArea"]  {
      
        +geometry: GM_MultiSurface
        +inspireIdLocalId: String254LeadingLetterOrNum
        +inspireIdNamespace: String254LeadingLetterOrNum
        +inspireIdVersionId: String25Type [0..1]
        +thematicIdentifier: FeatureUniqueEUCodeType
        +thematicIdentifierScheme: IdentifierScheme
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
        +specialisedZoneType: SpecialisedZoneTypeCode [0..1]
        +specialisedZoneIdentifier: String254LeadingLetterOrNum
        +legalBasisName: String254LeadingLetterOrNum [0..1]
        +legalBasisLink: URLType
        +legalBasisLevel: LegislationLevelValue
        +relatedZoneIdentifier: FeatureUniqueEUCodeType [0..1]
        +relatedZoneIdentifierScheme: IdentifierScheme [0..1]
        +sizeValue: PositiveDecimalType [0..1]
        +sizeUom: UomSize [0..1]
        +link: URLType [0..1]
    }
    class FeatureCollection ["«FeatureType»
    FeatureCollection"] {
        FeatureType
    }
   
  
    ProtectedArea "1..*" <-- FeatureCollection : +featureMember

```

Source: [https://cdr.eionet.europa.eu/help/WFD/WFD_715_2022/UML%20Data%20specification/WFD2022.EAP](https://cdr.eionet.europa.eu/help/WFD/WFD_715_2022/UML%20Data%20specification/WFD2022.EAP)

## Spatial data reporting – 2ⁿᵈ and 3ʳᵈ cycle

The WFD Protected Area spatial data reporting requirements were stable during the 2ⁿᵈ and 3ʳᵈ cycle of electronic reporting ({ref}`Table 1 <table-1>`).

The following generic principles were applied:

1) If the spatial data was already reported under a specific dataflow(e.g. for bathing waters, sensitive areas, nitrate vulnerable zones,or Natura 2000 protected sites), then spatial data was neither required nor accepted under the WFD.
2) If no specific dataflow existed (e.g. for drinking water protection areas, freshwater fish designated areas and shellfish designated areas), then the spatial data was reported under the WFD.

Several issues affected the reporting, causing redundancies and inconsistencies:

- For the protected area types under case 1), not all the data models followed the basic requirements of the WFD ProtectedArea data model.For example, the nitrate vulnerable zones do not have a unique identifier consistent with the syntax of the WISE identifiers.
- For protected area types under case 2), most issues affected the reporting of the drinking water protection areas. If the drinking water protection area matched the entire water body and the identifier was the same, then reporting the geometry of the protected area was not required – however, this approach was not followed consistently by Member States.
- In all cases, the association between the WFD ProtectedArea and one or more WFD water bodies is not reported (e.g. for the Natura 2000 protected sites) or was an optional attribute (e.g. bathing waters,sensitive areas, etc). Therefore, the association between the protected area and the water body was requested again in the WFD descriptive data – creating redundancies and potential inconsistencies due to the different reporting timelines.

These issues are addressed in the simplification of the reporting for the 4ᵗʰ cycle:

- Using the same spatial data model across all WFD ProtectedArea dataflows and datasets, therefore guaranteeing the existence of WISE **unique identifiers**.
- Reporting the association between protected areas and water bodies **only once**, in the ProtectedArea dataset (i.e. removing it from the WFD descriptive data reporting).

The principles above were applied for all WFD protected area types,except Natura2000 protected sites.

*Table 1. WFD Protected Area spatial data reporting requirements – 2ⁿᵈ and 3ʳᵈ cycle of reporting*

(table-1)=

| Reporting requirements under the WFD 2ⁿᵈ and 3ʳᵈ cycle of electronic reporting | Observations |
|---|---|
| **Drinking water protection areas** <br/>*Water bodies identified under WFD Article 7(1) are the only protected areas that are purely designated by WFD, i.e., there is no process to identify and designate these areas under other pieces of legislation, although obviously they are relevant for drinking water supply.* […] <br/><br/> *Member States practice varies in the designation of Drinking Water protected areas. The following two broad approaches could be identified in the first RBMP (River Basin Management Plans), for which guidance is provided as regards reporting of spatial data:*<br/>*a) Some Member States follow WFD Article 7 and designate as protected areas the water bodies used for the abstraction of water intended for human consumption (and those intended for such future use). Therefore, there is no different spatial delineation of the protected areas: these are coincident with the WFD water bodies. Therefore, no reporting of spatial data under the WFD is expected in this case.*<br/> *b) Some Member States delineate the part of the water bodies which they consider are protected areas. The spatial extent of the protected areas can therefore be different, typically smaller than WFD water bodies. This is often the case in large groundwater bodies. In this case the Member State is required to report the spatial extent of the protected areas* […]. | `zoneType = 'drinkingWaterProtectionArea'` |
| **Freshwater fish designated waters** <br/>*The Freshwater Fish Directive (2006/44/EC) was repealed by the WFD in 2013. The WFD Reporting Guidance recalls that "according to the WFD, the level of protection should be maintained through the inclusion of the designated areas as Protected Areas under WFD". In addition, "it is considered that the WFD objective of good ecological status integrates fully the objectives of the Fish Directive". Some Member States maintain the transposing legislation in order to maintain the same level of protection, and still consider this an important element in the protection of water resources. Spatial delineation of the protected areas under the Freshwater Fish Directive may or may not coincide with the delineation of the WFD water bodies. It is therefore possible to report the spatial extent of these protected areas* […]. *The reporting of this information is* **optional**. | `zoneType = 'designatedWaters'` AND `specialisedZoneType = 'freshwaterFishDesignatedWater'` |
| **Shellfish designated waters** <br/>*The Shellfish Directive (2006/113/EC) was repealed by the WFD in 2013. As with the Freshwater Fish Directive, after the repeal, the WFD requires Member States to maintain the same level of protection. However, in the case of the Shellfish Directive, the WFD objective of good ecological status does not integrate fully the objectives of the Shellfish Directive. Indeed, "microbiological standards are essential for the quality of shellfish water", and these are not part of the definition of ecological status. Therefore, "it is requested to report if these standards have been set (or maintained from the shellfish water directive) and if they are met" (WFD Reporting Guidance 2016). Given that the Shellfish Directive is no longer in force and therefore there is no self-standing reporting mechanism to report the protected areas, it is* **required** *that the spatial extents of the protected areas are reported under the WFD* […]. | `zoneType = 'designatedWaters'` AND `specialisedZoneType IN ('shellfishDesignatedWater')` |
| **Nitrate Vulnerable Zones** <br/>*Reporting of Nitrate Vulnerable Zones (NVZs) is done under the Nitrates Directive 91/676/EEC reporting process* ([rod.eionet.europa.eu/obligations/106](http://rod.eionet.europa.eu/obligations/106)). […] *The definition of the reporting requirements for NVZs does not include a unique ID for each zone* ([dd.eionet.europa.eu/tables/7762](http://dd.eionet.europa.eu/tables/7762)). […] *<br/>*If the Member State applies a 'whole territory' approach for the Nitrates Directive, it should not report protected areas under the WFD. In any case, no reporting of spatial data for NVZs is expected under the WFD.* | `zoneType = 'nitrateVulnerableZone'` |
| **UWWTD Sensitive Areas** <br/>*Reporting of spatial extent of sensitive areas is done through the regular reporting under the Urban Waste Water Directive 91/271/EEC* ([cdr.eionet.europa.eu/help/UWWTD](http://cdr.eionet.europa.eu/help/UWWTD)). […] *Sensitive areas are identified through a unique ID* […]. | `zoneType = 'sensitiveArea'` AND `specialisedZoneType in ('catchmentOfSensitiveArea', 'lessSensitiveArea', 'coastalSensitiveArea', 'transitionalSensitiveArea', 'lakeSensitiveArea', 'riverSensitiveArea', 'coastalBathingWater')` |
| **Bathing Waters** <br/>*The annual reporting under Bathing Water Directive 2006/7/EC* ([cdr.eionet.europa.eu/help/BWD](http://cdr.eionet.europa.eu/help/BWD)) *requires the identification of bathing waters by providing a point* […]. *As* [an] *optional element, the* […] *surface water body* [identifier is] *provided for each bathing water site* […]. | `ZoneType = 'bathingWaters'` AND `specialisedZoneType in ('transitionalBathingWater', 'lakeBathingWater', 'riverBathingWater')` |
| **Habitats and Birds Directives protected sites** <br/>*Reporting of protected sites is done under the Habitats and Birds reporting processes for Natura 2000 sites* ([rod.eionet.europa.eu/obligations/274](http://rod.eionet.europa.eu/obligations/274) *and* [rod.eionet.europa.eu/obligations/616](http://rod.eionet.europa.eu/obligations/616)). […] *Member States are expected to identify the water dependent protected areas associated with water bodies under the WFD* [reporting]. *This is done by reporting the Habitats and Birds Directive site code in the attribute euProtectedAreaCode. The WFD reporting process will automatically cross-check if the site ID is on the list of reported Natura 2000 areas. If this is not the case, the system will generate an error.* […] <br/>*No reporting of spatial data regarding Natura 2000* […] *protected areas is expected under the WFD.* | `<< not applicable >>` |

Source: Text in *italics* extracted from the documents referenced in footnote (1).

## Spatial data reporting – 4ᵗʰ cycle

In keeping with the approach taken in the 3ʳᵈ cycle, the reporting of spatial data related to WFD protected areas in done under the dataflows pertaining to the legal instruments under which the protected areas were defined ({ref}`Table 2 <table-2>`)

The WFD Protected Area spatial data reporting requirement for the 4ᵗʰ cycle of electronic reporting are detailed in ({ref}`Table 3 <table-3>`)

- The reporting of drinking water protection areas is moved to under Article 8 of the recast DWD, on the risk assessment and management of catchment areas for abstraction points of water intended for human consumption.
- The data model for the Nitrate Vulnerable Zones reporting is aligned with the model used for the other protected areas (except Natura 2000 protected sites).
- The reporting of the association between the protected areas and the water bodies is done only once – in the spatial data reporting (except Natura 2000 protected sites).

*Table 2. EU legal instruments under which the WFD Protected Areas are defined.*

(table-2)=

| Acronym             | Name                                                                                                                                                                                                                      | ELI                                                    | Reporting obligation                                                                |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | ----------------------------------------------------------------------------------- |
| WFD                 | **Directive 2000/60/EC of the European Parliament and of the Council of 23 October 2000 establishing a framework for Community action in the field of water policy**    | <http://data.europa.eu/eli/dir/2000/60/oj>               | <https://rod.eionet.europa.eu/obligations/780> (reporting under revision) |
| Shellfish Directive | Directive 2006/113/EC of the European Parliament and of the Council of 12 December 2006 on the quality required of shellfish waters *Note: implicitly repealed by WFD*                                                   | <http://data.europa.eu/eli/dir/2006/113/oj> | (included under WFD)                      |
| Fish Directive      | Directive 2006/44/EC of the European Parliament and of the Council of 6 September 2006 on the quality of fresh waters needing protection or improvement in order to support fish life *Note: implicitly repealed by WFD* | <http://data.europa.eu/eli/dir/2006/44/oj>  | (included under WFD)                      |
| BWD                 | Directive 2006/7/EC of the European Parliament and of the Council of 15 February 2006 concerning the management of bathing water quality and repealing Directive 76/160/EEC                                               | <http://data.europa.eu/eli/dir/2006/7/oj>     | <https://rod.eionet.europa.eu/obligations/788>                            |
| DWD (recast)        | Directive (EU) 2020/2184 of the European Parliament and of the Council of 16 December 2020 on the quality of water intended for human consumption (recast)                                                                | <http://data.europa.eu/eli/dir/2020/2184/oj>    | <https://rod.eionet.europa.eu/instruments/699> (reporting under revision) |
| NITRATES            | Council Directive of 12 December 1991 concerning the protection of waters against pollution caused by nitrates from agricultural sources (91/676/EEC)                                                                     | <http://data.europa.eu/eli/dir/1991/676/oj>     | <https://rod.eionet.europa.eu/obligations/106> (reporting under revision)             |
| UWWTD (recast)      | Directive (EU) 2024/3019 of the European Parliament and of the Council of 27 November 2024 concerning urban wastewater treatment (recast)                                                                                 | <http://data.europa.eu/eli/dir/2024/3019/oj>    | <https://rod.eionet.europa.eu/obligations/613> (reporting under revision) |
| Birds directive     | Directive 2009/147/EC of the European Parliament and of the Council of 30 November 2009 on the conservation of wild birds                                                                                                 | <http://data.europa.eu/eli/dir/2024/3019/oj>    | <https://rod.eionet.europa.eu/obligations/613> (reporting under revision) |
| Habitats directive  | Council Directive 92/43/EEC of 21 May 1992 on the conservation of natural habitats and of wild fauna and flora                                                                                                            | <http://data.europa.eu/eli/dir/2024/3019/oj>    | <https://rod.eionet.europa.eu/obligations/613> (reporting under revision) |

*Table 3. WFD Protected Area spatial data reporting requirements – 4ᵗʰ cycle of reporting*
(table-3)=

| Reporting requirements under the WFD 4ᵗʰ cycle of electronic reporting | Observations |
|---|---|
| **Drinking Water protection areas** <br/>The spatial data reporting *moves to the recast Drinking Water Directive*. Information about the drinking water protection areas and safeguard zones is part of the reporting under Article 8 of the recast DWD, on the risk assessment and management of catchment areas for abstraction points of water intended for human consumption.<br/> **The new spatial data model is similar to the WFD ProtectedArea model previously used.** The dataflow is currently being implemented in RN3 and will soon be available for testing.<br/>• Unique identifiers must be reported, following the WISE identifier syntax. <br/>• The association between protected areas and water bodies **must** be reported using the relatedZone columns. <br/>• A new **confidentialityStatus** column was added to allow data providers to report spatial data that will not be published. <br/>• The **specialisedZoneType** column allows the distinction between different types of protected area. <br/>Data providers are referred to the document *"Risk assessment and risk management of the catchment areas for abstraction points of water intended for human consumption. Conceptual model proposal for the electronic reporting under the recast Drinking Water Directive Article 8. Version 2025-12-18."* available [here](https://circabc.europa.eu/ui/group/65764c73-4a57-45dc-8199-473014cf65bf/library/c17c6a2e-41e5-482f-b353-3fd651bd9aca/details) for further information. | `zoneType = 'drinkingWaterProtectionArea'` AND `specialisedZoneType in ('catchmentArea', 'waterBody', 'waterAbstractionSafeguardZone')` |
| **Freshwater fish designated waters** <br/>The spatial data reporting *remains under Water Framework Directive*. <br/>• The association between each protected area and one or more surface water bodies **must** be reported, using the relatedZone columns. Reporting is **conditional**: <br/>• Member States that have reported Freshwater fish designated areas in the 3ʳᵈ reporting cycle **must** update the information previously reported (which will be prefilled using the data reported in the 3ʳᵈ cycle). <br/>• Other Member States **may** optionally report newly created or existing Freshwater fish designated areas. | `zoneType = 'designatedWaters'` AND `specialisedZoneType = 'freshwaterFishDesignatedWater'` |
| **Shellfish designated waters** <br/>The spatial data reporting *remains under Water Framework Directive*. <br/>• The association between each protected area and one or more surface water bodies **must** be reported, using the relatedZone columns. Reporting is **conditional**: <br/>• Member States that have reported Shellfish designated areas in the 3rd reporting cycle **must** update the information previously reported (which will be prefilled using the data reported in the 3ʳᵈ cycle). <br/>• Other Member States **must** report newly created or existing Shellfish fish designated areas. | `zoneType = 'designatedWaters'` AND `specialisedZoneType IN ('shellfishDesignatedWater')` |
| **Nitrate Vulnerable Zones**<br/> The spatial data reporting *remains under the Nitrates Directive*. <br/>The Nitrates Directive dataflows are currently under revision (with comments being requested from Member States). <br/><br/>**The new spatial data model is identical to the WFD ProtectedArea model.**<br/>• Unique identifiers **must** be reported, following the WISE identifier syntax.<br/>• The association between each protected area and one or more surface water bodies **should** be reported.<br/>• Member States that follow the "whole territory" approach do not report spatial data. | `zoneType = 'nitrateVulnerableZone'` |
| **UWWTD Sensitive Areas**<br/>The spatial data reporting *remains under the Urban Waste Water Treatment Directive*. <br/>The UWWTD dataflows are currently under revision. <br/><br/>**The spatial data model is already identical to the WFD ProtectedArea model.**<br/>• Unique identifiers **must** be reported, following the WISE identifier syntax.<br/>• The association between each protected area and one or more surface water bodies **must** be reported, using the relatedZone columns, if specialisedZoneType != 'catchmentOfSensitiveArea'. <br/>• If specialisedZoneType = 'catchmentOfSensitiveArea', then associated ProtectedArea (with specialisedZoneType != 'catchmentOfSensitiveArea') is reported in the relatedZone columns.<br/>• Member States that follow the "whole territory" approach do not report spatial data. | `zoneType = 'sensitiveArea'` AND `specialisedZoneType in ('catchmentOfSensitiveArea', 'lessSensitiveArea', 'coastalSensitiveArea', 'transitionalSensitiveArea', 'lakeSensitiveArea', 'riverSensitiveArea', 'coastalBathingWater')` |
|**Bathing Waters**<br/> The spatial data reporting *remains under the Bathing Water Directive dataflow*.<br/> The dataflow is currently being implemented in RN3 and will soon be available for testing.<br/> **The spatial data model is already identical to the WFD ProtectedArea model.**<br/>• Unique identifiers **must** be reported, following the WISE identifier syntax.<br/>• The association between each protected area and one surface water body **must** be reported. <br/> The Identification of Bathing Waters dataflow is annual – but reporting is only required if new bathing waters are designated OR if there is missing information about the association between the protected area and the surface water body. | `ZoneType = 'bathingWaters'` AND `specialisedZoneType in ('transitionalBathingWater', 'lakeBathingWater', 'riverBathingWater')` |
| **Habitats and Birds Directives protected sites** No spatial data reporting under the Water Framework Directive. | `<< not applicable >>` |

({ref}`Figure 1 <Figure 1>`) presents the class diagram for the proposed generic ProtectedArea dataset:

- Depending on the specific dataflow, different geometry types may be requested/allowed (either point, line or polygon).
- The relatedZoneIdentifier and relatedZoneIdentifierScheme are mandatory, and specific constraints will apply depending on the dataflow (i.e. on the type of protected area).
- The attribute confidentialityStatus was included (and applies to the drinking water protected areas) to address concerns about the publication of the location of some protected areas.
- The attributes sizeValue and sizeUom attributes are no longer requested.
- The attributes successorsIdentifier and successorsIdentifierScheme have been kept for clarity's sake although their value will always be NULL (the appropriate value will be derived and included in the
  published WISE datasets that refer to the previous reporting cycles).

*Figure 3. Class diagram for an abstract ProtectedArea dataset – 4ᵗʰ cycle of reporting.*

```{mermaid}
classDiagram
    class ProtectedArea {
        +geometry_polygon: geometry [0..1]
        +geometry_line: geometry [0..1]
        +geometry_point: geometry [0..1]
        +inspireIdLocalId: String
        +inspireIdNamespace: String
        +inspireIdVersionId: String [0..1]
        +thematicIdIdentifier: WISEIdentifier
        +thematicIdIdentifierScheme: IdentifierScheme
        +beginLifespanVersion: Date
        +endLifespanVersion: Date [0..1]
        +predecessorsIdentifier: comma-separated list of WISEIdentifier [0..1]
        +predecessorsIdentifierScheme: IdentifierScheme [0..1]
        -successorsIdentifier: comma-separated list of WISEIdentifier [0..1]
        -successorsIdentifierScheme: IdentifierScheme [0..1]
        +wiseEvolutionType: WiseEvolutionType
        +nameTextInternational: String
        +nameText: String
        +nameLanguage: Language
        +designationPeriodBegin: Date
        +designationPeriodEnd: Date [0..1]
        +zoneType: ZoneType
        +specialisedZoneType: SpecialisedZoneType
        +legalBasisName: String [0..1]
        +legalBasisLink: url [0..1]
        +legalBasisLevel: LegislationLevelValue [0..1]
        +relateZoneIdentifier: comma-separated list of WISEIdentifier
        +relatedZoneIdentifierScheme: IdentifierScheme
        +confidentialityStatus: ConfidentialityStatusValue [0..1]
        +link: url [0..1]
    }
```

## Special case – the Natura2000 protected sites

The Natura2000 dataflows do not include information about the association between protected sites and WFD water bodies. Therefore, a different approach is necessary to simplify the WFD reporting.
A provisional prefilled list of "water-dependent" Natura 2000 protected sites will be created, based on the Natura2000 reporting based on the habitat type and species type [^2]

A Natura 2000 site should be designated as "water-dependent" if it contains Annex I habitat types or Annex II species (Habitats Directive),or bird species (Birds Directive),  whose presence was the primary reason for the area's designation and that meet the ecological criteria below:

- habitats consisting of surface water or occurring entirely within surface water as defined by the WFD
- habitats that depend on frequent inundation by surface water or specific groundwater levels
- aquatic species living directly in surface waters
- species with at least one aquatic life stage dependent on surface water for essential activities such as breeding, incubation, juvenile
  development, feeding, or roosting.

The provisional prefilled list will be provided to Member States, for validation purposes:

- If missing, additional Natura 2000 protected site identifiers may be added (from the reference list already reported under the Natura 2000 dataflows).
- If incorrect, Natura 2000 protected site identifiers present in the provisional list may be flagged for removal from the WFD register of protected areas.
- For the Natura 2000 sites to be included in the WFD register of protected areas (because where the maintenance or improvement of water status is a critical factor for their protection), the association to water bodies should be reported.

## Descriptive data reporting

Specific objectives may be set for some types of protected areas:

- Shellfish designated waters
- Drinking water protection areas
- Natura 2000 protected sites included in the WFD register of protected
  areas

For Freshwater fish designated waters, the WFD good ecological status fully integrates the integrate Fish Directive (2006/44/EC) objectives. Similarly, the WFD good status integrates the Nitrates Directive and UWWTD objectives related to eutrophication. Therefore, no information on specific objectives is requested or expected for these types of protected area or for bathing waters.

The data reported for the 3ʳᵈ cycle can be used to estimate the impact of the simplification:

- 46% of the 84560 records reported for groundwater associated protected areas would not have been reported.
- 72% of the 71726 records reported for surface water associated protected areas would not have been reported.

The analysis of the 3ʳᵈ cycle reveals that no specific objectives were set for Nationally Designated Areas (NatDA, formerly known as CDDA). Information about this type of protected sites will no longer be requested.

[def]: #purpose-and-overview
[def2]: #_Toc222336798
[^1]: Extracts from the “Clarification note in relation to the reporting of spatial data for Water Framework Directive (WFD) protected areas, in the context of the March 2016 reporting of the second River Basin Management Plans (RBMPs)” [http://cdr.eionet.europa.eu/help/WFD/WFD_521_2016/GISGuidance/Clarification%20note%20protected%20areas.pdf](http://cdr.eionet.europa.eu/help/WFD/WFD_521_2016/GISGuidance/Clarification%20note%20protected%20areas.pdf) See also the “Clarification note in relation to the reporting of spatial data for Water Framework Directive (WFD) protected areas, in the context of the March 2022 reporting of the third River Basin Management Plans (RBMPs) 28 April 2022” [https://cdr.eionet.europa.eu/help/WFD/WFD_780_2022/GISGuidance/PA_Clarification_Note.pdf](https://cdr.eionet.europa.eu/help/WFD/WFD_780_2022/GISGuidance/PA_Clarification_Note.pdf)
    
[^2]: See for example Table 1 in the document "Links between the Water Framework Directive (WFD 2000/60/EC) and Nature Directives (BirdsDirective 2009/147/EC and Habitats Directive 92/43/EEC)."[https://circabc.europa.eu/ui/group/3f466d71-92a7-49eb-9c63-6cb0fadf29dc/library/f214c3f5-bf5c-404a-a18b-02c0553b82ad/details](https://circabc.europa.eu/ui/group/3f466d71-92a7-49eb-9c63-6cb0fadf29dc/library/f214c3f5-bf5c-404a-a18b-02c0553b82ad/details?open=true)
