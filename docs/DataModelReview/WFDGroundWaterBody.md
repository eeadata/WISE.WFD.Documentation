(heading_wfd_groundwater_bodies)=
# Groundwater bodies

```{warning}
Last updated - 2026-07-02

Changes based on feedback from WG DIS and WG Groundwater members.

* The "lithology placeholder" was removed. 
* The gwAtRiskQuantitative and gwReasonsForRiskQuantitative attributes were reintroduced.
* The gwPollutantCausingRisk and gwPollutantBackgroundLevelSet attributes were reintroduced.
* Further information about the 3rd cycle reporting of natural background levels was included
  {ref}`GroundWaterBody_3rdCycle_NaturalBackgroundLevel_Table`.

```

## Purpose and overview

This section revises the reporting of information related to
**Groundwater Bodies** in the 2nd and 3rd cycle of reporting
of the Water Framework Directive River Basin Management Plans.
It also presents a proposal for simplifying
the electronic reporting in the 4th cycle.

(heading_wfd_groundwater_3rd_cycle)=
## Current structure - 3rd cycle

In the 3rd cycle, the information about Groundwater bodies was reported in 4 separate schemas:

* the GWB_2022 schema, containing information about each groundwater body
  ({numref}`Groundwater_3rdCycle_GWB_ClassDiagram`)
* the GWMET_2022 schema, containing information about the methodologies
  (see {ref}`heading_wfd_groundwater_methodologies`)
* the GML_GroundWaterBody_2022 schema,
  containing the GroundWaterBody spatial dataset.
* the GML_GroundWaterBodyHorizon_2022 schema,
  containing the ancillary GroundWaterBodyHorizon spatial dataset.

(heading_wfd_groundwater_gwb_3rd_cycle)=
## GWB_2022 schema - 3rd cycle

The GWB_2022 schema was already partially revised with regard to the reporting of exemptions. See:

* {ref}`heading_wfd_exemptions_groundwater_bodies_chemical_exemptions_by_pollutant`
* {ref}`heading_wfd_exemptions_groundwater_bodies_quantitative_exemptions`
* {ref}`heading_wfd_exemptions_groundwater_bodies_protected_area_exemptions`

Other simplifications already discussed also apply to the GWB schema:

* removal of the textual reporting of "other" pollutants
* removal of the textual reporting of "other" pressures
* removal of the textual reporting of "other" impacts

The Commission has revised the **GroundWaterBody** class,
and removed the following elements:

* GWB/GroundWaterBody/gwEORiskQuantitative
* GWB/GroundWaterBody/gwEORiskChemical
* GWB/GroundWaterBody/gwAtRiskQuantitative
* GWB/GroundWaterBody/gwAtRiskChemical
* GWB/GroundWaterBody/gwReasonsForRiskQuantitative

The Commission has revised the **GWPollutant** class,
and removed the following elements:

* GWB/GroundWaterBody/GWPollutant/gwPollutantExceedancesNotCounted

```{mermaid} /DataModelReview/mmd/Groundwater_3rdCycle_GWB_ClassDiagram.mmd
:name: Groundwater_3rdCycle_GWB_ClassDiagram
:caption: Class diagram for the GWB_2022 schema in the 3rd cycle.
:align: center
```

In the 4th cycle of reporting, the data will be delivered in the Reportnet3 platform:

* the remaining GWMET_2022 classes and elements were reorganised
  into a relational model, as required by the migration to Reportnet3
* selective denormalisation was used to keep a low number of tables
  and facilitate the quality control
* the requirements of Directive 2006/118/EC also need to be taken into account

```{epigraph}
(36) In order to ensure a level playing field in the Union and allow comparability
of water body status between Member States, there is a need to harmonise national
threshold values for some man-made synthetic groundwater pollutants. Threshold
values should be established as necessary at Union level for pollutants which
have an anthropogenic origin or for the products of their degradation or
decomposition, provided that those pollutants and degradation products either do
not occur naturally in groundwater, or, if identical natural counterparts exist,
provided that their natural background levels are, at most, low. Those threshold
values should be included in the repository of harmonised threshold values for
man-made synthetic substances in groundwater of national, regional or local
concern in a new Part D of Annex II to Directive 2006/118/EC. A harmonised
threshold value for individual pharmaceuticals should be included for application
by Member States to any pharmaceutical active substance identified as posing a
risk at national level unless a stricter standard or threshold value has been
set specifically for that substance at Union or national level.

(37) All provisions of Directive 2006/118/EC relating to the assessment of
groundwater chemical status should be adapted to the introduction of the third
category of harmonised threshold values in a new Part D of Annex II to that
Directive, in addition to the quality standards set out in Annex I to that
Directive and the national threshold values set out in accordance with the
methodology set out in Part A of Annex II to that Directive.

-- ELI: http://data.europa.eu/eli/dir/2026/805/oj
```

(heading_wfd_groundwater_descriptive_4th_cycle)=
## Groundwater - descriptive data - 4th cycle

The proposed structure for the 4th cycle electronic reporting
is presented in the class diagram in {numref}`Groundwater_4thCycle_DescriptiveData_ClassDiagram`
and a brief description of each table is included in {numref}`Groundwater_4th_cycle_brief_table_description`.

* The core data about each groundwater body
  is reported in 3 tables: `GroundWaterBody`, `LinkSurfaceWaterBody` and `GWNaturalBackgroundLevel`.

  - The content of this set of tables does not depend
    of the status assessment, and can be prepared in advance.

* A second set of tables contains information about
  the chemical and quantitative status assessment
  and about pressures and impacts: `GroundWaterBodyStatus`, `GWQuantitativeStatus`, `GWPollutant` and `GWPressureImpact`.

  - The ancillary table `GWGrouping`
    supports the reporting of grouping (if used the assessment).
  - A link to the `GWMethodologies::ThresholdValue` table clarifies 
    which threshold value is applied to each pollutant.  
    (A list of the default EU threshold values will be provided
    where defined by the EU legislation.)

```{mermaid} /DataModelReview/mmd/Groundwater_4thCycle_DescriptiveData_ClassDiagram.mmd
:name: Groundwater_4thCycle_DescriptiveData_ClassDiagram
:caption: Groundwater - descriptive data - 4th cycle
:align: center
```

```{list-table} Groundwater - 4th cycle - brief table description
:name: Groundwater_4th_cycle_brief_table_description
:header-rows: 1
:width: 100%
:widths: 20 80
:align: left

* - Table
  - Description

* - GroundWaterBody
  - *modified*  
    The `GroundWaterBody` table contains the attributes 
    that describe the groundwater body 
    and that do not vary with the status of the water body.
    Therefore the table can be prepared immediately, 
    even if the 4th cycle RBMPs have not yet been finalised. 
    All the attributes existed in the 3rd cycle reporting. 

    The `linkSurfaceWaterBody` value 
    controls the content of the `LinkSurfaceWaterBody` table.

    In the 3rd cycle, the reporting guidance requested description of 
    "*the main geological formation of the aquifer type*".
    The usability of the reported data was limited, 
    beyond visualisation purposes.  
    For the 4th cycle, a suggestion is made to split 
    the data in two attributes: `aquiferMediaType` and `aquiferProductivity`, 
    using the separation already present 
    in the published WISE_WFD database and in the WISE visualisations.      
    However, expert guidance must be provided, 
    specially with regard to the aquifer productivity classes,
    their definition and comparability across Member States.

* - GWLinkSurfaceWaterBody
  - *modified*.  
    If the groundwater body is linked to one or more surface water bodies,
    that relation is reported in the `GWLinkSurfaceWaterBody` table.  
    The `linkType` attribute specifies the type of water flow 
    between the groundwater and the surface water body. 

* - GWNaturalBackgroundLevel
  - *modified*  
    The data related to the natural background level (NBL) 
    of substances in groundwater is moved from the GWPollutant class 
    into a separate `GWNaturalBackgroundLevel` table.  
    This facilitates both the reporting 
    and the quality control procedures that will be introduced to avoid mistakes in the reporting
    (see {ref}`heading_wfd_groundwater_annexes_nbl_3rd_cycle`).     

* - GWStatus
  - *new*  
    The `GWStatus` table synthesizes 
    information about the status of the water body,
    and the causes of failure (if applicable).
    
    Formally, the `chemicalStatusValue` 
    could be derived from the information in the `GWPollutant` table.  
    If, and only if, `chemicalStatusValue = 'unknown'` 
    and no assessment of the chemical status was done,
    may all corresponding rows in the `GWPollutant` table be missing.
    (An ERROR will raised by the quality control, since this is a non-compliance 
    and should not be reported by mistake.)

    Likewise, the `quantitativeStatusValue` 
    could be derived from the `GWQuantitativeStatus` table.  
    If, and only if, `quantitativeStatusValue = 'unknown'` 
    and no assessment of the quantitative status was done,
    may the corresponding row in the `GWQuantitativeStatus` table be missing.
    (An ERROR will raised by the quality control, since this is a non-compliance 
    and should not be reported by mistake.) 

* - GWPollutant
  - *modified*  
    The `GWPollutant` table contains data related to the chemical status at substance level.  
    The information about the assessment method, assessment confidence, 
    and assessment period can be reported at pollutant level, 
    allowing more flexibility in reporting different situations 
    for different pollutants or indicators of pollution. 
    (If the same method, confidence and period apply 
    to all substances assessed for a groundwater body, 
    then identical values can be reported for all substances)  
    The threshold value used in the assessment is specified 
    in the `gwThresholdIdentifier`attribute, 
    linking to the `GWMethodologies::ThresholdValue` table 
    (or to the European standard if applicable).
    
* - GWQuantitativeStatus
  - *new*  
    The `GWQuantitativeStatus` table gathers 
    the data related to quantitative status.  
    The assessment method, confidence and period 
    is reported using the same pattern 
    applied for groundwater pollutants.
    It is now possible to report the use of grouping 
    for the quantitative status assessment.

* - GWGrouping
  - *new*   
    If grouping was not used, this table is not necessary.  
    If grouping was used for the 
    assessment of quantitative or chemical status,
    the `GWGrouping` table is used 
    to define sets of water bodies 
    that were monitored and assessed together as an ensemble.
    The same ensemble can be used for different purposes. 
    The same water body can be a member of different ensembles.
    
    The `groupingIdentifier` value uniquely identifies an ensemble 
    using the WISE identifier syntax.
    The `euGroundWaterBodyCode` identifies a member of the ensemble.  
    If an ensemble is used 
    in the assessment of a given element, 
    then at least one of its water bodies
    must be monitored for that element
    (i.e. must have `gwPollutantAssessmentMethod = 'monitoring'`).  
    (To avoid mistakes and ambiguities, 
    the `groupingIdentifier` value must be different 
    from any known water body identifier. 
    It is recommended to use a clear pattern 
    to avoid conflicts with existing 
    and future water body identifiers.
    For example, using a '_GWGROUPING' suffix).       

* - GWPressureImpact
  - *modified*.  
    For the water bodies that do not achieve good quantitative status in 2027, 
    the significant pressures causing poor quantitative status 
    are reported in the `GWQuantitativeExemption` table 
    (see {numref}`Exemptions_4thCycle_GWQuantitativeExemption_ClassDiagram`) 
    and do not need to be reported again in the `GWPressureImpact` table.

    For water bodies that do not achieve good chemical status in 2027, 
    the significant pressures are reported in the `GWChemicalExemption` table 
    (see {numref}`Exemptions_4thCycle_GWChemicalExemption_ClassDiagram`) 
    and do not need to be reported again in the `GWPressureImpact` table.
    
    For cases where a pressure is not causing failure, 
    but still causes an impact that needs to be managed, 
    the `GWPressureImpact` table should be used.

    Note that the reporting of pressures and impacts 
    is combined into a single `GWPressureImpact` table. 
    In the 3rd cycle, the XML structure did not allow 
    a specific pressure to be link to a given impact.
    In the proposed structure, this is possible (but not mandatory).  
    Illustrative examples will be provided.  
```

(heading_wfd_groundwater_codelist_4th_cycle)=
## Groundwater - codelists - 4th cycle

* For the `AquiferMediaTypeValue` codelist,
  see {numref}`Codelist_4thCycle_AquiferMediaTypeValue_AquiferProductivity_ClassDiagram`.  
  The codelist was realigned with the INSPIRE codelist to allow more flexibility.

  - See the definitions in {numref}`Codelist_4thCycle_AquiferMediaTypeValue_Table`.

* For the `AquiferProductivity` codelist,
  see {numref}`Codelist_4thCycle_AquiferMediaTypeValue_AquiferProductivity_ClassDiagram`.  
  The codelist allows the reporting of aquifer productivity
  independently of the aquifer media values.  
  Further technical guidance on concepts, classification schemes and class boundaries
  is needed.{footcite}`gsi2026aquifer`

  - See the definitions in {numref}`Codelist_4thCycle_AquiferProductivity_Table`.

* For the `AssessmentMethod` codelist,
  see {numref}`Codelist_4thCycle_AssessmentMethod_AssessmentConfidence_ClassDiagram`.  
  The codelist is used to report
  the assessment method for the chemical status and for the quantitative status.  
  The same codelist is used for surface water bodies,
  for the assessment method of ecological status or potential,
  and for the assessment method of chemical status.

  - See the definitions in {numref}`Codelist_4thCycle_AssessmentMethod_Table`.

* For the `AssessmentConfidence` codelist,
  see also {numref}`Codelist_4thCycle_AssessmentMethod_AssessmentConfidence_ClassDiagram`.  
  The codelist allow the reporting of
  the level of confidence in the results of the status assessment.  
  The same codelist is used for surface water bodies.
  See also {footcite}`mastrandrea2010guidance` {footcite}`mastrandrea2011ipcc`  {footcite}`kause2022confidence`.

  - See the definitions in {numref}`Codelist_4thCycle_AssessmentConfidence_Table`.

* For the `GroundwaterSurfaceWaterLink` codelist,
  see {numref}`Codelist_4thCycle_GroundwaterSurfaceWaterLink_ClassDiagram`.  
  The codelist is used to report
  the type of link between a given groundwater body and a given surface water body. 

  - See the definitions in {numref}`Codelist_4thCycle_GroundwaterSurfaceWaterLink_Table`.

* For the `ReasonForFailure` codelist,
  see {numref}`Codelist_4thCycle_ReasonForFailure_ClassDiagram`.

  - See the definitions in {numref}`Codelist_4thCycle_ReasonForFailure_Table`.

  - For groundwater bodies in poor quantitative status,
    the codelist values are used
    in the `gwQuantitativeReasonsForFailure` attribute
    to provide further information about one or more causes of failure
    (the most frequent cause will be likely be `'waterBalance'`).  
    For groundwater bodies in good or unknown quantitative status,
    the option `notApplicable` must be used.

  - For groundwater bodies failing to achieve good chemical status,
    the codelist values are used
    in the `gwChemicalReasonsForFailure` attribute
    to provide further information about one or more causes of failure
    (the most frequent cause will be likely be `'waterQuality'`).  
    For groundwater bodies in good or unknown quantitative status,
    the option `notApplicable` must be used.
    For groundwater bodies in good or unknown chemical status,
    the option `notApplicable` must be used.

  - For groundwater bodies where good quantitative status is at risk,
    the codelist values are used
    in the `gwQuantitativeReasonsForRisk` attribute
    to provide further information about one or more causes of risk.
    For groundwater bodies where `gwAtRiskQuantitative = 'no'`
    the option `notApplicable` must be used.

* For the `PressureType` codelist,
  see {numref}`Codelist_4thCycle_PressureType_ClassDiagram` in
  the section {ref}`heading_wfd_pressure_type_codelist_4th_cycle`
  
% -----------------------------------------------------------------------------

```{mermaid} /DataModelReview/mmd/Codelist_4thCycle_AquiferMediaTypeValue_AquiferProductivity_ClassDiagram.mmd
:name: Codelist_4thCycle_AquiferMediaTypeValue_AquiferProductivity_ClassDiagram
:align: center
:caption: AquiferMediaTypeValue codelist and AquiferProductivity codelist - 4th cycle
```

```{include} /DataModelReview/tables/Codelist_4thCycle_AquiferMediaTypeValue_Table
```

```{include} /DataModelReview/tables/Codelist_4thCycle_AquiferProductivity_Table
```

% -----------------------------------------------------------------------------

```{mermaid} /DataModelReview/mmd/Codelist_4thCycle_AssessmentMethod_AssessmentConfidence_ClassDiagram.mmd
:name: Codelist_4thCycle_AssessmentMethod_AssessmentConfidence_ClassDiagram
:align: center
:caption: AssessmentMethod codelist and AssessmentConfidence codelist - 4th cycle
```

```{include} /DataModelReview/tables/Codelist_4thCycle_AssessmentMethod_Table
```

```{include} /DataModelReview/tables/Codelist_4thCycle_AssessmentConfidence_Table
```

% -----------------------------------------------------------------------------

```{mermaid} /DataModelReview/mmd/Codelist_4thCycle_GroundwaterSurfaceWaterLink_ClassDiagram.mmd
:name: Codelist_4thCycle_GroundwaterSurfaceWaterLink_ClassDiagram
:align: center
:caption: GroundwaterSurfaceWaterLink codelist - 4th cycle
```

```{include} /DataModelReview/tables/Codelist_4thCycle_GroundwaterSurfaceWaterLink_Table
```

% -----------------------------------------------------------------------------

```{mermaid} /DataModelReview/mmd/Codelist_4thCycle_ReasonForFailure_ClassDiagram.mmd
:name: Codelist_4thCycle_ReasonForFailure_ClassDiagram
:align: center
:caption: ReasonForFailure codelist - 4th cycle
```

```{include} /DataModelReview/tables/Codelist_4thCycle_ReasonForFailure_Table
```

```{todo}
Groundwater - Topics that require discussion and clarification.
* Revision of the **ImpactType** codelist.
* Mapping tables to 3rd cycle codelists
```

(heading_wfd_groundwater_annexes_3rd_cycle)=
## Annexes - Data analysis - 3rd cycle

```{include} /DataModelReview/FragmentAnnexesDataAnalysis3rdCycle
```

### Geological formation

The WFD2016 and WFD2022 *geologicalFormation* attribute values
are clearly similar to the *Aquifer Type Code* attribute
({numref}`IHME1500_InternationalHydrogeologicalMapOfEurope_Table`)
in the International Hydrogeological Map of Europe 1:1,500,000 (IHME1500),
although there is no reference to that source
is made in the WFD Reporting Guidance documents.

A provisional spatial analysis of the two datasets
(using only the topmost horizons)
reveals limited agreement between the classifications.  
In {numref}`AquiferTypesWFDVersusIHME`,
the rows represent the reported WFD geological formation
and the columns represent the IHME aquifer type.
The values show the percentage of the area of each WFD geological formation
classified under each IHME aquifer type. For example:

* 48% of the area reported as 'Fissured aquifers including karst - highly productive'
  under WFD is similarly classified under IHME
* 33% of the area reported as 'Fissured aquifers including karst - moderately productive'
  under WFD is classified under IHME as 'Practically non-aquiferous rocks, porous or fissured'.

In practice, this means that an existing pan-European hydrogeological map (IHME1500)
can not be easily used to replace the information reported under WFD,
but it also highlights the need for better clarification
of the aquifer type and aquifer productivity values to be used in the 4th cycle.

```{figure} /DataModelReview/img/AquiferTypesWFDversusIHME.png
:name: AquiferTypesWFDversusIHME
:width: 100%
:align: center
WFD geological formation and IHME1500 aquifer type.
```

```{dropdown} See detailed description
```{include} /DataModelReview/tables/IHME1500_InternationalHydrogeologicalMapOfEurope_Table
```

### Aquifer productivity

See {numref}`CIS_Guidance_2_Figure_9`: the CIS Guidance Document 2 does not provide quantitative guidelines,
beyond the mention to the 10 m3/d threshold for drinking water abstraction.
Does then the classification  `geologicalFormation = 'Insignificant aquifers'`
mean that the aquifer is not relevant in terms of potential yield,
but is significant due to dependent surface water bodies,
or groundwater dependent ecosystem?
This should be clarified in the codelist definitions.

```{figure} /DataModelReview/img/CIS_Guidance_2_Figure_9.png
:name: CIS_Guidance_2_Figure_9
:width: 100%
:align: center
Criteria for definition of an aquifer (CIS Document 2).
```

National documents vary, when addressing productivity in terms of potential long-term abstraction rate.

```{epigraph}
*Example* - Ireland 2026 {footcite}`gsi2026aquifer`: 
   
"Yield is one of the main concerns in aquifer development projects, 
yields from existing wells are conceptually linked with the main aquifer categories:

* Regionally important (R) aquifers should have (or be capable of having) 
  a large number of ‘excellent’ yields: in excess of approximately 400 m3/d.
* Locally important (L) aquifers are capable of ‘good’ well yields 100-400 m3/d.
* Poor (P) aquifers would generally have ‘moderate’ or ‘low’ well yields - less than 100 m3/d."
```

```{epigraph}

*Example* - Scotland 2004 {footcite}`macdonald2004gis`: 

"Productivity classes are a measure of the expected (i.e. potential) 
long-term abstraction rate of groundwater 
from a typical borehole at an individual abstraction site." 

|Class     |  Range   |Unit  |
|----------|----------|------|
|Very high |  (20,)   | L/s  |
|High      |  (10,20] | L/s  |
|Moderate  |  (1,10]  | L/s  |
|Low       |  (0.1,1] | L/s  |
|Very low  |  (0,0.1] | L/s  |

```

(heading_wfd_groundwater_annexes_reason_for_failure_3rd_cycle)=
### Reasons for failure

```{dropdown} Show code
  ```{code-block} sql
  :caption: [gwChemicalStatusValue] vs [gwChemicalReasonsForFailure] - 3rd cycle
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
  :caption: Number of reasons for chemical failure - 3rd cycle
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
  :caption: [gwQuantitativeStatusValue] vs [gwQuantitativeReasonsForFailure] - 3rd cycle
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
  :caption: Number of reasons for quantitative failure - 3rd cycle
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

(heading_wfd_groundwater_annexes_nbl_3rd_cycle)=
### Natural background levels

In the 3rd cycle, natural background levels (NBL)
were reported for 8608 water bodies (38.6%) and over 90 substances.

An exploratory analysis shows the expected high frequency of reporting of NBLs for metals and metalloids
(e.g. arsenic, cadmium or lead), major ions and nutrients
(e.g. chloride, sulphate, ammonium or nitrate)
and physico-chemical parameters like electrical conductivity
(likely as an indicator of saline intrusion).

Other parameters are more unexpected and are likely due to reporting errors (e.g. chlorite instead of chloride).

More importantly, the values reported
are sometimes physically impossible (e.g. above 1000mg/L)
or clearly unlikely.

```{dropdown} See table
```{include} /DataModelReview/tables/GroundWaterBody_3rdCycle_NaturalBackgroundLevel_Table
```

```{dropdown} Show code
  ```{code-block} sql
  :caption: Substances for which natural background levels were reported - 3rd cycle
  :linenos:
  -- https://discodata.eea.europa.eu/
  SELECT ISNULL(b.[parameterGroup],'undefined') AS [parameterGroup]
        ,[gwPollutantCode] AS [parameter]
        ,COUNT(DISTINCT [countryCode]) AS nCountries
        ,COUNT(DISTINCT [euGroundWaterBodyCode]) AS nWaterBodies
    FROM [WISE_WFD].[v2r1].[GWB_GroundWaterBody_GWPollutant] a
    LEFT JOIN (
    SELECT *
      FROM (VALUES
      ('Metals and Metalloids', 'CAS_7429-90-5', 'Aluminium and its compounds'),
      ('Metals and Metalloids', 'CAS_7440-36-0', 'Antimony'),
      ('Metals and Metalloids', 'CAS_7440-38-2', 'Arsenic and its compounds'),
      ('Metals and Metalloids', 'CAS_7440-39-3', 'Barium'),
      ('Metals and Metalloids', 'CAS_7440-42-8', 'Boron'),
      ('Metals and Metalloids', 'CAS_7440-43-9', 'Cadmium and its compounds'),
      ('Metals and Metalloids', 'CAS_7440-47-3', 'Chromium and its compounds'),
      ('Metals and Metalloids', 'CAS_18540-29-9', 'Chromium VI'),
      ('Metals and Metalloids', 'CAS_7440-48-4', 'Cobalt and its compounds'),
      ('Metals and Metalloids', 'CAS_7440-50-8', 'Copper and its compounds'),
      ('Metals and Metalloids', 'CAS_7439-89-6', 'Iron and its compounds'),
      ('Metals and Metalloids', 'CAS_7439-92-1', 'Lead and its compounds'),
      ('Metals and Metalloids', 'CAS_7439-96-5', 'Manganese and its compounds'),
      ('Metals and Metalloids', 'CAS_7439-97-6', 'Mercury and its compounds'),
      ('Metals and Metalloids', 'CAS_7439-98-7', 'Molybdenum and its compounds'),
      ('Metals and Metalloids', 'CAS_7440-28-0', 'Thallium'),
      ('Metals and Metalloids', 'CAS_7440-02-0', 'Nickel and its compounds'),
      ('Metals and Metalloids', 'CAS_7782-49-2', 'Selenium and its compounds'),
      ('Metals and Metalloids', 'CAS_7440-61-1', 'Uranium'),
      ('Metals and Metalloids', 'CAS_7440-62-2', 'Vanadium and its compounds'),
      ('Metals and Metalloids', 'CAS_7440-66-6', 'Zinc and its compounds'),
      ('Major Ions and Nutrients', 'CAS_14798-03-9', 'Ammonium'),
      ('Major Ions and Nutrients', 'CAS_7440-70-2', 'Calcium'),
      ('Major Ions and Nutrients', 'CAS_16887-00-6', 'Chloride'),
      ('Major Ions and Nutrients', 'CAS_16984-48-8', 'Fluoride'),
      ('Major Ions and Nutrients', 'CAS_71-52-3', 'Hydrogen Carbonate Bicarbonate HCO3'),
      ('Major Ions and Nutrients', 'CAS_7439-95-4', 'Magnesium'),
      ('Major Ions and Nutrients', 'CAS_14797-55-8', 'Nitrate'),
      ('Major Ions and Nutrients', 'CAS_14797-65-0', 'Nitrite'),
      ('Major Ions and Nutrients', 'CAS_14265-44-2', 'Phosphate'),
      ('Major Ions and Nutrients', 'CAS_7440-09-7', 'Potassium'),
      ('Major Ions and Nutrients', 'CAS_7440-23-5', 'Sodium'),
      ('Major Ions and Nutrients', 'CAS_18785-72-3', 'Sulphate'),
      ('Major Ions and Nutrients', 'CAS_7723-14-0', 'Total phosphorus'),
      ('Physico-chemical Parameters', 'EEA_3142-01-6', 'Electrical conductivity'),
      ('Physico-chemical Parameters', 'EEA_3152-01-0', 'pH'),
      ('Physico-chemical Parameters', 'EEA_3121-01-5', 'Water temperature')
  ) AS v(parameterGroup, parameterCode, name) ) b

      ON a.[gwPollutantCode] like b.parameterCode+' - %'

    WHERE a.[gwPollutantBackgroundLevelSet] = 'yes' 
        AND a.[cYear] = 2022 
        AND a.[hasDescriptiveData] = 1
        AND a.[gwPollutantCode] != 'EEA_00-00-0 - Other parameter'
    GROUP BY a.[gwPollutantCode]
        ,b.[parameterGroup]
    ORDER BY 1, 4 desc, a.[gwPollutantCode]
  ```

## References

```{footbibliography}
```
