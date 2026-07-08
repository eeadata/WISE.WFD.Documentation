(heading_wfd_surface_water_methodologies)=
# Surface water methodologies

```{Warning}
Last updated - 2026-07-06

Changes based on further input from DG ENV and WG DIS.

* {ref}`heading_wfd_surface_water_methodologies_SWTargetedQuestions_4th_cycle`

  - The SWTargetedQuestions table was modified.

* {ref}`heading_wfd_surface_water_methodologies_SWThresholdValue_4th_cycle` 
 
  - The SWThresholdValue table was simplified and aligned with GWThresholdValue.

* {ref}`heading_wfd_surface_water_methodologies_QE3Classification_4th_cycle` 
  
  - The QE3Classification table was modified.

* {ref}`heading_wfd_surface_water_methodologies_QE1Classification_BQEMethod_4th_cycle`

  - The QE1Classification table was simplified.
  - The association table QEClassification_SWType was modified 
    to allow the specification of the intercalibration type.
  - The BiologicalQualityElement enumeration was added to highlight the exclusion of QE1-2 and QE1-5.

* {ref}`heading_wfd_surface_water_methodologies_SWType_4th_cycle`

  - SWType table now includes the specification of the applicable QE elements.

```

(heading_wfd_surface_water_methodologies_purpose_and_overview)=
## Purpose and overview

This section:

* revises the information related to **Surface water methodologies**
  in the 2nd and 3rd cycle of reporting of the
  Water Framework Directive River Basin Management Plans
* presents a simplified proposal for the electronic reporting in the 4th cycle

(heading_wfd_surface_water_methodologies_reporting_of_surface_water_methodologies_3rd_cycle)=
## SWMET_2022 schema - 3rd cycle

The SWMET_2022 schema defined the required data about surface water methodologies.
For review purposes, the schema was divided in two groups:

* a group of six classes requesting generic information
  at river basin district level ({numref}`SurfaceWaterMethodologies_3rdCycle_SWMET_Part1_ClassDiagram`)
* a group of six classes requesting more technical information,
  about national types, thresholds, etc ({numref}`SurfaceWaterMethodologies_3rdCycle_SWMET_Part2_ClassDiagram`)

### Generic information

This section describes the revision of the following classes:
**SWExemptions**,
**SWMethodologies**,
**SWTargetedQ**,
**SWChemicalStatusClassificationRBD**,
**SWManagementObjectives** and
**SWPressures**.

```{mermaid} /DataModelReview/mmd/SurfaceWaterMethodologies_3rdCycle_SWMET_Part1_ClassDiagram.mmd
:name: SurfaceWaterMethodologies_3rdCycle_SWMET_Part1_ClassDiagram
:align: center
:caption: SWMET_2022 schema - generic data - 3rd cycle.
```

The SWMET_2022 schema was already partially revised (see {ref}`heading_wfd_exemptions_reporting_of_exemptions_3rd_cycle`).
Specifically, the **SWExemptions** data ({numref}`Exemptions_3rdCycle_SWMET_ClassDiagram`)
will not be requested in the 4th cycle reporting.

The Commission has revised and simplified the **SWMethodologies** class,
keeping only a subset of the elements requested in the 3rd cycle.
The following elements were removed:

* SWMET/SWMethodologies/typologyMethodologyReference
* SWMET/SWMethodologies/smallWBsMethodologyReference
* SWMET/SWMethodologies/otherMinimumCriteria
* SWMET/SWMethodologies/iRBDTypologyCoOrdinationReference

```{Warning}
The revised **SWTargetedQ** class was altered (2023-06-26).
```

The Commission has revised and simplified the **SWTargetedQ** class,
keeping only a subset of the elements requested in the 3rd cycle.
The following elements were removed:

* SWMET/SWTargetedQ/oneOutAllOut
* SWMET/SWTargetedQ/groupingExtrapolation
* SWMET/SWTargetedQ/gepDefined
* SWMET/SWTargetedQ/gepLevel
* SWMET/SWTargetedQ/gepBiology
* SWMET/SWTargetedQ/driversFailureEcologicalStatusPotentialReference
* SWMET/SWTargetedQ/mitigationMeasures

The following elements will be requested at water category level
(i.e. separately for rivers, lakes, transitional and coastal waters):

* SWMET/SWTargetedQ/gepApproach
* SWMET/SWTargetedQ/bqeForMEPGEP

The Commission has revised and simplified the **SWChemicalStatusClassificationRBD**
class, keeping only a subset of the elements requested in the 3rd cycle.
The following elements were removed:

* SWMET/SWChemicalStatusClassificationRBD/approachSWBNotMonitoredChemicalReference
* SWMET/SWChemicalStatusClassificationRBD/mixingZoneMeasuresReductionReference
* SWMET/SWChemicalStatusClassificationRBD/chemicalStatusReference

The Commission has revised and simplified the **SWManagementObjectives** class,
keeping only a subset of the elements requested in the 3rd cycle.
The following elements were removed:

* SWMET/SWManagementObjectives/managementObjectivesContinuityQuantitative

The Commission has revised **SWPressures** class. The following elements were removed:

* SWMET/SWPressures/swPressuresReference  
* SWMET/SWPressures/swSignificantPressureOtherSourceTools
* SWMET/SWPressures/swPressuresNotAssessed

The structure of the **SWPressures** class was also revised.

### Technical information

The full review of the classes and elements
depicted in {numref}`SurfaceWaterMethodologies_3rdCycle_SWMET_Part2_ClassDiagram`
is pending.

The preliminary technical analysis suggests the changes described below.

In the **SWRBSP** class, the following elements were removed:

* SWMET/SWRBSP/rbspOther
* SWMET/SWRBSP/rbspScale

In the **SWPrioritySubstance** class, the following elements were removed
(because they are not required or can be derived in the revised model):

* SWMET/SWPrioritySubstance/psScale
* SWMET/SWPrioritySubstance/psStatusAssessment
* SWMET/SWPrioritySubstance/psStandardsUsed

The **SWRBSP** and **SWPrioritySubstance** tables have similar structure and content.
A single table, similar to the `GWThresholdValue` table can be used
for both types of substances.

In the **SWPhysicoChemicalQE** class, the following elements were removed:

* SWMET/SWPhysicoChemicalQE/physChemParameterOther

A single threshold value, for the boundary between 'good' and 'moderate' status,
was requested for physico-chemical elements.
This approach was inadequate for several reasons:

* the datatype used in the 3rd cycle did not allow the reporting of intervals,
  specially disjoint intervals (e.g. for parameters like pH)
* the boundary between 'good' and 'high' (or 'maximum') potential
  was not recorded

Starting in 2028, monitoring results for physico-chemical parameters
will be reported biennially to the EEA and the Commission.
Knowledge of the classification boundaries will be necessary
for the status classes applicable to physico-chemical elements,
i.a. to allow a more adequate visualisation of progress over time.
Therefore, the data structure should allow the reporting of the boundaries
for different classes.
The datatype used for the reporting of thresholds and intervals will also be corrected.

In the **BQEMethod** class, the following elements were removed:

* SWMET/BQEMethod/bqePercentageOfTypes
* SWMET/BQEMethod/bqeSensitivityImpactOther
A unique identifier must be introduced, as well as an optional reference
to supporting documentation.
A clear separation between the original name (in the national language)
and a technically meaningful translation to English should also be made.

```{mermaid} /DataModelReview/mmd/SurfaceWaterMethodologies_3rdCycle_SWMET_Part2_ClassDiagram.mmd
:name: SurfaceWaterMethodologies_3rdCycle_SWMET_Part2_ClassDiagram
:align: center
:caption: SWMET_2022 schema - technical data - 3rd cycle.
```

Starting in 2028, monitoring results for biological elements
will be reported every three years to the EEA and the Commission.
In the 3rd cycle, information about class boundaries for biological elements was not reported.
Given the variety and complexity of the biological quality elements,
the range of of values must be normalised to allow some standardisation of the reporting.

In the EIONET WISE-2 Biology dataflow, a **BiologyEQRClassificationProcedure** table
({numref}`SurfaceWaterMethodologies_3rdCycle_WISE2_ClassDiagram`)
tried to capture this information using the concept of Ecological Quality Ratio (EQR).

The current review of the WFD data model, and the recent changes to the WFD reporting requirements,
provide an opportunity to align the WISE-2 and the WFD reporting, avoiding future duplications
and inconsistencies in the reporting of the biological quality elements classification.

```{mermaid} /DataModelReview/mmd/SurfaceWaterMethodologies_3rdCycle_WISE2_ClassDiagram.mmd
:name: SurfaceWaterMethodologies_3rdCycle_WISE2_ClassDiagram
:align: center
:caption: WISE2 Biology - BiologyEQRClassificationProcedure table.
```

```{todo}
SurfaceWaterMethodologies - 3rd cycle - Review

Review of the remaining classes in
{ref}`SurfaceWaterMethodologies_3rdCycle_SWMET_Part2_ClassDiagram`
namely the SWType attributes.
```

(heading_wfd_surface_water_methodologies_reporting_of_surface_water_methodologies_4th_cycle)=
## Descriptive dataset - 4th cycle

The revised structure for the surface water methodologies reporting
is presented in this section.

The `SWMethodologies`, `SWManagementObjectives` and `SWChemicalStatusClassification`
tables have a structure similar to the corresponding classes
in the 3rd cycle reporting, minus the attributes removed by the Commission's review.
See {numref}`SurfaceWaterMethodologies_4thCycle_SWMethodologies_SWManagementObjectives_SWChemicalStatusClassification_ClassDiagram`.

```{mermaid} /DataModelReview/mmd/SurfaceWaterMethodologies_4thCycle_SWMethodologies_SWManagementObjectives_SWChemicalStatusClassification_ClassDiagram.mmd
:name: SurfaceWaterMethodologies_4thCycle_SWMethodologies_SWManagementObjectives_SWChemicalStatusClassification_ClassDiagram
:align: center
:caption: Surface water methodologies - SWMethodologies, SWManagementObjectives, SWChemicalStatusClassification - 4th cycle.
```

(heading_wfd_surface_water_methodologies_SWTargetedQuestions_4th_cycle)=
### SWTargetedQuestions table

In the table `SWTargetedQuestions` ({numref}`SurfaceWaterMethodologies_4thCycle_SWTargetedQuestions_ClassDiagram`)
the questions regarding the approach used for the definition of good ecological potential (GEP)
differentiate between rivers, lakes, transitional and coastal waters.

If, for a given water category,
biological quality elements have been included in the definition of GEP,
then a list of the BQEs included must be provided.
For example, `bqeForMEPGEPRW` must be reported if, and only if,
`gepApproachRW NOT IN ('mitigationMeasuresPragueApproachWithoutBQE','gepHasNotBeenDefined')`.

```{mermaid} /DataModelReview/mmd/SurfaceWaterMethodologies_4thCycle_SWTargetedQuestions_ClassDiagram.mmd
:name: SurfaceWaterMethodologies_4thCycle_SWTargetedQuestions_ClassDiagram
:align: center
:caption: Surface water methodologies - SWTargetedQuestions - 4th cycle.
```

(heading_wfd_surface_water_methodologies_SWPressureAssessment_4th_cycle)=
### SWPressureAssessment table

The table `SWPressureAssessment` ({numref}`SurfaceWaterMethodologies_4thCycle_SWPressureAssessment_ClassDiagram`)
uses a different approach:

* the reporting of "pressures not assessed" is eliminated,
  because the data was difficult to analyse and contained inconsistencies
* instead, for each pressure (or group of pressures),
  three attributes are requested
  (`swPressureAssessmentMethod`,`swSignificanceDefinition`,`swSignificanceLinkFailure`)
* given that the pressure codelist is hierarchical,
  the granularity of the reporting is selected by Member States
* the quality control procedure will verify that different levels
  are not selected simultaneously for any given RBD

For more information see {ref}`heading_wfd_pressure_type_codelist_4th_cycle`.

```{mermaid} /DataModelReview/mmd/SurfaceWaterMethodologies_4thCycle_SWPressureAssessment_ClassDiagram.mmd
:name: SurfaceWaterMethodologies_4thCycle_SWPressureAssessment_ClassDiagram
:align: center
:caption: Surface water methodologies - SWPressureAssessment - 4th cycle.
```

(heading_wfd_surface_water_methodologies_SWThresholdValue_4th_cycle)=
### SWThresholdValue table

The reporting of thresholds for priority substances and for RBSPs
is combined into a single `SWThresholdValue` table
(see {numref}`SurfaceWaterMethodologies_4thCycle_SWThresholdValue_ClassDiagram`).
The `GWThresholdValue` table, in the groundwater methodologies dataset, has a similar structure
(see {ref}`heading_wfd_groundwater_methodologies_gwthresholdvalue_table`).

The associations between the `SWThresholdValue` table and other tables are depicted in
{numref}`SurfaceWaterMethodologies_4thCycle_SWThresholdValue_Associations_ClassDiagram`.

```{mermaid} /DataModelReview/mmd/SurfaceWaterMethodologies_4thCycle_SWThresholdValue_ClassDiagram.mmd
:name: SurfaceWaterMethodologies_4thCycle_SWThresholdValue_ClassDiagram
:align: center
:caption: Surface water methodologies - SWThresholdValue - 4th cycle.
```

```{mermaid} /DataModelReview/mmd/SurfaceWaterMethodologies_4thCycle_SWThresholdValue_Associations_ClassDiagram.mmd
:name: SurfaceWaterMethodologies_4thCycle_SWThresholdValue_Associations_ClassDiagram
:align: center
:caption: Surface water methodologies - SWThresholdValue associations with other tables - 4th cycle.
```

(heading_wfd_surface_water_methodologies_QE3Classification_4th_cycle)=
### QE3Classification table

The reporting of thresholds and class boundaries for physico-chemical quality elements
requires a new `QE3Classification` table
(see {numref}`SurfaceWaterMethodologies_4thCycle_QE3Classification_ClassDiagram`).

Formally, the classes 'poor' and 'bad' status are not defined for physico-chemical quality elements.
The optional attributes `classPoor` and `classBad` allow the reporting of the classification ranges
for those classes.

The associations between the `QE3Classification` table and other tables are depicted in
{numref}`SurfaceWaterMethodologies_4thCycle_QE3Classification_Associations_ClassDiagram`.

```{mermaid} /DataModelReview/mmd/SurfaceWaterMethodologies_4thCycle_QE3Classification_ClassDiagram.mmd
:name: SurfaceWaterMethodologies_4thCycle_QE3Classification_ClassDiagram
:align: center
:caption: Surface water methodologies - QE3Classification - 4th cycle.
```

```{mermaid} /DataModelReview/mmd/SurfaceWaterMethodologies_4thCycle_QE3Classification_Associations_ClassDiagram.mmd
:name: SurfaceWaterMethodologies_4thCycle_QE3Classification_Associations_ClassDiagram
:align: center
:caption: Surface water methodologies - QE3Classification associations with other tables - 4th cycle.
```

(heading_wfd_surface_water_methodologies_QE1Classification_BQEMethod_4th_cycle)=
### QE1Classification and BQEMethod table

The reporting of class boundaries for biological quality elements
requires a new `QE1Classification` table
(see {numref}`SurfaceWaterMethodologies_4thCycle_BQEMethod_QE1Classification_ClassDiagram`).
The table "replaces" the WISE2 Biology - BiologyEQRClassificationProcedure table.
All boundaries are reported using EQRs.

The associations between the `QE1Classification` table and other tables are depicted in
{numref}`SurfaceWaterMethodologies_4thCycle_BQEMethod_QE1Classification_Associations_ClassDiagram`.

```{mermaid} /DataModelReview/mmd/SurfaceWaterMethodologies_4thCycle_BQEMethod_QE1Classification_ClassDiagram.mmd
:name: SurfaceWaterMethodologies_4thCycle_BQEMethod_QE1Classification_ClassDiagram
:align: center
:caption: Surface water methodologies - BQEMethod and QE1Classification - 4th cycle.
```

```{mermaid} /DataModelReview/mmd/SurfaceWaterMethodologies_4thCycle_BQEMethod_QE1Classification_Associations_ClassDiagram.mmd
:name: SurfaceWaterMethodologies_4thCycle_BQEMethod_QE1Classification_Associations_ClassDiagram
:align: center
:caption: Surface water methodologies - BQEMethod and QE1Classification associations - 4th cycle.
```

(heading_wfd_surface_water_methodologies_SWType_4th_cycle)=
### SWType table

The `SWType` table contains information about
the national surface water types
defined in accordance to Annex II of the WFD.
This table is central to the surface water methodologies
(see {numref}`SurfaceWaterMethodologies_4thCycle_SWType_ClassDiagram`).

For each national surface water type, the quality elements
which used in the ecological status assessment
are declared in the `SWType` table.
Only the applicable quality elements
are reported in the `SWQualityElement` table.
The purpose is to minimise reporting burden
and to avoid the ambiguities observed in the 3rd cycle reporting
(see {ref}`heading_wfd_surface_water_bodies_annexes`).

```{mermaid} /DataModelReview/mmd/SurfaceWaterMethodologies_4thCycle_SWType_ClassDiagram.mmd
:name: SurfaceWaterMethodologies_4thCycle_SWType_ClassDiagram
:align: center
:caption: Surface water methodologies - SWType - 4th cycle.
```

Depending on the water body category,
some quality elements may be reported as `notUsed`:

* For rivers:

  - QE1-1 - Phytoplankton
  - QE1-2-1 - Macroalgae
  - QE1-2-2 - Angiosperms
  - QE3-1-1 - Transparency conditions

* For lakes:

  - QE1-2-1 - Macroalgae
  - QE1-2-2 - Angiosperms
  - QE2-2 - River continuity conditions
  
* For transitional waters:

  - QE1-2-3 - Macrophytes
  - QE1-2-4 - Phytobenthos
  - QE2-2 - River continuity conditions
  - QE3-1-5 - Acidification status
  
* For coastal waters:

  - QE1-4 - Fish
  - QE1-2-3 - Macrophytes
  - QE1-2-4 - Phytobenthos
  - QE2-2 - River continuity conditions
  - QE3-1-5 - Acidification status

In exceptional cases,
some biological quality elements may be reported as 'inapplicable'
(see e.g. Part 3 of Annex 1 {footcite}`intercalibration_2024`).

The data reported in the `SWType` table
controls the data that must be reported
in the `SWQualityElement` table:

* select 'all', if the quality element status *must* be assessed
  for all water bodies belonging to a given national surface water body type
* select 'some', if the hydromorphological quality element status,
  or the physico-chemical quality element status, *may* be assessed
  for the water bodies belonging to a given national surface water body type
* select 'inapplicable', if the quality element status is never assessed
  for the water bodies belonging to a given national surface water body type
  (see e.g. Part 3 of Annex 1 {footcite}`intercalibration_2024`)
* select 'notUsed', for the cases
  where the WFD does not foresee the use of a given quality element
  for a given water category (e.g. phytoplankton in rivers)
  and therefore the quality element was not used in the assessment

For example:

* If `surfaceWaterBodyCategory = 'CW'`, it is expected that `QE2_2 = 'notUsed'`.
  Therefore, in the `SWQualityElement` table,
  the value `qeCode = 'QE2-2'` will never occur for coastal water bodies.
* If `surfaceWaterBodyCategory = 'CW'`, it is expected that `QE1_4 = 'notUsed'`.
  Therefore, in the `SWQualityElement` table,
  the value `qeCode = 'QE1-4'` will never occur for coastal water bodies.

Another example:

* If `[surfaceWaterBodyCategory] = 'RW'`, it is possible to set `[QE1_1] = 'notUsed'`.
  In that case, in the `SWQualityElement` table,
  the value `[qeCode] = 'QE1-1'` will never occur for rivers belonging to that national type.

* If `[surfaceWaterBodyCategory] = 'RW'`, it is possible to set `[QE1_1] = 'some'`.
  In that case, in the `SWQualityElement` table,
  the value `[qeCode] = 'QE1-1'` **may** be reported for rivers belonging to that national type.

* If `[surfaceWaterBodyCategory] = 'RW'`, it is possible to set `[QE1_1] = 'all'`.
  In that case, in the `SWQualityElement` table,
  the value `[qeCode] = 'QE1-1'` **must** be reported for rivers belonging to that national type.

```{note}
The attribute names use the underscore character (`_`) 
instead of the hyphen character (`-`) for technical reasons.
```

(heading_wfd_surface_water_methodologies_codelists_4th_cycle)=
## Codelists - 4th cycle

* For the `GEPApproach` codelist,
  see {numref}`Codelist_4thCycle_GEPApproach_Table`.

* For the `MixingZoneMeasure` codelist,
  see {numref}`Codelist_4thCycle_MixingZoneMeasure_Table`.

* For the `PressureAssessmentMethod` codelist,
  see {numref}`Codelist_4thCycle_PressureAssessmentMethod_Table`.

```{dropdown} GEPApproach codelist
```{include} tables/Codelist_4thCycle_GEPApproach_Table
```

```{dropdown} MixingZoneMeasure codelist
```{include} tables/Codelist_4thCycle_MixingZoneMeasure_Table
```

```{dropdown} PressureAssessmentMethod codelist
```{include} tables/Codelist_4thCycle_PressureAssessmentMethod_Table
```

(heading_wfd_surface_water_methodologies_documents_dataset_4th_cycle)=
## Documents dataset - 4th cycle

The Documents dataset follows the standard structure used in various WISE dataflows
({numref}`SurfaceWaterMethodologies_4thCycle_Documents`):

* the `dcMetadata` table provides the basic Dublin Core metadata elements about the delivery
  
  - if required by the data providers, and especially if spatial data is being reported,
    the `licenseDocument` and the `metadataDocument` attributes
    allow the provision of additional information about the dataset
  - the `dcMetadata` table also functions as a "manifest file"
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
:caption: SurfaceWaterMethodologies - 4th cycle - Documents
:align: center
:zoom:
```

```{todo}
Surface water methodologies - {ref}`heading_wfd_surface_water_methodologies_documents_dataset_4th_cycle`

**Technical** review pending.
```

(heading_wfd_wfd_surface_water_methodologies_references)=
## References
