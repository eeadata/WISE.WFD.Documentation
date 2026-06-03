(heading_wfd_measures)=
# WFD measures

Last update: 2026-06-02

```{warning}
The online version of the text is being reviewed.  
See **PROPOSAL - Version 2026.02.17** {download}`PDF <pdf/WFD_4th_cycle_Measures_v20260217.pdf>`
```

## Purpose and overview

This section revises the **River Basin Management Plan & Programme of Measures** schema used in the 3ʳᵈ cycle of reporting of the Water Framework Directive River Basin Management Plans. 
It also presents a proposal for simplifying the electronic reporting in the 4ᵗʰ cycle.

Not all information in the RBMPs can be accurately provided using a common European model. However, it is possible to improve and simplify the reporting of structured data, accepting that part of the relevant information will remain in documentation to be analysed during the Commission's implementation assessment.

Using this principle, the data model can focus on aspects that are suitable for structured reporting, allowing adequate comparisons between different river basin districts (RBDs). Specific or more detailed information can be kept in the RBMP documents, the analysis of which can in the future be facilitated using, for example, large language models (LLMs) supported by retrieval‑augmented generation (RAG) techniques.

## Current structure - 3ʳᵈ cycle

The schema used in the 3ʳᵈ cycle of reporting contained 3 main groups ({numref}`ProgrammeOfMeasures_3rdCycle`):

1. Summary information about the *River Basin Management Plan*, the Progress since the previous River Basin Management Plan, 
 and the mechanisms of international Coordination (if applicable).
2. Information about the *Programme of Measures*, comprising a summary questionnaire of Targeted Questions and aggregated data about the overall Cost of measures. 
 Disaggregated information was requested about each Measure and its classification into key type of measures (*KTM*) and basic type of measures (if applicable).
3. Summary information about pressures and substances causing failure was also requested, along with their link to *KTM Indicators* and *Indicator Gaps*.

```{figure} img/Measures_RBMPPoM_2022_ClassDiagram.png
:name: ProgrammeOfMeasures_3rdCycle
:align: center
:width: 100%

River Basin Management Plan & Programme of Measures - 3ʳᵈ cycle - OBSOLETE
```

## Proposed structure - 4ᵗʰ cycle

1. The RBMP and Coordination tables are simplified to a single **RiverBasinManagementPlan** table, containing a selected subset of attributes. 
 The **Progress** table is modified to request only aggregated information about the overall status of the measures of the previous cycle (3ʳᵈ cycle).
2. The reporting of the Programme of Measures is also simplified. 
 The **TargetedQuestions** table, containing the questionnaire at RBD level, is simplified. 
 Information about measures is requested in a single **Measure** table. 
 Information about the planned **ExpenditurePerMeasure** is reported in a separate table, if data is available.
3. The KTM indicators and indicator gaps group is completely removed.


## River basin management plan, coordination and progress - 3ʳᵈ cycle

In the 3ʳᵈ cycle of reporting, this group comprised three tables, collecting summary information about the RBMP, the progress since the previous RBMP, and the mechanisms of international coordination, if applicable ({numref}`ProgrammeOfMeasuresPartial_3rdCycle`).

The data is structured as a simple questionnaire, mostly with Yes/No or multiple‑choice answers, accompanied by links to additional documentation (which can be uploaded or kept on national websites). Only one record per table is required for each River Basin District.

Reporting by MS should not present technical difficulties, and there is limited scope for technical simplification. Nevertheless, the Commission has reviewed whether the requested data is strictly required and proposes the simplification detailed in the next sections.

```{figure} img/RBDCA_RBDSUCA_2022_Partial_ClassDiagram.png
:name: ProgrammeOfMeasuresPartial_3rdCycle
:align: center
:width: 100%

River Basin Management Plan, international Coordination and Progress since the previous cycle - 3ʳᵈ cycle - OBSOLETE
```

## RiverBasinManagementPlan – 4ᵗʰ cycle

The simplified **RiverBasinManagementPlan** table contains a subset of the data previously requested in the RBMP and Coordination classes in the 3ʳᵈ cycle ({numref}`Measures_4thCycle_RiverBasinManagementPlan_ClassDiagram`):

* A new attribute, **coordinationNRRReference**, allows the reporting of information related to coordination with the Nature Restoration Regulation.

* The reporting of the **pomCoordinationArt5SWMI**, **pomCoordinationIRBMPPoM**, **pomCoordinationRoofReport** and **pomCoordinationFinancial** attributes 
 is only required for international RBDs. 

```{mermaid} /DataModelReview/mmd/Measures_4thCycle_RiverBasinManagementPlan_ClassDiagram.mmd
:name: Measures_4thCycle_RiverBasinManagementPlan_ClassDiagram
:caption: River Basin Management Plan table – 4ᵗʰ cycle of reporting
:align: center
```

## Progress table – 4ᵗʰ cycle

The **Progress** table is modified to provide an overview of the proportion of the measures of the 3ʳᵈ RBMPs that were executed, cancelled, or otherwise affected, 
as well as the obstacles encountered during the implementation of the 3ʳᵈ RBMP Programme of Measures ({numref}`Measures_4thCycle_Progress_ClassDiagram`).

The only constraint is that, for each RBD, the sum of the values in **percentageInStatus** must be **100**. 
The level of detail can be adapted depending on the needs and the data available at national level.

```{mermaid} /DataModelReview/mmd/Measures_4thCycle_Progress_ClassDiagram.mmd
:name: Measures_4thCycle_Progress_ClassDiagram
:caption: Progress table – 4ᵗʰ cycle of reporting
:align: center
```

A numerical example illustrates per proposed approach. 
Consider a hypothetical 3ʳᵈ RBMP Programme of Measures with 10 different measures, 
which are in different statuses and may have faced different obstacles ({numref}`measures_example_ten_measures`). 

```{table} Illustrative example - hypothetical list with the status of the 10 measures of the 3ʳᵈ cycle.
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

The example in {numref}`measures_example_progress` illustrates how to synthesize the information in the Progress table. 

```{table} Illustrative example - **Progress** table records for the example in the previous table.
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

## TargetedQuestions table – 4ᵗʰ cycle

The **TargetedQuestions** table collects summary information about the measures in the RBMP, and the progress since the previous cycle. 
For each RBMP, only one record is required. The data is structured as a simple questionnaire, with Yes/No or multiple-choice answers. 

Reporting by MS should not present technical difficulties, and there is limited scope for any technical simplification. 
The Commission has revised and simplified the **TargetedQuestions** table, keeping a subset of the questions requested in the previous cycle ({numref}`Measures_4thCycle_TargetedQuestions_ClassDiagram`).

```{mermaid} /DataModelReview/mmd/Measures_4thCycle_TargetedQuestions_ClassDiagram.mmd
:name: Measures_4thCycle_TargetedQuestions_ClassDiagram
:caption: TargetedQuestions table – 4ᵗʰ cycle of reporting
:align: center
```

## Measure table – 4ᵗʰ cycle 

The simplified Measure table proposed for the 4ᵗʰ cycle is illustrated in ({numref}`Measures_4thCycle_Measure_ClassDiagram`). 

For each measure:

* Use a unique persistent European identifier for each **measureCode**.
* Use the original **measureName** (or an English translation thereof).
* If needed, provide a link to documentation (**measureReference**).
* Identify the primary **measureLegalInstrument**, using a single codelist value.
* Identify the **measureType**, using a single codelist value.
* Classify the measure using a single **mainKeyTypeOfMeasure** codelist value from a simplified classification. The closest match should be selected.
* Optionally or if applicable, identify the main pressure or pressure group addressed by the measure using the **measurePressureType** attribute, 
 at the level of detail deemed more adequate. The closest match should be selected.
* Optionally or if applicable, identify the main substance or group of substances addressed by the measure using the **measureSubstanceType** attribute, 
 at the level of detail deemed more adequate.
* Flag the sectoral plans for which the measure might be relevant 
 using the **msfdRelevance**, **floodsRelevance**, **natureRestorationRegulationRelevance**, **draughtManagementPlanRelevance** and **climateAdaptationPlanRelevance** attributes.
* Specify the **geographicalCoverage** and **temporalCoverage** of the measure.

```{mermaid} /DataModelReview/mmd/Measures_4thCycle_Measure_ClassDiagram.mmd
:name: Measures_4thCycle_Measure_ClassDiagram
:caption: Measure table – 4ᵗʰ cycle of reporting
:align: center
```
### Measure table – 4ᵗʰ cycle - measureCode, measureName and measureReference

Each different measure must have a persistent unique identifier at national level and European level (**measureCode**), a descriptive name (**measureName**), and zero or more links to documentation (**measureReference**).  

### Measure table – 4ᵗʰ cycle - measureType

The **measureType** typology is described in {numref}`measures_measureType_definitions`. 

```{include} tables/Measures_MeasureType_ListTable
```

### Measure table – 4ᵗʰ cycle - measureLegalInstrument

The primary **measureLegalInstrument** under which the measure was defined must be clearly identified.  
This avoids double reporting in other Directives: the measures can be reported only once under the RBMP electronic reporting. 
An updated list of EU water and other environmental legislation is provided ({numref}`measureLegalInstrument_definitions`).

The scope of some basic measures is clearly linked to the two Daughter directives:

- Measures to prohibit direct discharges to groundwater: *Groundwater Directive*
- Measures to eliminate or reduce pollution by Priority Substances: *Environmental Quality Standards Directive*

These two legal instruments are part of the codelist. 
The option 'Other' (Other Directives mentioned in Part A of Annex VI of the WFD), that existed in the 3ʳᵈ cycle, 
is now eliminated because it did not convey relevant information.

```{include} tables/Measures_MeasureLegalInstrument_ListTable
```

### Measure table – 4ᵗʰ cycle - mainKeyTypeOfMeasure

The **mainKeyTypeOfMeasure** attribute contains the classification to be used for both basic and supplementary measures (see {numref}`measures_mainKeyTypeOfMeasure_definitions`).  
It simplifies, consolidates and replaces both the basicMeasureType and the keyTypeOfMeasure classifications used in the 2ⁿᵈ and 3ʳᵈ cycles. 


```{include} tables/Measures_MainKeyTypeOfMeasure_ListTable
```

### Measure table – 4ᵗʰ cycle - mainPressureType and mainSubstanceType

In the **3ʳᵈ cycle**, the reporting guidance stated that *“the name should reflect the pressure that is being tackled by the measure”* 
— meaning the pressure(s) should be described textually in the name of the measure. 
This recommendation was not consistently followed, and an analysis of the measure names across Europe does not yield useful results.

It is easier to keep the *original name of the measure*, and to allow MS to optionally select the **mainPressureType** that the measure addresses,
at the adequate level of detail (e.g. a generic measure may address **P2 – Diffuse sources**, while a more targeted measure may address only **P2‑5 – Diffuse – Contaminated sites or abandoned industrial sites**).

The **mainPressureType** attribute allows more clarity and flexibility and can be applied to supplementary measures too. 
The **mainPressureType** attribute is optional, except for measures of type **G** and **H**. 
For measures of type G and H, the Commission requires additional information to differentiate measures addressing issues related to Urban Waste Water (**P1‑1**) and diffuse pollution from Agriculture (**P2‑2**).

*If needed and applicable*, a similar approach can be used for **mainSubstanceType**, allowing MS to identify measures targeting specific substances or groups of substances.

### Measure table – 4ᵗʰ cycle - geographicalCoverage

The geographical scope of a measure is specified in the **geographicalCoverage** attribute, by selecting the most appropriate option: {'national' | 'riverBasinDistrict' | 'waterBody' |
'protectedArea'}

The option **geographicalCoverage = 'national'** should be used for measures that target any waterbody affected by a given significant pressure or substance failing. 
Similarly, the option **geographicalCoverage = 'riverBasinDistrict'** should be used for measures that target any waterbody affected by a given significant pressure or substance failing within the RBDs indicated in the **euRBDCode** attribute.
  
If appropriate and necessary, it is possible to specify that a measure only applies to a specific category of waterbodies, using the optional **waterCategory** attribute.

If appropriate and necessary, it is possible to specify that a measure only applies to a specific type of WFD protected area, using the optional **protectedAreaType** attribute.

The option **geographicalCoverage = 'waterBody'** should be reserved for measures that target specific water bodies (for example, a given river, or a set of lakes). 
The option **geographicalCoverage = 'protectedArea'** should be reserved for measures that target specific protected areas (for example, a set of bathing waters or a specific UWWTD sensitive area). 
In these cases, it is not requested to individually identify the waterbodies or protected areas.

### Measure table – 4ᵗʰ cycle - implementationPeriod and implementationStatus

The temporal scope of a measure is provided in the **implementationPeriod** – the range of years indicated is used to check the reporting of information related to expenditures (e.g. if a measure is yet to start, then no past expenditures exist). 
The **implementationStatus** attribute allows the distinction between planned and ongoing measures – and may also be used for measures planned for the 3ʳᵈ cycle but already executed or cancelled by the end of 2027.

## Economic data in the programme of measures

The revision of the electronic reporting focuses on the main issues described in the Note to the CIS Working Group Economics ([^1]) quoted below:

[^1]: P. Arnoldus, “Workstream 1: proposing a simplification and standardisation of the economic data reporting,” note to the CIS Working 
Group Economics, 15 December 2025,[Available](https://circabc.europa.eu/ui/group/9ab5926d-bed4-4322-9aa7-9964bbe8312d/library/2eef1f5c-5df6-41e2-93e8-c0f427d80eb1/details) in Circabc 

“[…] Both the Commission’s 6ᵗʰ and 7ᵗʰ WFD Implementation Reports indicate persistent problems in the (electronic) reporting on the investments and the costs of other measures in the Programme of Measures (PoM).

The 6ᵗʰ WFD Implementation Report notes that the Member States’ reporting on costs and financing of the PoMs appears overall patchy and that a consultant’s study estimate is an underestimation for the total costs, as there are significant data gaps and it excludes operational and infrastructure maintenance costs. The corresponding investment overview table shows indeed large gaps ([^2]) .

[^2]: 6th WFD Implementation Report,[ COM(2021) 970](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:52021DC0970),p15. The table concerns {numref}`measures_temporalcoverage`, p24, of [SWD(2021) 970](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:52021SC0970) – note that the differentiation is based.

The Commission’s evaluation of the 3ʳᵈ River Basin Management Plans ([^3]), as part of the 7ᵗʰ WFD Implementation Report, notes that the “third PoMs presented in the (…) RBMPs show that Member States continue to have different approaches to their design and reporting” and that “the costs and the financing of the planned measures are often missing.” Hence, the Commission recommends that “in order to effectively implement the PoMs to develop long‑term investment plans and clearly identifying the source of financing for each measure.” A good planning is also necessary for the acquisition of support from EU Funds, the EIB and other promotional banks.

[^3]: Quotes are from 7th WFD Implementation Report,[ COM(2025) 2](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:52025DC0002)(p15, p36) 

*The challenge is thus to improve the reporting of the costs of the PoM measures, including the investment amounts*, and to specify the funding of these investments and other measures. This requires a clear distinction between capital costs (CAPEX) and operational costs (OPEX). […]

The proposal here is to agree on a clear conceptual basis for the PoM costs.

It is natural to consider the PoM as a **budget of government outlays** – however, there can be costs on other economic agents without government payment involved (cf. banning an activity).

The budget orientation would imply to look at foreseen **spending amounts**. This has three
consequences:

- ‘Welfare costs’ should not be included in the reporting. However, they can be taken up as “negative benefits” in the **CEA (cost‑effectiveness analysis)**. 
- The reporting is on investment spending (purchases / commitments) and not on capital costs (depreciation). 
- To make the link with financial support from EU Funds, EIB and other promotional banks, one needs to distinguish OPEX and CAPEX when reporting investment cost.

There is a readily available conceptual basis for the reporting on the PoM investment and other costs, with which the Member States are already familiar, namely the **environmental protection expenditures**. They are namely required to collect and report this data annually to Eurostat ([^4]), who publishes the **Environmental Protection Expenditures Accounts (EPEA)** as one of the environmental‑economic satellite accounts to the economic National Accounts.The EPEA are based on a clear, publicly available protocol (following UN statistical standards), defining the environmental domains, spending economic sectors, and expenditure types. The latter includes the distinction between **capital** and **current** expenditures. Hence, it meets the features described in the three bullets points above.


[^4]: An obligation under Regulation (EU) No 691/2011, amended by Commission Delegated Regulation (EU) 2022/125; the consolidated 
version can be found [here](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A02011R0691-20250624)


A brief review of the reported data confirms the issues mentioned above.

In the **3ʳᵈ cycle** of reporting, the overall cost of the PoM was reported in the **Costs** class ({numref}`Measure_RBMPPoM_2022 schema_Costs_3rdCycle`). Reporting of costs was, de facto, optional – since all numerical attributes admitted the option **–9999** to denote “data not available”.

 Out of the 146 RBD reported by EU Member States, 24 do not have data on investments, 54 do not have data on operational costs and 64 do not have data on EU funds. 





```{mermaid} /DataModelReview/mmd/MeasuresCosts.mmd
:name: Measure_RBMPPoM_2022 schema_Costs_3rdCycle
:align: center
:caption: Class diagram for the RBMPPoM_2022 schema: Costs – 3ʳᵈ cycle of reporting.
```


The variability of the geographical and temporal coverage of the reported data adds to the difficulty in achieving a meaningful analysis.{numref}`measures_temporalcoverage` illustrates the issues regarding temporal coverage. {numref}`measures_geographiccoverage` illustrates the issue with geographical coverage.



```{table} Temporal coverage: period to which the reported costs refer – 3ʳᵈ RBMP electronic reporting (including Norway).
:name: measures_temporalcoverage
:width: 100%
| costOfMeasurePeriod20152021 | costOfMeasurePeriod20212027 | Number of RBDs |
|------------------------------|------------------------------|----------------|
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

```{table} Geographic coverage: scale to which the reported costs refer – 3ʳᵈ RBMP electronic reporting (including Norway).
:name: measures_geographiccoverage
:width: 100%
| costOfMeasuresScale20152021 | costOfMeasuresScale20212027 | Number of RBDs |
|------------------------------|------------------------------|----------------|
| National | National | 48 |
| River Basin District | River Basin District | 103 |
| National | River Basin District | 4 |
| River Basin District | National | 7 |
```


### ExpenditurePerMeasurePerSector table – 4ᵗʰ cycle

Figure 12 illustrates the ExpenditurePerMeasurePerSector table proposed for the 4ᵗʰ cycle.

The data is reported for each measure, *if it is available*: the **measureCode** identifier and the **expenditureDataAvailable** attribute are the only mandatory attributes.

The geographical scope of the measure is inherited from the parent record in the **Measure** table and does not need to be reported again. Likewise, the temporal scope is inherited from the parent records and can be used to verify the reported data ([^5]).

[^5]: An error should be raised when there is missing data. In pseudo-code (the && operators tests whether a range of values overlaps):<br>a) IF expenditureDataAvailable = 'Yes' AND Measure.implementationPeriod && '[2022,2027]' AND Measure.implementationStatus IN ('executed', 'ongoing', 'implemented') AND totalCapitalExpenditure3rdCycle IS NULL AND annualCurrentExpenditure3rdCycle IS NULL. <br>b) IF expenditureDataAvailable = 'Yes' AND Measure.implementationPeriod && '[2028,2033]' AND Measure.implementationStatus IN ('ongoing', 'implemented', 'planned') AND totalCapitalExpenditure4thCycle IS NULL AND annualCurrentExpenditure4thCycle IS NULL. 

The attribute **millionUnitsOfNationalCurrency** was introduced to facilitate reporting by MS outside the Euro area, in alignment with common statistical practices ([^6]). It also facilitates human analysis, namely the cross‑checking against the RBMP documentation.

[^6]: Data must be reported in Millions of Euro for Euro Area Member States, and in Millions of National currency for non-Euro Area countries. (The unit multiplier is set to 6 and it is applied to all the data, so it doesn't need to be specified.) Non-Euro Area countries 
hould use the relevant code for its national currency (e.g. BGN, CZK, DKK, HRK, HUF, PLN, RON, SEK) rather than common code for domestic currency (XDC). Euro Area countries must use EUR. Generally, the number of decimal digits is “0”. If a country wants to send a figure lower than 1 million, decimals may be used. In this case, the separator must be a dot (.). (Example: if a country wants to report a value of 10 000 the figure 0.01 must be sent). If necessary the proposal can be modified to use a different multiplier (e.g. thousands). 


```{mermaid} /DataModelReview/mmd/Measures_4thCycle_ExpenditurePerMeasurePerSector_ClassDiagram.mmd
:name: Measures_4thCycle_ExpenditurePerMeasurePerSector_ClassDiagram
:caption: Expenditure per Measure per Sector table – 4ᵗʰ cycle of reporting
:align: center
```


A clear separation is made between **capital** expenditure vs. **current** expenditure and between the 3ʳᵈ cycle and the 4ᵗʰ cycle data. Only total values are requested.

The **institutionalSector** attribute identifies the institutional sector doing the outlay. This aspect is explained below.

The European System of Accounts (ESA 2010) has a standard classification of institutional sectors (see {numref}`measures_ESA2010`). 
The topmost class (S.1 – Total Economy) encompasses all national institutional sectors; implicitly, the 3ʳᵈ cycle of WFD reporting used it. 
The dichotomous key in Figure 13 clarifies the allocation of units to sectors.

The Environmental Protection Expenditures Accounts (EPEA) uses four groups of sectors ([^7]):

[^7]: See e.g. the Environmental protection expenditure accounts Handbook , 2017 edition [https://ec.europa.eu/eurostat/documents/3859598/7903714/KS-GQ-17-004-EN-N.pdf/7ea9c74b-eda4-4c23-b7bd-897358bfc990?t=1489135578000](https://ec.europa.eu/eurostat/documents/3859598/7903714/KS-GQ-17-004-EN-N.pdf/7ea9c74b-eda4-4c23-b7bd-897358bfc990?t=1489135578000)
- S13 and S15 – General government and **NPISH** 
- S11 and S12 – Corporations
- S14 – Households
- S2 – Rest of the World

```{table} European System of Accounts (ESA 2010) sectors.
:name: measures_ESA2010
:width: 100%
| ESA Sector | Definition |
|------------|------------|
| S.1 | Total economy |
| S.11 | Non-financial corporations (e.g., waste companies, manufacturers). |
| S.11001 | Public non-financial corporations. All non-financial corporations, quasi-corporations and non-profit institutions, recognised as independent legal entities, that are market producers and are subject to control by government units. |
| S.11002 | National private non-financial corporations. |
| S.11003 | Foreign controlled non-financial corporations. |
| S.12 | Financial corporations (rarely main EPEA actors, but valid). |
| S.13 | General government. Central, state, and local government units (e.g., municipalities, ministries). |
| S.14 | Households. Private individuals acting as consumers. |
| S.15 | NPISH. Non-profit institutions serving households (e.g., environmental charities). |
| S.2 | Rest of the world. Used for reporting transfers (subsidies/grants) paid to or received from abroad. |
| S.21 | Member states and institutions and bodies of the European Union. |
| S.212 | Institutions and bodies of the European Union (e.g., European Central Bank, European Commission). |
| S.22 | Non-member countries and international organisations non-resident in the European Union. |
```



**Figure 13.** *European System of Accounts (ESA 2010) allocation of institutional units to sectors.*

```{mermaid} /DataModelReview/mmd/MeasuresUnitResidentflowchart.mmd
:align: center
```


{numref}`measures_institutionalsectors` presents a proposed list of institutional sectors that can be used in the **4ᵗʰ cycle** of reporting. The list should be revised and discussed with the CIS WG Economics.

It is also important to provide technical guidance and examples on the proper reporting of expenditures. For example, in the context of the EPEA, research and development (R&D) expenditure is primarily classified as current expenditure, while the National Accounts framework (ESA 2010) typically capitalizes R&D as an investment.

```{table} Proposed list of institutional sectors – 4ᵗʰ cycle.
:name: measures_institutionalsectors
:width: 100%
| ESA Sector* | Definition and comments |
|------------------|--------------------------|
| S.1 | Total economy. Allows the provision of aggregated data. |
| S.13 | General government. The "default" option, if the RBMPs only include government outlays. |
| S.13_S.15 | General government + NPISH. Aligned with EPEA, can be used if preferred. |
| S.11_S.12 | Corporations. Aligned with EPEA, can be used if preferred. |
| S.11 | Non-financial corporations. Can be used if the distinction of outlays by public and private companies is not relevant. |
| S.11001 | Public non-financial corporations. Can be used if the distinction of outlays by public and private companies is relevant. |
| S.11002_S.11003 | Private non-financial corporations. Can be used if the distinction of outlays by public and private companies is relevant. |
| S.212 | Institutions and bodies of the European Union (e.g. European Central Bank, European Commission). |
```
\* *The underscore '_' denotes a list of code values (Code1_Code2). The hyphen '-' denotes a range of code values (StartCode-EndCode)*


It is also important to address the reporting of transfers of EU Funds.

If institutionalSector = 'S.212' then the value represents a transfer of EU funds into the national economy. Depending on the purpose, it can be a capital transfer (e.g. to build a new UWWT plant), or a current transfer (e.g. a CAP subsidy to pay farmers to reduce or eliminate pesticides). It is not necessary to identify which sector receives the transfer.

A numerical example can be used to illustrate the proposed approach.

A new Urban Waste Water Treatment Plant required a total capital expenditure of 10M€.

* Scenario 1 : the General Government (S.13) built the plant using national funds. 
* Scenario 2 : a public utility company (S.11001) built the plant, using 10M€ of national funds transferred by the government. 
* Scenario 3 : the government built the plant using 8M€ of national funds and 2M€ from the EU Cohesion Fund. 
* Scenario 4 : a public utility company (S.11001) built the plant, using 8M€ of national funds transferred by the General Government (S.13) to the company and 2M€ of EU funds transferred to the company via the national government. 
* Scenario 5 : a public utility company (S.11001) built the plant, using 5M€ of their own funds, 4M€ of national funds transferred by the General Government (S.13) to the company and 1M€ of EU funds transferred to the company via the national government.

{numref}`measures_reportingSectorExample` illustrates the reporting of the different scenarios.

Note that scenario 1 and scenario 2 are identical from a reporting point‑of‑view.  
Likewise, scenario 3 and scenario 4 are identical.

```{table} Illustrative example with the reporting of expenditure per sector.
:name: measures_reportingSectorExample
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


The Commission must provide guidance on the reporting of expenditure for measures where 
mainKeyTypeOfMeasure IN ('C - Measure to promote efficient and sustainable water use', 'E - Measure to control abstraction from surface and groundwater, and impoundment of surface 
water') which may be outside the scope of the EPEA.

**Alignment with the Classification of environmental protection activities**

The EPEA categorises activities using the Classification of environmental protection activities (CEPA 2000, {numref}`measures_SubsetOfCEPAClasses`). 
The proposed classification of Measures using the mainKeyTypeOfMeasure value ({numref}`measures_mainKeyTypeOfMeasure_definitions`) is not based on the CEPA 2000 classification.

Note also that CEPA strictly covers Environmental Protection (preventing pollution and degradation) and excludes Resource Management (saving water or energy), which falls under CReMA([^8]) (Classification of Resource Management Activities).

[^8]: [https://ec.europa.eu/eurostat/documents/1798247/12177560/CEPA+and+CReMA+explanatory+notes++technical+note.pdf/b3517fb9-1cb3-7cd9-85bd-4e3a3807e28a?t=1609863934103](https://ec.europa.eu/eurostat/documents/1798247/12177560/CEPA+and+CReMA+explanatory+notes++technical+note.pdf/b3517fb9-1cb3-7cd9-85bd-4e3a3807e28a?t=1609863934103)

Nevertheless, it seems to be possible to map most of the mainKeyTypeOfMeasure classes to a primary CEPA 2000 class ({numref}`measures_mainKeyTypeOfMeasure_to_CEPA2000_mapping`). 

The mapping and post-classification can be done by the Commission, using the reported data per Measure, to analyse and aggregate the data according CEPA classes, if that is required.

## Annexes 

### Simplified classification of measures – 4ᵗʰ cycle

This annex presents the **mainKeyTypeOfMeasure**, a simplified classification of measures that consolidates and replaces the **basicMeasureType** and the **keyTypeOfMeasure** classifications used in the 3ʳᵈ cycle.

The purpose of the simplified classification is: 
* To reduce the number of classes to a manageable set (19 options). 
* To use a single classification scheme applicable to both basic measures and supplementary measures. 
* To avoid redundancy and reporting burden in the classification of the measures. 
* To maintain the options directly linked to the basic measure types in Articles 11(3)(b) to 11(3)(l) of the WFD – see codes B, C, D, E, F, G, H, J, K, L. 
* To maintain the disaggregation in the measures to address significant impacts in the status of water as per Article 11(3)(i) – see codes I2-2, I2-3 and I2-4. 
* To allow flexibility in the reporting of the measures to address significant pressures, when combined with the optional mainPressureType attribute. 
* To maintain the previous KTM that do not fit the criteria above and were reported with high frequency in the 3ʳᵈ cycle – see codes X01, X12, X14, X23 and X24.

{numref}`measures_MappingmainKeyTypeOfMeasure` aligns the **mainKeyTypeOfMeasure** with the previous separate classification 
schemes. It supports MS in the migration to the single simplified codelist to be used in the 
**mainKeyTypeOfMeasure** attribute in the 4ᵗʰ cycle of reporting.

The proposed classification is provisional and can be reviewed by MS to detect potential issues and clarify the scope of the definitions.

Regarding the measures to address significant impacts in the status of water as per Article 11(3)(i) – see codes I2-2, I2-3 and I2-4 note that only some of the impacts applicable to surface water are detailed.

```{include} tables/Measures_MappingMainKeyTypeOfMeasure_ListTable
```

### Classification of environmental protection activities (CEPA 2000)

Based on the information in (http://publications.europa.eu/resource/dataset/cepa2000).  
**Note: this table is not relevant for the reporting process, it is only relevant for the analysis of reported data.**

```{include} tables/Measures_SubsetOfCEPAClasses_ListTable
```

### Mapping between mainKeyTypeOfMeasure and CEPA 2000 

```{include} tables/Measures_MainKeyTypeOfMeasure_CEPA2000_ListTable
```

(heading_wfd_measures_references)=
## References

```{include} FragmentReportingGuidanceFiles
```