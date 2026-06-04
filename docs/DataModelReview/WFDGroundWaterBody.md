(heading_wfd_groundwater_bodies)=
# WFD groundwater bodies

Last update: 2026-06-03

```{warning}
Public Version - Pending Discussion
```

## Purpose and overview

This section revises the reporting of information related to **Groundwater Bodies** 
in the 2ⁿᵈ and 3ʳᵈ cycle of reporting of the Water Framework Directive River Basin Management Plans. 
It also presents a proposal for simplifying the electronic reporting in the 4ᵗʰ cycle.

(heading_wfd_groundwater_3rd_cycle)=
## Current structure - 3ʳᵈ cycle

In the 3ʳᵈ cycle, the information about Groundwater bodies was reported in 4 separate schemas:

* the GWB_2022 schema, containing information about each groundwater body 
  ({numref}`Groundwater_3rdCycle_GWB_ClassDiagram`)
* the GWMET_2022 schema, containing information about the methodologies 
  (see {ref}`heading_wfd_groundwater_methodologies`)
* the GML_GroundWaterBody_2022 schema, 
  containing the GroundWaterBody spatial dataset.
* the GML_GroundWaterBodyHorizon_2022 schema, 
  containing the ancillary GroundWaterBodyHorizon spatial dataset.

(heading_wfd_groundwater_gwb_3rd_cycle)=
## GWB_2022 schema - 3ʳᵈ cycle

The GWB_2022 schema was already partially revised with regard to the reporting of exemptions. See:

* {ref}`heading_wfd_exemptions_groundwater_bodies_chemical_exemptions_by_pollutant`
* {ref}`heading_wfd_exemptions_groundwater_bodies_quantitative_exemptions`
* {ref}`heading_wfd_exemptions_groundwater_bodies_protected_area_exemptions`

Other simplifications already discussed also apply to the GWB schema:

* removal of the textual reporting of "other" pollutants
* removal of the textual reporting of "other" pressures
* removal of the textual reporting of "other" impacts

Based on the Commission's review of the 3ʳᵈ cycle reporting, 
the following elements were removed:

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

In the 4ᵗʰ cycle of reporting, the data will be delivered in the Reportnet3 platform:
* the remaining GWMET_2022 classes and elements were reorganised 
  into a relational model, as required by the migration to Reportnet3
* selective denormalisation was used to keep a low number of tables 
  and facilitate the quality control
* the requirements of Directive 2006/118/EC also need to be taken into account

```{epigraph}
(36) In order to ensure a level playing field in the Union and allow comparability of water body status between Member States, there is a need to harmonise national threshold values for some man-made synthetic groundwater pollutants. Threshold values should be established as necessary at Union level for pollutants which have an anthropogenic origin or for the products of their degradation or decomposition, provided that those pollutants and degradation products either do not occur naturally in groundwater, or, if identical natural counterparts exist, provided that their natural background levels are, at most, low. Those threshold values should be included in the repository of harmonised threshold values for man-made synthetic substances in groundwater of national, regional or local concern in a new Part D of Annex II to Directive 2006/118/EC. A harmonised threshold value for individual pharmaceuticals should be included for application by Member States to any pharmaceutical active substance identified as posing a risk at national level unless a stricter standard or threshold value has been set specifically for that substance at Union or national level.

(37) All provisions of Directive 2006/118/EC relating to the assessment of groundwater chemical status should be adapted to the introduction of the third category of harmonised threshold values in a new Part D of Annex II to that Directive, in addition to the quality standards set out in Annex I to that Directive and the national threshold values set out in accordance with the methodology set out in Part A of Annex II to that Directive.

-- ELI: http://data.europa.eu/eli/dir/2026/805/oj
```

(heading_wfd_groundwater_descriptive_4th_cycle)=
## Groundwater - descriptive data - 4ᵗʰ cycle

The proposed structure for the 4ᵗʰ cycle electronic reporting 
is presented in the class diagram in {numref}`Groundwater_4thCycle_DescriptiveData_ClassDiagram` 
and a brief description of each table is included in {numref}`Groundwater_4th_cycle_brief_table_description`.

* The core data about each groundwaterbody 
  is reported in 3 tables: `GroundWaterBody`, `LinkSurfaceWaterBody` and `GWNaturalBackgroundLevel`.

  * The content of this group of tables does not depend 
    of the status assessment, and can be prepared in advance.

* A second group of tables contains information about 
  the chemical and quantitative status assessment 
  and about pressures and impacts: `GroundWaterBodyStatus`, `GWQuantitativeStatus`, `GWPollutant` and `GWPressureImpact`.

  * The ancillary table `GWGrouping` 
    supports the reporting of grouping (if used the assessment).
  * A link to the `GWMethodologies::ThresholdValue` table clarifies which threshold value is applied to each pollutant.  
    (A list of the default EU threshold values will be provided 
    where defined by the EU legislation.)

```{mermaid} /DataModelReview/mmd/Groundwater_4thCycle_DescriptiveData_ClassDiagram.mmd
:name: Groundwater_4thCycle_DescriptiveData_ClassDiagram
:caption: Groundwater - descriptive data - 4ᵗʰ cycle
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
  - *modified*  
    The `GroundWaterBody` table contains the attributes 
    that describe the groundwater body 
    and that do not vary with the status of the waterbody.
    Therefore the table can be prepared immediately, 
    even if the 4ᵗʰ cycle RBMPs have not yet been finalised. 
    All the attributes existed in the 3ʳᵈ cycle reporting.  

    The `linkSurfaceWaterBody` value 
    controls the content of the `LinkSurfaceWaterBody` table.

    In the 3ʳᵈ cycle, the reporting guidance requested description of 
    "*the main geological formation of the aquifer type*".
    The usabilibility of the reported data was limited, 
    beyond visualisation purposes.  
    For the 4ᵗʰ cycle, a suggestion is made to split 
    the data in two attributes: `aquiferMediaType` and `aquiferProductivity`, 
    using the separation already present 
    in the published WISE_WFD database and in the WISE visualisations.      
    However, expert guidance must be provided, 
    specially with regard to the aquifer productivity classes,
    their definition and comparability across Member States.

    Under the name `aquiferLithology`, 
    a placeholder attribute is included in the diagram,
    as a suggestion to provide an aquifer typology 
    relevant for the geochemical characterisation of the groundwater body,
    and the definition of natural background levels 
    and substances threshold values. [^BRIDGE] 

* - GWLinkSurfaceWaterBody
  - *modified*.  
    If the groundwater body is linked to one or more surface water bodies,
    that relation is reported in the `GWLinkSurfaceWaterBody` table.  
    The `linkType` attribute specifies the type of water flow 
    between the groundwater and the surdace water body. 

* - GWNaturalBackgroundLevel
  - *modified*  
    The data related to the natural background level (NBL) 
    of substances in groundwater is moved from the GWPollutant class into a separate `GWNaturalBackgroundLevel` table.  
    This facilitates both the reporting and the quality control
    (see {ref}`heading_wfd_groundwater_annexes_nbl_3rd_cycle`). 

* - GroundWaterBodyStatus
  - *new*  
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
    to define sets of waterbodies 
    that were monitored and assessed as a group.
    The same grouping can be used for different purposes. 
    The same water body can be a member of different groups.
    
    The `groupIdentifier` value uniquely identifies the group 
    using the WISE identifier syntax.
    The `euGroundWaterBodyCode` identifies a member of the group.  
    If a group is used 
    in the assessment of a given element, 
    then at least one waterbody of the group 
    must be monitored for that element
    (i.e. must have `gwPollutantAssessmentMethod = 'monitoring'`).  
      (To avoid mistakes and ambiguities, 
    the `groupIdentifier` value must be different 
    from any known water body identifier. 
    It is recomended to use a clear pattern 
    to avoid conflicts with existing 
    and future water body identifiers.
    For example, using a '_GWGROUP' suffix).       

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
    In the 3ʳᵈ cycle, the XML structure did not allow 
    a specific pressure to be link to a given impact.
    In the proposed structure, this is possible (but not mandatory).  
    Illustrative examples will be provided.  
```

(heading_wfd_groundwater_codelist_4th_cycle)=
## Groundwater - codelists - 4ᵗʰ cycle

* For the `AquiferMediaTypeValue` codelist, 
  see {numref}`Codelist_4thCycle_AquiferMediaTypeValue_AquiferProductivity_ClassDiagram`.  
  The codelist was realigned with the INSPIRE codelist to allow more flexibility 
  (see {numref}`Codelist_4thCycle_AquiferMediaTypeValue_Table`).

* For the `AquiferProductivity` codelist, 
  see {numref}`Codelist_4thCycle_AquiferMediaTypeValue_AquiferProductivity_ClassDiagram`.  
  The codelist allows the reporting of aquifer productivity 
  independently of the aquifer media values 
  (see {numref}`Codelist_4thCycle_AquiferProductivity_Table`).  
  Further technical guidance on concepts, classification schemes and class boundaries 
  is needed. [^aquiferProductivityIreland]

* For the `AssessmentMethod` codelist, 
  see {numref}`Codelist_4thCycle_AssessmentMethod_AssessmentConfidence_ClassDiagram`.  
  The codelist is used to report 
  the assessment method for the chemical status and for the quantitative status 
  (see {numref}`Codelist_4thCycle_AssessmentMethod_Table`).  
  The same codelist is used for surface water bodies, 
  for the assessment method of ecological status or potential,
  and for the assessment method of chemical status.

* For the `AssessmentConfidence` codelist, 
  see also {numref}`Codelist_4thCycle_AssessmentMethod_AssessmentConfidence_ClassDiagram`.  
  The codelist allow the reporting of 
  the level of confidence in the results of the status assessment
  (see {numref}`Codelist_4thCycle_AssessmentConfidence_Table`).  
  The same codelist is used for surface water bodies. 
  See also [^IPCC_Authors] [^IPCC_WorkingGroups] [^IPCC_Readers].

* For the `GroundwaterSurfaceWaterLink` codelist,
  see {numref}`Codelist_4thCycle_GroundwaterSurfaceWaterLink_ClassDiagram`.  
  The codelist is used to report 
  the type of link between a given groundwater body and a given surface water body 
  (see {numref}`Codelist_4thCycle_GroundwaterSurfaceWaterLink_Table`).

* For the `ReasonForFailure` codelist, 
  see {numref}`Codelist_4thCycle_ReasonForFailure_ClassDiagram` 
  and {numref}`Codelist_4thCycle_ReasonForFailure_Table`.

  * For groundwater bodies in poor quantitative status, 
    the codelist values are used 
    in the `gwQuantitativeReasonsForFailure` attribute 
    to provide further information about one or more causes of failure 
    (the most frequent cause will be likely be `'waterBalance'`).  
    For groundwater bodies in good or unknown quantitative status, 
    the option `notApplicable` must be used.

  * For groundwater bodies failing to achieve good chemical status, 
    the codelist values are used 
    in the `gwChemicalReasonsForFailure` attribute 
    to provide further information about one or more causes of failure 
    (the most frequent cause will be likely be `'waterQuality'`).  
    For groundwater bodies in good or unknown quantitative status, 
    the option `notApplicable` must be used.
    For groundwater bodies in good or unknown chemical status, 
    the option `notApplicable` must be used. 

% -----------------------------------------------------------------------------

```{mermaid} /DataModelReview/mmd/Codelist_4thCycle_AquiferMediaTypeValue_AquiferProductivity_ClassDiagram.mmd
:name: Codelist_4thCycle_AquiferMediaTypeValue_AquiferProductivity_ClassDiagram
:align: center
:caption: AquiferMediaTypeValue codelist and AquiferProductivity codelist - 4ᵗʰ cycle
```

```{include} /DataModelReview/tables/Codelist_4thCycle_AquiferMediaTypeValue_Table
```

```{include} /DataModelReview/tables/Codelist_4thCycle_AquiferProductivity_Table
```

% -----------------------------------------------------------------------------

```{mermaid} /DataModelReview/mmd/Codelist_4thCycle_AssessmentMethod_AssessmentConfidence_ClassDiagram.mmd
:name: Codelist_4thCycle_AssessmentMethod_AssessmentConfidence_ClassDiagram
:align: center
:caption: AssessmentMethod codelist and AssessmentConfidence codelist - 4ᵗʰ cycle
```

```{include} /DataModelReview/tables/Codelist_4thCycle_AssessmentMethod_Table
```

```{include} /DataModelReview/tables/Codelist_4thCycle_AssessmentConfidence_Table
```

% -----------------------------------------------------------------------------

```{mermaid} /DataModelReview/mmd/Codelist_4thCycle_GroundwaterSurfaceWaterLink_ClassDiagram.mmd
:name: Codelist_4thCycle_GroundwaterSurfaceWaterLink_ClassDiagram
:align: center
:caption: GroundwaterSurfaceWaterLink codelist - 4ᵗʰ cycle
```

```{include} /DataModelReview/tables/Codelist_4thCycle_GroundwaterSurfaceWaterLink_Table
```

% -----------------------------------------------------------------------------

```{mermaid} /DataModelReview/mmd/Codelist_4thCycle_ReasonForFailure_ClassDiagram.mmd
:name: Codelist_4thCycle_ReasonForFailure_ClassDiagram
:align: center
:caption: ReasonForFailure codelist - 4ᵗʰ cycle
```

```{include} /DataModelReview/tables/Codelist_4thCycle_ReasonForFailure_Table
```

```{todo}
Groundwater - Topics that require discussion and clarification.
* Aquifer productivity
* Aquifer lithology / typology
* Revision of the **ImpactType** codelist.
* Mapping tables to 3rd cycle codelists
```

(heading_wfd_groundwater_annexes_3rd_cycle)=
## Annexes - Data analysis - 3ʳᵈ cycle

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
In {numref}`AquiferTypesWFDversusIHME`, 
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
of the aquifer type and aquifer productivity values to be used in the 4ᵗʰ cycle.

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
*Example* - Ireland 2026 [^aquiferProductivityIreland]: 
   
"Yield is one of the main concerns in aquifer development projects, yields from existing wells are conceptually linked with the main aquifer categories:
* Regionally important (R) aquifers should have (or be capable of having) a large number of ‘excellent’ yields: in excess of approximately 400 m3/d.
* Locally important (L) aquifers are capable of ‘good’ well yields 100-400 m3/d.
* Poor (P) aquifers would generally have ‘moderate’ or ‘low’ well yields - less than 100 m3/d."
```

```{epigraph}

*Example* - Scotland 2004 [^aquiferProductivityScoland]: 

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

(heading_wfd_groundwater_annexes_nbl_3rd_cycle)=
### Natural background levels

In the 3ʳᵈ cycle, natural background levels (NBL) 
were reported for 8608 waterbodies (38.6%) and over 90 substances. 

An exploratory analysis shows the expected high frequency of reporting of NBLs for metals and metalloids 
(e.g. arsenic, cadmium or lead), major ions and nutrients
(e.g. chloride, sulphate, ammonium or nitrate) 
and physico-chemical parameters like electrical conductivity
(likely as an indicator of saline intrusion).   

Other parameters are more unexpected and are likely due to reporting errors (e.g. chlorite instead of chloride). 

More importantly, the values reported 
are sometimes physically impossible (e.g. above 1000mg/L) 
or clearly unlikely.

% Footnotes

[^BRIDGE]: 
    Wendland, Frank & Blum, Ariane & Coetsiers, Marleen & Gorova, R. & Griffioen, J. & Grima-Olmedo, Juan & Hinsby, Klaus & Kunkel, Ralf & Marandi, Andres & de Melo, M T & Panagopoulos, Andreas & Pauwels, Hélène & Ruisi, M. & Traversa, Paola & Vermooten, Sophie & Walraevens, Kristine. (2008). 
    European aquifer typology: A practical framework for an overview of major groundwater composition at European scale. 
    Environmental Geology. 55. 77-85. 10.1007/s00254-007-0966-5. 

[^aquiferProductivityIreland]: 
    Geological Survey Ireland is a Division of Department of Climate, Energy and the Environment © 2026
    https://www.gsi.ie/en-ie/programmes-and-projects/groundwater/activities/understanding-ireland-groundwater/aquifer-classification/Pages/Aquifer-classification-how-to.aspx

[^aquiferProductivityScoland]: 
    MACDONALD A M, BALL D F and Ó DOCHARTAIGH B É. 2004. 
    A GIS of aquifer productivity in Scotland: explanatory notes. 
    British Geological Survey Commissioned Report, CR/04/047N. 21pp.
    https://nora.nerc.ac.uk/id/eprint/504764/1/CR-04-047N_SEPA%20Aq%20productivity.pdf 

[^IPCC_Authors]: 
    Mastrandrea, MD, Field CB, Stocker TF, Edenhofer O, Ebi KL, Frame DJ, Held H, Kriegler E, Mach KJ, Matschoss PR, Plattner GK (2010) 
    Guidance note for lead authors of the IPCC fifth assessment report on consistent treatment of uncertainties. 
    https://www.ipcc.ch/site/assets/uploads/2017/08/AR5_Uncertainty_Guidance_Note.pdf

[^IPCC_WorkingGroups]: 
    Mastrandrea, M.D., Mach, K.J., Plattner, GK. et al. (2011) 
    The IPCC AR5 guidance note on consistent treatment of uncertainties: a common approach across the working groups. 
    Climatic Change 108, 675 . https://doi.org/10.1007/s10584-011-0178-6

[^IPCC_Readers]: 
    Kause, A., Bruine de Bruin, W., Persson, J. et al. (2022) 
    Confidence levels and likelihood terms in IPCC reports: a survey of experts from different scientific disciplines. Climatic Change 173, 2 . https://doi.org/10.1007/s10584-022-03382-3

(heading_wfd_wfd_groundwater_bodies_references)=
## References

```{include} FragmentReportingGuidanceFiles
```

