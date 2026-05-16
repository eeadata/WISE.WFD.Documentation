(heading_wfd_groundwater_methodologies)=
# WFD groundwater methodologies

Last update: 2026-05-14

```{warning}
DRAFT INTERNAL VERSION - PENDING DISCUSSION - DO NOT USE
```

(heading_wfd_groundwater_methodologies_purpose_and_overview)=
## Purpose and overview

This section revises the reporting of information related to **Groundwater methodologies** 
in the 2ⁿᵈ and 3ʳᵈ cycle of reporting of the Water Framework Directive River Basin Management Plans. 

It also presents a proposal for simplifying the electronic reporting in the 4ᵗʰ cycle.

(heading_wfd_groundwater_methodologies_reporting_of_groundwater_methodologies_3rd_cycle)=
## Groundwater methodologies - 3ʳᵈ cycle

The GWMET schema defined the structure for the information about the groundwater methodologies ({numref}`ClassDiagram_GWMET_2022`).

```{figure} img/ClassDiagram_GWMET_2022.png
:name: ClassDiagram_GWMET_2022
:align: center
:width: 75%

GWMET_2022 Schema - 3ʳᵈ cycle - Obsolete
```

(heading_wfd_groundwater_methodologies_reporting_of_groundwater_methodologies_GWMET_schema_3rd_cycle)=
## GWMET schema - 3ʳᵈ cycle

The GWMET schema was already partially revised with regard to the reporting of exemptions (see {ref}`heading_wfd_exemptions_reporting_of_exemptions_3rd_cycle`).  
Specifically, the GWExemption data ({numref}`Exemptions_3rdCycle_GWMET_ClassDiagram`) is no longer requested in the 4ᵗʰ cycle.

{numref}`GroundwaterMethodologies_3rdCycle_GWMET_ClassDiagram` shows a simplified diagram 
to help focus the discussion on the remaining issues.

```{mermaid} /DataModelReview/mmd/GroundwaterMethodologies_3rdCycle_GWMET_ClassDiagram.mmd
:name: GroundwaterMethodologies_3rdCycle_GWMET_ClassDiagram
:align: center
:caption: Class diagram for the GWMET_2022 schema in the 3ʳᵈ cycle.
```


(heading_wfd_groundwater_methodologies_reporting_of_groundwater_methodologies_4th_cycle_pending_issues)=
## Groundwater methodologies - 4ᵗʰ cycle - pending issues


Based on DG ENV's review, {numref}`_DRAFT_GroundwaterMethodologies_4thCycle_ClassDiagram` 
shows a DRAFT diagram including the issues requiring clarification, in the classes marked in red.


The Commission has revised and simplified the **GWMethodologies** class, keeping only a subset of the elements requested in the 3ʳᵈ cycle.  
The following elements were removed:

* GWMET/GWMethodologies/diminutionDamage
* GWMET/GWMethodologies/methodCriterionExtentExceedance
* GWMET/GWMethodologies/proportionExceedanceAllowed
* GWMET/GWMethodologies/impactsGWAbstractionBalance
* GWMET/GWMethodologies/impactsGWAbstractionSWObjective
* GWMET/GWMethodologies/impactsGWAbstractionSWDiminutionStatus
* GWMET/GWMethodologies/impactsGWAbstractionDamageGWDE
* GWMET/GWMethodologies/impactsGWAbstractionSalineIntrusion
* GWMET/GWMethodologies/availableGroundwaterResource
* GWMET/GWMethodologies/needsTerritorialEcosystems
* GWMET/GWMethodologies/balanceRechargeAbstraction
* GWMET/GWMethodologies/gwMethodologiesChemicalStatusClassificationReference
* GWMET/GWMethodologies/gwMethodologiesQuantitativeClassificationReference
* GWMET/GWMethodologies/gwMethodologiesTransboundaryReference
* GWMET/GWMethodologies/transboundaryGWBPresent

The Commission has revised and simplified the **ThresholdValue** class, keeping only a subset of the elements requested in the 3ʳᵈ cycle.  
The following elements were removed:

* GWMET/ThresholdValue/pollutantIndicatorCodeOther
* GWMET/ThresholdValue/thresholdValueDerivedFromCV
* GWMET/ThresholdValue/cvDrinkingWaterValueRange
* GWMET/ThresholdValue/cvDrinkingWaterValueUnit
* GWMET/ThresholdValue/cvIrrigationValueRange
* GWMET/ThresholdValue/cvIrrigationValueUnit
* GWMET/ThresholdValue/cvIndustryValueRange
* GWMET/ThresholdValue/cvIndustryValueUnit
* GWMET/ThresholdValue/cvOtherValueRange
* GWMET/ThresholdValue/cvOtherValueUnit
* GWMET/ThresholdValue/thresholdValueScale

The revision of the **GWPressures** class is pending.

```{mermaid} /DataModelReview/mmd/_DRAFT_GroundwaterMethodologies_4thCycle_ClassDiagram.mmd
:name: _DRAFT_GroundwaterMethodologies_4thCycle_ClassDiagram
:align: center
:caption: DRAFT DIAGRAM - ISSUES PENDING DISCUSSION - Groundwater methodologies - 4ᵗʰ cycle
```

Several topics require further discussion and clarification.
See:

* {ref}`GroundwaterMethodologies_Issues_Pending_Discussion_GWMethodologies`

* {ref}`GroundwaterMethodologies_Issues_Pending_Discussion_ThresholdValue`

```{list-table} PENDING - Groundwater Methodologies - 4ᵗʰ cycle - **GWMethodologies** table
    :name: GroundwaterMethodologies_Issues_Pending_Discussion_GWMethodologies
    :width: 100%
    :widths: 40 40 20
    :header-rows: 1
    :align: left

* - Attribute
  - Description
  - Status

* - thresholdValueElementProtectionGWDE
  - Marked for discussion by the Commission.
  - Pending

* - thresholdValueElementProtectionUses
  - Marked for discussion by the Commission.
  - Pending

* - thresholdValueElementSalineIntrusion
  - Marked for discussion by the Commission.
  - Pending

* - thresholdValueBackgroundLevels
  - Marked for discussion by the Commission.
  - Pending
```

```{list-table} PENDING - Groundwater Methodologies - 4ᵗʰ cycle - **ThresholdValue** table
    :name: GroundwaterMethodologies_Issues_Pending_Discussion_ThresholdValue
    :width: 100%
    :widths: 40 40 20
    :header-rows: 1
    :align: left

* - Attribute
  - Description
  - Status

* - gwThresholdIdentifier
  - Addressing duplicates.
  - Pending

* - startingPointTrendReversal
  - Addressing ambiguous reporting of percentages & proportions.
  - Pending

* - (to be defined)
  - Addressing background levels and other chemical conditions.
  - Pending

* - (to be defined)
  - Addressing geographical scope (if needed).
  - Pending

* - thresholdValueRange
  - TECHNICAL: discuss and document the range datatype
  - Pending
```

(heading_wfd_groundwater_methodologies_references)=
## References

```{include} FragmentWFD2022ReportingSchemas
```