(heading_wfd_surface_water_methodologies)=
# WFD surface water methodologies

Last update: 2026-05-29

```{danger}
DRAFT INTERNAL VERSION - PENDING DISCUSSION - DO NOT USE
```

(heading_wfd_surface_water_methodologies_purpose_and_overview)=
## Purpose and overview

This section:
* revises the information related to **Surface water methodologies** 
  in the 2ⁿᵈ and 3ʳᵈ cycle of reporting of the 
  Water Framework Directive River Basin Management Plans
* presents a simplified proposal for the electronic reporting in the 4ᵗʰ cycle.

(heading_wfd_surface_water_methodologies_reporting_of_surface_water_methodologies_3rd_cycle)=
## SWMET_2022 schema - 3ʳᵈ cycle

The SWMET_2022 schema defined the structure for the information about the surface water methodologies. 
For review purposes, the schema was divided in two groups:  
* A first group of six classes containing generic information 
  requested at river basin district level ({numref}`SurfaceWaterMethodologies_3rdCycle_SWMET_Part1_ClassDiagram`).
* A second group of six classes containing more technical information,
  about national types, thresholds, etc  ({numref}`SurfaceWaterMethodologies_3rdCycle_SWMET_Part2_ClassDiagram`)

The SWMET schema was already partially revised (see {ref}`heading_wfd_exemptions_reporting_of_exemptions_3rd_cycle`). 
Specifically, the SWExemption data ({numref}`Exemptions_3rdCycle_SWMET_ClassDiagram`) is no longer requested in the 4ᵗʰ cycle.

### Generic information

```{mermaid} /DataModelReview/mmd/SurfaceWaterMethodologies_3rdCycle_SWMET_Part1_ClassDiagram.mmd
:name: SurfaceWaterMethodologies_3rdCycle_SWMET_Part1_ClassDiagram
:align: center
:caption: SWMET_2022 schema - generic data - 3ʳᵈ cycle.
```

The Commission has revised and simplified the **SWMethodologies** class, keeping only a subset of the elements requested in the 3ʳᵈ cycle.  
The following elements were removed:

* SWMET/SWMethodologies/typologyMethodologyReference  
* SWMET/SWMethodologies/smallWBsMethodologyReference  
* SWMET/SWMethodologies/otherMinimumCriteria
* SWMET/SWMethodologies/iRBDTypologyCoOrdinationReference

The Commission has revised and simplified the **SWTargetedQ** class, keeping only a subset of the elements requested in the 3ʳᵈ cycle.  
The following elements were removed:

* SWMET/SWTargetedQ/oneOutAllOut,   
* SWMET/SWTargetedQ/groupingExtrapolation
* SWMET/SWTargetedQ/gepDefined
* SWMET/SWTargetedQ/gepLevel
* SWMET/SWTargetedQ/gepApproach
* SWMET/SWTargetedQ/gesGepComparison
* SWMET/SWTargetedQ/driversFailureEcologicalStatusPotentialReference

The Commission has revised and simplified the **SWChemicalStatusClassificationRBD** class, keeping only a subset of the elements requested in the 3ʳᵈ cycle.  
The following elements were removed:
* SWMET/SWChemicalStatusClassificationRBD/approachSWBNotMonitoredChemicalReference
* SWMET/SWChemicalStatusClassificationRBD/mixingZoneMeasuresReductionReference
* SWMET/SWChemicalStatusClassificationRBD/chemicalStatusReference

The Commission has revised and simplified the **SWManagementObjectives** class, keeping only a subset of the elements requested in the 3ʳᵈ cycle.  
The following elements were removed:
* SWMET/SWManagementObjectives/managementObjectivesContinuityQuantitative

The Commission has revised **SWPressures** class.
The following elements were removed:
* SWMET/SWPressures/swSignificantPressureOtherSourceTools
* SWMET/SWPressures/swPressuresNotAssessed  

The struture of the **SWPressures** class was also revised.

### Technical information

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

The tables `SWMethodologies`, `SWManagementObjectives`, `SWTargetedQuestions` and  `SWChemicalStatusClassification` follow the struture of the corresponding classes 
in the 3ʳᵈ cycle reporting (minus the attributes by the Commission's review).

The table `SWPressureAssessment` uses a different approach:
* the reporting of "pressures not assessed" is eliminated,
  because the data was difficult to analyse and contained inconsistencies,
* instead, for each pressure (or group of pressures),
  three attributes are requested (`swPressureAssessmentMethod`,`swSignificanceDefinition`,`swSignificanceLinkFailure`),
* given that the pressure codelist is hierarchical, 
  the granularity of the reporting is selected by Member States
* the quality control procedure will verify that different levels 
  are not selected simultaneously for any given RBD.

```{mermaid} /DataModelReview/mmd/SurfaceWaterMethodologies_4thCycle_SWMET_Part1_ClassDiagram.mmd
:name: SurfaceWaterMethodologies_4thCycle_SWMET_Part1_ClassDiagram
:align: center
:caption: Surface water methodologies - generic data - 4ᵗʰ cycle.
```
(heading_wfd_surface_water_methodologies_codelists_4th_cycle)=
## Codelists - 4ᵗʰ cycle

Note: this section includes only the codelists specific to the surface water methodologies.

```{dropdown} MitigationMeasure codelist
```{include} tables/SurfaceWaterMethodologies_4thCycle_MitigationMeasure_Table
```

```{dropdown} PressureAssessmentMethod codelist
```{include} tables/PressureAssessmentMethod_Codelist_4thCycle_Table
```

```{dropdown} MixingZoneMeasure codelist
```{include} tables/SurfaceWaterMethodologies_4thCycle_MixingZoneMeasure_Table
```

(heading_wfd_surface_water_methodologies_documents_dataset_4th_cycle)=
## Documents dataset - 4ᵗʰ cycle

The Documents dataset follows the standard structure used in various WISE dataflows ({numref}`SurfaceWaterMethodologies_4thCycle_Documents`):

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