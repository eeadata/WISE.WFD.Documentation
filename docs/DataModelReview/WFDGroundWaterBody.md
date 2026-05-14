# WFD - Groundwater bodies

Last update: 2026-05-14

```{warning}
DRAFT INTERNAL VERSION - PENDING DISCUSSION - DO NOT USE
```

```{contents} Table of Contents
:depth: 2
:local:
```

## Purpose and overview

This section revises the reporting of information related to **Groundwater Bodies** 
in the 2ⁿᵈ and 3ʳᵈ cycle of reporting of the Water Framework Directive River Basin Management Plans. 
It also presents a proposal for simplifying the electronic reporting in the 4ᵗʰ cycle.

## Current structure - 3ʳᵈ cycle

The information about Groundwater bodies was reported in two separate schemas:

* The GWB schema, containing information about each groundwater body ({numref}`Groundwater_3rdCycle_GWB_ClassDiagram`)
* The GWMET schema, containing information about the methodologies.

```{mermaid} /DataModelReview/mmd/Groundwater_3rdCycle_GWB_ClassDiagram.mmd
:name: Groundwater_3rdCycle_GWB_ClassDiagram
:align: center
:caption: Class diagram for the GWB_2022 schema in the 3ʳᵈ cycle.
```

## GWB schema - 3ʳᵈ cycle

The GWB schema was already partially revised with regard to the reporting of exemptions.  
See:

* {ref}`heading_wfd_exemptions_groundwater_bodies_chemical_exemptions_by_pollutant`
* {ref}`heading_wfd_exemptions_groundwater_bodies_quantitative_exemptions`
* {ref}`heading_wfd_exemptions_groundwater_bodies_protected_area_exemptions`

Other simplifications already discussed also apply to the revision of the GWB schema:

* Removal of the textual reporting of "other" pollutants
* Removal of the textual reporting of "other" pressures
* Removal of the textual reporting of "other" impacts

{numref}`Groundwater_3rdCycle_GWB_Simplified_ClassDiagram` shows a simplified diagram 
to help focus the discussion on the remaining issues.

```{mermaid} /DataModelReview/mmd/Groundwater_3rdCycle_GWB_Simplified_ClassDiagram.mmd
:name: Groundwater_3rdCycle_GWB_Simplified_ClassDiagram
:align: center
:caption: PARTIAL class diagram for the GWB_2022 schema in the 3ʳᵈ cycle.
```

## Groundwater - descriptive data - 4ᵗʰ cycle - pending issues

Based on DG ENV's review, {numref}`_DRAFT_Groundwater_DescriptiveData_4thCycle_ClassDiagram` 
shows a DRAFT diagram including the issues requiring clarification, in the classes marked in red.

The following elements were removed:

* GWB/GroundWaterBody/gwEORiskQuantitative 
* GWB/GroundWaterBody/gwEORiskChemical 
* GWB/GroundWaterBody/GWPollutant/gwPollutantExceedancesNotCounted


```{mermaid} /DataModelReview/mmd/_DRAFT_Groundwater_DescriptiveData_4thCycle_ClassDiagram.mmd
:name: _DRAFT_Groundwater_DescriptiveData_4thCycle_ClassDiagram
:align: center
:caption: DRAFT DIAGRAM - ISSUES PENDING DISCUSSION - Groundwater - 4ᵗʰ cycle
```

Several topics require further discussion and clarification.
See:

* {ref}`Groundwater_Issues_Pending_Discussion_GroundWaterBodyStatus`
* {ref}`Groundwater_Issues_Pending_Discussion_GWPollutant`
* {ref}`Groundwater_Issues_Pending_Discussion_GWQuantitativeStatus`
* {ref}`Groundwater_Issues_Pending_Discussion_LinkSurfaceWaterBody`

Also pending discussion is the revision of the **PressureTpe** and **ImpactType** codelists.

```{list-table} PENDING - Groundwater - 4ᵗʰ cycle - **GroundWaterBodyStatus** table
    :name: Groundwater_Issues_Pending_Discussion_GroundWaterBodyStatus
    :width: 100%
    :widths: 40 40 20
    :header-rows: 1
    :align: left

* - Attribute
  - Description
  - Status

* - gwQuantitativeStatusValue
  - Can be removed. It is already in GWQuantitativeStatus table.
  - Pending

* - gwChemicalStatusValue
  - Can be derived from the data in the GWPollutant table.  
    Else, it can be mantained **for QC purposes**.
  - Pending

* - gwAtRiskQuantitative
  - To be removed, if the time frame no longer applies.  
    Else, the definition must be clarified.
  - Pending

* - gwAtRiskChemical
  - To be removed, if the time frame no longer applies.  
    Else, can be derived from the data in the GWPollutant table.  
    Else, it can be mantained **for QC purposes** and the definition must be clarified.
  - Pending

* - gwQuantitativeReasonsForFailure
  - To be analysed - potential overlaps with pressures.  
  - Pending

* - gwChemicalReasonsForFailure
  - To be analysed - potential overlaps with pressures.  
  - Pending

* - gwReasonsForRiskQuantitative
  - To be analysed - potential overlaps with pressures.  
    Also depends on the decision about gwAtRiskQuantitative.
  - Pending

```


```{list-table} PENDING - Groundwater - 4ᵗʰ cycle - **GWPollutant** table
    :name: Groundwater_Issues_Pending_Discussion_GWPollutant
    :width: 100%
    :widths: 40 40 20
    :header-rows: 1
    :align: left

* - Attribute
  - Description
  - Status

* - gwPollutantCausingRisk
  - To be removed, if the time frame no longer applies.  
    Else, the definition must be clarified and which in the subset of pollutants to which it applies.
  - Pending

* - gwPollutantAssessmentMethod
  - To be discussed together with the SW part.
  - Pending  

* - gwPollutantAssessmentGrouping
  - To be discussed together with the SW part.
  - Pending  
```

```{list-table} PENDING - Groundwater - 4ᵗʰ cycle - **GWQuantitativeStatus** table
    :name: Groundwater_Issues_Pending_Discussion_GWQuantitativeStatus
    :width: 100%
    :widths: 40 40 20
    :header-rows: 1
    :align: left

* - Attribute
  - Description
  - Status

* - gwQuantitativeAssessmentMethod
  - To be discussed together with the SW part.
  - Pending  

* - gwQuantitativeAssessmentGrouping
  - To be discussed together with the SW part.
  - Pending  
```

```{list-table} PENDING - Groundwater - 4ᵗʰ cycle - **LinkSurfaceWaterBody** table
    :name: Groundwater_Issues_Pending_Discussion_LinkSurfaceWaterBody
    :width: 100%
    :widths: 40 40 20
    :header-rows: 1
    :align: left

* - Attribute
  - Description
  - Status

* - linkType
  - Add attribute to clarify the type of link?
  - Pending

```


## Groundwater - descriptive data - 4ᵗʰ cycle

{numref}`_INCOMPLETE_Groundwater_DescriptiveData_4thCycle_ClassDiagram` shows an INCOMPLETE diagram 
with the a structure that may not require further internal discussion.

The data was organised into a relational structure with 6 tables:

```{list-table} Groundwater - 4ᵗʰ cycle - brief table description
    :name: Groundwater_4th_cycle_brief_table_description
    :width: 100%
    :widths: 30 70
    :header-rows: 1
    :align: left

* - Table
  - Description

* - GroundWaterBody
  - The **GroundWaterBody** table contains attributes that describe the groundwater body 
    and that do not vary with the status of the waterbody.  
    The geologicalFormation attribute was divided in **aquiferType** and **aquiferProductivity**, 
    using the approach already in place in the published WISE_WFD database.

* - LinkSurfaceWaterBody
  - If **GroundWaterBody.linkSurfaceWaterBody = 'yes'**, 
    then the LinkSurfaceWaterBody table is used to report the identifier(s) 
    of the linked surface water body(ies).

* - GWPressureImpact
  - In the reporting of pressures and impacts is combined into a single **GWPressureImpact** table.  
    In the 3ʳᵈ cycle, the XML structure did not allow a specific pressure to be associated with a given impact.
    In the proposed structure, this is possible (but not mandatory).  
    Illustrative examples will be provided.

* - GWQuantitativeStatus
  - The **GWQuantitativeStatus** table gathers the data related to quantitative status.  
    The GWQuantitativeStatus data has a one-to-one relationship with the GroundWaterBody.  
    The separation into two tables simplifies the reporting process 
    (by allowing the GroundWaterBody table to be prepared in advance).

* - GWPollutant
  - The **GWPollutant** table gathers the data related to chemical status.  
    Note that the information about the gwPollutantAssessmentPeriod and gwPollutantAssessmentConfidence is now at gwPollutantCode level, 
    and not at water body level.  
    This allows more flexibility in the reporting. 
    If data is not available at pollutant level, 
    use the same values for all pollutants 
    (i.e. use the same approach as in the 3ʳᵈ cycle).
* - GroundWaterBodyStatus
  - Finally, the **GroundWaterBodyStatus** table contains information that can be derived from other tables and attributes.  
    This means that the table *can* possibly be removed from the reporting (depending on the pending decisions),  
    or can be kept for *quality control purposes* (namely to guarantee that there was no mistake in the reporting of substances causing failure).  
```

```{mermaid} /DataModelReview/mmd/_INCOMPLETE_Groundwater_DescriptiveData_4thCycle_ClassDiagram.mmd
:name: _INCOMPLETE_Groundwater_DescriptiveData_4thCycle_ClassDiagram
:align: center
:caption: INCOMPLETE DIAGRAM - Groundwater - 4ᵗʰ cycle
```

## References

The complete schemas for the 3ʳᵈ cycle of reporting can be found in the [WFD2022 EAP file](https://cdr.eionet.europa.eu/help/WFD/WFD_715_2022/UML%20Data%20specification/WFD2022.EAP).

