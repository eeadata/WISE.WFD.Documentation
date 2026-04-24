# WFD - Exemptions

## Reporting of Exemptions - 3rd cycle

* The information related to exemptions in the surface water methodologies schema (SWExemption class, see {numref}`SWExemptions_GWExemptions`)
  will no longer requested in the structured data reporting for the 4th cycle (i.e. the it is provided only in the RBMP documents).
  
* The information related to exemptions in the groundwater water methodologies schema (GWExemption class, see {numref}`SWExemptions_GWExemptions`).
  will no longer requested in the structured data reporting for the 4th cycle (i.e. it is provided only in the RBMP documents).
  
  
```{mermaid}  /DataModelReview/mmd/Exemptions_3rdCycle_SWMET_GWMET_ClassDiagram.mmd
:name: SWExemptions_GWExemptions
:caption: SWExemptions and GWExemptions - 3rd cycle - OBSOLETE
:align: center
```

## Reporting of Exemptions - 4th cycle

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
:caption: Exemption - 4th cycle - Abstract pattern for illustrative purposes
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

## Surface Water Bodies - Ecological exemptions by Quality Element

Ecological exemptions are reported using the table in {numref}`SWEcologicalExemptionClass`.

Ecological exemptions are not applicable to Territorial Waters.
For other surface water body categories, reporting is mandatory when the following conditions apply:
* the qeCode value starts with QE1 or qeCode starts with QE3 
* and the quality element is causing failure to achieve good status, i.e. qeStatusOrPotentialValue in (3, 4, 5).

Ecological exemptions are reported at Quality Element level only:
* exemptions are not applicable to quality elements with unknown status
* exemptions are not applicable to quality elements not used in the ecological status assessment.

(Note that the duplicate reporting of the ecological exemptions - both at surface water body level *and* at quality element level - is removed in the revised model for the 4th cycle reporting.)

```{mermaid}
:name: SWEcologicalExemptionClass
:caption: Surface Water Body - Ecological Exemption - 4th cycle
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

The diagram below presents the applicability criteria for the different exemption types ({numref}`SWEcologicalExemptionFlowchart`).

```{mermaid} /DataModelReview/mmd/Exemptions_EcologicalExemption_Flowchart.mmd
:name: SWEcologicalExemptionFlowchart
:caption: Surface Water Body - Ecological Exemption Decision Tree - 4th cycle
:align: center
```

## Surface Water Bodies - Chemical exemptions by Priority Substance

Chemical exemptions are reported using the table in {numref}`SWChemicalExemptionClass`.

Reporting is mandatory if the following conditions apply:
* the swPollutantCode value is a 2013 Priority Substance  
* all the Priority Substance is causing failure to achieve good status (i.e. swPollutantCausingFailure = 'Yes').

Chemical exemptions are reported at Pollutant level only:
* exemptions are only applicable to priority substances
* exemptions are not applicable to substances with unknown status.

Article 4(7) exemptions may be applicable for indirect deterioration of chemical status, where it is the indirect result of modifications to physical characteristics (Article 4(7), first indent). 

In the 4th cycle of reporting, exemptions associated with river basin specific pollutants 
are reported as exemptions associated with the quality element "QE3-3 - River Basin Specific Pollutants".

```{mermaid}
:name: SWChemicalExemptionClass
:caption: Surface Water Body - Chemical Exemption - 4th cycle
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

The diagram below presents the applicability criteria for the different exemption types ({numref}`ChemicalExemptionFlowchart`).

```{mermaid} /DataModelReview/mmd/Exemptions_ChemicalExemption_Flowchart.mmd
:name: ChemicalExemptionFlowchart
:caption: Surface Water Body - Chemical Exemption Decision Tree - 4th cycle
:align: center
```

## Surface Water Bodies - Protected area exemptions

Specific objectives may be set for waterbodies associated with some types of protected areas:
* Shellfish designated waters
* Drinking water protection areas
* Natura 2000 protected sites included in the WFD register of protected areas

*If the specific objectives have not been met*, then exemptions may be reported.
(Note that the euProtectedAreaCode value is only requested for Natura 2000 sites.)

Based on the data reported in the 3rd cycle, it is likely that the number of exemptions is relatively low. Therefore the attributes of related to exemptions were simply added to the SWAssociatedProtectedArea table ({numref}`SWAssociatedProtectedAreaClass`).

```{mermaid}
:name: SWAssociatedProtectedAreaClass
:caption: Surface Water Body - Associated Protected Area Exemption - 4th cycle
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

## Groundwater Bodies - Chemical exemptions by Pollutant

Chemical exemptions are reported using the table in {numref}`GWChemicalExemptionClass`.

Reporting is mandatory if the following condition applies:
* the substance is causing failure to achieve good status (i.e. gwPollutantCausingFailure = 'Yes').

Chemical exemptions are reported at Pollutant level only:
* exemptions are not applicable to substances with unknown status.

Article 4(7) exemptions may be applicable for indirect deterioration of chemical status, where it is the indirect result of modifications to physical characteristics (Article 4(7), first indent). 

```{mermaid}
:name: GWChemicalExemptionClass
:caption: Groundwater Body - Chemical Exemption - 4th cycle
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

The diagram with the criteria applicable to surface water chemical exemptions ({numref}`ChemicalExemptionFlowchart`)
is also applicable to groundwater bodies: note that, for groundwater, 
chemical exemptions can be applied to any groundwater pollutant. 

## Groundwater Bodies - Quantitative exemptions 

Quantitative exemptions are reported using the table in {numref}`GWQuantitativeExemptionClass`.

Reporting is mandatory if the following conditions apply:
* the waterbody is failing to achieve good quantitative status

```{mermaid}
:name: GWQuantitativeExemptionClass
:caption: Groundwater Body - Quantitative Exemption - 4th cycle
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
 ({numref}`QuantitativeExemptionFlowchart`).


```{mermaid} /DataModelReview/mmd/Exemptions_QuantitativeExemption_Flowchart.mmd
:name: QuantitativeExemptionFlowchart
:caption: Surface Water Body - Quantitative Exemption Decision Tree - 4th cycle
:align: center
```

## Groundwater Bodies - Protected area exemptions

Specific objectives may be set for waterbodies associated with some types of protected areas:

* Drinking water protection areas
* Natura 2000 protected sites included in the WFD register of protected areas

*If the specific objectives have not been met*, then exemptions may be reported.

(Note that the euProtectedAreaCode value is only requested for Natura 2000 sites.)

Based on the data reported in the 3rd cycle, it is likely that the number of exemptions is relatively low. Therefore the attributes of related to exemptions were simply added to the GWAssociatedProtectedArea table ({numref}`GWAssociatedProtectedAreaClass`).

```{mermaid}
:name: GWAssociatedProtectedAreaClass
:caption: Groundwater Body - Associated Protected Area Exemption - 4th cycle
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

## Codelists associated with the Exemptions

Codelists associated with the reporting of exemptions are presented in {numref}`ExemptionCodelist`.

Note the dependencies between the two codelists, which will be verified by the qulaity control:
* the allowable values for the exemption type depent on the water body type (gwdArticle63_exemptionOfMeasures are not applicable to surface water bodies)
* the allowable values for the exemption rationale depend on the exemption type


```{mermaid}
:name: ExemptionCodelist
:caption: Codelists associated with the Exemption classes - 4th cycle
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
    until2027
    until2033
    until2039
    lessStringentObjectiveAlreadyAchieved
    indeterminate
    }
```


## Annex - Exploratory analysis of data reported in the 3rd cycle

This section is not relevant for the understanding of the proposed model. 
It contains some of the data analysis that supported the revision of the data model.

### Surface water - ecological exemptions at water body - 3rd cycle 

In the 3rd cycle, the reporting of ecological exemptions was requested:

* directly at surface water body level, in the SWEcologicalExemptionType class
* also at quality element level, in the qeEcologicalExemptionType element of the QualityElement class.

In 96.5% of the cases, the data reported is redundant with regard to the reporting at quality element level.

<details>
<summary>Show code</summary>

```sql

  /**
    "Duplicate" reporting of ecological exemptions 
    at surface water body level and at quality element level 
    in the 3rd cycle reporting
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
    in the 3rd cycle reporting
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

### Surface water - ecological exemptions at quality element level - 3rd cycle

In 98.9% of the cases, only one type of exemption was reported per quality element and water body.

<details>
<summary>Show code</summary>

```sql

  /**
    Analysis of the number of different exemptions 
    reported at quality element level,
    for a given water body and quality element, 
    in the 3rd cycle reporting
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
	
### Surface water - Chemical exemptions by pollutant and water body - 3rd cycle

In 99.1% of the cases, only one type of exemption was reported per priority substance and water body.
	
<details>
<summary>Show code</summary>
	
```sql

  /**
    Analysis of the number of different exemptions 
    reported at priority substance level,
    for a given water body and priority substance, 
    in the 3rd cycle reporting
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
	
### Groundwater - Chemical exemptions by pollutant and water body - 3rd cycle

In 99.5% of the cases, only one type of exemption was reported per pollutant and water body.

<details>
<summary>Show code</summary>
	
```sql

  /**
    Analysis of the number of different exemptions 
    reported at pollutant level,
    for a given water body and pollutant, 
    in the 3rd cycle reporting
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
	
### Groundwater - Quantitative exemptions by water body - 3rd cycle

In 93.7% of the cases, only one type of exemption was reported per water body.

<details>
<summary>Show code</summary>
	
```sql

  /**
    Analysis of the number of different exemptions 
    reported for a given water body 
    in the 3rd cycle reporting
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
	
### Surface water - Exemptions by associated protected area and water body - 3rd cycle

This information is only reported for drinking waters, shellfish designated waters, and Natura 2000 protected sites included in the WFD register of protected areas, *if specific objectives have been set for the associated surface water body*.

<details>
<summary>Show code</summary>
	
```sql
  /**
    Analysis of the water bodies 
    for which specific objectives where set
    due to associated protected areas
    in the 3rd cycle reporting
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
    in the 3rd cycle reporting
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
	
### Groundwater - Exemptions by associated protected area and water body - 3rd cycle

This information is only reported for drinking waters and Natura 2000 protected sites included in the WFD register of protected areas,
*if specific objectives have been set for the associated groundwater body*.

<details>
<summary>Show code</summary>
	
```sql
  
  /**
    Analysis of the water bodies 
    for which specific objectives where set
    due to associated protected areas
    in the 3rd cycle reporting
  **/

  --   https://discodata.eea.europa.eu/

  SELECT [protectedAreaType], [protectedAreaObjectivesSet], [protectedAreaObjectivesMet] 
      ,COUNT(DISTINCT [euGroundWaterBodyCode]) AS [numberOfWaterBodies]
      ,COUNT(DISTINCT [euProtectedAreaCode]) AS [numberOfAssociatedProtectedAreas]
    ,COUNT(DISTINCT [countryCode]) AS [numberOfCountries]
  FROM [WISE_WFD].[latest].[GWB_GroundWaterBody_GWAssociatedProtectedArea]
  WHERE hasDescriptiveData = 1
      AND [cYear] = 2022
      AND [protectedAreaType] 
        IN ('Drinking water protection area','Natura 2000 protected site')
      AND [protectedAreaObjectivesMet] in ('No','Yes','Unknown')
  GROUP BY [protectedAreaType], [protectedAreaObjectivesSet], [protectedAreaObjectivesMet] 

```
</details><br/>
	
Exemptions were reported for a total of 198 water bodies associated with a total of 273 protected areas, in 9 countries. 

<details>
<summary>Show code</summary>
	
```sql

  /**
    Analysis of the water bodies 
    for which exemptions were applied 
    when specific objectives set due to associated protected areas
    where not met
    in the 3rd cycle reporting
  **/

  --   https://discodata.eea.europa.eu/

  SELECT LEFT([protectedAreaExemption],CHARINDEX('-',[protectedAreaExemption])-2) AS [protectedAreaExemptionType]
        ,COUNT(DISTINCT [euGroundWaterBodyCode]) AS [numberOfWaterBodies]
        ,COUNT(DISTINCT [euProtectedAreaCode]) AS [numberOfAssociatedProtectedAreas]
      ,COUNT(DISTINCT [countryCode]) AS [numberOfCountries]
    FROM [WISE_WFD].[latest].[GWB_GroundWaterBody_GWAssociatedProtectedArea_protectedAreaExemption]
    WHERE hasDescriptiveData = 1
      AND [cYear] = 2022
      AND [protectedAreaExemption] IS NOT NULL
      AND [protectedAreaExemption] != 'None'
      AND [protectedAreaType] 
        IN ('Drinking water protection area','Natura 2000 protected site')
      AND [protectedAreaObjectivesMet] = 'No'
    GROUP BY
        LEFT([protectedAreaExemption],CHARINDEX('-',[protectedAreaExemption])-2)

 ```
	
</details><br/>

