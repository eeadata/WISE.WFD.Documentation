(heading_wfd_surface_water_bodies)=
# Surface water bodies

Last update: 2026-06-04

```{Warning}
Public Version - Pending Discussion
```

(heading_wfd_surface_water_bodies_purpose_and_overview)=
## Purpose and overview

This section revises the reporting of information related to **Surface Water Bodies**
in the 2nd and 3rd cycle of reporting of the Water Framework Directive River Basin Management Plans.
It also presents a proposal for simplifying the electronic reporting in the 4th cycle.

(heading_wfd_surface_water_bodies_current_structure_3rd_cycle)=
## Current structure - 3rd cycle

The information about Surface water bodies was reported in five separate schemas:

* the SWB_2022 schema, containing information about each surface water body ({numref}`SurfaceWater_3rdCycle_SWB_ClassDiagram`)
* the SWMET_2022 schema, containing information about the methodologies (see {ref}`heading_wfd_surface_water_methodologies`)
* the GML_SurfaceWaterBody_2022 schema and GML_SurfaceWaterBodyLine_2022 schema, containing the SurfaceWaterBody spatial dataset.
* the GML_SurfaceWaterBodyCentreline_2022 schema, containing the ancillary SurfaceWaterBodyCentreline spatial dataset.

```{mermaid} /DataModelReview/mmd/SurfaceWater_3rdCycle_SWB_ClassDiagram.mmd
:name: SurfaceWater_3rdCycle_SWB_ClassDiagram
:align: center
:caption: Class diagram for the SWB_2022 schema in the 3rd cycle of reporting.
```

(heading_wfd_surface_water_bodies_SWB_schema_3rd_cycle)=
## SWB_2022 schema - 3rd cycle

The SWB_2022 schema was already partially revised with regard to the reporting of exemptions.
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
:caption: PARTIAL class diagram for the SWB_2022 schema in the 3rd cycle of reporting.
```

## Surface water - descriptive data - 4th cycle

The proposed structure for the 4th cycle electronic reporting is presented in the class diagram in ({numref}`SurfaceWater_4thCycle_DescriptiveData_ClassDiagram`) and a brief description of each table is included in {numref}`SurfaceWater_4th_cycle_brief_table_description`.

```{mermaid} /DataModelReview/mmd/SurfaceWater_4thCycle_DescriptiveData_ClassDiagram.mmd
:name: SurfaceWater_4thCycle_DescriptiveData_ClassDiagram
:align: center
:caption: Surface water - 4th cycle
```

```{list-table} Surface water - 4th cycle - brief table description
:name: SurfaceWater_4th_cycle_brief_table_description
:header-rows: 1
:width: 100%
:widths: 20 80
:align: left

* - Table
  - Description

* - SurfaceWaterBody
  - *modified*  
    The `SurfaceWaterBody` table contains the attributes 
    that describe the surface water body 
    and that do not vary with the status of the water body.
    Therefore the table can be prepared immediately, 
    even if the 4th cycle RBMPs have not yet been finalised. 
    All the attributes existed in the 3rd cycle reporting. 

* - SWHeavilyModifiedWaterBody
  - *modified*  
    

* - SWStatus
  - *new*  
    The `SWStatus` table synthesizes 
    information about the status of the water body.
    
    Formally, the `chemicalStatusValue` 
    could be derived from the information in the `SWPollutant` table.  
    If, and only if, `chemicalStatusValue = 'unknown'` 
    and no assessment of the chemical status was done,
    may all corresponding rows in the `SWPollutant` table be missing.
    (An ERROR will raised by the quality control, since this is a non-compliance 
    and should not be reported by mistake.)

    Likewise, the `swEcologicalStatusOrPotentialValue` 
    could be derived from the `SWQualityElement` table.  
    If, and only if, `swEcologicalStatusOrPotentialValue = 'unknown'` 
    and no assessment of the ecological status was done,
    may the corresponding rows in the `SWQualityElement` table be missing.
    (An ERROR will raised by the quality control, since this is a non-compliance 
    and should not be reported by mistake.) 

* - SWPollutant
  - *modified*  
    The `SWPollutant` table contains data related to the chemical status at substance level.  
    The information about the assessment method, assessment confidence, 
    and assessment period can be reported at pollutant level, 
    allowing more flexibility in reporting different situations 
    for different pollutants or indicators of pollution. 
    (If the same method, confidence and period apply 
    to all substances assessed for a surface water body, 
    then identical values can be reported for all substances).
    
* - SWQualityElement
  - *new*  
    The `SWQualityElement` table gathers 
    the data related to ecological status or potential.  
    The assessment method, confidence and period 
    is reported using the same pattern 
    applied for surface water pollutants.

* - SWGrouping
  - *new*   
    If grouping was not used, this table is not necessary.  
    If grouping was used for the 
    assessment of ecological or chemical status,
    the `SWGrouping` table is used 
    to define sets of water bodies 
    that were monitored and assessed as an ensemble.
    The same ensemble can be used for different purposes. 
    The same water body can be a member of different ensembles.
    
    The `groupingIdentifier` value uniquely identifies an ensemble 
    using the WISE identifier syntax.
    The `euSurfaceWaterBodyCode` identifies a member of the ensemble.  
    If an ensemble is used 
    in the assessment of a given element,
    then at least one of its water bodies
    must be monitored for that element
    (e.g. must have `swPollutantAssessmentMethod = 'monitoring'`).  
    (To avoid mistakes and ambiguities, 
    the `groupingIdentifier` value must be different 
    from any known water body identifier. 
    It is recommended to use a clear pattern 
    to avoid conflicts with existing 
    and future water body identifiers.
    For example, using a '_SWGROUPING' suffix).       

* - SWPressureImpact
  - *modified*.  
    For the water bodies that do not achieve good ecological status or potential in 2027, 
    the significant pressures causing poor ecological status or potential 
    are reported in the `SWEcologicalExemption` table 
    (see {numref}`Exemptions_4thCycle_SWEcologicalExemption_ClassDiagram`) 
    and do not need to be reported again in the `SWPressureImpact` table.

    For water bodies that do not achieve good chemical status in 2027, 
    the significant pressures are reported in the `SWChemicalExemption` table 
    (see {numref}`Exemptions_4thCycle_SWChemicalExemption_ClassDiagram`) 
    and do not need to be reported again in the `SWPressureImpact` table.
    
    For cases where a pressure is not causing failure, 
    but still causes an impact that needs to be managed, 
    the `SWPressureImpact` table should be used.

    Note that the reporting of pressures and impacts 
    is combined into a single `SWPressureImpact` table. 
    In the 3rd cycle, the XML structure did not allow 
    a specific pressure to be link to a given impact.
    In the proposed structure, this is possible (but not mandatory).  
    Illustrative examples will be provided.  
```

(heading_wfd_surface_water_codelist_4th_cycle)=
## Surface water - codelists - 4th cycle

* For the `Reservoir` codelist,
  see {numref}`Codelist_4thCycle_Reservoir_HMWBWaterUse_HMWBPhysicalAlteration_ClassDiagram`.  
  All reservoirs must be reported as artificial or heavily modified lakes
  (see {numref}`Codelist_4thCycle_Reservoir_Table`).

* For the `HMWBPhysicalAlteration` codelist,
  see {numref}`Codelist_4thCycle_Reservoir_HMWBWaterUse_HMWBPhysicalAlteration_ClassDiagram`.  
  For heavily modified water bodies only, use this codelist to report the physical
  alteration that has resulted in the designation of the surface water body as a HMWB.  
  In the context of designation as a HMWB, physical alterations means
  any significant alterations that have resulted in substantial changes
  to the hydromorphology of a surface water body such that the surface water body
  is substantially changed in character.
  In general, these hydromorphological characteristics are long term
  and alter both the morphological and hydrological characteristics.
  (See {numref}`Codelist_4thCycle_HMWBPhysicalAlteration_Table`.)

* For the `HMWBWaterUse` codelist,
  see {numref}`Codelist_4thCycle_Reservoir_HMWBWaterUse_HMWBPhysicalAlteration_ClassDiagram`.  
  For heavily modified water bodies only, use this codelist to report the water use for
  which the water body has been designated. According to Art. 4(3) of the WFD,
  the water use for which a HMWB
  was designated is the water use that would be affected significantly by the changes that would be
  necessary to achieve good ecological status.
  (See {numref}`Codelist_4thCycle_HMWBWaterUse_Table`.)  

* For the `AssessmentMethod` codelist,
  see {numref}`Codelist_4thCycle_AssessmentMethod_AssessmentConfidence_ClassDiagram`.  
  The codelist is used to report
  the assessment method for the chemical status and
  the assessment method for the ecological status
  (see {numref}`Codelist_4thCycle_AssessmentMethod_Table`).  
  The same codelist is used for groundwater bodies,
  to report the assessment method of quantitative status,
  and the assessment method of chemical status.

* For the `AssessmentConfidence` codelist,
  see also {numref}`Codelist_4thCycle_AssessmentMethod_AssessmentConfidence_ClassDiagram`.  
  The codelist allow the reporting of
  the level of confidence in the results of the status assessment
  (see {numref}`Codelist_4thCycle_AssessmentConfidence_Table`).  
  The same codelist is used for groundwater bodies.

* For the `PressureType` codelist,
  see {numref}`Codelist_4thCycle_PressureType_ClassDiagram` in
  the section {ref}`heading_wfd_pressure_type_codelist_4th_cycle`

% -----------------------------------------------------------------------------

```{mermaid} /DataModelReview/mmd/Codelist_4thCycle_Reservoir_HMWBWaterUse_HMWBPhysicalAlteration_ClassDiagram.mmd
:name: Codelist_4thCycle_Reservoir_HMWBWaterUse_HMWBPhysicalAlteration_ClassDiagram
:align: center
:caption: Reservoir codelist, HMWBWaterUse codelist, and HMWBPhysicalAlteration codelist - 4th cycle
```

```{include} /DataModelReview/tables/Codelist_4thCycle_Reservoir_Table
```

```{include} /DataModelReview/tables/Codelist_4thCycle_HMWBWaterUse_Table
```

```{dropdown} Click to see the mapping table between 3rd cycle and 4th cycle codes
```{include} /DataModelReview/tables/MappingTable_4thCycle_HMWBWaterUse_Table
```

```{include} /DataModelReview/tables/Codelist_4thCycle_HMWBPhysicalAlteration_Table
```

% -----------------------------------------------------------------------------

(heading_wfd_surface_water_bodies_ecological_status)=
## Ecological status and potential

The diagram below, adapted from Figure 1 in the CIS Guidance Document 13,
illustrates the assessment criteria for ecological status ({numref}`SurfaceWater_EcologicalStatus_CISGuidance_Flowchart`).

```{mermaid} /DataModelReview/mmd/SurfaceWater_EcologicalStatus_CISGuidance_Flowchart.mmd
:name: SurfaceWater_EcologicalStatus_CISGuidance_Flowchart
:caption: Surface Water Body - Ecological status assessment
:align: center
```

The diagram below, adapted from Figure 2 in the CIS Guidance document 13,
illustrates the assessment criteria for ecological potential ({numref}`SurfaceWater_EcologicalPotential_CISGuidance_Flowchart`).

```{mermaid} /DataModelReview/mmd/SurfaceWater_EcologicalPotential_CISGuidance_Flowchart.mmd
:name: SurfaceWater_EcologicalPotential_CISGuidance_Flowchart
:caption: Surface Water Body - Ecological potential assessment
:align: center
```

(heading_wfd_surface_water_bodies_annexes)=
## Annexes - Data analysis - 3rd cycle

```{admonition} Changes to the quality check during the 3rd cycle reporting phase
:class: dropdown

Several data quality issues where detected 
while the 3rd cycle was ongoing (i.e. after the testing phase).

That required the implementation of additional quality checks, 
or the correction of existing quality checks.

For example, the reporting guidance 
was not always clear in the distinction 
between conditions in the form *"if A then B"*
versus conditions in the form *if and only if A then B*.

On a case-by-case decision, 
resubmissions may have been requested or not. 
Therefore the database may contain inconsistencies (e.g. in early submissions) that were detected and blocked (in later submissions).
```

### Quality element status (3rd, 2nd and 1st RBMP), by category

The following dashboard shows the number of quality elements
used in the assessment of the ecological status or potential:

```{figure} https://tableau-public.discomap.eea.europa.eu/views/WFD_SWB_QualityElement_Status_Compare/SWB_QualityElement_Category.png
:width: 1024
:alt: Click to open an interactive dashboard
:name: dashboard_WFD_SWB_QualityElement_Status_Compare_SWB_QualityElement_Category
:target: https://tableau-public.discomap.eea.europa.eu/views/WFD_SWB_QualityElement_Status_Compare/SWB_QualityElement_Category

Surface water bodies: Quality element status (3rd, 2nd and 1st RBMP), by category

```

### Number of quality elements used

The following dashboard shows the number of quality elements
used in the assessment of the ecological status or potential:

```{figure} https://tableau-public.discomap.eea.europa.eu/views/WFD_SWB_QualityElement_QEUsed/SWB_QualityElement_QEUsed_Category.png
:width: 1024
:alt: Click to open an interactive dashboard
:name: dashboard_WFD_SWB_QualityElement_QEUsed/SWB_QualityElement_QEUsed_Category
:target: https://tableau-public.discomap.eea.europa.eu/views/WFD_SWB_QualityElement_QEUsed/SWB_QualityElement_QEUsed_Category

Surface water bodies: Number of quality elements used in the assessment of the ecological status or potential
```

### Status calculated from the quality elements

The following dashboard shows the reported ecological status vs. calculated ecological status (based on the quality elements):

```{figure} https://tableau-public.discomap.eea.europa.eu/views/WFD_SWB_EcologicalStatus_Calculated/SWB_EcologicalStatus_Calculated_Category.png
:width: 1024
:alt: Click to open an interactive dashboard
:name: dashboard_WFD_SWB_EcologicalStatus_Calculated_SWB_EcologicalStatus_Calculated_Category
:target: https://tableau-public.discomap.eea.europa.eu/views/WFD_SWB_EcologicalStatus_Calculated/SWB_EcologicalStatus_Calculated_Category

Surface water bodies: Ecological status or potential calculated from the quality elements, by category
```

### Quality element status

In the 3rd cycle reporting,
the quality element status value was reported
using the following values:

* '1' meaning 'high' status or potential
* '2' meaning 'good' status or potential
* 'Unknown' meaning 'unknown' status or potential
* "Not applicable" meaning the quality element is not applicable
   in the surface water category or water body national type
   to which the water body in question belongs.

For *biological quality elements* **only**,
the following values were also used:

* '3' meaning 'moderate' status or potential
* '4' meaning 'poor' status or potential
* '5' meaning 'bad' status or potential

For *hydro-morphological and physico-chemical quality elements* **only**,
the following values were also used:

* '3' meaning 'less than good' status or potential
* "Monitored but not used" meaning than
   the QE was monitored but no standard has been developed **and/or**
   the QE is not used for status assessment

```{dropdown} Show technical detail: encoding quality element status

  To harmonise the data in different codelists and reporting cycles, 
  the reported values were recoded in the published [WISE_WFD].  
  {numref}`mapping_lov_for_QEStatusCode_3rd_cycle_table` 
  shows the original codes (`id`) and the published codes (`mappingId`).

  ```{table} Encoding quality element status in the [WISE_WFD] database.
  :name: mapping_lov_for_QEStatusCode_3rd_cycle_table
  :width: 100%
  :align: center

  |tableName|id|label|mappingTable|mappingId|
  |---|---|---|---|---|
  |QEStatusCode|-1|Not a value(NULL).|NilReasonType|unpopulated|
  |QEStatusCode|1|1|WFDStatus|1|
  |QEStatusCode|2|2|WFDStatus|2|
  |QEStatusCode|3|3|WFDStatus|3|
  |QEStatusCode|4|4|WFDStatus|4|
  |QEStatusCode|5|5|WFDStatus|5|
  |QEStatusCode|6|MonitoredButNotUsed|NilReasonType|none|
  |QEStatusCode|7|Unknown|NilReasonType|unknown|
  |QEStatusCode|8|NotApplicable|NilReasonType|inapplicable|
  ```

### *"Monitored but not used"*

The option *"Monitored but not used"* was inherently ambiguous,
because it could be applied to signify that
the quality element was being monitored
although it was in fact not applicable
to a specific water category or water body national type.

```{todo}
The option *"Monitored but not used"* should be removed, 
because it does not convey concrete information about the *status*.  
Member States can report monitoring results 
under the WISE-6 Water Quality dataflow: 
that provides concrete information 
about what is being monitored 
beyond the requirements of the ecological status assessment.
```

### *"Not applicable"*

The 3rd cycle reporting guidance provided
a clear definition of the option *"Not applicable"*.  

```{epigraph}
If the QE is not applicable in the surface water category or type to which the
water body in question belongs, then select ‘Not applicable’ from the enumeration list. 
```

Theoretically, it should be possible to derive
the applicability of the quality elements
to a given type or category.

```{dropdown} Show code: applicable QEs per water category or national type

  ```{code-block} sql
  :caption: Quality elements per water category or national type.
  :linenos:
  -- https://discodata.eea.europa.eu/
  SELECT  [countryCode]
        ,[surfaceWaterBodyCategory]
        ,[NCSWaterBodyType]
        ,[qeCode]
        ,MAX(IIF([qeStatusOrPotentialValue] IN ('1','2','3','4','5','unknown'),1,0)) AS qeApplicable
        ,MAX(IIF([qeStatusOrPotentialValue] IN ('inapplicable'),1,0)) AS qeInapplicable
    FROM [WISE_WFD].[v2r1].[SWB_SurfaceWaterBody_QualityElement] a
    WHERE a.[cYear] = 2022
    AND a.[hasDescriptiveData] = 1
    AND a.[qeCode] != 'QE3-3 - River Basin Specific Pollutants'
    GROUP BY [countryCode]
            ,[surfaceWaterBodyCategory]
            ,[NCSWaterBodyType]
            ,[qeCode]
    -- uncomment the next two lines to identify reporting errors
    -- HAVING MAX(IIF([qeStatusOrPotentialValue] IN ('1','2','3','4','5','unknown'),1,0)) = 1
    --  AND MAX(IIF([qeStatusOrPotentialValue] IN ('inapplicable'),1,0)) = 1
    ORDER BY [countryCode]
            ,[surfaceWaterBodyCategory]
            ,[NCSWaterBodyType]
            ,[qeCode]
  ```

For 77% of the 3384 reported national types,
the applicability of the quality elements
can indeed be derived.  
Unfortunately, for the remaining 772 national types
(23% of the total) the information is inconsistent,
and a given quality element is simultaneously reported
as applicable (because it has a reported status)
and not applicable to the assessment of ecological status.

It is possible that the inconsistencies
are due to an interchangeable use or interpretation
of the options 'unknown' and 'inapplicable',
or are due to a mistake in the reporting of some water bodies only.

Nevertheless, the inconsistencies reveal a flaw in the reporting model,
and an opportunity for both improvement and simplification.
the applicability of the quality elements
should be reported in the *surface water methodologies*
and *only* the applicable quality elements should be
reported in the *quality elements* table.

### Proposed changes

The removal of the options *"Not applicable"* and *"Monitored but not used"*
reduces the reported data by 25%
and provides a clearer and consistent overview
of the assessment criteria.

```{table} Number of records per QE status
:name: number_of_records_per_qe_status_3rd_cycle_table
:width: 100%
:align: center

|qeStatusOrPotentialValue|number of records|% of records|
|---|---|---|
|1,2,3,4,5|  636,742|  25%|
|Unknown|  1,208,667|  48%|
|*"Not applicable"*|  541,637|  21%|
|*"Monitored but not used"*|  136,743  |5%|
```

```{todo}
The applicability of the quality elements 
should be reported in the *surface water methodologies* 
and *only* the applicable quality elements should be
reported in the *quality elements* table.
```

### Ecological status and BQE status

If a biological quality element fails to achieve 'good' or 'high' status,
then the ecological status or potential cannot be 'good' or 'high'.

The majority of reported data complies with this rule.

A total of 216 water bodies does *not* comply with this rule.
The question is, *can the reported ecological status or potential be 'unknown'*?

```{dropdown} Show code

  ```{code-block} sql
  :caption: Ecological status vs. failing biological quality element status.
  :linenos:
  -- https://discodata.eea.europa.eu/
  
  SELECT a.[swEcologicalStatusOrPotentialValue]
      ,COUNT(DISTINCT IIF(a.[qeStatusOrPotentialValue] IN ('3','4','5'), [euSurfaceWaterBodyCode], null)) AS wbWithFailingBQE
  FROM  [WISE_WFD].[v2r1].[SWB_SurfaceWaterBody_QualityElement] a
  WHERE a.[qeCode] LIKE 'QE1%'
    AND a.[cYear] = 2022
    AND a.[hasDescriptiveData] = 1
  GROUP BY a.[swEcologicalStatusOrPotentialValue]
  ```

From a logical (mathematical) perspective, the ecological status can be 'undeterminate',
if not all the relevant biological quality elements were assessed,
and therefore it could be 'moderate', 'poor' or 'bad'.
But the ecological status is known to fail to achieve good status.

Furthermore, the analysis of the 216 water bodies shows that:

* in 71 cases, the ecological status should have been reported as 'bad'
* in 69 cases, the ecological status could never be 'moderate'.

```{table} Unknown ecological status of water bodies with failing BQEs.
:name: unknown_ecological_status_and_failing_bqes_3rd_cycle_table
:width: 100%
:align: center

|worstBQE|numberOfWB|numberOfCountries|
|---|---|---|
|3|76|5|
|4|69|3|
|5|71|3|
||216|5|

```

The low frequency of these cases suggests a reporting error,
that must be captured in the quality control during the 4th cycle.

### Proposed change

If at least one biological quality element
has 'moderate', 'poor' or 'bad' status or potential,
then the ecological status cannot be 'unknown'.

```{todo}
If at least one biological quality element 
has 'moderate', 'poor' or 'bad' status or potential, 
then the ecological status cannot be 'unknown'. 

Clearer guidance must be provided to MS with regard to these cases.  
The quality control must enforce the adopted guidance.
```

```{dropdown} Show code

  ```{code-block} sql
  :caption: Worst biological quality element status and ecological status.
  :linenos:
  -- https://discodata.eea.europa.eu/

  SELECT a.[worstBQE]
        ,COUNT(DISTINCT a.[euSurfaceWaterBodyCode]) AS numberOfWB
        ,COUNT(DISTINCT a.[countryCode]) AS numberOfCountries
  FROM

    (SELECT a.[countryCode]
        ,a.[euSurfaceWaterBodyCode] 
        ,MAX(a.[qeStatusOrPotentialValue]) AS worstBQE
        ,COUNT(DISTINCT a.[euSurfaceWaterBodyCode]) AS numberOfWB
    FROM  [WISE_WFD].[v2r1].[SWB_SurfaceWaterBody_QualityElement] a
    WHERE a.[qeCode] LIKE 'QE1%'
    AND a.[qeStatusOrPotentialValue] IN ('3','4','5')
    AND a.[swEcologicalStatusOrPotentialValue] IN ('Unknown')
    AND a.[cYear] = 2022
    AND a.[hasDescriptiveData] = 1
    GROUP BY a.[countryCode],
            a.[euSurfaceWaterBodyCode]
    ) a
  GROUP BY ROLLUP(a.[worstBQE])
  ```

### One-out-all-out: ecological status

```{todo}
Include the CIS Guidance flowcharts
for the ecological status assessment.
```

According to the WFD Annex V
and as clarified in the CIS Guidance document 13,
the ecological status is assessed
using biological quality elements (QE1 a.k.a. BQE).

The physico-chemical quality elements (QE3)
act as *modifiers* of the BQE assessment:

* all applicable QE3 statuses must be 'high',
  for the ecological status to be 'high',
* if any applicable QE3 status is 'less than good',
  then the ecological status cannot be 'good'.

Likewise, the hydromorphological quality elements (QE2)
act as *modifiers* of the BQE assessment:

* all applicable QE2 statuses must be 'high',
  for the ecological status to be 'high',
* if any applicable QE3 status is 'less than good',
  then the ecological status cannot be 'good'.

In the 3rd cycle reporting,
the quality control checks enforced the interpretation above.
**Pending: confirm whether if changes are required.**

The hydromorphological quality elements

According to the 3rd cycle reporting guidance:

* *Rule 1:* "If SWB/SurfaceWaterBody/swEcologicalStatusOrPotentialValue = 1
  Then it cannot be lower than the highest of the values reported
  under SWB/SurfaceWaterBody/QualityElement/qeStatusOrPotentialValue"
* *Rule 2:* "If SWB/SurfaceWaterBody/swEcologicalStatusOrPotentialValue in (2,3,4,5)
  Then it cannot be lower than the highest of the values reported
  under SWB/SurfaceWaterBody/QualityElement/qeStatusOrPotentialValue
  for the set of quality elements
  where qeCode starts with QE1 or qeCode starts with QE3."
* *Rule 3:*  "If SWB/SurfaceWaterBody/swEcologicalStatusOrPotentialValue = 1
  Then at least one hydromorphological quality element (QE2%) must be assessed."
* *Rule 4:* "If the surface water body has a known status (1,2,3,4 or 5)
  the status of all Quality Elements cannot be 'Unknown', 'Not Applicable' or 'Monitored but not used'."

Preliminary comments:

* *Rule 3* requires that a QE2 be assessed,
  but does not explicitly mention the QE2 *status*,
  which should also be taken into account.
* *Rule 4* requires that at least one QE be assessed,
  but it should also require
  that at least at least one **QE1** be assessed.
* According to the CIS Guidance documents,
  the QE2 status should also be assessed
  if the ecological status is '1'
  and the worst QE3 status is also '1'.
* According to the CIS Guidance documents,
  the QE2 status should also be assessed
  for the artificial and highly modified water bodies.

Checking the *rule 2* (the ecological status cannot be worse than the worst QE1 or QE3):

* *As expected:* 114204 surface water bodies with ecological status
  equal to the status of the worst known QE1 or QE3

* *NOT as expected:* 309 surface water bodies with ecological status
  better than the status of the worst known QE1 or QE3.
  All the cases where due QE3-3 status (River Basin Specific Pollutants).

* *NOT as expected:* 5665 surface water bodies with ecological status
  worse than the status of the worst known QE1 or QE3.

  * *of which* 1717 surface water bodies
    failing to achieve good ecological status,
    when none of the QE1 or or QE3 status is failing.

Repeating the analysis without *'QE3-3 - River Basin Specific Pollutants'*,
the values are similar.

* *As expected:* 112315 surface water bodies with ecological status
  equal to the status of the worst known QE1, QE3-1 or QE3-2

* *As expected:* zero surface water bodies with ecological status
  better than the status of the worst known QE1, QE3-1 or QE3-2

* *NOT as expected:* 7015 surface water bodies with ecological status
  worse than the status of the worst known QE1, QE3-1 or QE3-2

  * *of which* 2535 surface water bodies
    failing to achieve good ecological status,
    when none of the QE1, QE3-1 or QE3-2 status is failing

This raises the question of how to compare
the ecological status reported in the 3rd cycle,
with the ecological status that will be reported in the 4th cycle.

Deriving the ecological status
from the reported quality elements statuses
might somewhat reduce the problem
(in the visualisations).

```{dropdown} Show code

  ```{code-block} sql
  :caption: Natural water bodies: ecological status vs the worst QE1, QE3-1 or QE3-2.
  :linenos:
  -- https://discodata.eea.europa.eu/
  SELECT COUNT(DISTINCT IIF([swEcologicalStatusOrPotentialValue] = [worstQE1OrQE3Status], [euSurfaceWaterBodyCode], NULL)) AS numberOfWB_StatusEqualToWorstQE1OrQE3Status
    ,COUNT(DISTINCT IIF([swEcologicalStatusOrPotentialValue] < [worstQE1OrQE3Status], [euSurfaceWaterBodyCode], NULL)) AS numberOfWB_StatusBetterThanWorstQE1OrQE3Status
    ,COUNT(DISTINCT IIF([swEcologicalStatusOrPotentialValue] > [worstQE1OrQE3Status], [euSurfaceWaterBodyCode], NULL)) AS numberOfWB_StatusWorseThanWorstQE1OrQE3Status
    ,COUNT(DISTINCT IIF([swEcologicalStatusOrPotentialValue] IN ('3','4','5') AND [worstQE1OrQE3Status] NOT IN ('3','4','5'),[euSurfaceWaterBodyCode], NULL)) AS numberOfWB_StatusWorseThanGood
  FROM
  (SELECT a.[swEcologicalStatusOrPotentialValue] 
        ,a.[euSurfaceWaterBodyCode]
        ,MAX(a.[qeStatusOrPotentialValue]) AS worstQE1OrQE3Status
    FROM  [WISE_WFD].[v2r1].[SWB_SurfaceWaterBody_QualityElement] a
    WHERE (a.[qeCode] LIKE 'QE1%' OR a.[qeCode] LIKE 'QE3-1%' OR a.[qeCode] LIKE 'QE3-2%')
    AND a.[qeStatusOrPotentialValue] IN ('1','2','3','4','5')
    AND a.[swEcologicalStatusOrPotentialValue] IN ('1','2','3','4','5')
    --AND a.[naturalAWBHMWB] = 'Natural water body'
    AND a.[cYear] = 2022
    AND a.[hasDescriptiveData] = 1
    GROUP BY a.[swEcologicalStatusOrPotentialValue] 
            ,a.[euSurfaceWaterBodyCode]) b
  ```

### River basin specific pollutants

According to the rules in the 3rd cycle of reporting,  
if the status or potential of 'QE3-3 - River Basin Specific Pollutants'
is less than good, than the failing RBSP must be reported.

This rule was enforced by the quality control.

```{dropdown} Show code

  ```{code-block} sql
  :caption: Reporting QE3-3 - River Basin Specific Pollutants and failing RBSPs.
  :linenos:
  -- https://discodata.eea.europa.eu/
  SELECT a.[countryCode]
      ,a.[euRBDCode]
      ,a.[euSurfaceWaterBodyCode]
      ,a.[swEcologicalStatusOrPotentialValue]
      ,a.[swChemicalStatusValue]
      ,a.[qeCode]
      ,a.[qeStatusOrPotentialValue]
      ,b.[swFailingRBSP]
  FROM  [WISE_WFD].[v2r1].[SWB_SurfaceWaterBody_QualityElement] a
  LEFT JOIN [WISE_WFD].[v2r1].[SWB_SurfaceWaterBody_FailingRBSP] b
  ON a.[euSurfaceWaterBodyCode] = b.[euSurfaceWaterBodyCode]
  AND a.[cYear] = b.[cYear]
  WHERE a.[qeCode] = 'QE3-3 - River Basin Specific Pollutants'
  AND a.[qeStatusOrPotentialValue] = '3'
  AND a.[cYear] = 2022
  AND a.[hasDescriptiveData] = 1
  ORDER BY a.[countryCode]
      ,a.[euRBDCode]
      ,a.[euSurfaceWaterBodyCode]
      ,a.[swEcologicalStatusOrPotentialValue]
  ```

The following table should that 2588 of those water bodies
were reported as being in good or unknown chemical status.
Incorporating the RBSPs into the chemical status assessment
changes the percentage of water bodies
not achieving good chemical status from 38% to 40%.

```{table} Chemical status of water bodies with failing QE3-3.
:name: chemical_status_with_failing_rbsp_3rd_cycle_table
:width: 100%
:align: center

|swChemicalStatusValue|numberOfCountries|numberOfWB|numberOfRBSP|
|---|---|---|---|
|2|18|2453|110|
|3|25|5192|167|
|Unknown|10|135|21|
|Total|25|7780|177|

```

```{dropdown} Show code

  ```{code-block} sql
  :caption: Reporting QE3-3 - River Basin Specific Pollutants and failing RBSPs.
  :linenos:
  -- https://discodata.eea.europa.eu/
  SELECT a.[swChemicalStatusValue]
    ,COUNT(DISTINCT a.[countryCode]) AS numberOfCountries
    ,COUNT(DISTINCT a.[euSurfaceWaterBodyCode]) AS numberOfWB
    ,COUNT(DISTINCT b.[swFailingRBSP]) AS numberOfRBSP
  FROM  [WISE_WFD].[v2r1].[SWB_SurfaceWaterBody_QualityElement] a
  LEFT JOIN [WISE_WFD].[v2r1].[SWB_SurfaceWaterBody_FailingRBSP] b
    ON a.[euSurfaceWaterBodyCode] = b.[euSurfaceWaterBodyCode]
    AND a.[cYear] = b.[cYear]
  WHERE a.[qeCode] = 'QE3-3 - River Basin Specific Pollutants'
    AND a.[qeStatusOrPotentialValue] = '3'
    AND a.[cYear] = 2022
    AND a.[hasDescriptiveData] = 1
  GROUP BY a.[swChemicalStatusValue]

  ```

(heading_wfd_heavily_modified_water_bodies)=
### Heavily modified water bodies

For 60% of the heavily modified water bodies, only one physical alteration and only one water use is reported.
It doesn't make sense to keep the two separate tables used in the 3rd cycle:
it complicates the reporting and does not allow a link to be made between the alteration and the use.

```{figure} /DataModelReview/img/HMWB_NumberOfAlteration_NumberOfUses.png
:name: HMWB_NumberOfAlteration_NumberOfUses
:width: 100%
:align: center
Heavily modified water bodies - Number of different physical alterations per water use.
```

```{dropdown} Show code

  ```{code-block} sql
  :caption: Heavily modified water bodies - Number of different physical alterations per water use.
  :linenos:
  -- https://discodata.eea.europa.eu/

  SELECT 
  numberOfHMWBPhysicalAlteration,
  numberOfHMWBWaterUse,
  COUNT(DISTINCT [euSurfaceWaterBodyCode]) AS numberOfSurfaceWaterBodies
  FROM 
  (SELECT [euSurfaceWaterBodyCode],
  COUNT(DISTINCT [hmwbPhysicalAlteration]) AS numberOfHMWBPhysicalAlteration,
  COUNT(DISTINCT [hmwbWaterUse]) AS numberOfHMWBWaterUse
  FROM 

  (  SELECT a.[euSurfaceWaterBodyCode]
          ,a.[surfaceWaterBodyCategory]
          ,a.[naturalAWBHMWB]
          ,a.[hmwbPhysicalAlteration]
          ,b.[hmwbWaterUse]
      FROM [WISE_WFD].[v2r1].[SWB_SurfaceWaterBody_hmwbPhysicalAlteration] a
      JOIN  [WISE_WFD].[v2r1].[SWB_SurfaceWaterBody_hmwbWaterUse] b
      ON a.[euSurfaceWaterBodyCode] = b.[euSurfaceWaterBodyCode]
      AND a.[cYear] = b.[cYear]
      WHERE a.[hasDescriptiveData] = 1
      AND a.[cYear] = 2022) AS a

  GROUP BY [euSurfaceWaterBodyCode]) AS b
  
  GROUP BY numberOfHMWBPhysicalAlteration, numberOfHMWBWaterUse
  ORDER BY numberOfHMWBPhysicalAlteration, numberOfHMWBWaterUse

 ```
