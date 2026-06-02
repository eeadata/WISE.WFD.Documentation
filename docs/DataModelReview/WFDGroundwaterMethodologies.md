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
* presents a simplified proposal for the electronic reporting in the 4ᵗʰ cycle

(heading_wfd_groundwater_methodologies_reporting_of_groundwater_methodologies_GWMET_schema_3rd_cycle)=
## GWMET_2022 schema - 3ʳᵈ cycle

The GWMET_2022 schema defined the required data about  about the groundwater methodologies ({numref}`ClassDiagram_GWMET_2022`).

```{figure} img/ClassDiagram_GWMET_2022.png
:name: ClassDiagram_GWMET_2022
:align: center
:width: 75%

GWMET_2022 Schema - 3ʳᵈ cycle - Obsolete
```

The GWMET_2022 schema was already partially revised (see {ref}`heading_wfd_exemptions_reporting_of_exemptions_3rd_cycle`). 
Specifically, the GWExemptions data ({numref}`Exemptions_3rdCycle_GWMET_ClassDiagram`) is no longer requested in the 4ᵗʰ cycle.

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
* GWMET/GWMethodologies/trendAssessmentMethodology

The following elements were moved or revised:

* GWMET/GWMethodologies/trendAssessmentStatisticalElements
* GWMET/GWMethodologies/thresholdValueBackgroundLevels 

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

(heading_wfd_groundwater_methodologies_descriptive_4th_cycle)=
## Descriptive dataset - 4ᵗʰ cycle

{numref}`GroundwaterMethodologies_4thCycle_ClassDiagram` shows proposed struture for the groundwater methodologies reporting.

The `GWMethodologies` table has a structure similar to the corresponding class 
in the 3ʳᵈ cycle reporting (minus the attributes removed by the Commission's review).

The `GWPressureAssessment` table has a modified structure:

* the reporting of "pressures not assessed" is eliminated,
  because the data was difficult to analyse and contained inconsistencies
* instead, for each pressure (or group of pressures),
  three attributes are requested 
  (`gwPressureAssessmentMethod`,`gwSignificanceDefinition`,`gwSignificanceLinkFailure`)
* given that the pressure codelist is hierarchical, 
  the granularity of the reporting is selected by Member States
* the quality control procedure will verify that different levels 
  are not selected simultaneously for any given RBD

The `ThresholdValue` table has a structure similar to the corresponding class 
in the 3ʳᵈ cycle reporting (minus the attributes removed by the Commission's review).
Note that:

* a unique `gwThresholdIdentifier` was introduced to avoid duplication 
* for naturally occurring substances, if natural background levels 
  were taken into account in the definition of the threshold value,
  then the applicable `nblValueRange` is provided 
  (in the same unit of measure as the `thresholdValueRange`) 

```{mermaid} /DataModelReview/mmd/GroundwaterMethodologies_4thCycle_ClassDiagram.mmd
:name: GroundwaterMethodologies_4thCycle_ClassDiagram
:align: center
:caption: Groundwater methodologies - 4ᵗʰ cycle
```

(heading_wfd_groundater_methodologies_codelists_4th_cycle)=
## Codelists - 4ᵗʰ cycle

* For the `PressureAssessmentMethod` codelist, 
  see {numref}`PressureAssessmentMethod_Codelist_4thCycle_Table`.
* For the `TrendStatisticalMethod` codelist, 
  see {numref}`TrendStatisticalMethod_Codelist_4thCycle_Table`.

```{dropdown} TrendStatisticalMethod codelist
```{include} tables/TrendStatisticalMethod_Codelist_4thCycle_Table
```

(heading_wfd_groundater_methodologies_documents_dataset_4th_cycle)=
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

## Annexes - Data analysis - 3ʳᵈ cycle

### trendAssessmentMethodology

The WFD2022 guidance document definitions for the 
trendAssessmentPerformed, trendAssessmentMethodology and statisticalElements elements 
of the GWMethodologies class are transcribed in 
{numref}`trendAssessmentMethodology_definition_3rdCycle`.

```{list-table} Definitions for trendAssessmentPerformed, trendAssessmentMethodology and statisticalElements – 3ʳᵈ cycle.
:name: trendAssessmentMethodology_definition_3rdCycle
:width: 100%
:widths: 35 40 25
:header-rows: 1
:align: left

* - Element
  - Guidance
  - Option
* - trendAssessmentPerformed
  - Required.  
    Indicate whether trend assessment in groundwater pollutants was performed. 
  - 'Yes'  
    'No'
* - trendAssessmentMethodology
  - Conditional.  
    If trend assessment in groundwater pollutants was performed, 
    indicate whether a methodology for identifying 
    significant and upward trends in any pollutant’s concentration has been applied.
  - 'Yes'  
    'No'
* - statisticalElements
  - Conditional.  
    If trend assessment in groundwater pollutants was performed, 
    select from the enumeration list which statistical element was used.
  - 'Statistical significance'  
    'Confidence intervals'  
    'None' 
```

The reported data for combinations of the three elements is presentes in 
{numref}`trendAssessmentMethodology_reported_data_3rdCycle`.

The first four records may be interpreted as:
* in 95 river basin districts, trends were assessed 
  and a test for statistical significance of an upward trend was used  
  (e.g. using a linear regression t-test or a non-parametric Mann-Kendall test) 
* in 36 river basin districts, trends were not assessed 
* in 16 river basin districts, trends were assessed
  and the magnitude of significant upward trends 
  was quantified using confidence intervals
* in 2 river basin districts, trends were assessed
  but no methodology for detecting *significant* upward trends exists, 
  and no statistical element was used (i.e. only expert judgement was used?)

The last two records are difficult to interpret, and possibly result from reporting mistakes:
* in 6 river basin districts trends were assessed,
  a methodology for detecting *significant* upward trends was applied,
  but somehow no statistical element was used
* in 1 river basin districts trends were assessed,
  a methodology for detecting *significant* upward trends was not applied,
  but somehow statistical significance was determined

In conclusion:
* the trendAssessmentMethodology element appears to be redundant 
  with respect to the statisticalElements element,
  and may be removed to simplify the reporting and avoid mistakes
* the meaning of the statisticalElements element should be made clearer 
  to both data provider and end-users, to facilitate the interpretation

```{csv-table} Reported data for trendAssessmentPerformed, trendAssessmentMethodology and statisticalElements – 3ʳᵈ cycle.
:name: trendAssessmentMethodology_reported_data_3rdCycle
:header-rows: 1
:delim: "|"
trendAssessmentPerformed|trendAssessmentMethodology|statisticalElements|numberOfRBDs|numberOfCountries
Yes|Yes|Statistical significance|95|20
No|«null»|«null»|36|5
Yes|Yes|Confidence intervals|16|6
Yes|No|None|2|1
Yes|Yes|None|6|2
Yes|No|Statistical significance|1|1
```

(heading_wfd_groundwater_methodologies_references)=
## References

```{include} FragmentReportingGuidanceFiles
```