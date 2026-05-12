# WFD - Surface water bodies

```{warning}
DRAFT INTERNAL VERSION - PENDING DISCUSSION - DO NOT USE
```

## Purpose and overview

This section revises the reporting of information related to **Surface Water Bodies** 
in the 2ⁿᵈ and 3ʳᵈ cycle of reporting of the Water Framework Directive River Basin Management Plans. 
It also presents a proposal for simplifying the electronic reporting in the 4ᵗʰ cycle.

## Current structure - 3ʳᵈ cycle

The information about Surface water bodies was reported in two separate schemas:

* The SWB schema, containing information about each surface water body ({numref}`SurfaceWater_3rdCycle_SWB_ClassDiagram`)
* The SWMET schema, containing information about the methodologies.

```{mermaid} /DataModelReview/mmd/SurfaceWater_3rdCycle_SWB_ClassDiagram.mmd
:name: SurfaceWater_3rdCycle_SWB_ClassDiagram
:align: center
:caption: Class diagram for the SWB_2022 schema in the 3ʳᵈ cycle of reporting.
```

## SWB schema - 3ʳᵈ cycle

The SWB schema was already partially revised with regard to the reporting of exemptions.  
See:

* {ref}`heading_wfd_exemptions_surface_water_bodies_chemical_exemptions_by_pollutant`
* {ref}`heading_wfd_exemptions_surface_water_bodies_ecological_exemptions_by_quality_element`
* {ref}`heading_wfd_exemptions_surface_water_bodies_protected_area_exemptions`

Other simplifications already discussed also apply to the revision of the SWB schema:

* Removal of the textual reporting of "other" pollutants or RBSPs
* Removal of the textual reporting of "other" pressures
* Removal of the textual reporting of "other" impacts
* Removal of the reporting of subunits

{numref}`SurfaceWater_3rdCycle_SWB_Simplified_ClassDiagram` shows a simplified diagram 
to help focus the discussion on the remaining issues.

```{mermaid} /DataModelReview/mmd/SurfaceWater_3rdCycle_SWB_Simplified_ClassDiagram.mmd
:name: SurfaceWater_3rdCycle_SWB_Simplified_ClassDiagram
:align: center
:caption: PARTIAL class diagram for the SWB_2022 schema in the 3ʳᵈ cycle of reporting.
```