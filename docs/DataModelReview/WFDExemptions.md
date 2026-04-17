# WFD Exemptions

## Reporting of Exemptions - 3rd cycle

* The information related to exemptions in the surface water methodologies schema (SWExemption class)
  will no longer requested in the structured data reporting for the 4th cycle (i.e. it is provided only in the RBMP documents).
  
* The information related to exemptions in the groundwater water methodologies schema (GWExemption class)
  will no longer requested in the structured data reporting for the 4th cycle (i.e. it is provided only in the RBMP documents).
  
  
```{mermaid}
classDiagram 
namespace SWMET{
class SWExemptions <<XSDComplexType>> {
  <<XSElement>>
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
class GWExemptions <<XSDComplexType>> {
  <<XSDElement>>
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
classDiagram
class Exemption <<Abstract>>{
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
%%{init: {'theme': 'default'}}%%
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

```{mermaid}
:file: mmd/EcologicalExemptionType_Flowchart.mmd
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
---
config:
  class:
    hideEmptyMembersBox: true
  layout: dagre
  theme: neutral
  look: neo
title: Surface Water Body - Chemical Exemptions - 4th cycle
---
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

```{mermaid}
%%{init: {'theme': 'neutral'}}%%

flowchart LR

%% Surface Water Chemical Exemptions and Groundwater Chemical Exemptions
title@{ shape: braces, label: "Surface Water Chemical Exemptions \n and Groundwater Chemical Exemptions" }

%% Defining the nodes
		
initial([start])
final([end])

%% duplicate nodeS for just for flowchart readability
hasNoApplicableExemption_1("no exemption \n required"):::stateBlue
hasNoApplicableExemption_2("no exemption \n applicable"):::stateRed
hasNoApplicableExemption_3("no exemption \n required"):::stateBlue
hasNoApplicableExemption_4("no exemption \n applicable"):::stateRed

hasExemption44("Article 4(4) \n Extension of deadline"):::state
hasExemption45("Article 4(5) \n Less stringent objectives"):::state
hasExemption46("Article 4(6) \n Temporary deterioration"):::state
hasExemption47("Article 4(7) \n New modification/project"):::state

%% Defining the decisions

%% WE NEED THE LISTS!
is2026Substance{"2008 or 2013 \n priority substance?"}
is2013Substance{"2013 substance?"}

isCausingFailureIn2027{"Causing failure \n in 2027?"}
isDeteriorationExpected{"Deterioration expected \n beyond 2027?"}
isDeteriorationObserved{"Deterioration observed \n in 2027 or earlier?"}
isGoodStatusAchievable{"Is good status \n achievable?"}
isDelayDueToNaturalConditions{"Delay due to \n natural conditions?"}
isDelayDueToFeasibilityOrCost{"Delay due to \n technical feasibility OR \n disproportionate cost?"}

%% Flow to TERMINATORS

initial --> is2026Substance
hasNoApplicableExemption_1 --> final
hasNoApplicableExemption_2 --> final
hasNoApplicableExemption_3 --> final
hasNoApplicableExemption_4 --> final

hasExemption47 --> final 
hasExemption46 --> final 
hasExemption45 --> final 
hasExemption44 --> final 

%% THE IMPORTANT PART STARTS HERE

    %% EXEMPTIONS DON'T APPLY TO 2026 SUBSTANCES
    is2026Substance ==> |no| hasNoApplicableExemption_1
    is2026Substance ==> |yes| isCausingFailureIn2027

    %% NO EXEMPTION POSSIBLE - If the status is unknown, then exemptions cannot be reported
    isCausingFailureIn2027 ==> |unknown| hasNoApplicableExemption_2

    %% NO EXEMPTION NEEDED - if the status is not failing and no deterioration is expected, then no exemption is needed
    isCausingFailureIn2027 ==> |no| isDeteriorationExpected
    isDeteriorationExpected ==> |no| hasNoApplicableExemption_3

    %% ARTICLE 4(7) - DETERIORATION DUE TO NEW MODIFICATION OR PROJECT
    isDeteriorationExpected ==> |"yes \n [new modification \n OR sustainable human development]"| hasExemption47
        
    %% ARTICLE 4(6) - DETERIORATION DUE TO ACCIDENTS OR FORCE MAJEURE OR NATURAL CAUSES
    isCausingFailureIn2027 ==> |yes| isDeteriorationObserved
    isDeteriorationObserved ==> |"yes \n [new modification \n OR sustainable human development]"| hasExemption47
    isDeteriorationObserved ==> |"yes \n [accidents  \n OR force majeure  \n OR natural causes]"| hasExemption46
    isDeteriorationObserved ==> |no| isGoodStatusAchievable

    %% ARTICLE 4(5) - LESS STRINGENT OBJECTIVES
    isGoodStatusAchievable ==>|no| hasExemption45

    %% ARTICLE 4(4) EXTENSION OF DEADLINE - NATURAL CONDITIONS
    isGoodStatusAchievable ==> |yes| isDelayDueToNaturalConditions
            
    isDelayDueToNaturalConditions ==> |yes| hasExemption44
            
    %% ARTICLE 4(5) EXTENSION OF DEADLINE - FEASIBILITY OR COST - ONLY FOR 2013 SUBSTANCES
    isDelayDueToNaturalConditions ==> |no| isDelayDueToFeasibilityOrCost
    isDelayDueToFeasibilityOrCost ==> |yes| is2013Substance

    is2013Substance ==> |yes| hasExemption44

    is2013Substance ==> |no| hasNoApplicableExemption_4

    isDelayDueToFeasibilityOrCost ==> |no| hasNoApplicableExemption_4
    

%% styling
classDef state stroke-width:4px,fill:transparent
classDef stateRed stroke:red,fill:transparent
classDef stateBlue stroke:blue,fill:transparent
```
## Surface Water Bodies - Protected area exemptions

Specific objectives may be set for waterbodies associated with some types of protected areas:
* Shellfish designated waters
* Drinking water protection areas
* Natura 2000 protected sites included in the WFD register of protected areas

If the specific objectives have not been met, then exemptions may be reported.

(Note that the euProtectedAreaCode value is only requested for Natura 2000 sites.)

```{mermaid}
---
config:
  class:
    hideEmptyMembersBox: true
  layout: dagre
  theme: neutral
  look: neo
title: Surface Water Body - Protected Area Exemptions - 4th cycle
---
classDiagram
class SWAssociatedProtectedArea{
	+ euSurfaceWaterBodyCode : wiseIdentifier
	+ euProtectedAreaType : ProtectedAreaType 
	+ euProtectedAreaCode : wiseIdentifier [0..1]
	+ swProtectedAreaObjectivesSet : YesNo
	+ swProtectedAreaObjectivesMet : YesNoUnknown
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
---
config:
  class:
    hideEmptyMembersBox: true
  layout: dagre
  theme: neutral
  look: neo
title: Groundwater Body - Chemical Exemptions - 4th cycle
---
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
---
config:
  class:
    hideEmptyMembersBox: true
  layout: dagre
  theme: neutral
  look: neo
title: Groundwater Body - Quantitative Exemptions - 4th cycle
---
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


```{mermaid}
%%{init: {'theme': 'neutral'}}%%

flowchart LR

%% Groundwater Quantitative Status Exemptions
title@{ shape: braces, label: "Groundwater Quantitative Status Exemptions" }

%% Defining the nodes
		
initial([start])
final([end])

%% duplicate nodeS for just for flowchart readability
hasNoApplicableExemption_1("no exemption \n applicable"):::stateRed
hasNoApplicableExemption_2("no exemption \n required"):::stateBlue
hasNoApplicableExemption_3("no exemption \n applicable"):::stateRed

hasExemption44n("Article 4(4) \n Extension of deadline \n (natural conditions)"):::state
hasExemption45("Article 4(5) \n Less stringent objectives"):::state
hasExemption46("Article 4(6) \n Temporary deterioration"):::state
hasExemption47("Article 4(7) \n New modification/project"):::state

%% Defining the decisions

isQuantitativeStatusIn2027{"Quantitative \n Status \n in 2027?"}
isDeteriorationExpected{"Deterioration expected \n beyond 2027?"}
isDeteriorationObserved{"Deterioration observed \n in 2027 or earlier?"}
isGoodStatusAchievable{"Is good status \n achievable?"}
isDelayDueToNaturalConditions{"Delay due to \n natural conditions?"}

%% Flow to TERMINATORS

initial --> isQuantitativeStatusIn2027
hasNoApplicableExemption_1 --> final
hasNoApplicableExemption_2 --> final
hasNoApplicableExemption_3 --> final
hasExemption47 --> final 
hasExemption46 --> final 
hasExemption45 --> final 
hasExemption44n --> final 

%% THE IMPORTANT PART STARTS HERE

    %% NO EXEMPTION POSSIBLE - If the status is unknown, then exemptions cannot be reported
    isQuantitativeStatusIn2027 ==>|unknown|hasNoApplicableExemption_1

    %% NO EXEMPTION NEEDED - if the status is not failing and no deterioration is expected, then no exemption is needed
    isQuantitativeStatusIn2027 ==>|not failing|isDeteriorationExpected
    isDeteriorationExpected ==>|no|hasNoApplicableExemption_2

    %% ARTICLE 4(7) - DETERIORATION DUE TO NEW MODIFICATION OR PROJECT
    isDeteriorationExpected ==>|"yes \n [new modification \n OR sustainable human development]"|hasExemption47
        
    %% ARTICLE 4(6) - DETERIORATION DUE TO ACCIDENTS OR FORCE MAJEURE OR NATURAL CAUSES
    isQuantitativeStatusIn2027 ==>|failing|isDeteriorationObserved
    isDeteriorationObserved ==>|"yes \n [new modification \n OR sustainable human development]"|hasExemption47
    isDeteriorationObserved ==>|"yes \n [accidents  \n OR force majeure  \n OR natural causes]"|hasExemption46
    isDeteriorationObserved ==>|no|isGoodStatusAchievable

    %% ARTICLE 4(5) - LESS STRINGENT OBJECTIVES
    isGoodStatusAchievable ==>|no|hasExemption45

    %% ARTICLE 4(4) EXTENSION OF DEADLINE - NATURAL CONDITIONS
    isGoodStatusAchievable ==>|yes|isDelayDueToNaturalConditions
            
    isDelayDueToNaturalConditions ==>|yes|hasExemption44n
            
    %% ARTICLE 4(5) EXTENSION OF DEADLINE - FEASIBILITY OR COST - NO EXEMPTION POSSIBLE
    isDelayDueToNaturalConditions ==>|no|hasNoApplicableExemption_3

%% styling
classDef state stroke-width:4px,fill:transparent
classDef stateRed stroke:red,fill:transparent
classDef stateBlue stroke:blue,fill:transparent
```

## Groundwater Bodies - Protected area exemptions

Specific objectives may be set for waterbodies associated with some types of protected areas:

* Drinking water protection areas
* Natura 2000 protected sites included in the WFD register of protected areas

If the specific objectives have not been met, then exemptions may be reported.

(Note that the euProtectedAreaCode value is only requested for Natura 2000 sites.)

```{mermaid}
---
config:
  class:
    hideEmptyMembersBox: true
  layout: dagre
  theme: neutral
  look: neo
title: Groundwater - Protected Area Exemptions - 4th cycle
---
classDiagram
class GWAssociatedProtectedArea{
	+ euGroundWaterBodyCode : wiseIdentifier
	+ euProtectedAreaType : ProtectedAreaType
	+ euProtectedAreaCode : wiseIdentifier [0..1]
	+ gwProtectedAreaObjectivesSet : YesNo
	+ gwProtectedAreaObjectivesMet : YesNoUnknown
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
---
config:
  class:
    hideEmptyMembersBox: true
  layout: dagre
  theme: neutral
  look: neo
title: DRAFT - Exemptions - Codelists
---
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


## Exploratory analysis of the data reported in the 3rd cycle

### Surface water - ecological exemptions at water body - 3rd cycle 

In the 3rd cycle, the reporting of ecological exemptions was requested:

* directly at surface water body level, in the SWEcologicalExemptionType class
* also at quality element level, in the qeEcologicalExemptionType element of the QualityElement class.

In 96.5% of the cases, the data reported is redundant.

| exemptionTypeTable | numberOfRecords | numberOfSurfaceWaterBodies | numberOfCountries |
|---|---:|---:|---:|
| Both | 63044 | 61709 | 27 |
| SWB | 2267 | 2105 | 13 |

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

SELECT COALESCE(qe.[countryCode], swb.[countryCode]) AS [countryCode],
	COALESCE(qe.[euSurfaceWaterBodyCode], swb.[euSurfaceWaterBodyCode]) AS [euSurfaceWaterBodyCode],
	COALESCE(qe.[swEcologicalStatusOrPotentialValue], swb.[swEcologicalStatusOrPotentialValue]) AS [swEcologicalStatusOrPotentialValue],
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