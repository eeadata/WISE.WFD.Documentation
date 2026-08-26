(heading_wfd_measures)=
# Programme of measures

Last update: 2026-08-25

(heading_wfd_measures_purpose_and_overview)=
## Purpose and overview

This section revises the **River Basin Management Plan & Programme of Measures** schema
used in the 3rd cycle of reporting of the Water Framework Directive River Basin Management Plans.
It also presents a proposal for simplifying the electronic reporting in the 4th cycle.

Not all information in the RBMPs can be accurately provided using a common European model.
However, it is possible to improve and simplify the reporting of structured data,
accepting that part of the relevant information will remain in documentation
to be analysed during the Commission's implementation assessment.

Using this principle, the data model can focus on aspects that are suitable for structured reporting,
allowing adequate comparisons between different river basin districts (RBDs).
Specific or more detailed information can be kept in the RBMP documents,
the analysis of which can in the future be facilitated using, for example,
large language models (LLMs) supported by retrieval‑augmented generation (RAG) techniques.

## Current structure - 3rd cycle

The schema used in the 3rd cycle of reporting contained 4 main groups
({numref}`Measures_RBMPPoM_2022_ClassDiagram`):

* summary information about the **River Basin Management Plan**,
  the **Progress** since the previous River Basin Management Plan,
  and the mechanisms of international **Coordination** (if applicable)

* information about the **Programme of Measures**,
  comprising a summary questionnaire of **Targeted Questions**
  and aggregated data about the overall **Cost** of measures  

* disaggregated information was requested about each **Measure**
  and its classification into **Key Types of Measures** (KTM)
  and basic type of measures (if applicable)

* further information about **Significant pressures and substances** causing failure,
  along with their link to **KTM Indicators** and **Indicator Gaps**

```{figure} img/Measures_RBMPPoM_2022_ClassDiagram.png
:name: Measures_RBMPPoM_2022_ClassDiagram
:align: center
:width: 100%

River Basin Management Plan & Programme of Measures table - 3rd cycle
```

## RBMP, Coordination and Progress table - 3rd cycle

In the 3rd cycle of reporting, this group comprised three tables, collecting summary information
about the **RBMP**, the **Progress** since the previous **RBMP**, and the mechanisms of international
**Coordination**, if applicable ({numref}`RBDCA_RBDSUCA_2022_Partial_ClassDiagram`).

The data is structured as a simple questionnaire, mostly with Yes/No or multiple‑choice answers,
accompanied by links to additional documentation (which can be uploaded or kept on national
websites). Only one record per table is required for each River Basin District.

Reporting by MS should not present technical difficulties, and there is limited scope for technical
simplification. Nevertheless, the Commission has reviewed whether the requested data is strictly
required and proposes the simplification detailed in the next sections.

```{figure} img/RBDCA_RBDSUCA_2022_Partial_ClassDiagram.png
:name: RBDCA_RBDSUCA_2022_Partial_ClassDiagram
:align: center
:width: 100%

River Basin Management Plan, international Coordination and Progress - 3rd cycle
```

## Costs table - 3rd cycle

Regarding the economic data in the programme of measure,
the revision of the electronic reporting focuses on the main issues
described in the Note to the CIS Working Group Economics quoted below
{footcite}`Arnoldus2025`:

```{epigraph}
“[…] Both the Commission’s 6th and 7th WFD Implementation Reports indicate persistent problems in
the (electronic) reporting on the investments and the costs of other measures in the Programme of
Measures (**PoM**).

The 6th WFD Implementation Report notes that the Member States’ reporting on costs and financing of
the **PoMs** appears overall patchy and that a consultant’s study estimate is an underestimation for
the total costs, as there are significant data gaps and it excludes operational and infrastructure
maintenance costs. The corresponding investment overview table shows indeed large gaps.
{footcite}`6thWFDImplementationReport`

The Commission’s evaluation of the 3rd River Basin Management Plans 
{footcite}`7thWFDImplementationReport`, as part of the 7th WFD Implementation Report, 
notes that the “third **PoMs** presented in the (…) RBMPs show
that Member States continue to have different approaches to their design and reporting” and that
“the costs and the financing of the planned measures are often missing.” Hence, the Commission
recommends that “in order to effectively implement the **PoMs** to develop long‑term investment plans
and clearly identifying the source of financing for each measure.” A good planning is also necessary
for the acquisition of support from EU Funds, the EIB and other promotional banks.

*The challenge is thus to improve the reporting of the costs of the **PoM** measures, including the
investment amounts*, and to specify the funding of these investments and other measures. This
requires a clear distinction between capital costs (CAPEX) and operational costs (OPEX). […]

The proposal here is to agree on a clear conceptual basis for the **PoM** costs.

It is natural to consider the **PoM** as a **budget of government outlays** – however, there can be
costs on other economic agents without government payment involved (cf. banning an activity).

The budget orientation would imply to look at foreseen **spending amounts**. This has three
consequences:

* ‘Welfare costs’ should not be included in the reporting. However, they can be taken up as
  “negative benefits” in the **CEA (cost‑effectiveness analysis)**.
* The reporting is on investment spending (purchases / commitments) and not on capital costs
  (depreciation).
* To make the link with financial support from EU Funds, EIB and other promotional banks, one
  needs to distinguish OPEX and CAPEX when reporting investment cost.

There is a readily available conceptual basis for the reporting on the **PoM** investment and other
costs, with which the Member States are already familiar, namely the **environmental protection
expenditures**. They are namely required to collect and report this data annually to Eurostat
{footcite}`EEEAccounts`, who publishes the **Environmental Protection Expenditures Accounts (EPEA)**
as one of the environmental‑economic satellite accounts to the economic National Accounts.
The EPEA are based on a clear, publicly available protocol (following UN statistical standards),
defining the environmental domains, spending economic sectors, and expenditure types. 
The latter includes the distinction between **capital** and **current** expenditures. 
Hence, it meets the features described in the three bullets points above.

```

A brief review of the reported data confirms the issues mentioned above.

In the **3rd cycle** of reporting, the overall cost of the **PoM** was reported in the **Costs** class
({numref}`Measures_3rdCycle_Costs`). Reporting of costs was, de facto, optional –
since all numerical attributes admitted the option **–9999** to denote “data not available”.

 Out of the 146 RBD reported by EU Member States, 24 do not have data on investments, 54 do not
 have data on operational costs and 64 do not have data on EU funds.

```{mermaid} /DataModelReview/mmd/Measures_3rdCycle_Costs.mmd
:name: Measures_3rdCycle_Costs
:align: center
:caption: Class diagram for the RBMPPoM_2022 schema: Costs – 3rd cycle
```

The variability of the geographical and temporal coverage of the reported data adds to the
difficulty in achieving a meaningful analysis.
{numref}`Measures_3rdCycle_TemporalCoverage` illustrates the issues regarding temporal coverage.
{numref}`Measures_3rdCycle_GeographicalCoverage` illustrates the issue with geographical coverage.

```{table} Temporal coverage: period to which the reported costs refer – 3rd cycle (including Norway).
:name: Measures_3rdCycle_TemporalCoverage
:width: 100%
| costOfMeasurePeriod20152021 | costOfMeasurePeriod20212027 | Number of RBDs |
|---|---|---|
| 2014--2020 | 2022--2027 | 5 |
| 2015--2020 | 2021--2027 | 1 |
| 2015--2020 | 2022--2027 | 2 |
| 2015--2021 | 2007--2027 | 1 |
| 2015--2021 | 2021--2027 | 62 |
| 2015--2021 | 2022--2027 | 23 |
| 2016--2021 | 2009--2015 | 1 |
| 2016--2021 | 2010--2015 | 7 |
| 2016--2021 | 2021--2027 | 4 |
| 2016--2021 | 2022--2027 | 40 |
| 2016--2021 | 2023--2027 | 3 |
| 2016--2022 | 2023--2027 | 4 |
| 2016--2027 | 2019 | 4 |
| 2017--2021 | 2021--2027 | 4 |
| 2017--2021 | 2022--2027 | 1 |
```

```{table} Geographic coverage: scale to which the reported costs refer – 3rd cycle (including Norway).
:name: Measures_3rdCycle_GeographicalCoverage
:width: 100%
| costOfMeasuresScale20152021 | costOfMeasuresScale20212027 | Number of RBDs |
|---|---|---|
| National | National | 48 |
| River Basin District | River Basin District | 103 |
| National | River Basin District | 4 |
| River Basin District | National | 7 |
```

(heading_wfd_measures_proposed_structure_4th_cycle)=
## Proposed structure - 4th cycle

* The former RBMP and Coordination tables are simplified
  to a single `RiverBasinManagementPlan` table,
  containing a selected subset of attributes.  

* The `Progress` table is modified to request only aggregated information
  about the overall status of the measures of the previous cycle (3rd cycle).

* The reporting of the Programme of Measures is also simplified.
  The `TargetedQuestions` table, containing the questionnaire at RBD level, is simplified.  

* Information about measures is requested in a single `Measure` table.

* The former Costs table is removed.
  Information about the planned `ExpenditurePerMeasure`
  is reported in a separate table, if data is available.
  
* The KTM classification, KTM indicators and indicator gaps data is completely removed.

```{mermaid} /DataModelReview/mmd/Measures_4thCycle_Overview_ClassDiagram.mmd
:name: Measures_4thCycle_Overview_ClassDiagram
:caption:  Programmes of measures dataflow - overview - 4th cycle
:align: center
```

## Descriptive dataset - 4th cycle

### RiverBasinManagementPlan table

The simplified `RiverBasinManagementPlan` table contains a subset of the data previously requested
in the **RBMP** and **Coordination** classes in the 3rd cycle
({numref}`Measures_4thCycle_RiverBasinManagementPlan_ClassDiagram`):

* The new `coordinationNRRReference` attribute allows the reporting of information related to
  coordination with the Nature Restoration Regulation.
* The `pomCoordinationArt5SWMI`, `pomCoordinationIRBMPPoM`, `pomCoordinationRoofReport` and
  `pomCoordinationFinancial` attributes are only required for international RBDs.

```{mermaid} /DataModelReview/mmd/Measures_4thCycle_RiverBasinManagementPlan_ClassDiagram.mmd
:name: Measures_4thCycle_RiverBasinManagementPlan_ClassDiagram
:caption: River Basin Management Plan table – 4th cycle
:align: center
```

### Progress table

The `Progress` table is modified to provide an
overview of the proportion of the measures of the 3rd RBMPs
that were executed, cancelled, or otherwise affected,
as well as the obstacles encountered during the implementation
of the 3rd RBMP Programme of Measures ({numref}`Measures_4thCycle_Progress_ClassDiagram`).

The only constraint is that, for each RBD,
the sum of the values in `percentageInStatus` must be **100**.
The level of detail can be adapted depending on the needs and the data available at national level.

```{mermaid} /DataModelReview/mmd/Measures_4thCycle_Progress_ClassDiagram.mmd
:name: Measures_4thCycle_Progress_ClassDiagram
:caption: Progress table – 4th cycle
:align: center
```

A numerical example illustrates the proposed approach.
Consider a hypothetical 3rd RBMP Programme of Measures with 10 different measures,
which are in different statuses and may have faced different obstacles
({numref}`measures_example_ten_measures`).

```{table} Illustrative example - hypothetical list with the status of the 10 measures of the 3rd cycle.
:name: measures_example_ten_measures
:width: 100%

| Measure | Status | Obstacles |
| --- | --- | --- |
| M01 | Ongoing | No obstacles. |
| M02 | Executed | No obstacles. |
| M03 | Executed | No obstacles. |
| M04 | Executed | Extreme event. |
| M05 | Executed | Extreme event. |
| M06 | Cancelled | Extreme event. |
| M07 | Cancelled | Extreme event. |
| M08 | Postponed to the next cycle | Delays, Lack of finance. |
| M09 | Postponed to the next cycle | Delays, Lack of finance. |
| M10 | Cancelled | Not cost effective. |

```

The example in {numref}`measures_example_progress`
illustrates how to synthesize the information in the Progress table.

```{table} Illustrative example - Progress table records for the previous example.
:name: measures_example_progress
:width: 100%

| previousRBMPMeasureStatus | percentageInStatus | obstaclesDelays | obstaclesLackOfFinance | obstaclesMeasureNotCostEffective | obstaclesExtremeEvents |
| --- | --- | --- | --- | --- | --- |
| ongoing | 10 | No | No | No | No |
| executed | 20 | No | No | No | No |
| executed | 20 | No | No | No | Yes |
| cancelled | 20 | No | No | No | Yes |
| planned | 20 | Yes | Yes | No | No |
| cancelled | 10 | No | No | Yes | No |
```

### TargetedQuestions table

The `TargetedQuestions` table collects summary information about the measures in the RBMP,
and the progress since the previous cycle. For each RBMP, only one record is required.
The data is structured as a simple questionnaire, with Yes/No or multiple-choice answers.

Reporting by MS should not present technical difficulties,
and there is limited scope for any technical simplification.
The Commission has revised and simplified the `TargetedQuestions` table,
keeping a subset of the questions requested in the previous cycle
({numref}`Measures_4thCycle_TargetedQuestions_ClassDiagram`).

```{mermaid} /DataModelReview/mmd/Measures_4thCycle_TargetedQuestions_ClassDiagram.mmd
:name: Measures_4thCycle_TargetedQuestions_ClassDiagram
:caption: TargetedQuestions table – 4th cycle
:align: center
```

### Measure table

The simplified `Measure` table proposed for the 4th cycle is illustrated in
({numref}`Measures_4thCycle_Measure_ClassDiagram`).

For each measure:

* create a unique persistent European identifier `measureCode`
* use the original descriptive `measureName` (or an English translation thereof)
* if needed, provide links to documentation (`measureReference`)
* identify the primary `measureLegalInstrument`, using a single codelist value
* identify the `measureType`, using a single codelist value
* classify the measure using a single `mainKeyTypeOfMeasure` codelist value from a simplified
  classification. The closest match should be selected
* optionally or if applicable, identify the main pressure addressed by the measure using the
  `measurePressureType` attribute,
  at the level of detail deemed more adequate. The closest match should be selected
* optionally or if applicable, identify the main substance or group of substances
  addressed by the measure using the `measureSubstanceType` attribute,
  at the level of detail deemed more adequate
* flag the sectoral plans for which the measure might be relevant
  using the `msfdRelevance`, `floodsRelevance`, `natureRestorationRegulationRelevance`,
  `draughtManagementPlanRelevance` and `climateAdaptationPlanRelevance` attributes
* specify the `geographicalCoverage` and `temporalCoverage` of the measure

```{mermaid} /DataModelReview/mmd/Measures_4thCycle_Measure_ClassDiagram.mmd
:name: Measures_4thCycle_Measure_ClassDiagram
:caption: Measure table – 4th cycle
:align: center
```

* The primary `measureLegalInstrument` under which the measure was defined
  must be clearly identified.
  This avoids double reporting in other Directives:
  the measures can be reported only once under the RBMP electronic reporting.
  An updated list of EU water and other environmental legislation is provided
  ({numref}`Codelist_4thCycle_LegalInstrument_Table`).

  The scope of some basic measures is clearly linked to the two Daughter directives:

  - Measures to prohibit direct discharges to groundwater: *Groundwater Directive*
  - Measures to eliminate or reduce pollution by Priority Substances:
    *Environmental Quality Standards Directive*

  These two legal instruments are part of the codelist.
  The option 'Other' (Other Directives mentioned in Part A of Annex VI of the WFD),
  that existed in the 3rd cycle,
  is now eliminated because it did not convey relevant information.

* The `mainKeyTypeOfMeasure` attribute contains the classification to be used
  for both basic and supplementary measures (see {numref}`Codelist_4thCycle_MainKeyTypeOfMeasure_Table`).
  It simplifies, consolidates and replaces both
  the **basicMeasureType** and the **keyTypeOfMeasure** classifications used in the 2nd and 3rd cycles.

  The purpose of the simplified classification is:

  - To reduce the number of classes to a manageable set (19 options).
  - To use a single classification scheme applicable to both basic measures and supplementary
    measures.
  - To avoid redundancy and reporting burden in the classification of the measures.
  - To maintain the options directly linked to the basic measure types in Articles 11(3)(b) to
    11(3)(l) of the WFD – see codes B, C, D, E, F, G, H, J, K, L.
  - To maintain the disaggregation in the measures to address significant impacts in the status of
    water as per Article 11(3)(i) – see codes I2-2, I2-3 and I2-4.
  - To allow flexibility in the reporting of the measures to address significant pressures, when
    combined with the optional mainPressureType attribute.
  - To maintain the previous KTM that do not fit the criteria above and were reported with high
    frequency in the 3rd cycle – see codes X01, X12, X14, X23 and X24.
  - Regarding the measures to address significant impacts in the status of water
    as per Article 11(3)(i) – see codes I2-2, I2-3 and I2-4.
    Note that only some of the impacts applicable to surface water are detailed.

* A mapping table ({numref}`Measures_MainKeyTypeOfMeasure_MappingTable`)
  if provided with the correspondence between the `mainKeyTypeOfMeasure` classes
  and the previous separate classification schemes used in the 3rd cycle.
  
* In the **3rd cycle**, the reporting guidance stated that
  "the name [of the measure] should reflect the pressure that is being tackled by the measure"
  {footcite}`WFD2022_ReportingGuidance` —
  meaning the pressure(s) should be described textually in the name of the measure.
  This recommendation was not consistently followed, and an analysis of the measure names across
  Europe does not yield useful results.

  It is easier to keep the *original name of the measure*,
  and to allow MS to optionally select the `mainPressureType` that the measure addresses,
  at the adequate level of detail (e.g. a generic measure may address `'P2'` (Diffuse sources), while
  a more targeted measure may address only `'P2‑5'` (Diffuse – Contaminated sites or abandoned
  industrial sites).

  The `mainPressureType` attribute allows more clarity and flexibility and can be applied to
  supplementary measures too.
  The `mainPressureType` attribute is optional, except for measures of type `'G'` and `'H'`.
  For measures of type G and H, the Commission requires additional information to differentiate
  measures addressing issues related to Urban Waste Water - `'P1‑1'` -
  from issues related to diffuse pollution from Agriculture - `'P2-2'`.

* *If needed and applicable*, a similar approach can be used for `mainSubstanceType`,
  allowing MS to identify measures targeting specific substances or groups of substances.

* The geographical scope of a measure is specified in the `geographicalCoverage` attribute:

  - use `geographicalCoverage = 'national'` for measures
    that target any water body affected by a given significant pressure or substance failing

  - use `geographicalCoverage = 'riverBasinDistrict'` for measures
    that target any water body affected by a given significant pressure or substance failing
    within the RBD indicated in the `euRBDCode` attribute value

  - if appropriate and necessary, it is possible to specify that a measure
    only applies to a specific category of water bodies,
    using the optional `waterCategory` attribute

  - if appropriate and necessary, it is possible to specify that a measure
    only applies to a specific type of WFD protected area,
    using the optional `protectedAreaType` attribute

  - the option `geographicalCoverage = 'waterBody'` should be reserved for measures
    that target specific water bodies (for example, one river, or a set of lakes)

  - the option `geographicalCoverage = 'protectedArea'` should be reserved for measures
    that target specific protected areas
    (for example, a set of bathing waters or a specific UWWTD sensitive area)

  - in the 2 previous cases, it is NOT requested to individually identify
    the water bodies or protected areas, respectively.

* The temporal scope of a measure is provided in the `implementationPeriod` value.

  - the range of years indicated in the `implementationPeriod` is used
    to check the reporting of information related to expenditures
    (e.g. if a measure is yet to start, then no past expenditures exist)

* The `implementationStatus` value allows the distinction between planned and ongoing measures.  
  It may also be used for measures planned for the 3rd cycle
  but already executed or cancelled by the end of 2027.

### ExpenditurePerMeasurePerSector table

{numref}`Measures_4thCycle_ExpenditurePerMeasurePerSector_ClassDiagram`
illustrates the `ExpenditurePerMeasurePerSector` table proposed for the 4th cycle.
The data is reported for each measure, *if it is available*: the `measureCode` identifier and the
`expenditureDataAvailable` attribute are the only mandatory attributes.

```{mermaid} /DataModelReview/mmd/Measures_4thCycle_ExpenditurePerMeasurePerSector_ClassDiagram.mmd
:name: Measures_4thCycle_ExpenditurePerMeasurePerSector_ClassDiagram
:caption: Expenditure per Measure per Sector table – 4th cycle of reporting
:align: center
```

The geographical scope of the measure is inherited from the parent record
in the `Measure` table and does not need to be reported again.
Likewise, the temporal scope is inherited from the parent records
and can be used to verify the reported data.

* An error should be raised when there is missing data for the 3rd cycle
  In pseudo-code (the && operator tests whether a range of values overlaps):

  ```{code-block} sql
  WHERE expenditureDataAvailable = 'Yes' 
  AND Measure.implementationStatus IN ('executed', 'ongoing','implemented') 
  AND Measure.implementationPeriod && '[2022,2027]' 
  AND totalCapitalExpenditure3rdCycle IS NULL 
  AND annualCurrentExpenditure3rdCycle IS NULL
  ```

* An error should be raised when there is missing data for the 4th cycle
  In pseudo-code (the && operator tests whether a range of values overlaps):

  ```{code-block} sql
  WHERE expenditureDataAvailable = 'Yes' 
  AND Measure.implementationStatus IN ('ongoing', 'implemented', 'planned') 
  AND Measure.implementationPeriod && '[2028,2033]' 
  AND totalCapitalExpenditure4thCycle IS NULL 
  AND annualCurrentExpenditure4thCycle IS NULL
  ```

The attribute `millionUnitsOfNationalCurrency` was introduced to facilitate reporting by MS
outside the Euro area, in alignment with common statistical practices.
It also facilitates human analysis, namely the cross‑checking against the RBMP documentation.

* Data must be reported in Millions of Euro for Euro Area Member States,
  and in Millions of National currency for non-Euro Area countries.
  The unit multiplier is set to 6 and it is applied to all the data, so it doesn't need to be specified.

* Non-Euro Area countries should use the relevant code for its national currency
  (e.g. CZK, DKK, HUF, PLN, RON, SEK) rather than common code for domestic currency (XDC).
  Euro Area countries must use EUR.

* Generally, the number of decimal digits is “0”.
  If a country wants to send a figure lower than 1 million, decimals may be used.
  In this case, the separator must be a dot (.).
  Example: if a country wants to report a value of 10 000 the figure 0.01 must be sent.
  If necessary the proposal can be modified to use a different multiplier (e.g. thousands).

A clear separation is made between **capital** expenditure vs. **current** expenditure and between
the 3rd cycle and the 4th cycle data. Only total values are requested.

The `institutionalSector` attribute identifies the institutional sector doing the outlay. This
aspect is explained below.

The European System of Accounts (ESA 2010) has a standard classification of institutional sectors
(see {numref}`Measures_ESA2010_Table`).
The topmost class (S.1 – Total Economy) encompasses all national institutional sectors; implicitly,
the 3rd cycle of WFD reporting used it.

```{include} /DataModelReview/tables/Measures_ESA2010_Table
```

The dichotomous key in {numref}`Measures_ESA2010_Allocation_of_institutional_units_to_sectors`
clarifies the allocation of units to sectors.

```{mermaid} /DataModelReview/mmd/Measures_ESA2010_Allocation_of_institutional_units_to_sectors.mmd
:name: Measures_ESA2010_Allocation_of_institutional_units_to_sectors
:align: center
:caption: European System of Accounts (ESA 2010) allocation of institutional units to sectors
```

The Environmental Protection Expenditures Accounts (EPEA) uses four groups of sectors {footcite}`eurostat2017epea`:

* S13 and S15 – General government and NPISH (Non-Profit Institutions Serving Households)
* S11 and S12 – Corporations
* S14 – Households
* S2 – Rest of the World

{numref}`Codelist_4thCycle_SEA2010SectorCode_Table` presents
a proposed list of institutional sectors that can be used in the 4th cycle of reporting.
The list should be revised and discussed with the CIS WG Economics.

It is also important to provide technical guidance and examples
on the proper reporting of expenditures.
For example, in the context of the EPEA,
research and development (R&D) expenditure is primarily classified as current expenditure,
while the National Accounts framework (ESA 2010) typically capitalizes R&D as an investment.

```{include} /DataModelReview/tables/Codelist_4thCycle_SEA2010SectorCode_Table
```

It is also important to address the reporting of transfers of EU Funds.

If `institutionalSector = 'S.212'` then the value
represents a transfer of EU funds into the national economy.
Depending on the purpose, it can be a capital transfer (e.g. to build a new UWWT plant),
or a current transfer (e.g. a CAP subsidy to pay farmers to reduce or eliminate pesticides).
It is not necessary to identify which sector receives the transfer.

A numerical example can be used to illustrate the proposed approach.

A new Urban Waste Water Treatment Plant required a total capital expenditure of 10M€.

* Scenario 1 : the General Government (S.13) built the plant using national funds.
* Scenario 2 : a public utility company (S.11001) built the plant,
  using 10M€ of national funds transferred by the government.
* Scenario 3 : the government built the plant
  using 8M€ of national funds and 2M€ from the EU Cohesion Fund.
* Scenario 4 : a public utility company (S.11001) built the plant,
  using 8M€ of national funds transferred by the General Government (S.13) to the company
  and 2M€ of EU funds transferred to the company via the national government.
* Scenario 5 : a public utility company (S.11001) built the plant,
  using 5M€ of their own funds,
  4M€ of national funds transferred by the General Government (S.13) to the company
  and 1M€ of EU funds transferred to the company via the national government.

{numref}`Measures_ReportingExpenditurePerSector_Example` illustrates
the reporting of the different scenarios.

Note that scenario 1 and scenario 2 are identical from a reporting point‑of‑view.  
Likewise, scenario 3 and scenario 4 are identical.

```{table} Illustrative example with the reporting of expenditure per sector.
:name: Measures_ReportingExpenditurePerSector_Example
:widths: 10 70 20
:width: 100%
| Scenario | Institutional Sector | Total Capital Expenditure |
| --- | --- | --- |
| 1 | S.13 – General Government | 10 M€ |
| 2 | S.13 – General Government | 10 M€ |
| 3 | S.13 – General Government | 8 M€ |
| 3 | S.212 – Institutions and bodies of the European Union | 2 M€ |
| 4 | S.13 – General Government | 8 M€ |
| 4 | S.212 – Institutions and bodies of the European Union | 2 M€ |
| 5 | S.11001 – Public non-financial corporations | 5 M€ |
| 5 | S.13 – General Government | 4 M€ |
| 5 | S.212 – Institutions and bodies of the European Union | 1 M€ |
```

The Commission will provide guidance on the reporting of
expenditure for which may be outside the scope of the EPEA.

* Measures to promote efficient and sustainable water use:
  `mainKeyTypeOfMeasure = 'C'`
* Measure to control abstraction from surface and groundwater,
  and impoundment of surface water: `mainKeyTypeOfMeasure = 'E'`

(heading_wfd_measures_documents_dataset_4th_cycle)=
## Documents dataset - 4th cycle

The Documents dataset follows the standard structure used in various WISE dataflows
({numref}`Measures_4thCycle_Documents_ClassDiagram`):

* The `dcMetadata` table provides the basic Dublin Core metadata elements about the delivery.
  
  - If required by the data providers,
    the `licenseDocument` attribute allows the provision
    of additional information about the dataset.
  - The `dcMetadata` table also functions as a "manifest file"
    explaining if the delivery contains data for a given river basin district or not.

* The `Document` table allows the upload of documents (for example, PDFs)
  or the provision of a `hyperlink` to a document stored in a publicly accessible national web site.

* The `Reference` table is also standard in the WISE dataflows:
  the `bookmark` it allows the identification of the chapter(s), sections(s) or page range(s)
  where the relevant information about a `subject`
  can be found within a document.

```{mermaid} /DataModelReview/mmd/Measures_4thCycle_Documents_ClassDiagram.mmd
:name: Measures_4thCycle_Documents_ClassDiagram
:caption: Programmes of measures dataflow - 4th cycle - Documents
:align: center
```

The following criteria apply:

01. The `dcMetadata` table must contain *one and only one* record
    for each of the country's river basin districts, identified by the `euRBDCode`.

02. The descriptive dataset tables are **national**,
    but the quality control will allow deliveries
    where some, or all, the river basin districts have `includesDescriptiveData = no`.

## Codelists - 4th cycle

* For the `SubPlansCoverage` codelist, see {numref}`Measures_4thCycle_RiverBasinManagementPlan_ClassDiagram`.
* For the `OngoingStakeholderInvolvement` codelist, see {numref}`Measures_4thCycle_RiverBasinManagementPlan_ClassDiagram`.
* For the `Coordination` codelist, see {numref}`Measures_4thCycle_RiverBasinManagementPlan_ClassDiagram`.
* For the `InternationalCoordination` codelist, see {numref}`Measures_4thCycle_RiverBasinManagementPlan_ClassDiagram`.
* For the `StakeholderGroups` codelist, see {numref}`Measures_4thCycle_RiverBasinManagementPlan_ClassDiagram`.

* For the `PlannedOngoingExecutedCancelled` codelist, see {numref}`Measures_4thCycle_Progress_ClassDiagram`.

* For the `MeasuresChanges` codelist, see {numref}`Measures_4thCycle_TargetedQuestions_ClassDiagram`.
* For the `MeasureScope` codelist, see {numref}`Measures_4thCycle_TargetedQuestions_ClassDiagram`.
* For the `BasicMeasuresArt113eThreshold` codelist, see {numref}`Measures_4thCycle_TargetedQuestions_ClassDiagram`.
* For the `BasicMeasuresArt113eImpoundment` codelist, see {numref}`Measures_4thCycle_TargetedQuestions_ClassDiagram`.
* For the `BasicMeasuresArt113gThreshold` codelist, see {numref}`Measures_4thCycle_TargetedQuestions_ClassDiagram`.
* For the `BasicMeasuresArt113hRules` codelist, see {numref}`Measures_4thCycle_TargetedQuestions_ClassDiagram`.
* For the `BasicMeasuresArt113j` codelist, see {numref}`Measures_4thCycle_TargetedQuestions_ClassDiagram`.
* For the `EcologicalFlow` codelist, see {numref}`Measures_4thCycle_TargetedQuestions_ClassDiagram`.

* For the `MeasureType` codelist, see {numref}`Measures_4thCycle_Measure_ClassDiagram`.
* For the `LegalInstrument` codelist, see {numref}`Measures_4thCycle_Measure_ClassDiagram`.
* For the `WFDGeographicCoverage` codelist, see {numref}`Measures_4thCycle_Measure_ClassDiagram`.

* For the `MeasureType` codelist, see {numref}`Measures_4thCycle_Measure_ClassDiagram`.
  
  - See the definitions in {numref}`Codelist_4thCycle_MeasureType_Table`.

* For the `LegalInstrument` codelist, see {numref}`Measures_4thCycle_Measure_ClassDiagram`.
  
  - See the definitions in {numref}`Codelist_4thCycle_LegalInstrument_Table`.

* For the `MainKeyTypeOfMeasure` codelist, see {numref}`Measures_4thCycle_Measure_ClassDiagram`.
  
  - See the definitions in {numref}`Codelist_4thCycle_MainKeyTypeOfMeasure_Table`.
  - See the mapping table between the 3rd and 4th cycle classifications in {numref}`Measures_MainKeyTypeOfMeasure_MappingTable`.

* For the `PressureType` codelist,
  see {numref}`Codelist_4thCycle_PressureType_ClassDiagram` in
  the section {ref}`heading_wfd_pressure_type_codelist_4th_cycle`.

  - See the mapping table between the 3rd and 4th cycle classifications in {numref}`PressuresType_3rdCycle_4thCycle_MappingTable`.

* For the `ProtectedAreaType` codelist, see {numref}`Measures_4thCycle_Measure_ClassDiagram`.

* For the `SEA2010SectorCode` codelist, see {numref}`Measures_4thCycle_ExpenditurePerMeasurePerSector_ClassDiagram`.

  - See the definitions in {numref}`Codelist_4thCycle_SEA2010SectorCode_Table`.

* For the `CurrencyCode` codelist, see {numref}`Measures_4thCycle_ExpenditurePerMeasurePerSector_ClassDiagram`.

```{include} tables/Codelist_4thCycle_MeasureType_Table
```

```{include} tables/Codelist_4thCycle_LegalInstrument_Table
```

```{include} tables/Codelist_4thCycle_MainKeyTypeOfMeasure_Table
```

```{include} tables/Measures_MainKeyTypeOfMeasure_MappingTable
```

## Annexes

### Classification of environmental protection activities

*Note*:  
The classification of environmental protection activities (CEPA 2000)
{footcite}`eurostat2017epea`
is not relevant for the reporting process,
it is only relevant for the analysis of reported data.

```{dropdown} Click to show the CEPA 2000 table
```{include} tables/Measures_SubsetOfCEPAClasses_ListTable
```

### Mapping between mainKeyTypeOfMeasure and CEPA 2000

The EPEA categorises activities using the CEPA 2000,
the Classification of Environmental Protection Activities ({numref}`Measures_SubsetOfCEPAClasses_ListTable`).

The proposed classification of Measures using the `mainKeyTypeOfMeasure` value
({numref}`Codelist_4thCycle_MainKeyTypeOfMeasure_Table`)
is not based on the CEPA 2000 classification.

Note also that CEPA strictly covers Environmental Protection (preventing pollution and degradation)
and excludes Resource Management (saving water or energy),
which falls under CReMA, the Classification of Resource Management Activities {footcite}`eurostat2020cepa_crema`.

Nevertheless, it seems to be possible to map most of the `mainKeyTypeOfMeasure` classes
to a primary CEPA 2000 class ({numref}`Measures_MainKeyTypeOfMeasure_CEPA2000_ListTable`).

The mapping and post-classification can be done by the Commission,
using the reported data per Measure,
to analyse and aggregate the data according CEPA classes, if that is required.

```{dropdown} Click to show the mapping table
```{include} tables/Measures_MainKeyTypeOfMeasure_CEPA2000_ListTable
```

(heading_wfd_measures_references)=
## References

```{footbibliography}
```

```{warning}
The original document containing this revised model
can still be downloaded but should no longer be used.
See **PROPOSAL - Version 2026.02.17** {download}`PDF <pdf/WFD_4th_cycle_Measures_v20260217.pdf>`
```
