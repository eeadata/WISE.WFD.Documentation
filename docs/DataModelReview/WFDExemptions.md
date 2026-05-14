(heading_wfd_exemptions)=
# WFD - Exemptions

Last update: 2026-05-13

```{warning}

  See {ref}`heading_wfd_exemptions_clarifications`

```

```{contents} Table of Contents
:depth: 2
:local:
```

(heading_wfd_exemptions_purpose_and_overview)=
## Purpose and overview

This section revises the reporting of information related to Exemptions in the 2ⁿᵈ and 3ʳᵈ cycle of reporting of the Water Framework Directive River Basin Management Plans.  
It also presents a proposal for simplifying the electronic reporting in the 4ᵗʰ cycle.

(heading_wfd_exemptions_reporting_of_exemptions_3rd_cycle)=
## Reporting of exemptions - 3ʳᵈ cycle

* The information related to exemptions in the surface water methodologies schema (SWExemption class, see {numref}`Exemptions_3rdCycle_SWMET_ClassDiagram`)
  will no longer requested in the structured data reporting for the 4ᵗʰ cycle (i.e. the it is provided only in the RBMP documents).
  
* The information related to exemptions in the groundwater water methodologies schema (GWExemption class, see {numref}`Exemptions_3rdCycle_GWMET_ClassDiagram`).
  will no longer requested in the structured data reporting for the 4ᵗʰ cycle (i.e. it is provided only in the RBMP documents).
  
  
```{mermaid}  /DataModelReview/mmd/Exemptions_3rdCycle_SWMET_ClassDiagram.mmd
:name: Exemptions_3rdCycle_SWMET_ClassDiagram
:caption: SWMET schema, SWExemptions class - 3ʳᵈ cycle - OBSOLETE
:align: center
```

```{mermaid}  /DataModelReview/mmd/Exemptions_3rdCycle_GWMET_ClassDiagram.mmd
:name: Exemptions_3rdCycle_GWMET_ClassDiagram
:caption: GWMET schema, GWExemptions class - 3ʳᵈ cycle - OBSOLETE
:align: center
```

(heading_wfd_exemptions_reporting_of_exemptions_4th_cycle)=
## Reporting of exemptions - 4ᵗʰ cycle

The reporting of ecological, chemical and quantitative exemptions is aligned into tables with a similar structure:

  * The waterbody to which the exemption applies is always identified.
  * For ecological exemptions, the quality element is identified.
  * For chemical exemptions, the substance is identified.
  * For exemptions associated with protected areas were specific objectives were set but not met, the protected area is identified.

The remaining attributes (see {numref}`ExemptionAbstractClass`) identify the exemption type (exemptionType), the reason why it is applied (exemptionRationale), the expected exemption period (exemptionPeriod), and the significant pressure causing failure, if applicable (exemptionPressureType).
Reference to additional information in the RBMPs documentation can be provided via the exemptionReference.

Ecological exemptions are only reported at quality element level, avoiding duplication.

The *exemptionPeriod* covers the period until good status is achieved (see {numref}`ExemptionCodelist`): this attribute replaces the former attributes  *swEcologicalStatusOrPotentialExpectedAchievementDate*, *swChemicalStatusExpectedAchievementDate*, *gwChemicalStatusExpectedAchievementDate* and *gwQuantitativeStatusExpectedAchievementDate*.

```{mermaid}
:name: ExemptionAbstractClass
:caption: Exemption - 4ᵗʰ cycle - Abstract pattern for illustrative purposes
:align: center
%%{init: {'theme': 'neutral'}}%%
classDiagram
class Exemption ["«Abstract»
Exemption"]{
    / exemptionType : ExemptionType
    + exemptionRationale : ExemptionRationale [1..n]
    + exemptionPeriod : ExemptionPeriod
    + exemptionReference : referenceIdentifier [0..1]
	+ exemptionPressureType : PressureType [0..n]
}
```

(heading_wfd_exemptions_surface_water_bodies_ecological_exemptions_by_quality_element)=
## Surface water bodies - ecological exemptions by quality element

Ecological exemptions are reported using the table in {numref}`SWEcologicalExemptionClass`.

Ecological exemptions are not applicable to Territorial Waters.
For other surface water body categories, reporting is mandatory when the following conditions apply:
* the qeCode value starts with QE1 or qeCode starts with QE3 
* and the quality element is causing failure to achieve good status, i.e. qeStatusOrPotentialValue in (3, 4, 5).

Ecological exemptions are reported at Quality Element level only:
* exemptions are not applicable to quality elements with unknown status
* exemptions are not applicable to quality elements not used in the ecological status assessment.

(Note that the duplicate reporting of the ecological exemptions - both at surface water body level *and* at quality element level - is removed in the revised model for the 4ᵗʰ cycle reporting.)

```{mermaid}
:name: SWEcologicalExemptionClass
:caption: Surface Water Body - Ecological Exemption - 4ᵗʰ cycle
:align: center
%%{init: {'theme': 'neutral'}}%%
classDiagram
class SWEcologicalExemption{
    + euSurfaceWaterBodyCode : wiseIdentifier
    + qeCode : QualityElement 
    / exemptionType : ExemptionType
    + exemptionRationale : ExemptionRationale [1..n]
    + exemptionPeriod : ExemptionPeriod
    + exemptionReference : referenceIdentifier [0..1]
    + significantPressureType : PressureType [1..n]
}
```

The diagram below presents the applicability criteria for the different exemption types ({numref}`Exemptions_EcologicalExemption_Flowchart`).

```{mermaid} /DataModelReview/mmd/Exemptions_EcologicalExemption_Flowchart.mmd
:name: Exemptions_EcologicalExemption_Flowchart
:caption: Surface Water Body - Ecological Exemption Decision Tree - 4ᵗʰ cycle
:align: center
```

(heading_wfd_exemptions_surface_water_bodies_chemical_exemptions_by_pollutant)=
## Surface water bodies - chemical exemptions by pollutant

Chemical exemptions are reported using the table in {numref}`SWChemicalExemptionClass`.

Reporting is mandatory if the following conditions apply:
* the swPollutantCode value is a 2013 Priority Substance  
* all the Priority Substance is causing failure to achieve good status (i.e. swPollutantCausingFailure = 'Yes').

Chemical exemptions are reported at Pollutant level only:
* exemptions are only applicable to priority substances
* exemptions are not applicable to substances with unknown status.

Article 4(7) exemptions may be applicable for indirect deterioration of chemical status, where it is the indirect result of modifications to physical characteristics (Article 4(7), first indent). 

In the 4ᵗʰ cycle of reporting, exemptions associated with river basin specific pollutants 
are reported as exemptions associated with the quality element "QE3-3 - River Basin Specific Pollutants".

```{mermaid}
:name: SWChemicalExemptionClass
:caption: Surface Water Body - Chemical Exemption - 4ᵗʰ cycle
:align: center
%%{init: {'theme': 'neutral'}}%%
classDiagram
class SWChemicalExemption{
    + euSurfaceWaterBodyCode : wiseIdentifier
    + swPollutantCode : Substance
    / exemptionType : ExemptionType
    + exemptionRationale : ExemptionRationale [1..n]
    + exemptionPeriod : ExemptionPeriod
    + exemptionReference : referenceIdentifier [0..1]
    + significantPressureType : PressureType [1..n]
}
```

The diagram below presents the applicability criteria for the different exemption types ({numref}`Exemptions_ChemicalExemption_Flowchart`).

```{mermaid} /DataModelReview/mmd/Exemptions_ChemicalExemption_Flowchart.mmd
:name: Exemptions_ChemicalExemption_Flowchart
:caption: Surface Water Body - Chemical Exemption Decision Tree - 4ᵗʰ cycle
:align: center
```

(heading_wfd_exemptions_surface_water_bodies_protected_area_exemptions)=
## Surface water bodies - protected area related exemptions

Specific objectives may be set for waterbodies associated with some types of protected areas:
* Shellfish designated waters
* Drinking water protection areas
* Natura 2000 protected sites included in the WFD register of protected areas

*If the specific objectives have not been met*, then exemptions may be reported.
(Note that the euProtectedAreaCode value is only requested for Natura 2000 sites.)

Based on the data reported in the 3ʳᵈ cycle, it is likely that the number of exemptions is relatively low. Therefore the attributes of related to exemptions were simply added to the SWAssociatedProtectedArea table ({numref}`SWAssociatedProtectedAreaClass`).

```{mermaid}
:name: SWAssociatedProtectedAreaClass
:caption: Surface Water Body - Associated Protected Area Exemption - 4ᵗʰ cycle
:align: center
%%{init: {'theme': 'neutral'}}%%
classDiagram
class SWAssociatedProtectedArea{
	+ euSurfaceWaterBodyCode : wiseIdentifier
	+ euProtectedAreaType : ProtectedAreaType 
	+ euProtectedAreaCode : wiseIdentifier [0..1]
	+ protectedAreaObjectivesSet : YesNo
	+ protectedAreaObjectivesMet : YesNoUnknown
	/ exemptionType : ExemptionType [0..1]
	+ exemptionRationale : ExemptionRationale [0..n]
	+ exemptionPeriod : ExemptionPeriod [0..1]
	+ exemptionReference : referenceIdentifier [0..1]
	   } 
```

(heading_wfd_exemptions_groundwater_bodies_chemical_exemptions_by_pollutant)=
## Groundwater bodies - chemical exemptions by pollutant

Chemical exemptions are reported using the table in {numref}`GWChemicalExemptionClass`.

Reporting is mandatory if the following condition applies:
* the substance is causing failure to achieve good status (i.e. gwPollutantCausingFailure = 'Yes').

Chemical exemptions are reported at Pollutant level only:
* exemptions are not applicable to substances with unknown status.

Article 4(7) exemptions may be applicable for indirect deterioration of chemical status, where it is the indirect result of modifications to physical characteristics (Article 4(7), first indent). 

```{mermaid}
:name: GWChemicalExemptionClass
:caption: Groundwater Body - Chemical Exemption - 4ᵗʰ cycle
:align: center
%%{init: {'theme': 'neutral'}}%%
classDiagram
class GWChemicalExemption{
	+ euGroundWaterBodyCode : wiseIdentifier
	+ gwPollutantCode : Substance
	/ exemptionType : ExemptionType
	+ exemptionRationale : ExemptionRationale [1..n]
	+ exemptionPeriod : ExemptionPeriod
	+ exemptionReference : referenceIdentifier [0..1]
	+ significantPressureType : PressureType [1..n]
}
```

The diagram with the criteria applicable to surface water chemical exemptions ({numref}`Exemptions_ChemicalExemption_Flowchart`)
is also applicable to groundwater bodies: note that, for groundwater, 
chemical exemptions can be applied to any groundwater pollutant. 

(heading_wfd_exemptions_groundwater_bodies_quantitative_exemptions)=
## Groundwater bodies - quantitative exemptions 

Quantitative exemptions are reported using the table in {numref}`GWQuantitativeExemptionClass`.

Reporting is mandatory if the following conditions apply:
* the waterbody is failing to achieve good quantitative status

```{mermaid}
:name: GWQuantitativeExemptionClass
:caption: Groundwater Body - Quantitative Exemption - 4ᵗʰ cycle
:align: center
%%{init: {'theme': 'neutral'}}%%
classDiagram
class GWQuantitativeExemption{
	+ euGroundWaterBodyCode : wiseIdentifier
	/ exemptionType : ExemptionType
	+ exemptionRationale : ExemptionRationale [1..n]
	+ exemptionPeriod : ExemptionPeriod
	+ exemptionReference : referenceIdentifier [0..1]
	+ significantPressureType : PressureType [1..n]
}
```

The diagram below presents the applicability criteria for the different exemption types
 ({numref}`Exemptions_QuantitativeExemption_Flowchart`).


```{mermaid} /DataModelReview/mmd/Exemptions_QuantitativeExemption_Flowchart.mmd
:name: Exemptions_QuantitativeExemption_Flowchart
:caption: Surface Water Body - Quantitative Exemption Decision Tree - 4ᵗʰ cycle
:align: center
```

(heading_wfd_exemptions_groundwater_bodies_protected_area_exemptions)=
## Groundwater bodies - protected area exemptions

Specific objectives may be set for waterbodies associated with some types of protected areas:

* Drinking water protection areas
* Natura 2000 protected sites included in the WFD register of protected areas

*If the specific objectives have not been met*, then exemptions may be reported.

(Note that the euProtectedAreaCode value is only requested for Natura 2000 sites.)

Based on the data reported in the 3ʳᵈ cycle, it is likely that the number of exemptions is relatively low. Therefore the attributes of related to exemptions were simply added to the GWAssociatedProtectedArea table ({numref}`GWAssociatedProtectedAreaClass`).

```{mermaid}
:name: GWAssociatedProtectedAreaClass
:caption: Groundwater Body - Associated Protected Area Exemption - 4ᵗʰ cycle
:align: center
%%{init: {'theme': 'neutral'}}%%
classDiagram
class GWAssociatedProtectedArea{
	+ euGroundWaterBodyCode : wiseIdentifier
	+ euProtectedAreaType : ProtectedAreaType
	+ euProtectedAreaCode : wiseIdentifier [0..1]
	+ protectedAreaObjectivesSet : YesNo
	+ protectedAreaObjectivesMet : YesNoUnknown
	/ exemptionType : ExemptionType [0..1]
	+ exemptionRationale : ExemptionRationale [0..n]
	+ exemptionPeriod : ExemptionPeriod [0..1]
	+ exemptionReference : referenceIdentifier [0..1]
	   } 
```

(heading_wfd_exemptions_codelists_associated_with_the_reporting_of_exemptions)=
## Codelists associated with the Exemption tables

Codelists associated with the reporting of exemptions are presented in {numref}`ExemptionCodelist`.

Note the dependencies between the two codelists, which will be verified by the qulaity control:
* the allowable values for the exemption type depent on the water body type (gwdArticle63_exemptionOfMeasures are not applicable to surface water bodies)
* the allowable values for the exemption rationale depend on the exemption type


```{mermaid}
:name: ExemptionCodelist
:caption: Codelists associated with the Exemption classes - 4ᵗʰ cycle
:align: center
%%{init: {'theme': 'neutral'}}%%
classDiagram
class ExemptionType{
    <<enumeration>>
    article44_extensionOfDeadline
    article45_lessStringentObjectives
    article46_temporaryDeterioration
    article47_newModificationOrProject
    gwdArticle63_exemptionOfMeasures
    notApplicable
    }

class ExemptionRationale{
    <<enumeration>>
    article44_technicalFeasibility
    article44_disproportionateCost
    article44_naturalConditions
    article45_feasibility
    article45_disproportionateCost
    article46_naturalCauses
    article46_forceMajeure
    article46_accidents
    article47_newModification
    article47_sustainableHumanDevelopment
    article47_shortTermImpact
    article47_relocationOfWaterOrSediment
    article47_domesticUrbanWasteWaterArticle154
    gwdArticle63_accidentsExceptionalCircumstances
    gwdArticle63_artificialRechargeAugmentation
    gwdArticle63_directDischarges
    gwdArticle63_interventionInSurfaceWaters
    gwdArticle63_measuresDisproportionateCost
    gwdArticle63_measuresIncreaseRisk
    gwdArticle63_smallDischarges
    notApplicable
    }
	
class ExemptionPeriod{
    <<enumeration>>
    upToOneYear
    upToThreeYears
    until2027
    until2033
    until2039
    lessStringentObjectiveAlreadyAchieved
    indeterminate
    }
```

(heading_wfd_exemptions_clarifications)=
## Clarifications requested by Member States

### Exemptions under Article 4(7a) - short term-impact

Introduced by the *Directive (EU) 2026/805 of the European Parliament and of the Council of 30 March 2026 amending Directive 2000/60/EC establishing a framework for Community action in the field of water policy, Directive 2006/118/EC on the protection of groundwater against pollution and deterioration and Directive 2008/105/EC on environmental quality standards in the field of water policy* [ELI: http://data.europa.eu/eli/dir/2026/805/oj](http://data.europa.eu/eli/dir/2026/805/oj). 


> ‘7a.   Member States will not be in breach of this Directive when any negative short-term impact on one or more quality elements of a body of water caused by a new project or a modification to an existing project in that body of water is no longer detectable after one year or, for biological quality elements, after a maximum of three years beyond initiation of the execution of the project, and all the following conditions are met:
> 
> (a) the negative impact is not the result of direct discharges, emissions or losses of a pollutant;
> 
> (b) the potential for the negative impact to occur is reliably assessed ex ante by a competent authority, and it is concluded that there would be no negative impact for the body of water concerned or any connected body of water after one year or, for biological quality elements, after a maximum of three years;
> 
> (c) an ex post verification is carried out;
> 
> (d) all practicable measures are taken to mitigate any negative impacts on the body and any connected bodies of water; and
> 
> (e) a summary of the main activities carried out in accordance with this paragraph, the relevant ex post verification results, and the measures taken to mitigate negative impacts, is included in the river basin management plan required under Article 13.
> 
> For the purposes of carrying out the ex -post verification under point (c) of the first subparagraph, existing monitoring arrangements set up pursuant to Annex V may be used and, where necessary, they shall be supplemented by additional ad-hoc monitoring.

**Actions taken:**

* A new code **article47_shortTermImpact** was added to the **ExemptionRationale** codelist (see {numref}`ExemptionCodelist`).
* Two new codes **upToOneYear** and **upToThreeYears** were added to the **ExemptionPeriod** codelist (see {numref}`ExemptionCodelist`).

**Quality checks to be implemented:**

* For ecological exemptions, the maximum exemption period is 3 years.

  * ERROR: table.name in ('SWEcologicalExemption') 
    AND exemptionRationale = 'article47_shortTermImpact' 
    AND exemptionPeriod NOT IN ('upToOneYear','upToThreeYears')

* For other exemptions, the maximum exemption period is 1 year.

  * ERROR: table.name in ('SWChemicalExemption','GWChemicalExemption','GWQuantitativeExemption') 
    AND exemptionRationale = 'article47_shortTermImpact' 
    AND exemptionPeriod NOT IN ('upToOneYear')

### Exemptions under Article 4(7b) - relocation of water or sediment

Introduced by the *Directive (EU) 2026/805 of the European Parliament and of the Council of 30 March 2026 amending Directive 2000/60/EC establishing a framework for Community action in the field of water policy, Directive 2006/118/EC on the protection of groundwater against pollution and deterioration and Directive 2008/105/EC on environmental quality standards in the field of water policy* [ELI: http://data.europa.eu/eli/dir/2026/805/oj](http://data.europa.eu/eli/dir/2026/805/oj). 

> 7b. Member States will not be in breach of this Directive when deterioration occurs in the status of a receiving body of surface water as a result of relocating, by human activity, water or sediment from the same or another body of surface water, or from a body of groundwater to the receiving body of surface water, without causing a net increase in pollutant load, and all the following conditions are met:
> 
> (a) all practicable steps, in particular the treatment of the water or sediment, if feasible, to minimise the transfer of pollutant load are taken to mitigate the adverse impact on the status of the bodies of water impacted by the relocation;
> 
> (b) the composition of the water or sediments to be relocated is established, and the relocation does not increase the overall risk to human health and the environment compared to the existing risk prior to the relocation;
> 
> (c) the receiving body of surface water is confirmed as already not being in good chemical status with respect to most of the pollutants relocated, and in particular with respect to the most persistent and bioaccumulative pollutants relocated, and the ecological status or potential of the receiving body of water is not expected to fall into a lower class as a result of the relocation of those pollutants;
> 
> (d) the relocation shall not result in an increase in the purification treatment required for the production of drinking water;
> 
> (e) within the receiving body of water, a zone where relocation is prohibited has been established around any abstraction point for water intended for human consumption;
> 
> (f) there are no significantly better environmental options for reasons of technical feasibility or disproportionate cost;
> 
> (g) the relocation is subject to prior regulation or authorisation; and
> 
> (h) a summary, including information related to points (a) to (g) of this paragraph and the reasons for the relocation, is included in the river basin management plan required under Article 13.’

**Actions taken:**

* A new code **article47_relocationOfWaterOrSediment** was added to the **ExemptionRationale** codelist (see {numref}`ExemptionCodelist`).

**Quality checks to be implemented:**

* Not applicable to ecological exemptions nor to quantitative exemptions

  * ERROR: table.name in ('SWEcologicalExemption','GWQuantitativeExemption') 
    AND exemptionRationale = 'article47_relocationOfWaterOrSediment' 

* If applied to chemical exemptions, 
  the receiving water body must be confirmed as already not being in good chemical status

  * ERROR: table.name in ('SWChemicalExemption','GWChemicalExemption') 
    AND exemptionRationale = 'article47_relocationOfWaterOrSediment' 
    AND GroundWaterBody.gwPollutantCausingFailure != 'No'

### Exemptions under Article 15(4) of the recast Urban Waste Water Treatment Directive 

*Clarification provided by DG ENV 2026-05-13 in reply to the clarification request during the WG DIS meeting on 2026-04-22:*

> The recast Urban Waste Water Treatment Directive was adopted 27/11/2024 and MS need to transpose the revised provisions by 31 July 2027.
> 
> Article 15(4) includes a new exemption from the obligations under the WFD if a water body deteriorates status or does not achieve good status as a result of :
> -	increased loads of domestic wastewater treated by a new/refurbished urban wastewater treatment plant, otherwise untreated (NOT industrial wastewater). 
> -	The increase is subject to prior authorisation setting out all technically feasible mitigation measures to minimize the negative impact of the UWWTP on water status
> -	all technically feasible mitigating measures are implemented to minimise the negative impact of other activities causing similar pressures in the same water bodies  
> -	There are no better environmental means that are not disproportionately costly (eg alternative points of discharge)
> -	The authorisation and its conditions are referred to in the RBMP

**Actions taken:**

* A new code **article47_domesticUrbanWasteWaterArticle154** was added to the **ExemptionRationale** codelist (see {numref}`ExemptionCodelist`).
* The {ref}`Exemptions_EcologicalExemption_Flowchart` was updated.
* The {ref}`Exemptions_ChemicalExemption_Flowchart` was updated.

**Quality checks to be implemented:**

* Not applicable to quantitative exemptions
  
  * ERROR: table.name in ('GWQuantitativeExemption') 
    AND exemptionRationale = 'article47_domesticUrbanWasteWaterArticle154' 

### Exemptions related to Protected Areas

*Clarification provided by DG ENV 2026-05-13 in reply to the clarification request during the WG DIS meeting on 2026-04-22:*

> -	Where objectives are set in terms of WFD quality /quantity status elements 
> (eg stricter quality standards are set for ‘good’ status in view of protecting certain species), 
> exemptions from good status can be applied. 
> -	If no such objectives have been set and protected areas objectives are only set under other legislation, 
> it’s not possible/necessary to exempt from compliance with those objectives: 
> non compliance would imply a breach of those other directives (and of WFD by virtue of Art 4(1)(c ) WFD)

**Actions taken:**

* no action required.

### Exemptions related to River Basin Specific Pollutants


```{warning}
  Clarification pending
```

## Annex - Exploratory analysis of data reported in the 3ʳᵈ cycle

This section is not relevant for the understanding of the proposed model. 
It contains some of the data analysis that supported the revision of the data model.

### Surface water - ecological exemptions at water body - 3ʳᵈ cycle 

In the 3ʳᵈ cycle, the reporting of ecological exemptions was requested:

* directly at surface water body level, in the SWEcologicalExemptionType class
* also at quality element level, in the qeEcologicalExemptionType element of the QualityElement class.

In 96.5% of the cases, the data reported is redundant with regard to the reporting at quality element level.

<details>
<summary>Show code</summary>

```sql

  /**
    "Duplicate" reporting of ecological exemptions 
    at surface water body level and at quality element level 
    in the 3ʳᵈ cycle reporting
  **/

  --  https://discodata.eea.europa.eu

  SELECT [exemptionTypeTable],
  COUNT (*) AS [numberOfRecords],
  COUNT  (DISTINCT [euSurfaceWaterBodyCode]) AS [numberOfSurfaceWaterBodies],
  COUNT  (DISTINCT [countryCode]) AS [numberOfCountries]
  FROM
  (
  SELECT COALESCE(qe.[countryCode], swb.[countryCode]) AS [countryCode],
    COALESCE(qe.[euSurfaceWaterBodyCode], swb.[euSurfaceWaterBodyCode]) AS [euSurfaceWaterBodyCode],
    COALESCE(qe.[exemptionType_QE], swb.[exemptionType_SWB]) AS [exemptionType],
    IIF(qe.[exemptionType_QE] IS NOT NULL AND swb.[exemptionType_SWB] IS NOT NULL, 'Both', 
      IIF(qe.[exemptionType_QE] IS NOT NULL, 'QE', 
        IIF(swb.[exemptionType_SWB] IS NOT NULL, 'SWB', 'None'))) AS [exemptionTypeTable]
  FROM 
    (SELECT DISTINCT [countryCode]
        ,[euSurfaceWaterBodyCode]
        ,[qeEcologicalExemptionTypeGroup] AS [exemptionType_QE]
      FROM [WISE_WFD].[LATEST].[SWB_SurfaceWaterBody_QualityElement_qeEcologicalExemptionType]
      WHERE hasDescriptiveData = 1
      and [qeEcologicalExemptionTypeGroup] != 'None'
      and [cYear] = 2022
      ) qe
  FULL OUTER JOIN 
    (SELECT DISTINCT [countryCode]
        ,[euSurfaceWaterBodyCode]
        ,[swEcologicalExemptionTypeGroup] AS [exemptionType_SWB]
      FROM [WISE_WFD].[latest].[SWB_SurfaceWaterBody_SWEcologicalExemptionType]
      WHERE hasDescriptiveData = 1
      and [swEcologicalExemptionTypeGroup] != 'None'
      and [cYear] = 2022
      ) swb
  ON qe.[countryCode] = swb.[countryCode]
  AND qe.[euSurfaceWaterBodyCode] = swb.[euSurfaceWaterBodyCode]
  AND qe.[exemptionType_QE] = swb.[exemptionType_SWB] ) t
  GROUP BY [exemptionTypeTable]

```

</details><br/>
	
Based on the analysis of the remaining 3.5% of cases, it is likely that the missing qualitity element level exemption is simply a reporting error not detected by the quality control.

<details>
<summary>Show code</summary>

```sql

  /**
    Analysis of the cases where 
    ecological exemptions reported at surface water body level
    do not match an exemption reported at quality element level 
    in the 3ʳᵈ cycle reporting
  **/

  --  https://discodata.eea.europa.eu

  SELECT COALESCE(qe.[countryCode], swb.[countryCode]) AS [countryCode],
    COALESCE(qe.[euSurfaceWaterBodyCode], swb.[euSurfaceWaterBodyCode]) AS [euSurfaceWaterBodyCode],
    COALESCE(qe.[swEcologicalStatusOrPotentialValue], swb.[swEcologicalStatusOrPotentialValue]) 
      AS [swEcologicalStatusOrPotentialValue],
    COALESCE(qe.[exemptionType_QE], swb.[exemptionType_SWB]) AS [exemptionType],
    IIF(qe.[exemptionType_QE] IS NOT NULL AND swb.[exemptionType_SWB] IS NOT NULL, 'Both', 
      IIF(qe.[exemptionType_QE] IS NOT NULL, 'QE', 
        IIF(swb.[exemptionType_SWB] IS NOT NULL, 'SWB', 'None'))) AS [exemptionTypeTable],  
    [numberOfQualityElementWithExemptions],
    [numberOfQualityElementExemptionTypes]
  FROM 
    (SELECT DISTINCT [countryCode]
        ,[euSurfaceWaterBodyCode]
        ,[swEcologicalStatusOrPotentialValue]
        ,[qeEcologicalExemptionTypeGroup] AS [exemptionType_QE]
      FROM [WISE_WFD].[LATEST].[SWB_SurfaceWaterBody_QualityElement_qeEcologicalExemptionType]
      WHERE hasDescriptiveData = 1
      AND [qeEcologicalExemptionTypeGroup] != 'None'
      AND [cYear] = 2022
      ) qe
  FULL OUTER JOIN 
    (SELECT DISTINCT [countryCode]
        ,[euSurfaceWaterBodyCode]
        ,[swEcologicalStatusOrPotentialValue]
        ,[swEcologicalExemptionTypeGroup] AS [exemptionType_SWB]
      FROM [WISE_WFD].[latest].[SWB_SurfaceWaterBody_SWEcologicalExemptionType]
      WHERE hasDescriptiveData = 1
      AND [swEcologicalExemptionTypeGroup] != 'None'
      AND [cYear] = 2022
      ) swb
  ON qe.[euSurfaceWaterBodyCode] = swb.[euSurfaceWaterBodyCode]
  AND qe.[exemptionType_QE] = swb.[exemptionType_SWB] 

  LEFT JOIN 

    (SELECT [euSurfaceWaterBodyCode],
        COUNT (DISTINCT [qeCode]) AS [numberOfQualityElementWithExemptions],
          COUNT (DISTINCT [qeEcologicalExemptionTypeGroup]) AS [numberOfQualityElementExemptionTypes]
      FROM [WISE_WFD].[LATEST].[SWB_SurfaceWaterBody_QualityElement_qeEcologicalExemptionType]
      WHERE hasDescriptiveData = 1
      AND [qeEcologicalExemptionTypeGroup] != 'None'
      AND [cYear] = 2022
      GROUP BY [euSurfaceWaterBodyCode]
      ) swb_with_qe_exemption

  ON swb_with_qe_exemption.[euSurfaceWaterBodyCode] = swb.[euSurfaceWaterBodyCode] 

  WHERE qe.[exemptionType_QE] IS NULL 
  AND [numberOfQualityElementExemptionTypes] IS NULL
  -- AND swb.[swEcologicalStatusOrPotentialValue] IN ('1','2')
  ORDER BY [numberOfQualityElementExemptionTypes]
```

</details><br/>

### Surface water - ecological exemptions at quality element level - 3ʳᵈ cycle

In 98.9% of the cases, only one type of exemption was reported per quality element and water body.

<details>
<summary>Show code</summary>

```sql

  /**
    Analysis of the number of different exemptions 
    reported at quality element level,
    for a given water body and quality element, 
    in the 3ʳᵈ cycle reporting
  **/

  --  https://discodata.eea.europa.eu

    SELECT [numberOfExemptionTypes],
      COUNT  (*) AS [numberOfRecords],
      COUNT  (DISTINCT [euSurfaceWaterBodyCode]) AS [numberOfWaterBodies],
      COUNT  (DISTINCT [countryCode]) AS [numberOfCountries]
    FROM 
      (SELECT [countryCode]
          ,[euSurfaceWaterBodyCode]
          ,[qeCode]
          ,COUNT(DISTINCT [qeEcologicalExemptionTypeGroup]) AS [numberOfExemptionTypes]
        FROM [WISE_WFD].[LATEST].[SWB_SurfaceWaterBody_QualityElement_qeEcologicalExemptionType]
        WHERE hasDescriptiveData = 1
        and [qeEcologicalExemptionTypeGroup] != 'None'
        and [cYear] = 2022
        GROUP BY [countryCode],[euSurfaceWaterBodyCode],[qeCode]) t
    GROUP BY [numberOfExemptionTypes]
    ORDER BY [numberOfExemptionTypes] ASC

```

</details><br/>
	
### Surface water - chemical exemptions by pollutant and water body - 3ʳᵈ cycle

In 99.1% of the cases, only one type of exemption was reported per priority substance and water body.
	
<details>
<summary>Show code</summary>
	
```sql

  /**
    Analysis of the number of different exemptions 
    reported at priority substance level,
    for a given water body and priority substance, 
    in the 3ʳᵈ cycle reporting
  **/

  -- https://discodata.eea.europa.eu/

  SELECT [numberOfExemptionTypes],
    COUNT  (*) AS [numberOfRecords],
    COUNT  (DISTINCT [euSurfaceWaterBodyCode]) AS [numberOfWaterBodies],
    COUNT  (DISTINCT [countryCode]) AS [numberOfCountries]
  FROM 
    (SELECT [countryCode]
        ,[euSurfaceWaterBodyCode]
        ,[swPrioritySubstanceCode]
        ,COUNT(DISTINCT [swChemicalExemptionTypeGroup]) AS [numberOfExemptionTypes]
      FROM [WISE_WFD].[LATEST].[SWB_SurfaceWaterBody_SWPrioritySubstance_SWChemicalExemptionType]
      WHERE hasDescriptiveData = 1
      and [swChemicalExemptionTypeGroup] != 'None'
      and [cYear] = 2022
      GROUP BY
        [countryCode]
        ,[euSurfaceWaterBodyCode]
        ,[swPrioritySubstanceCode]) t
    GROUP BY [numberOfExemptionTypes]
    ORDER BY [numberOfExemptionTypes] ASC

```	  

</details><br/>
	
### Groundwater - chemical exemptions by pollutant and water body - 3ʳᵈ cycle

In 99.5% of the cases, only one type of exemption was reported per pollutant and water body.

<details>
<summary>Show code</summary>
	
```sql

  /**
    Analysis of the number of different exemptions 
    reported at pollutant level,
    for a given water body and pollutant, 
    in the 3ʳᵈ cycle reporting
  **/

  -- https://discodata.eea.europa.eu/

  SELECT [numberOfExemptionTypes],
  COUNT  (*) AS [numberOfRecords],
  COUNT  (DISTINCT [euGroundWaterBodyCode]) AS [numberOfWaterBodies],
  COUNT  (DISTINCT [countryCode]) AS [numberOfCountries]
  FROM 
  (SELECT [countryCode]
          ,[euGroundWaterBodyCode]
          ,[gwPollutantCode]+isnull([gwPollutantOther],'') AS [pollutantCode]
          ,COUNT(DISTINCT [gwChemicalExemptionTypeGroup]) AS [numberOfExemptionTypes]
      FROM [WISE_WFD].[LATEST].[GWB_GroundWaterBody_GWPollutant_GWChemicalExemptionType]
      WHERE hasDescriptiveData = 1
      and [gwChemicalExemptionTypeGroup] != 'None'
      and [cYear] = 2022
      GROUP BY
          [countryCode]
          ,[euGroundWaterBodyCode]
          ,[gwPollutantCode]+isnull([gwPollutantOther],'') ) t
  GROUP BY [numberOfExemptionTypes]
  ORDER BY [numberOfExemptionTypes] ASC

```	   

</details><br/>
	
### Groundwater - quantitative exemptions by water body - 3ʳᵈ cycle

In 93.7% of the cases, only one type of exemption was reported per water body.

<details>
<summary>Show code</summary>
	
```sql

  /**
    Analysis of the number of different exemptions 
    reported for a given water body 
    in the 3ʳᵈ cycle reporting
  **/

  --   https://discodata.eea.europa.eu/

  SELECT [numberOfExemptionTypes],
    COUNT  (*) AS [numberOfRecords],
    COUNT  (DISTINCT [euGroundWaterBodyCode]) AS [numberOfWaterBodies],
    COUNT  (DISTINCT [countryCode]) AS [numberOfCountries]
  FROM 
  (SELECT [countryCode]
          ,[euGroundWaterBodyCode]
          ,COUNT(DISTINCT [gwQuantitativeExemptionTypeGroup]) AS [numberOfExemptionTypes]
      FROM [WISE_WFD].[latest].[GWB_GroundWaterBody_gwQuantitativeExemptionType]
      WHERE hasDescriptiveData = 1
      and [gwQuantitativeExemptionTypeGroup] != 'None'
      and [cYear] = 2022
      GROUP BY
          [countryCode]
          ,[euGroundWaterBodyCode] ) t
  GROUP BY [numberOfExemptionTypes]
  ORDER BY [numberOfExemptionTypes] ASC

```
	
</details><br/>
	
### Surface water - exemptions by associated protected area and water body - 3ʳᵈ cycle

This information is only reported for drinking waters, shellfish designated waters, and Natura 2000 protected sites included in the WFD register of protected areas, *if specific objectives have been set for the associated surface water body*.

<details>
<summary>Show code</summary>
	
```sql
  /**
    Analysis of the water bodies 
    for which specific objectives where set
    due to associated protected areas
    in the 3ʳᵈ cycle reporting
  **/

  --   https://discodata.eea.europa.eu/
  SELECT [protectedAreaType], [protectedAreaObjectivesSet], [protectedAreaObjectivesMet] 
      ,COUNT(DISTINCT [euSurfaceWaterBodyCode]) AS [numberOfWaterBodies]
      ,COUNT(DISTINCT [euProtectedAreaCode]) AS [numberOfAssociatedProtectedAreas]
    ,COUNT(DISTINCT [countryCode]) AS [numberOfCountries]
  FROM [WISE_WFD].[latest].[SWB_SurfaceWaterBody_SWAssociatedProtectedArea]
  WHERE hasDescriptiveData = 1
      AND [cYear] = 2022
      AND [protectedAreaType] 
        IN ('Drinking water protection area',
            'Shellfish designated water',
            'Natura 2000 protected site')
      AND [protectedAreaObjectivesMet] in ('No','Yes','Unknown')
  GROUP BY [protectedAreaType], [protectedAreaObjectivesSet], [protectedAreaObjectivesMet]

```
</details><br/>
	
Exemptions were reported for a total of 667 water bodies associated with a total of 327 protected areas, in 7 countries. 

<details>
<summary>Show code</summary>

```sql
  
  /**
    Analysis of the water bodies 
    for which exemptions were applied 
    when specific objectives set due to associated protected areas
    where not met
    in the 3ʳᵈ cycle reporting
  **/

  --   https://discodata.eea.europa.eu/
  
  SELECT LEFT([protectedAreaExemption],CHARINDEX('-',[protectedAreaExemption])-2) AS [protectedAreaExemptionType]
        ,COUNT(DISTINCT [euSurfaceWaterBodyCode]) AS [numberOfWaterBodies]
        ,COUNT(DISTINCT [euProtectedAreaCode]) AS [numberOfAssociatedProtectedAreas]
      ,COUNT(DISTINCT [countryCode]) AS [numberOfCountries]
    FROM [WISE_WFD].[latest].[SWB_SurfaceWaterBody_SWAssociatedProtectedArea_protectedAreaExemption]
    WHERE hasDescriptiveData = 1
      AND [cYear] = 2022
      AND [protectedAreaExemption] IS NOT NULL
      AND [protectedAreaExemption] != 'None'
      AND [protectedAreaType] IN 
        ('Drinking water protection area',
         'Natura 2000 protected site',
         'Shellfish designated water')
      AND [protectedAreaObjectivesMet] = 'No'
    GROUP BY
        LEFT([protectedAreaExemption],CHARINDEX('-',[protectedAreaExemption])-2)

 ```

</details><br/>
	
### Groundwater - exemptions by associated protected area and water body - 3ʳᵈ cycle

This information is only reported for drinking waters and Natura 2000 protected sites included in the WFD register of protected areas,
*if specific objectives have been set for the associated groundwater body*.

<details>
<summary>Show code</summary>
	
```sql
  
  /**
    Exemptions associated to protected areas in the 3ʳᵈ cycle reporting
  **/

  --   https://discodata.eea.europa.eu/

  SELECT [protectedAreaExemption]
        ,COUNT(DISTINCT [countryCode]) AS [Countries]
        ,COUNT(DISTINCT[euGroundWaterBodyCode]) AS [WaterBodies]
        ,COUNT(DISTINCT[euProtectedAreaCode]) AS [ProtectedAreas]
    FROM [WISE_WFD].[latest].[GWB_GroundWaterBody_GWAssociatedProtectedArea_protectedAreaExemption]
    WHERE [cYear] = 2022 
    AND [hasDescriptiveData] = 1 
    AND [protectedAreaType] IN ('Natura 2000 protected site', 'Drinking water protection area')
    AND [protectedAreaExemption] != 'None'
    AND [protectedAreaObjectivesMet] = 'No'
    GROUP BY [protectedAreaExemption],[protectedAreaObjectivesMet]

```
</details><br/>
	
Exemptions were reported for a total of 198 water bodies associated with a total of 273 protected areas, in 9 countries. 

|protectedAreaExemption	|Countries	|WaterBodies|ProtectedAreas|
|---|---|---|---|
|Article 4(4) - Disproportionate cost	|2|	32|	50|
|Article 4(4) - Natural conditions	|8|	122|	182|
|Article 4(4) - Technical feasibility	|5|	63|	76|
|Article 4(5) - Disproportionate cost	|1|	14|	14|
|Article 4(5) - Technical feasibility	|2|	18|	18|


<details>
<summary>Show code</summary>
	
```sql

  /**
    Exemptions associated to protected areas in the 3ʳᵈ cycle reporting
  **/

  --   https://discodata.eea.europa.eu/
  SELECT [protectedAreaExemption] 
        ,COUNT(DISTINCT [countryCode]) AS [Countries]
        ,COUNT(DISTINCT[euSurfaceWaterBodyCode]) AS [WaterBodies]
        ,COUNT(DISTINCT[euProtectedAreaCode]) AS [ProtectedAreas]
    FROM [WISE_WFD].[latest].[SWB_SurfaceWaterBody_SWAssociatedProtectedArea_protectedAreaExemption]
    WHERE [cYear] = 2022 
    AND [hasDescriptiveData] = 1 
    AND [protectedAreaType] IN ('Natura 2000 protected site', 'Drinking water protection area','Shellfish designated water')
    AND [protectedAreaExemption] != 'None'
    AND [protectedAreaObjectivesMet] = 'No'
    GROUP BY [protectedAreaExemption],[protectedAreaObjectivesMet]
 ```
	
</details><br/>

|protectedAreaExemption|Countries|WaterBodies|ProtectedAreas|
|---|---|---|---|
|Article 4(4) - Disproportionate cost|	2|	336|	87|
|Article 4(4) - Natural conditions|	4|	193|	190|
|Article 4(4) - Technical feasibility|	4|	426|	123|
|Article 4(5) - Disproportionate cost|	1|	72|	12|
|Article 4(5) - Technical feasibility|	2|	74|	14|

(heading_wfd_wfd_exemptions_references)=
## References

The complete schemas for the 3ʳᵈ cycle of reporting can be found in the [WFD2022 EAP file](https://cdr.eionet.europa.eu/help/WFD/WFD_715_2022/UML%20Data%20specification/WFD2022.EAP).

