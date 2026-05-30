(heading_wfd_groundwater_bodies)=
# WFD groundwater bodies

Last update: 2026-05-30

```{danger}
INTERNAL VERSION - PENDING DISCUSSION - DO NOT USE
```

## Purpose and overview

This section revises the reporting of information related to **Groundwater Bodies** 
in the 2ⁿᵈ and 3ʳᵈ cycle of reporting of the Water Framework Directive River Basin Management Plans. 
It also presents a proposal for simplifying the electronic reporting in the 4ᵗʰ cycle.

## Current structure - 3ʳᵈ cycle

The information about Groundwater bodies was reported in 4 separate schemas:

* The GWB_2022 schema, containing information about each groundwater body ({numref}`Groundwater_3rdCycle_GWB_ClassDiagram`)
* The GWMET_2022 schema, containing information about the methodologies.
* The GML_GroundWaterBody_2022 schema, containing the GroundWaterBody spatial dataset.
* The GML_GroundWaterBodyHorizon_2022 schema, containing the ancillary GroundWaterBodyHorizon spatial dataset.

## GWB_2022 schema - 3ʳᵈ cycle

The GWB_2022 schema was already partially revised with regard to the reporting of exemptions.  
See:

* {ref}`heading_wfd_exemptions_groundwater_bodies_chemical_exemptions_by_pollutant`
* {ref}`heading_wfd_exemptions_groundwater_bodies_quantitative_exemptions`
* {ref}`heading_wfd_exemptions_groundwater_bodies_protected_area_exemptions`

Other simplifications already discussed also apply to the GWB schema:

* Removal of the textual reporting of "other" pollutants
* Removal of the textual reporting of "other" pressures
* Removal of the textual reporting of "other" impacts

Based on the Commission's review of the 3ʳᵈ cycle reporting, the following elements were removed:

* GWB/GroundWaterBody/gwEORiskQuantitative 
* GWB/GroundWaterBody/gwEORiskChemical 
* GWB/GroundWaterBody/gwAtRiskQuantitative
* GWB/GroundWaterBody/gwAtRiskChemical
* GWB/GroundWaterBody/gwReasonsForRiskQuantitative
* GWB/GroundWaterBody/GWPollutant/gwPollutantExceedancesNotCounted

```{mermaid} /DataModelReview/mmd/Groundwater_3rdCycle_GWB_ClassDiagram.mmd
:name: Groundwater_3rdCycle_GWB_ClassDiagram
:caption: Class diagram for the GWB_2022 schema in the 3ʳᵈ cycle.
:align: center
```

The remaining attributes were reorganised to try and facilitate the reporting, 
and the structure was aligned also with the approach proposed for surface water bodies.

## Groundwater - descriptive data - 4ᵗʰ cycle

{numref}`Groundwater_DescriptiveData_4thCycle_ClassDiagram` 
shows proposed structure for the 4ᵗʰ cycle electronic reporting. 
The data was reorganised organised into a relational structure 
with seven tables (see {numref}`Groundwater_4th_cycle_brief_table_description`).

```{mermaid} /DataModelReview/mmd/Groundwater_DescriptiveData_4thCycle_ClassDiagram.mmd
:name: Groundwater_DescriptiveData_4thCycle_ClassDiagram
:caption: Groundwater - descriptice data - 4ᵗʰ cycle
:align: center
```

```{list-table} Groundwater - 4ᵗʰ cycle - brief table description
:name: Groundwater_4th_cycle_brief_table_description
:header-rows: 1
:width: 100%
:widths: 20 80
:align: left

* - Table
  - Description

* - GroundWaterBody
  - *Modified*.  
    The `GroundWaterBody` table now contains only the attributes 
    that describe the groundwater body 
    and that do not vary with the status of the waterbody.
    Therefore the table can be prepared immediately, 
    even if the 4ᵗʰ cycle RBMPs have not yet been finalised. 
    All the attributes existed in the 3ʳᵈ cycle reporting.  

    The former geologicalFormation attribute was split 
    in two attributes: `aquiferType` and `aquiferProductivity`. 
    This separation already existed 
    in the published WISE_WFD database 
    and in the WISE visualisations. 
    It now allows greater flexibility 
    in the description of the groundwater bodies,
    with no additional reporting burden. 

    The `linkSurfaceWaterBody` value 
    controls the content of the `LinkSurfaceWaterBody` table.

* - LinkSurfaceWaterBody
  - *Modified*.  
    If the groundwater body is linked to one or more surface water bodies,
    that relation is reported in the `LinkSurfaceWaterBody` table.  
    The `linkType` attribute specifies the type of water flow 
    between the groundwater and the surdace water body. 

* - GroundWaterBodyStatus
  - *New*
    The `GroundWaterBodyStatus` table synthesizes 
    information about the status of the water body,
    and the causes of failure (if applicable).  
    Formally, the `chemicalStatusValue` 
    could be derived from the information in the `GWPollutant` table. 
    Likewise, the `quantitativeStatusValue` 
    could be derived from the `GWQuantitativeStatus` table.
    Nevertheless, a decision was taken to keep both attributes 
    in the `GroundWaterBodyStatus` table, 
    for *quality control purposes* 
    (e.g. to guarantee that there was no mistake 
    in the reporting of substances causing failure).  


* - GWPollutant
  - *Modified*
    The `GWPollutant` table gathers the data related to chemical status.  
    The information about the assessment method, assessment confidence, 
    and assessment period cn now be reported at pollutant level, 
    allowing more flexibility in reporting different situations 
    for different pollutants or indicators of pollution. 
    It is now possible to report the use of grouping 
    for the chemical status assessment in groundwater. 
    
* - GWQuantitativeStatus
  - *New*  
    The `GWQuantitativeStatus` table gathers 
    the data related to quantitative status.  
    Note the possibility to report 
    the assessment method and assessment confidence 
    using the same pattern applied for groundwater pollutants.
    It is now possible to report the use of grouping 
    for the quantitative status assessment.

* - GWGrouping
  - *New*.  
    If grouping was not used, this table is not reported.

    If grouping was used for the 
    assessment of quantitative or chemical status,
    the GWGrouping defines sets of waterbodies 
    that were monitored as a group.
    The same grouping can be used for different purposes. 
    The same water body can be a member of different groups.
    
    The `groupIdentifier` value uniquely identifies the group 
    using the WISE identifier syntax.
    The `euGroundWaterBodyCode` identifies a member of the group.

    If a group is used 
    in the assessment of a given element, 
    then at least one waterbody of the group 
    must be monitored for that element.
  
    (To avoid mistakes and ambiguities, 
    the `groupIdentifier` value must be different 
    from any known water body identifier. 
    It is recomended to use a clear pattern 
    to avoid conflicts with existing 
    and future water body identifiers.
    For example, using a '_GWGROUP' suffix).       

* - GWPressureImpact
  - *Modified*.  
    For water bodies that do not achieve good quantitative status in 2027, 
    the significant pressures causing poor quantitative status 
    are reported in the GWQuantitativeExemption table 
    ({numref}`Exemptions_4thCycle_GWQuantitativeExemption_ClassDiagram`) 
    and do not need to be reported again in the GWPressureImpact table.

    For water bodies that do not achieve good chemical status in 2027, 
    the significant pressures are reported in the GWChemicalExemption table 
    ({numref}`Exemptions_4thCycle_GWChemicalExemption_ClassDiagram`) 
    and do not need to be reported again in the GWPressureImpact table.
    
    For cases where a pressure is not causing failure, 
    but still causes an impact that needs to be managed, 
    the `GWPressureImpact` table should be used.

    Note that the reporting of pressures and impacts 
    is combined into a single `GWPressureImpact` table.  
    In the 3ʳᵈ cycle, the XML structure did not allow 
    a specific pressure to be link to a given impact.
    In the proposed structure, this is possible (but not mandatory).       
    Illustrative examples will be provided.  
    
```

## Groundwater - codelists - 4ᵗʰ cycle

### AquiferMediaTypeValue and AquiferProductivity

The `AquiferMediaTypeValue` codelist was realigned with the INSPIRE codelist to allow more flexibility 
({numref}`AquiferMediaTypeValue_Codelist_4thCycle_Table`).

The `AquiferProductivity` codelist allows the reporting of aquifer productivity 
independently of the aquifer media values 
({numref}`AquiferProductivity_Codelist_4thCycle_Table`).

```{mermaid} /DataModelReview/mmd/Groundwater_AquiferMediaTypeValue_AquiferProductivity_Codelist_4thCycle_ClassDiagram.mmd
:name: Groundwater_AquiferMediaTypeValue_AquiferProductivity_Codelist_4thCycle_ClassDiagram
:align: center
:caption: AquiferMediaTypeValue codelist and AquiferProductivity codelist - 4ᵗʰ cycle
```

```{include} /DataModelReview/tables/AquiferMediaTypeValue_Codelist_4thCycle_Table
```

```{include} /DataModelReview/tables/AquiferProductivity_Codelist_4thCycle_Table
```

### AssessmentMethod and AssessmentConfidence

The `AssessmentMethod` codelist is used to report 
the assessment method for the chemical status and for the quantitative status 
({numref}`AssessmentMethod_Codelist_4thCycle_Table`).

The `AssessmentConfidence` codelist is used to report 
the level of confidence in the results of the assessment of the status 
({numref}`AssessmentConfidence_Codelist_4thCycle_Table`).

The same codelists are also used for surface water bodies, 
in the scope of the assessment of ecological status or potential, and chemical status.

[^IPCC_Authors]: Mastrandrea, MD, Field CB, Stocker TF, Edenhofer O, Ebi KL, Frame DJ, Held H, Kriegler E, Mach KJ, Matschoss PR, Plattner GK (2010) Guidance note for lead authors of the IPCC fifth assessment report on consistent treatment of uncertainties. https://www.ipcc.ch/site/assets/uploads/2017/08/AR5_Uncertainty_Guidance_Note.pdf

[^IPCC_WorkingGroups]: Mastrandrea, M.D., Mach, K.J., Plattner, GK. et al. (2011) The IPCC AR5 guidance note on consistent treatment of uncertainties: a common approach across the working groups. Climatic Change 108, 675 . https://doi.org/10.1007/s10584-011-0178-6

[^IPCC_Readers]: Kause, A., Bruine de Bruin, W., Persson, J. et al. (2022) Confidence levels and likelihood terms in IPCC reports: a survey of experts from different scientific disciplines. Climatic Change 173, 2 . https://doi.org/10.1007/s10584-022-03382-3

See also [^IPCC_Authors] [^IPCC_WorkingGroups] [^IPCC_Readers].

```{mermaid} /DataModelReview/mmd/AssessmentMethod_AssessmentConfidence_Codelist_4thCycle_ClassDiagram.mmd
:name: AssessmentMethod_AssessmentConfidence_Codelist_4thCycle_ClassDiagram
:align: center
:caption: AssessmentMethod codelist and AssessmentConfidence codelist - 4ᵗʰ cycle
```

```{include} /DataModelReview/tables/AssessmentMethod_Codelist_4thCycle_Table
```

```{include} /DataModelReview/tables/AssessmentConfidence_Codelist_4thCycle_Table
```

### GroundwaterSurfaceWaterLink

The `GroundwaterSurfaceWaterLink` codelist is used to qualify  
the type of link between a given groundwater body and a given surface water body 
({numref}`GroundwaterSurfaceWaterLink_Codelist_4thCycle_Table`).

```{mermaid} /DataModelReview/mmd/Groundwater_GroundwaterSurfaceWaterLink_Codelist_4thCycle_ClassDiagram.mmd
:name: Groundwater_GroundwaterSurfaceWaterLink_Codelist_4thCycle_ClassDiagram
:align: center
:caption: GroundwaterSurfaceWaterLink codelist - 4ᵗʰ cycle
```

```{include} /DataModelReview/tables/GroundwaterSurfaceWaterLink_Codelist_4thCycle_Table
```

### ReasonForFailure

For groundwater bodies in poor quantitative status, 
the `GroundwaterSurfaceWaterLink` codelist values are used 
in the `gwQuantitativeReasonsForFailure` attribute 
to provide further about one or more causes of failure 
(the most frequent cause will be likely be `'waterBalance'`).  
For groundwater bodies in good or unknown quantitative status, 
the option `notApplicable` must be used.

For groundwater bodies failing to achieve good chemical status, 
in the `gwChemicalReasonsForFailure` attribute 
to provide further about one or more causes of failure 
(the most frequent cause will be likely be `'waterQaulity'`).  
For groundwater bodies in good or unknown chemical status, 
the option `notApplicable` must be used.

```{mermaid} /DataModelReview/mmd/Groundwater_ReasonForFailure_Codelist_4thCycle_ClassDiagram.mmd
:name: Groundwater_ReasonForFailure_Codelist_4thCycle_ClassDiagram
:align: center
:caption: ReasonForFailure codelist - 4ᵗʰ cycle
```

```{include} /DataModelReview/tables/ReasonForFailure_Codelist_4thCycle_Table
```

```{todo}
Groundwater - Topics that require discussion and clarification.

* gwPollutantAssessmentMethod and gwPollutantAssessmentGrouping
* gwQuantitativeAssessmentMethod and gwQuantitativeAssessmentGrouping
* Final revision of the **PressureType** codelist.
* Revision of the **ImpactType** codelist.
* Mapping tables to 3rd cycle codelists
```

## Annexes - Data analysis - 3ʳᵈ cycle

```{include} /DataModelReview/FragmentAnnexesDataAnalysis3rdCycle
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

