(heading_wfd_groundwater_methodologies)=
# WFD groundwater methodologies

Last update: 2026-05-29

```{danger}
DRAFT INTERNAL VERSION - PENDING DISCUSSION - DO NOT USE
```

(heading_wfd_groundwater_methodologies_purpose_and_overview)=
## Purpose and overview

This section:
* revises the information related to **Groundwater methodologies** 
  in the 2ⁿᵈ and 3ʳᵈ cycle of reporting of the 
  Water Framework Directive River Basin Management Plans
* presents a simplified proposal for the electronic reporting in the 4ᵗʰ cycle.

(heading_wfd_groundwater_methodologies_reporting_of_groundwater_methodologies_GWMET_schema_3rd_cycle)=
## GWMET_2022 schema - 3ʳᵈ cycle

The GWMET schema defined the structure for the information about the groundwater methodologies ({numref}`ClassDiagram_GWMET_2022`).

```{figure} img/ClassDiagram_GWMET_2022.png
:name: ClassDiagram_GWMET_2022
:align: center
:width: 75%

GWMET_2022 Schema - 3ʳᵈ cycle - Obsolete
```

The GWMET schema was already partially revised (see {ref}`heading_wfd_exemptions_reporting_of_exemptions_3rd_cycle`). 
Specifically, the GWExemption data ({numref}`Exemptions_3rdCycle_GWMET_ClassDiagram`) is no longer requested in the 4ᵗʰ cycle.

{numref}`GroundwaterMethodologies_3rdCycle_GWMET_ClassDiagram` shows a simplified diagram 
to help focus the discussion on the remaining issues.

```{mermaid} /DataModelReview/mmd/GroundwaterMethodologies_3rdCycle_GWMET_ClassDiagram.mmd
:name: GroundwaterMethodologies_3rdCycle_GWMET_ClassDiagram
:align: center
:caption: Class diagram for the GWMET_2022 schema in the 3ʳᵈ cycle.
```

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

The Commission has revised **GWPressures** class.
The following elements were removed:
* GWMET/GWPressures/gwSignificantPressureOtherSourceTools
* GWMET/GWPressures/gwPressuresNotAssessed

The struture of the **GWPressures** class was also revised.

(heading_wfd_groundwater_methodologies_reporting_of_groundwater_methodologies_4th_cycle_pending_issues)=
## Descritive dataset - 4ᵗʰ cycle - pending issues

The revised strutured for the groundwater methodologies reporting 
is presented in the DRAFT {numref}`GroundwaterMethodologies_4thCycle_ClassDiagram`,
including the issues requiring clarification, in the classes marked in red.

The tables `GWMethodologies` and `ThresholdValue` follow the struture of the corresponding classes 
in the 3ʳᵈ cycle reporting (minus the attributes by the Commission's review).

The table `GWPressureAssessment` uses a different approach:
* the reporting of "pressures not assessed" is eliminated,
  because the data was difficult to analyse and contained inconsistencies,
* instead, for each pressure (or group of pressures),
  three attributes are requested (`gwPressureAssessmentMethod`,`gwSignificanceDefinition`,`gwSignificanceLinkFailure`),
* given that the pressure codelist is hierarchical, 
  the granularity of the reporting is selected by Member States
* the quality control procedure will verify that different levels 
  are not selected simultaneously for any given RBD.

```{mermaid} /DataModelReview/mmd/GroundwaterMethodologies_4thCycle_ClassDiagram.mmd
:name: GroundwaterMethodologies_4thCycle_ClassDiagram
:align: center
:caption: Groundwater methodologies - DRAFT - 4ᵗʰ cycle
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

(heading_wfd_groundater_methodologies_codelists_4th_cycle)=
## Codelists - 4ᵗʰ cycle

Note: this section includes only the codelists specific to the groundwater methodologies.

(heading_wfd_groundater_methodologies_documents_dataset_4th_cycle)=
## Documents dataset - 4ᵗʰ cycle

The Documents dataset follows the standard structure used in various WISE dataflows ({numref}`GroundWaterMethodologies_4thCycle_Documents`):

* The `dcMetadata` table provides the basic Dublin Core metadata elements about the delivery.
  
  * If required by the data providers, and especially if spatial data is being reported, 
    the `licenseDocument` and the `metadataDocument` attributes allow the provision of additional information about the dataset.
  * The `dcMetadata` table also functions as a "manifest file" 
    explaining if the delivery contains data for a given river basin district or not.
   
* The `Document` table allows the upload of documents (for example, PDFs) 
  or the provision of a `hyperlink` to a document stored in a publicly accessible national web site.

* The `Reference` table is also standard in the WISE dataflows:
  the `bookmark` it allows the identification of the chapter(s), sections(s) or page range(s) 
  where the relevant information about a `subject`
  can be found within a document.

The following criteria apply:

01. The `dcMetadata` table must contain *one and only one* record 
    for each of the country's river basin districts, identified by the `euRBDCode`.
    
02. For countries reporting under the WFD, 
    the quality control will raise an **ERROR**,
    if some, or all, the river basin districts have `includesDescriptiveData = no`.

```{mermaid} /DataModelReview/mmd/GroundWaterMethodologies_4thCycle_Documents_ClassDiagram.mmd
:name: GroundWaterMethodologies_4thCycle_Documents
:caption: GroundWaterMethodologies - 4ᵗʰ cycle - Documents
:align: center
:zoom:
```

```{todo}
Groundwater methodologies - {ref}`heading_wfd_groundater_methodologies_documents_dataset_4th_cycle`

**Technical** review pending.
```




(heading_wfd_groundwater_methodologies_references)=
## References

```{include} FragmentReportingGuidanceFiles
```