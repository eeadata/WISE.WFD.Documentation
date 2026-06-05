(heading_wfd_surface_water_methodologies)=
# Surface water methodologies

Last update: 2026-06-04

```{Warning}
Public Version - Pending Discussion
```

(heading_wfd_surface_water_methodologies_purpose_and_overview)=
## Purpose and overview

This section:

* revises the information related to **Surface water methodologies** 
  in the 2ⁿᵈ and 3ʳᵈ cycle of reporting of the 
  Water Framework Directive River Basin Management Plans
* presents a simplified proposal for the electronic reporting in the 4ᵗʰ cycle

(heading_wfd_surface_water_methodologies_reporting_of_surface_water_methodologies_3rd_cycle)=
## SWMET_2022 schema - 3ʳᵈ cycle

The SWMET_2022 schema defined the required data about surface water methodologies. 
For review purposes, the schema was divided in two groups:

* a group of six classes requesting generic information 
  at river basin district level ({numref}`SurfaceWaterMethodologies_3rdCycle_SWMET_Part1_ClassDiagram`)
* a group of six classes requesting more technical information,
  about national types, thresholds, etc ({numref}`SurfaceWaterMethodologies_3rdCycle_SWMET_Part2_ClassDiagram`)

### Generic information

The SWMET_2022 schema was already partially revised (see {ref}`heading_wfd_exemptions_reporting_of_exemptions_3rd_cycle`). 
Specifically, the SWExemptions data ({numref}`Exemptions_3rdCycle_SWMET_ClassDiagram`) 
will not be requested in the 4ᵗʰ cycle reporting.

```{mermaid} /DataModelReview/mmd/SurfaceWaterMethodologies_3rdCycle_SWMET_Part1_ClassDiagram.mmd
:name: SurfaceWaterMethodologies_3rdCycle_SWMET_Part1_ClassDiagram
:align: center
:caption: SWMET_2022 schema - generic data - 3ʳᵈ cycle.
```

The Commission has revised and simplified the **SWMethodologies** class, 
keeping only a subset of the elements requested in the 3ʳᵈ cycle.
The following elements were removed:

* SWMET/SWMethodologies/typologyMethodologyReference
* SWMET/SWMethodologies/smallWBsMethodologyReference
* SWMET/SWMethodologies/otherMinimumCriteria
* SWMET/SWMethodologies/iRBDTypologyCoOrdinationReference

The Commission has revised and simplified the **SWTargetedQ** class, 
keeping only a subset of the elements requested in the 3ʳᵈ cycle.
The following elements were removed:

* SWMET/SWTargetedQ/oneOutAllOut
* SWMET/SWTargetedQ/groupingExtrapolation
* SWMET/SWTargetedQ/gepDefined
* SWMET/SWTargetedQ/gepLevel
* SWMET/SWTargetedQ/gepApproach
* SWMET/SWTargetedQ/gesGepComparison
* SWMET/SWTargetedQ/driversFailureEcologicalStatusPotentialReference

The Commission has revised and simplified the **SWChemicalStatusClassificationRBD** class, 
keeping only a subset of the elements requested in the 3ʳᵈ cycle. 
The following elements were removed:

* SWMET/SWChemicalStatusClassificationRBD/approachSWBNotMonitoredChemicalReference
* SWMET/SWChemicalStatusClassificationRBD/mixingZoneMeasuresReductionReference
* SWMET/SWChemicalStatusClassificationRBD/chemicalStatusReference

The Commission has revised and simplified the **SWManagementObjectives** class, 
keeping only a subset of the elements requested in the 3ʳᵈ cycle. 
The following elements were removed:

* SWMET/SWManagementObjectives/managementObjectivesContinuityQuantitative

The Commission has revised **SWPressures** class. The following elements were removed:

* SWMET/SWPressures/swSignificantPressureOtherSourceTools
* SWMET/SWPressures/swPressuresNotAssessed  

The struture of the **SWPressures** class was also revised.

### Technical information

The review of the classes and elements 
depicted in {numref}`SurfaceWaterMethodologies_3rdCycle_SWMET_Part2_ClassDiagram`
is pending.

The preliminary technical analysis suggests the changes described below.

In the **BQEMethod** class, the following elements were removed:
* SWMET/BQEMethod/bqePercentageOfTypes
* SWMET/BQEMethod/bqeSensitivityImpactOther
A unique identifier is introduced, as well as the possibility to reference supporting documentation.

In the **SWPhysicoChemicalQE** class, the following elements were removed:
* SWMET/SWPhysicoChemicalQE/physChemParameterOther

In the **SWRBSP** class, the following elements were removed:
* SWMET/SWRBSP/rbspOther
* SWMET/SWRBSP/rbspScale

In the **SWPrioritySubstance** class, the following elements were removed (because they are not required or can be derived in the revised model):
* SWMET/SWPrioritySubstance/psScale
* SWMET/SWPrioritySubstance/psStatusAssessment
* SWMET/SWPrioritySubstance/psStandardsUsed

```{mermaid} /DataModelReview/mmd/SurfaceWaterMethodologies_3rdCycle_SWMET_Part2_ClassDiagram.mmd
:name: SurfaceWaterMethodologies_3rdCycle_SWMET_Part2_ClassDiagram
:align: center
:caption: SWMET_2022 schema - technical data - 3ʳᵈ cycle.
```

```{todo} 
SurfaceWaterMethodologies - 3ʳᵈ cycle - Review

Review of the remaining classes in
{ref}`SurfaceWaterMethodologies_3rdCycle_SWMET_Part2_ClassDiagram`
```

(heading_wfd_surface_water_methodologies_reporting_of_surface_water_methodologies_4th_cycle)=
## Descriptive dataset - 4ᵗʰ cycle

The revised strutured for the generic data in the surface water methodologies reporting 
is presented in {numref}`SurfaceWaterMethodologies_4thCycle_SWMET_Part1_ClassDiagram`,
including the applicable codelists.

The `SWMethodologies`, `SWManagementObjectives`, `SWTargetedQuestions` and  `SWChemicalStatusClassification` tables have a struture similar to the corresponding classes 
in the 3ʳᵈ cycle reporting (minus the attributes removed by the Commission's review).

The table `SWPressureAssessment` uses a different approach:

* the reporting of "pressures not assessed" is eliminated,
  because the data was difficult to analyse and contained inconsistencies
* instead, for each pressure (or group of pressures),
  three attributes are requested 
  (`swPressureAssessmentMethod`,`swSignificanceDefinition`,`swSignificanceLinkFailure`)
* given that the pressure codelist is hierarchical, 
  the granularity of the reporting is selected by Member States
* the quality control procedure will verify that different levels 
  are not selected simultaneously for any given RBD

```{mermaid} /DataModelReview/mmd/SurfaceWaterMethodologies_4thCycle_SWMET_Part1_ClassDiagram.mmd
:name: SurfaceWaterMethodologies_4thCycle_SWMET_Part1_ClassDiagram
:align: center
:caption: Surface water methodologies - generic data - 4ᵗʰ cycle.
```

```{mermaid} /DataModelReview/mmd/SurfaceWaterMethodologies_4thCycle_SWThresholdValue_ClassDiagram.mmd
:name: SurfaceWaterMethodologies_4thCycle_SWThresholdValue_ClassDiagram
:align: center
:caption: Surface water methodologies - SWThresholdValue - 4ᵗʰ cycle.
```

```{mermaid} /DataModelReview/mmd/SurfaceWaterMethodologies_4thCycle_QE3Classification_ClassDiagram.mmd
:name: SurfaceWaterMethodologies_4thCycle_QE3Classification_ClassDiagram
:align: center
:caption: Surface water methodologies - QE3Classification - 4ᵗʰ cycle.
```

```{mermaid} /DataModelReview/mmd/SurfaceWaterMethodologies_4thCycle_BQEMethod_QE1Classification_ClassDiagram.mmd
:name: SurfaceWaterMethodologies_4thCycle_BQEMethod_QE1Classification_ClassDiagram
:align: center
:caption: Surface water methodologies - BQEMethod and QE1Classification - 4ᵗʰ cycle.
```

```{mermaid} /DataModelReview/mmd/SurfaceWaterMethodologies_4thCycle_SWType_ClassDiagram.mmd
:name: SurfaceWaterMethodologies_4thCycle_SWType_ClassDiagram
:align: center
:caption: Surface water methodologies - SWType - 4ᵗʰ cycle.
```

(heading_wfd_surface_water_methodologies_codelists_4th_cycle)=
## Codelists - 4ᵗʰ cycle

* For the `MitigationMeasure` codelist, 
  see {numref}`Codelist_4thCycle_MitigationMeasure_Table`.

* For the `MixingZoneMeasure` codelist, 
  see {numref}`Codelist_4thCycle_MixingZoneMeasure_Table`.

* For the `PressureAssessmentMethod` codelist, 
  see {numref}`Codelist_4thCycle_PressureAssessmentMethod_Table`.

```{dropdown} MitigationMeasure codelist
```{include} tables/Codelist_4thCycle_MitigationMeasure_Table
```

```{dropdown} MixingZoneMeasure codelist
```{include} tables/Codelist_4thCycle_MixingZoneMeasure_Table
```

```{dropdown} PressureAssessmentMethod codelist
```{include} tables/Codelist_4thCycle_PressureAssessmentMethod_Table
```

(heading_wfd_surface_water_methodologies_documents_dataset_4th_cycle)=
## Documents dataset - 4ᵗʰ cycle

The Documents dataset follows the standard structure used in various WISE dataflows 
({numref}`SurfaceWaterMethodologies_4thCycle_Documents`):

* the `dcMetadata` table provides the basic Dublin Core metadata elements about the delivery
  
  * if required by the data providers, and especially if spatial data is being reported, 
    the `licenseDocument` and the `metadataDocument` attributes allow the provision of additional information about the dataset
  * the `dcMetadata` table also functions as a "manifest file" 
    explaining if the delivery contains data for a given river basin district or not
   
* the `Document` table allows the upload of documents (for example, PDFs) 
  or the provision of a `hyperlink` to a document stored in a publicly accessible national web site

* the `Reference` table is also standard in the WISE dataflows:
  the `bookmark` it allows the identification of the chapter(s), sections(s) or page range(s) 
  where the relevant information about a `subject`
  can be found within a document

The following criteria apply:

01. the `dcMetadata` table must contain *one and only one* record 
    for each of the country's river basin districts, identified by the `euRBDCode`
    
02. for countries reporting under the WFD, 
    the quality control will raise an **ERROR**,
    if some, or all, the river basin districts have `includesDescriptiveData = no`

```{mermaid} /DataModelReview/mmd/SurfaceWaterMethodologies_4thCycle_Documents_ClassDiagram.mmd
:name: SurfaceWaterMethodologies_4thCycle_Documents
:caption: SurfaceWaterMethodologies - 4ᵗʰ cycle - Documents
:align: center
:zoom:
```

```{todo}
Surface water methodologies - {ref}`heading_wfd_surface_water_methodologies_documents_dataset_4th_cycle`

**Technical** review pending.
```

(heading_wfd_wfd_surface_water_methodologies_references)=
## References

```{include} FragmentReportingGuidanceFiles
```