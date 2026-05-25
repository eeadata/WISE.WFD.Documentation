(heading_wfd_surface_water_methodologies)=
# WFD surface water methodologies

Last update: 2026-05-14

```{danger}
DRAFT INTERNAL VERSION - PENDING DISCUSSION - DO NOT USE
```

(heading_wfd_surface_water_methodologies_purpose_and_overview)=
## Purpose and overview

This section revises the reporting of information related to **Surface water methodologies** 
in the 2ⁿᵈ and 3ʳᵈ cycle of reporting of the Water Framework Directive River Basin Management Plans. 

It also presents a proposal for simplifying the electronic reporting in the 4ᵗʰ cycle.

(heading_wfd_surface_water_methodologies_reporting_of_surface_water_methodologies_3rd_cycle)=
## Surface water methodologies - 3ʳᵈ cycle

The SWMET_2022 schema defined the structure for the information about the surface water methodologies. 
For review purposes, the schema was divided in two groups:  
* A first group of six classes containing generic information 
  requested at river basin district level ({numref}`SurfaceWaterMethodologies_3rdCycle_SWMET_Part1_ClassDiagram`).
  After revision by the Commission, the classes and elements in {numref}`SurfaceWaterMethodologies_3rdCycle_SWMET_Part1_ClassDiagram_Removed` 
  were removed from this group.
* A second group of six classes containing more technical information,
  about national types, thresholds, etc  ({numref}`SurfaceWaterMethodologies_3rdCycle_SWMET_Part2_ClassDiagram`)

```{todo} 
SurfaceWaterMethodologies - 3ʳᵈ cycle - Review

Review of the remaining classes in
{ref}`SurfaceWaterMethodologies_3rdCycle_SWMET_Part2_ClassDiagram`
```

```{mermaid} /DataModelReview/mmd/SurfaceWaterMethodologies_3rdCycle_SWMET_Part1_ClassDiagram.mmd
:name: SurfaceWaterMethodologies_3rdCycle_SWMET_Part1_ClassDiagram
:align: center
:caption: Partial class diagram - SWMET_2022 schema - 3ʳᵈ cycle - Generic information.
```

```{list-table} SWMET_2022 schema - 3ʳᵈ cycle - Generic data - Removed Classes and/or Elements.
:name: SurfaceWaterMethodologies_3rdCycle_SWMET_Part1_ClassDiagram_Removed
:width: 100%
:header-rows: 1
:align: left

* - Class
  - Element
* - SWExemption
  - Entire class. See {ref}`heading_wfd_exemptions_reporting_of_exemptions_3rd_cycle`.
* - SWMethodologies
  - typologyMethodologyReference,  
    smallWBsMethodologyReference,   
    otherMinimumCriteria,  
    iRBDTypologyCoOrdinationReference,   
* - SWTargetedQ
  - oneOutAllOut,   
    groupingExtrapolation,  
    gepDefined,   
    gepLevel,   
    gepApproach,   
    gesGepComparison,   
    driversFailureEcologicalStatusPotentialReference
* - SWChemicalStatusClassificationRBD
  - approachSWBNotMonitoredChemicalReference,   
    mixingZoneMeasuresReductionReference,  
    chemicalStatusReference,  
* - SWManagementObjectives
  - managementObjectivesContinuityQuantitative
* - SWPressures
  - swPressuresReference
```


```{mermaid} /DataModelReview/mmd/SurfaceWaterMethodologies_3rdCycle_SWMET_Part2_ClassDiagram.mmd
:name: SurfaceWaterMethodologies_3rdCycle_SWMET_Part2_ClassDiagram
:align: center
:caption: Partial class diagram - SWMET_2022 schema - 3ʳᵈ cycle - National types, methods, thresholds.
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

```{mermaid} /DataModelReview/mmd/SurfaceWaterMethodologies_4thCycle_Documents_ClassDiagram.mmd
:name: SurfaceWaterMethodologies_4thCycle_Documents
:caption: SurfaceWaterMethodologies - 4ᵗʰ cycle - Documents
:align: center
:zoom:
```

The following criteria apply:

01. The `dcMetadata` table must contain *one and only one* record 
    for each of the country's river basin districts, identified by the `euRBDCode`.
    
02. For countries reporting under the WFD, 
    the quality control will raise an **ERROR**,
    if some, or all, the river basin districts have `includesDescriptiveData = no`.

```{todo}
Surface water methodologies - {ref}`heading_wfd_surface_water_methodologies_documents_dataset_4th_cycle`

**Technical** review pending.
```

(heading_wfd_surface_water_methodologies_reporting_of_surface_water_methodologies_4th_cycle)=
## Descriptive dataset - 4ᵗʰ cycle

{numref}`SurfaceWaterMethodologies_4thCycle_SWMET_Part1_ClassDiagram` 
shows the revised structure for the surface water methodologies 
group of tables with generic information, including applicable codelists.

See also {numref}`SurfaceWaterMethodologies_4thCycle_MitigationMeasure_Table`,
 {numref}`SurfaceWaterMethodologies_4thCycle_SignificantPressureTools_Table`,
  {numref}`SurfaceWaterMethodologies_4thCycle_MixingZoneMeasure_Table` for the list of options in each codelist.


```{mermaid} /DataModelReview/mmd/SurfaceWaterMethodologies_4thCycle_SWMET_Part1_ClassDiagram.mmd
:name: SurfaceWaterMethodologies_4thCycle_SWMET_Part1_ClassDiagram
:align: center
:caption: Surface water methodologies - generic data - 4ᵗʰ cycle.
```

```{dropdown} MitigationMeasure codelist
```{include} tables/SurfaceWaterMethodologies_4thCycle_MitigationMeasure_Table
```

```{dropdown} SignificantPressureTools codelist
```{include} tables/SurfaceWaterMethodologies_4thCycle_SignificantPressureTools_Table
```

```{dropdown} MixingZoneMeasure codelist
```{include} tables/SurfaceWaterMethodologies_4thCycle_MixingZoneMeasure_Table
```

```{todo} 
SurfaceWaterMethodologies - 4ᵗʰ cycle - Codelists

Include the PressureType codelist.
Include the BiologicalQualityElement codelist.
```

(heading_wfd_wfd_surface_water_methodologies_references)=
## References

The complete schemas for the 3ʳᵈ cycle of reporting can be found in the [WFD2022 EAP file](https://cdr.eionet.europa.eu/help/WFD/WFD_715_2022/UML%20Data%20specification/WFD2022.EAP).