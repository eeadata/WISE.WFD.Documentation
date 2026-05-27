(heading_wfd_groundwater_bodies)=
# WFD groundwater bodies

Last update: 2026-05-14

```{danger}
DRAFT INTERNAL VERSION - PENDING DISCUSSION - DO NOT USE
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

Based on the Commission's review of the 3ʳᵈ cycle reporting, the following elements were removed:

* GWB/GroundWaterBody/gwEORiskQuantitative 
* GWB/GroundWaterBody/gwEORiskChemical 
* GWB/GroundWaterBody/gwAtRiskQuantitative
* GWB/GroundWaterBody/gwAtRiskChemical
* GWB/GroundWaterBody/gwReasonsForRiskQuantitative
* GWB/GroundWaterBody/GWPollutant/gwPollutantExceedancesNotCounted

## Groundwater - descriptive data - 4ᵗʰ cycle

{numref}`Groundwater_DescriptiveData_4thCycle_ClassDiagram` 
shows a DRAFT diagram including the issues requiring clarification, in the classes marked in red.

```{mermaid} /DataModelReview/mmd/Groundwater_DescriptiveData_4thCycle_ClassDiagram.mmd
:name: Groundwater_DescriptiveData_4thCycle_ClassDiagram
:align: center
:caption: DRAFT DIAGRAM - ISSUES PENDING DISCUSSION - Groundwater - 4ᵗʰ cycle
```

```{todo}
Groundwater - Topics that require discussion and clarification.

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

* - gwQuantitativeReasonsForFailure
  - To be analysed - potential overlaps with pressures.  
  - Pending

* - gwChemicalReasonsForFailure
  - To be analysed - potential overlaps with pressures.  
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

The data was organised into a relational structure with 6 tables:

```{list-table} Groundwater - 4ᵗʰ cycle - brief table description
    :name: Groundwater_4th_cycle_brief_table_description
    :width: 100%
    :widths: 30 70
    :header-rows: 1
    :align: left

* - Table
  - Description

* - `GroundWaterBody`
  - The `GroundWaterBody` table contains attributes that describe the groundwater body 
    and that do not vary with the status of the waterbody.  
    The geologicalFormation attribute was divided in `aquiferType` and `aquiferProductivity`, 
    using the approach already in place in the published WISE_WFD database.

* - `LinkSurfaceWaterBody`
  - If `GroundWaterBody.linkSurfaceWaterBody = 'yes'`, 
    then the `LinkSurfaceWaterBody` table is used to report the identifier(s) 
    of the linked surface water body(ies).

* - `GWPressureImpact`
  - In the reporting of pressures and impacts 
    is combined into a single `GWPressureImpact` table.  
    In the 3ʳᵈ cycle, the XML structure did not allow a specific pressure to be associated with a given impact.
    In the proposed structure, this is possible (but not mandatory).  
    Illustrative examples will be provided.

* - `GWQuantitativeStatus`
  - The `GWQuantitativeStatus` table gathers the data related to quantitative status.  
    Each `GWQuantitativeStatus` record has a one-to-one relationship with a `GroundWaterBody` record.  
    The separation into two tables simplifies the reporting process 
    (by allowing the `GroundWaterBody` table to be prepared in advance, 
    and without any dependency to the statuses of the waterbody).

* - `GWPollutant`
  - The `GWPollutant` table gathers the data related to chemical status.  
    Note that the information about the `gwPollutantAssessmentPeriod` and `gwPollutantAssessmentConfidence` is now reported at `gwPollutantCode` level, 
    and not at water body level.  
    This allows more flexibility in the reporting. 
    If data is not available at pollutant level, the same values of `gwPollutantAssessmentPeriod` and `gwPollutantAssessmentConfidence` 
    can be used for all pollutants 
    (i.e. use the same approach as in the 3ʳᵈ cycle).

* - `GroundWaterBodyStatus`
  - Finally, the `GroundWaterBodyStatus` table contains information 
    that can be derived from other tables and attributes. 
    The table could be removed from the reporting, 
    but will be kept for *quality control purposes*,
    e.g. to guarantee that there was no mistake 
    in the reporting of substances causing failure.  
```

## Annexes - Data analysis - 3ʳᵈ cycle

```{include} FragmentAnnexesDataAnalysis3rdCycle
```

```{dropdown} Show code
  ```{code-block} sql
  :caption: [gwChemicalStatusValue] vs [gwChemicalReasonsForFailure] - 3ʳᵈ cycle
  :linenos:
  -- https://discodata.eea.europa.eu/

  SELECT [gwChemicalStatusValue]
    ,[gwChemicalReasonsForFailure]
    ,COUNT(DISTINCT [euGroundWaterBodyCode]) AS numberOfGroundWaterBodies
    ,COUNT(DISTINCT [countryCode]) AS numberOfCountries
  FROM [WISE_WFD].[v2r1].[GWB_GroundWaterBody_gwChemicalReasonsForFailure]
  WHERE [cYear] = 2022 AND [hasDescriptiveData] = 1
  GROUP BY [gwChemicalStatusValue],[gwChemicalReasonsForFailure]
  ```

```{dropdown} Show code
  ```{code-block} sql
  :caption: Number of reasons for chemical failure - 3ʳᵈ cycle
  :linenos:
  -- https://discodata.eea.europa.eu/
  SELECT [numberOfReasonsForFailure],
	COUNT(DISTINCT [euGroundWaterBodyCode]) AS [numberOfGroundWaterBodies],
	COUNT(DISTINCT [countryCode]) AS [numberOfCountries]
  FROM 
  (
  SELECT [countryCode],[euGroundWaterBodyCode]
    ,COUNT(DISTINCT [gwChemicalReasonsForFailure]) AS [numberOfReasonsForFailure]
  FROM [WISE_WFD].[v2r1].[GWB_GroundWaterBody_gwChemicalReasonsForFailure]
  WHERE [cYear] = 2022 AND [hasDescriptiveData] = 1 
  GROUP BY [countryCode],[euGroundWaterBodyCode]
  ) AS a
  GROUP BY [numberOfReasonsForFailure]
  ```

```{dropdown} Show code
  ```{code-block} sql
  :caption: [gwQuantitativeStatusValue] vs [gwQuantitativeReasonsForFailure] - 3ʳᵈ cycle
  :linenos:
  -- https://discodata.eea.europa.eu/

  SELECT [gwQuantitativeStatusValue]
    ,[gwQuantitativeReasonsForFailure]
    ,COUNT(DISTINCT [euGroundWaterBodyCode]) AS numberOfGroundWaterBodies
    ,COUNT(DISTINCT [countryCode]) AS numberOfCountries
  FROM [WISE_WFD].[v2r1].[GWB_GroundWaterBody_gwQuantitativeReasonsForFailure]
  WHERE [cYear] = 2022 AND [hasDescriptiveData] = 1
  GROUP BY [gwQuantitativeStatusValue],[gwQuantitativeReasonsForFailure]
  ```

```{dropdown} Show code
  ```{code-block} sql
  :caption: Number of reasons for quantitative failure - 3ʳᵈ cycle
  :linenos:
  -- https://discodata.eea.europa.eu/

  SELECT [numberOfReasonsForFailure],
    COUNT(DISTINCT [euGroundWaterBodyCode]) AS numberOfGroundWaterBodies,
    COUNT(DISTINCT [countryCode]) AS numberOfCountries
  FROM 
  (
  SELECT [countryCode],[euGroundWaterBodyCode]
    ,COUNT(DISTINCT [gwQuantitativeReasonsForFailure]) AS [numberOfReasonsForFailure]
  FROM [WISE_WFD].[v2r1].[GWB_GroundWaterBody_gwQuantitativeReasonsForFailure]
  WHERE [cYear] = 2022 AND [hasDescriptiveData] = 1 
  GROUP BY [countryCode],[euGroundWaterBodyCode]
  ) AS a
  GROUP BY [numberOfReasonsForFailure]
  ```

(heading_wfd_wfd_groundwater_bodies_references)=
## References

```{include} FragmentReportingGuidanceFiles
```
