# WFD - Exemptions

## Reporting of Exemptions - 3rd cycle

* The information related to exemptions in the surface water methodologies schema (SWExemption class)
  will no longer requested in the structured data reporting for the 4th cycle (i.e. it is provided only in the RBMP documents).
  
* The information related to exemptions in the groundwater water methodologies schema (GWExemption class)
  will no longer requested in the structured data reporting for the 4th cycle (i.e. it is provided only in the RBMP documents).
  
  
```{mermaid}
:name: SWExemptions_GWExemptions
:caption: SWExemptions and GWExemptions - 3rd cycle [no longer requested]
:align: center

classDiagram 
namespace SWMET{
class SWExemptions ["«XSDcomplexType»
SWExemptions"]{
  «XSElement»
  + swExemption44Impact: SignificantImpactType_Enum [1..*]
  + swExemption44Driver: Driver_Enum [1..*]
  + swExemption45Impact: SignificantImpactType_Enum [1..*]
  + swExemption45Driver: Driver_Enum [1..*]
  + swDisproportionateCost: YesNoCode_Enum
  + swDisproportionateCostScale: GeographicalScale_Enum [0..*]
  + swDisproportionateCostAnalysis: DisproportionateCostAnalysis_Enum [0..*]
  + swDisproportionateCostAlternativeFinancing: DisproportionateCostAlternativeFinancing_Enum [0..*]
  + swDisproportionateCostOtherEULegislation: YesNoCode_Enum [0..1]
  + swTechnicalInfeasibility: TechnicalInfeasibility_Enum [1..*]
  + swNaturalConditions: SWNaturalConditions_Enum [1..*]
  + swExemption46: Exemption46_Enum [1..*]
  + swExemption47: Exemption47_Enum [1..*]
  + swExemptionsTransboundary: YesNoNotApplicable_Union_Enum
  + swExemptionsReference: ReferenceType [1..*]
  + driversSWExemptionsReference: ReferenceType [1..*]
}
}
namespace GWMET{
class GWExemptions["«XSDcomplexType» GWExemptions"]{
  «XSDElement»
  + gwExemption44Impact: SignificantImpactType_Enum [1..*]
  + gwExemption44Driver: Driver_Enum [1..*]
  + gwExemption45Impact: SignificantImpactType_Enum [1..*]
  + gwExemption45Driver: Driver_Enum [1..*]
  + gwDisproportionateCost: YesNoCode_Enum
  + gwDisproportionateCostScale: GeographicalScale_Enum [0..*]
  + gwDisproportionateCostAnalysis: DisproportionateCostAnalysis_Enum [0..*]
  + gwDisproportionateCostAlternativeFinancing: DisproportionateCostAlternativeFinancing_Enum [0..*]
  + gwDisproportionateCostOtherEULegislation: YesNoCode_Enum [0..1]
  + gwTechnicalInfeasibility: TechnicalInfeasibility_Enum [1..*]
  + gwNaturalConditions: GWNaturalConditions_Enum [1..*]
  + gwExemption46: Exemption46_Enum [1..*]
  + gwExemption47: Exemption47_Enum [1..*]
  + gwExemptionsTransboundary: YesNoNotApplicable_Union_Enum
  + gwExemptionsReference: ReferenceType [1..*]
  + driversGWExemptionsReference: ReferenceType [1..*]
}
}

```


## Reporting of Exemptions - 4th cycle

The reporting of ecological, chemical and quantitative exemptions is aligned into tables with a similar structure:

  * The waterbody to which the exemption applies is always identified.
  * For ecological exemptions, the quality element is identified.
  * For chemical exemptions, the substance is identified.
  * For exemptions associated with protected areas were specific objectives were set but not met, the protected area is identified.

The remaining attributes identify the exemption type (exemptionType), the reason why it is applied (exemptionRationale), the expected exemption period (exemptionPeriod), and the significant pressure causing failure, if applicable (exemptionPressureType).
Reference to additional information in the RBMPs documentation can be provided via the exemptionReference.

Ecological exemptions are only reported at quality element level, avoiding duplication.

The *exemptionPeriod* covers the period until good status is achieved: this attribute replaces the former attributes  *swEcologicalStatusOrPotentialExpectedAchievementDate*, *swChemicalStatusExpectedAchievementDate*, *gwChemicalStatusExpectedAchievementDate* and *gwQuantitativeStatusExpectedAchievementDate*.


```{mermaid}
:name: ExemptionAbstractClass
:caption: Exemption - 4th cycle - Abstract pattern for illustrative purposes
:align: center
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

Ecological exemptions are not applicable to Territorial Waters.
For other surface water body categories, reporting is mandatory when the following conditions apply:
* the qeCode value starts with QE1 or qeCode starts with QE3 
* and the quality element is causing failing to achieve good status, i.e. qeStatusOrPotentialValue in (3, 4, 5).

Ecological exemptions are reported at Quality Element level only:
* exemptions are not applicable to quality elements with unknown status
* exemptions are not applicable to quality elements not used in the ecological status assessment.

```{mermaid}
:name: SWEcologicalExemptionClass
:caption: Surface Water Body - Ecological Exemption - 4th cycle
:align: center
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

The diagram below presents the applicability criteria for the different exemption types.

```{mermaid} /DataModelReview/mmd/EcologicalExemption_Flowchart.mmd
:name: SWEcologicalExemptionFlowchart
:caption: Surface Water Body - Ecological Exemption Decision Tree - 4th cycle
:align: center
```

## Surface Water Bodies - Chemical exemptions by Priority Substance

Reporting is mandatory if the following conditions apply:
* the swPollutantCode value is a 2013 Priority Substance  
* all the Priority Substance is causing failing to achieve good status (i.e. swPollutantCausingFailure = 'Yes').

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

The diagram below presents the applicability criteria for the different exemption types.

```{mermaid} /DataModelReview/mmd/ChemicalExemption_Flowchart.mmd
:name: ChemicalExemptionFlowchart
:caption: Surface Water Body - Chemical Exemption Decision Tree - 4th cycle
:align: center
```

## Surface Water Bodies - Protected area exemptions

Specific objectives may be set for waterbodies associated with some types of protected areas:
* Shellfish designated waters
* Drinking water protection areas
* Natura 2000 protected sites included in the WFD register of protected areas

If the specific objectives have not been met, then exemptions may be reported.

(Note that the euProtectedAreaCode value is only requested for Natura 2000 sites.)

```{mermaid}
:name: SWAssociatedProtectedAreaClass
:caption: Surface Water Body - Associated Protected Area Exemption - 4th cycle
:align: center
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

Reporting is mandatory if the following conditions apply:
* the substance is causing failing to achieve good status (i.e. gwPollutantCausingFailure = 'Yes').

Chemical exemptions are reported at Pollutant level only:
* exemptions are not applicable to substances with unknown status.

Article 4(7) exemptions may be applicable for indirect deterioration of chemical status, where it is the indirect result of modifications to physical characteristics (Article 4(7), first indent). 

```{mermaid}
:name: GWChemicalExemptionClass
:caption: Groundwater Body - Chemical Exemption - 4th cycle
:align: center
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

The diagram with the criteria applicable to surface water chemical exemptions 
is also applicable to groundwater bodies: note that, for groundwater, 
chemical exemptions can be applied to any groundwater pollutant. 

## Groundwater Bodies - Quantitative exemptions 

Reporting is mandatory if the following conditions apply:
* the waterbody is failing to achieve good quantitative status

```{mermaid}
:name: GWQuantitativeExemptionClass
:caption: Groundwater Body - Quantitative Exemption - 4th cycle
:align: center
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

The diagram below presents the applicability criteria for the different exemption types.


```{mermaid} /DataModelReview/mmd/QuantitativeExemption_Flowchart.mmd
:name: QuantitativeExemptionFlowchart
:caption: Surface Water Body - Quantitative Exemption Decision Tree - 4th cycle
:align: center
```

## Groundwater Bodies - Protected area exemptions

Specific objectives may be set for waterbodies associated with some types of protected areas:

* Drinking water protection areas
* Natura 2000 protected sites included in the WFD register of protected areas

If the specific objectives have not been met, then exemptions may be reported.

(Note that the euProtectedAreaCode value is only requested for Natura 2000 sites.)

```{mermaid}
:name: GWAssociatedProtectedAreaClass
:caption: Groundwater Body - Associated Protected Area Exemption - 4th cycle
:align: center
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

Note the dependencies between the two codelists, which will be verified by the qulaity control:
* the allowable values for the exemption type depent on the water body type (gwdArticle63_exemptionOfMeasures are not applicable to surface water bodies)
* the allowable values for the exemption rationale depend on the exemption type


```{mermaid}
:name: ExemptionCodelist
:caption: Codelists associated with the Exemption classes - 4th cycle
:align: center
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
    article45_technicalFeasibility
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

</details>
	
Based on the analysis of the remaining 3.5% of cases, it is likely that the missing qualitity element level exemption is simply a reporting error not detected by the quality control.

<details>
<summary>Show code</summary>

```sql

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

</details>

### Surface water - ecological exemptions at quality element level - 3rd cycle

In 98.9% of the cases, only one type of exemption was reported per quality element and water body.

<details>
<summary>Show code</summary>

```sql

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

</details>
	
### Surface water - Chemical exemptions by pollutant and water body - 3rd cycle

In 99.1% of the cases, only one type of exemption was reported per priority substance and water body.
	
<details>
<summary>Show code</summary>
	
```sql

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

</details>
	
### Groundwater - Chemical exemptions by pollutant and water body - 3rd cycle

In 99.5% of the cases, only one type of exemption was reported per pollutant and water body.

<details>
<summary>Show code</summary>
	
```sql

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

</details>
	
### Groundwater - Quantitative exemptions by water body - 3rd cycle

In 93.7% of the cases, only one type of exemption was reported per water body.

<details>
<summary>Show code</summary>
	
```sql

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
	
</details>
	
### Surface water - Exemptions by associated protected area and water body - 3rd cycle

This information is only reported for drinking waters, shellfish designated waters, and Natura 2000 protected sites included in the WFD register of protected areas, *if specific objectives have been set for the associated surface water body*.

<details>
<summary>Show code</summary>
	
```sql

  --   https://discodata.eea.europa.eu/
  SELECT [protectedAreaType], [protectedAreaObjectivesSet], [protectedAreaObjectivesMet] 
      ,COUNT(DISTINCT [euSurfaceWaterBodyCode]) AS [numberOfWaterBodies]
      ,COUNT(DISTINCT [euProtectedAreaCode]) AS [numberOfAssociatedProtectedAreas]
    ,COUNT(DISTINCT [countryCode]) AS [numberOfCountries]
  FROM [WISE_WFD].[latest].[SWB_SurfaceWaterBody_SWAssociatedProtectedArea]
  WHERE hasDescriptiveData = 1
      AND [cYear] = 2022
      AND [protectedAreaType] IN ('Drinking water protection area','Shellfish designated water','Natura 2000 protected site')
      AND [protectedAreaObjectivesMet] in ('No','Yes','Unknown')
  GROUP BY [protectedAreaType], [protectedAreaObjectivesSet], [protectedAreaObjectivesMet]

```
</details>
	
Exemptions were reported for a total of 667 water bodies associated with a total of 327 protected areas, in 7 countries. 

<details>
<summary>Show code</summary>

```sql

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
      AND [protectedAreaType] IN ('Drinking water protection area','Natura 2000 protected site','Shellfish designated water')
      AND [protectedAreaObjectivesMet] = 'No'
    GROUP BY
        LEFT([protectedAreaExemption],CHARINDEX('-',[protectedAreaExemption])-2)

 ```

</details>
	
### Groundwater - Exemptions by associated protected area and water body - 3rd cycle

This information is only reported for drinking waters and Natura 2000 protected sites included in the WFD register of protected areas,
*if specific objectives have been set for the associated groundwater body*.

<details>
<summary>Show code</summary>
	
```sql

  SELECT [protectedAreaType], [protectedAreaObjectivesSet], [protectedAreaObjectivesMet] 
      ,COUNT(DISTINCT [euGroundWaterBodyCode]) AS [numberOfWaterBodies]
      ,COUNT(DISTINCT [euProtectedAreaCode]) AS [numberOfAssociatedProtectedAreas]
    ,COUNT(DISTINCT [countryCode]) AS [numberOfCountries]
  FROM [WISE_WFD].[latest].[GWB_GroundWaterBody_GWAssociatedProtectedArea]
  WHERE hasDescriptiveData = 1
      AND [cYear] = 2022
      AND [protectedAreaType] IN ('Drinking water protection area','Natura 2000 protected site')
      AND [protectedAreaObjectivesMet] in ('No','Yes','Unknown')
  GROUP BY [protectedAreaType], [protectedAreaObjectivesSet], [protectedAreaObjectivesMet] 

  SELECT [protectedAreaType], [protectedAreaObjectivesSet], [protectedAreaObjectivesMet] 
      ,COUNT(DISTINCT [euSurfaceWaterBodyCode]) AS [numberOfWaterBodies]
      ,COUNT(DISTINCT [euProtectedAreaCode]) AS [numberOfAssociatedProtectedAreas]
    ,COUNT(DISTINCT [countryCode]) AS [numberOfCountries]
  FROM [WISE_WFD].[latest].[SWB_SurfaceWaterBody_SWAssociatedProtectedArea]
  WHERE hasDescriptiveData = 1
      AND [cYear] = 2022
      AND [protectedAreaType] IN ('Drinking water protection area','Shellfish designated water','Natura 2000 protected site')
      AND [protectedAreaObjectivesMet] in ('No','Yes','Unknown')
  GROUP BY [protectedAreaType], [protectedAreaObjectivesSet], [protectedAreaObjectivesMet] 

```
</details>
	
Exemptions were reported for a total of 198 water bodies associated with a total of 273 protected areas, in 9 countries. 

<details>
<summary>Show code</summary>
	
```sql

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
      AND [protectedAreaType] IN ('Drinking water protection area','Natura 2000 protected site')
      AND [protectedAreaObjectivesMet] = 'No'
    GROUP BY
        LEFT([protectedAreaExemption],CHARINDEX('-',[protectedAreaExemption])-2)

 ```
	
</details>