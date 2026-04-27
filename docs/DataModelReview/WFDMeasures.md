# WFD - Measures

**PROPOSAL - Version 2026.02.17** {download}`PDF <pdf/WFD_4rd_cycle_Measures_v20260217.pdf>`

## Purpose and Overview

This document revises the **River Basin Management Plan & Programme of Measures** schema used in the 3ʳᵈ cycle of reporting of the Water Framework Directive River Basin Management Plans ({ref}`Figure 1 <Figure 1>`). It also presents a proposal for simplifying the electronic reporting in the 4ᵗʰ cycle ({ref}`Figure 2 <Figure 2>`).

Not all information in the RBMPs can be accurately provided using a common European model. However, it is possible to improve and simplify the reporting of structured data, accepting that part of the relevant information will remain in documentation to be analysed during the Commission's implementation assessment.

Using this principle, the data model can focus on aspects that are suitable for structured reporting, allowing adequate comparisons between different river basin districts (RBDs). Specific or more detailed information can be kept in the RBMP documents, the analysis of which can in the future be facilitated using, for example, large language models (LLMs) supported by retrieval‑augmented generation (RAG) techniques.

**Figure 1.** *Partial class diagram for River Basin Management Plan & Programme of Measures (RBMPPoM_2022) schema.*
(Figure 1)=
```{mermaid} /DataModelReview/mmd/MeasuresFigure1.mmd
:align: center
```


Source : (https://cdr.eionet.europa.eu/help/WFD/WFD_715_2022/UML%20Data%20specification/WFD2022.EAP)

**Figure 2.** *River Basin Management Plan & Programme of Measures – 4ᵗʰ cycle of reporting*

(Figure 2)=
```{mermaid} /DataModelReview/mmd/MeasuresRBDPlan.mmd
:align: center
```

### Current structure (3rd cycle of reporting)

The schema used in the 3rd cycle of reporting contains 3 main groups:
1. Summary information about the **RBMP**, the Progress since the previous RBMP, the mechanisms of international **Coordination** (if applicable).
2. Information about the **Programme of Measures**, comprising a summary questionnaire of **Targeted Questions** and aggregated data about the overall Cost of measures. 
Disaggregated information is requested about each **Measure** and its classification into key type of measures (**KTM**) and basic type of measures (if applicable).
3. Summary information about pressures and substances causing failure and their link to **KTM Indicators** and **Indicator Gaps**.

### Proposed structure (4th cycle of reporting)

1. The RBMP and Coordination tables are simplified to a single **RiverBasinManagementPlan table**, containing a selected subset of attributes. The Progress table is modified to request only aggregated information about the overall status of the measures of the previous cycle (3rd cycle).
2. The reporting of the Programme of Measures is also simplified. The **TargetedQuestions** table, containing the questionnaire at RBD level, is simplified. Information about measures is requested in a single **Measure** table. Information about the planned **ExpenditurePerMeasure** is reported in a separate table, if data is available.
3. The KTM indicators and indicator gaps group is completely removed.





## River Basin Management Plan, Coordination and Progress

### Current structure (3ʳᵈ cycle of reporting)

In the 3ʳᵈ cycle of reporting, this group comprised three tables, collecting summary information about the RBMP, the progress since the previous RBMP, and the mechanisms of international coordination, if applicable ({ref}`Figure 3 <Figure 3>`).

The data is structured as a simple questionnaire, mostly with Yes/No or multiple‑choice answers, accompanied by links to additional documentation (which can be uploaded or kept on national websites). Only one record per table is required for each River Basin District.

Reporting by MS should not present technical difficulties, and there is limited scope for technical simplification. Nevertheless, the Commission has reviewed whether the requested data is strictly required and proposes the simplification detailed in the next sections.

**Figure 3.** *Class diagram for the RBMPPoM_2022 schema: River Basin Management Plan, international Coordination and 
Progress since the previous cycle – 3ʳᵈ cycle of reporting*

(Figure 3)=
![RBMP diagram](img/MeasuresFigure3.JPEG)



### RiverBasinManagementPlan – 4ᵗʰ cycle of reporting

The simplified **RiverBasinManagementPlan** table ({ref}`Figure 4 <Figure 4>`) contains a subset of the data previously requested in the RBMP and Coordination classes in the 3ʳᵈ cycle.

A new attribute, **coordinationNRRReference**, allows the reporting of information related to coordination with the **Nature Restoration Regulation**.

The reporting of the **pomCoordinationArt5SWMI**, **pomCoordinationIRBMPPoM**, **pomCoordinationRoofReport** and **pomCoordinationFinancial** attributes is only required for international RBDs. 

**Figure 4.** *RiverBasinManagementPlan table – 4ᵗʰ cycle of reporting.*


(Figure 4)=
```{mermaid} /DataModelReview/mmd/MeasuresRBDPlan4thCycle.mmd
:align: center
```


## Progress – 4ᵗʰ cycle of reporting

The **Progress** table is modified to provide an overview of the proportion of the measures of the 3ʳᵈ RBMPs that were executed, cancelled, or otherwise affected, as well as the obstacles encountered during the implementation of the 3ʳᵈ RBMP Programme of Measures ({ref}`Figure 5 <Figure 5>`).

The only constraint is that, for each RBD, the sum of the values in **percentageInStatus** must be **100**. The level of detail can be adapted depending on needs and the data available.

**Figure 5.** *Progress table – 4ᵗʰ cycle of reporting.*

(Figure 5)=
```{mermaid} /DataModelReview/mmd/MeasuresProgressTable.mmd
:align: center
```


A numerical example illustrates per proposed approach.
Consider a hypothetical 3ʳᵈ RBMP Programme of Measures with 10 different measures, which are in different statuses and may have faced different obstacles ({ref}`Figure 6 <Figure 6>`). The example in Figure 7 illustrates how to synthesize the information in the Progress table. 


**Figure 6.** *Illustrative example -  hypothetical list with the status of the 10 measures of the 3ʳᵈ cycle.*


(Figure 6)=
| Measure | Status                       | Obstacles                 |
|---------|------------------------------|---------------------------|
| M01     | Ongoing                      | No obstacles.             |
| M02     | Executed                     | No obstacles.             |
| M03     | Executed                     | No obstacles.             |
| M04     | Executed                     | Extreme event.            |
| M05     | Executed                     | Extreme event.            |
| M06     | Cancelled                    | Extreme event.            |
| M07     | Cancelled                    | Extreme event.            |
| M08     | Postponed to the next cycle  | Delays, Lack of finance.  |
| M09     | Postponed to the next cycle  | Delays, Lack of finance.  |
| M10     | Cancelled                    | Not cost effective.       |


**Figure 7.** *Illustrative example: Progress table records for the example in Figure 6.*


(Figure 7)=
| previousRBMPMeasureStatus | percentageInStatus | obstaclesDelays | obstaclesLackOfFinance | obstaclesMeasureNotCostEffective | obstaclesExtremeEvents |
|---------------------------|--------------------|------------------|-------------------------|----------------------------------|-------------------------|
| Ongoing                   | 10                 | No               | No                      | No                               | No                      |
| Executed                  | 20                 | No               | No                      | No                               | No                      |
| Executed                  | 20                 | No               | No                      | No                               | Yes                     |
| Cancelled                 | 20                 | No               | No                      | No                               | Yes                     |
| Planned                   | 20                 | Yes              | Yes                     | Yes                              | No                      |
| Cancelled                 | 10                 | No               | No                      | Yes                              | No                      |


## Programme of Measures

In the 3ʳᵈ cycle of reporting, the Programme of Measures group comprised several tables ({ref}`Figure 8 <Figure 8>`). Most of the analysis in the current document is focused on ways to clarify and simplify the reporting of measures and the classification of measures.

**Figure 8.** *Class diagram for the RBMPPoM_2022 schema: Programme of Measures – 3ʳᵈ cycle of reporting.*

(Figure 8)=
![RBMP diagram](img/MeasuresFigure8.JPEG)


### TargetedQuestions – 4ᵗʰ cycle of reporting 

The **TargetedQuestions** table collects summary information about the measures in the RBMP, and the progress since the previous cycle. For each RBMP, only one record is required. The data is structured as a simple questionnaire, with Yes/No or multiple-choice answers.   
Reporting by MS should not present technical difficulties, and there is limited scope for any technical simplification. The Commission has revised and simplified the **TargetedQuestions** table ({ref}`Figure 9 <Figure 9>`), keeping a subset of the questions requested in the previous cycle.



**Figure 9.** *TargetedQuestions table - 4ᵗʰ cycle of reporting.* 

(Figure 9)=
```{mermaid} /DataModelReview/mmd/MeasuresTargetedQuestions.mmd
:align: center
```

### Measure – 4ᵗʰ cycle of reporting 
Figure 10 illustrates the simplified Measure table proposed for the 4ᵗʰ cycle. 

**Figure 10.** *Measure table – 4ᵗʰ cycle of reporting.*

(Figure 10)=
```{mermaid} /DataModelReview/mmd/MeasuresTable.mmd
:align: center
```


For each measure:

- Use a unique persistent European identifier for each **measureCode**.
- Use the original **measureName** (or an English translation thereof).
- If needed, provide a link to documentation (**measureReference**).
- Identify the primary **measureLegalInstrument**, using a single codelist value.
- Identify the **measureType**, using a single codelist value.
- Classify the measure using a single **mainKeyTypeOfMeasure** codelist value from a simplified classification. The closest match should be selected.
- Optionally or if applicable, identify the main pressure or pressure group addressed by the measure using the **measurePressureType** attribute, at the level of detail deemed more adequate. The closest match should be selected.
- Optionally or if applicable, identify the main substance or group of substances addressed by the measure using the **measureSubstanceType** attribute, at the level of detail deemed more adequate.
- Flag the sectoral plans for which the measure might be relevant using the **msfdRelevance**, **floodsRelevance**, **natureRestorationRegulationRelevance**, **draughtManagementPlanRelevance** and **climateAdaptationPlanRelevance** attributes.
- Specify the **geographicalCoverage** and **temporalCoverage** of the measure.

Narrative description:


Each different measure must have a persistent unique identifier at national level and European level (**measureCode**), a descriptive name (**measureName**), and zero or more links to documentation (**measureReference**). The **measureType** typology is described in ({ref}`Table 1 <Table 1>`). The primary **measureLegalInstrument** under which the measure was defined must be clearly identified. This avoids double reporting in other Directives: the measures can be reported only once under the RBMP electronic reporting. An updated list of EU water and other environmental legislation is provided (Table 2).

The scope of some basic measures is clearly linked to the two Daughter directives:

- Measures to prohibit direct discharges to groundwater: *Groundwater Directive*
- Measures to eliminate or reduce pollution by Priority Substances: *Environmental Quality Standards Directive*

These two legal instruments are part of the codelist (see {ref}`Table 2 <Table 2>`). The option 'Other' (Other Directives mentioned in Part A of Annex VI of the WFD) is eliminated: it was frequently used in the 3ʳᵈ cycle and does not convey relevant information.

*Table 1. Types of measures: proposed measureType values, definitions and example – 4ᵗʰ cycle of reporting.*

(Table 1)=
| Measure Type                       | Definition                                                                                                                                     | Examples |
|------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| LegislativeOrRegulatoryMeasure     | Measures that involve the adoption or modification of laws, by-laws, and binding standards to restrict activities or enforce compliance with environmental objectives. | Legislative and regulatory measures include water-related actions. Nitrates Action Plans: Measures to reduce nutrient pollution from agriculture through regulatory changes (e.g., Germany, Netherlands). Bans on Substances: Prohibitions on specific hazardous substances (e.g., PAH coatings in the Netherlands). Ecological Flow Standards: Establishing legally binding standards for ecological flows in rivers. |
| AdministrativeOrGovernanceMeasure  | Procedural actions taken by competent authorities to manage water use, including permits, inspections, and governance structures.               | Permitting and Authorization: Controlling activities through licensing systems (e.g., Germany, Spain). Review of Permits: Periodic updates of existing licenses (e.g., France). Registers: Maintaining databases of physical modifications (e.g., Latvia). Inspections: Enforcement activities to ensure compliance (e.g., Estonia). Advisory Services: Support for environment-friendly practices (e.g., Finland). |
| PhysicalOrTechnicalMeasure         | Concrete interventions involving construction, removal, or modification of infrastructure to reduce emissions or restore morphology.            | Wastewater Infrastructure: Construction or upgrade of wastewater treatment plants (e.g., Czechia, Romania). River Continuity and Restoration: Removal of barriers or installation of passes (e.g., Austria, Luxembourg). Reduction of Leakages: Improving irrigation infrastructure (e.g., Spain). Remediation: Cleanup of contaminated sites (e.g., Czechia, 15,772 km²). |
| EconomicOrFinancialMeasure         | Economic and financial instruments, taxes, or subsidies designed to influence behavior for environmental improvements.                          | Water Pricing: Application of tariffs for water services (e.g., Italy, Hungary). Subsidies and Compensation: Payments to support sustainable practices (e.g., Estonia, Slovakia, Netherlands). |
| KnowledgeOrPreparatoryMeasure      | Actions focused on research, data collection, and gap analyses to reduce uncertainty and inform future decision-making.                         | Research Studies: Poland studied 23% of its 3rd RBMP measures to improve knowledge base. Gap Analyses: Poland performed gap assessments for nutrient reductions. Source Identification: Finland completed detailed work to identify point sources and diffuse emissions for 53 monitored substances. |


*Table 2. Legal instruments: proposed measureLegalInstrument options – 4ᵗʰ cycle of reporting. *

(Table 2)=
| Acronym | Name | ELI |
|----------|------|-----|
| WFD | Directive 2000/60/EC of the European Parliament and of the Council of 23 October 2000 establishing a framework for Community action in the field of water policy | http://data.europa.eu/eli/dir/2000/60/oj |
| FLOODS | Directive 2007/60/EC of the European Parliament and of the Council of 23 October 2007 on the assessment and management of flood risks | http://data.europa.eu/eli/dir/2007/60/oj |
| MSFD | Directive 2008/56/EC of the European Parliament and of the Council of 17 June 2008 establishing a framework for community action in the field of marine environmental policy (Marine Strategy Framework Directive) | http://data.europa.eu/eli/dir/2008/56/2017-06-07 |
| BWD | Directive 2006/7/EC of the European Parliament and of the Council of 15 February 2006 concerning the management of bathing water quality and repealing Directive 76/160/EEC | http://data.europa.eu/eli/dir/2006/7/oj |
| DWD (recast) | Directive (EU) 2020/2184 of the European Parliament and of the Council of 16 December 2020 on the quality of water intended for human consumption (recast) | http://data.europa.eu/eli/dir/2020/2184/oj |
| EIA Directive | Directive 2011/92/EU of the European Parliament and of the Council of 13 December 2011 on the assessment of the effects of certain public and private projects on the environment | http://data.europa.eu/eli/dir/2011/92/2014-15-15 |
| EQSD2008 | Directive 2008/105/EC of the European Parliament and of the Council of 16 December 2008 on environmental quality standards in the field of water policy, amending and subsequently repealing Council Directives 82/176/EEC, 83/513/EEC, 84/156/EEC, 84/491/EEC, 86/280/EEC and amending Directive 2000/60/EC of the European Parliament and of the Council | http://data.europa.eu/eli/dir/2008/105 |
| EQSD2013 | Directive 2013/39/EU of the European Parliament and of the Council of 12 August 2013 amending Directives 2000/60/EC and 2008/105/EC as regards priority substances in the field of water policy | http://data.europa.eu/eli/dir/2008/105/2013-09-13 |
| GWD | Directive 2006/118/EC of the European Parliament and of the Council of 12 December 2006 on the protection of groundwater against pollution and deterioration | http://data.europa.eu/eli/dir/2006/118/oj |
| Birds Directive | Directive 2009/147/EC of the European Parliament and of the Council of 30 November 2009 on the conservation of wild birds | http://data.europa.eu/eli/dir/2009/147/2019-06-26 |
| Habitats Directive | Council Directive 92/43/EEC of 21 May 1992 on the conservation of natural habitats and of wild fauna and flora | http://data.europa.eu/eli/dir/1992/43/2025-07-14 |
| IED (formerly IPPC) | Directive 2010/75/EU of the European Parliament and of the Council of 24 November 2010 on industrial emissions (integrated pollution prevention and control) | http://data.europa.eu/eli/dir/2010/75/2024-08-04 |
| NRR | Regulation (EU) 2024/1991 of the European Parliament and of the Council of 24 June 2024 on nature restoration and amending Regulation (EU) 2022/869 | http://data.europa.eu/eli/reg/2024/1991/oj |
| NITRATES | Council Directive of 12 December 1991 concerning the protection of waters against pollution caused by nitrates from agricultural sources (91/676/EEC) | http://data.europa.eu/eli/dir/1991/676/oj |
| PPP (formerly PPPD) | Regulation (EC) No 1107/2009 of the European Parliament and of the Council of 21 October 2009 concerning the placing of plant protection products on the market and repealing Council Directives 79/117/EEC and 91/414/EEC | http://data.europa.eu/eli/reg/2009/1107/2022-11-21 |
| Seveso III Directive | Directive 2012/18/EU of the European Parliament and of the Council of 4 July 2012 on the control of major-accident hazards involving dangerous substances, amending and subsequently repealing Council Directive 96/82/EC Text with EEA relevance | http://data.europa.eu/eli/dir/2012/18/oj |
| Sewage Sludge Directive | Council Directive of 12 June 1986 on the protection of the environment, and in particular of the soil, when sewage sludge is used in agriculture (86/278/EEC) | http://data.europa.eu/eli/dir/1986/278/2022-01-01 |
| UWWTD (recast) | Directive (EU) 2024/3019 of the European Parliament and of the Council of 27 November 2024 concerning urban wastewater treatment (recast) | http://data.europa.eu/eli/dir/2024/3019/oj |
| WRR | Regulation (EU) 2020/741 of the European Parliament and of the Council of 25 May 2020 on minimum requirements for water reuse | http://data.europa.eu/eli/reg/2020/741/oj |


The **mainKeyTypeOfMeasure** attribute contains the classification to be used for both basic and supplementary measures (see {ref}`Table 3 <Table 3>`). It simplifies, consolidates and replaces both the basicMeasureType and the keyTypeOfMeasure classifications used in the 2ʳᵈ and 3ʳᵈ cycles. 

*Table 3. Proposed simplified classification of measures: mainKeyTypeOfMeasure – 4ᵗʰ cycle of reporting.*
(Table 3)=
| mainKeyTypeOfMeasure (4th cycle)                                                                 | mainPressureType     | mainSubstanceType |
|--------------------------------------------------------------------------------------------------|-----------------------|--------------------|
| B - Measure to implement recovery of costs for water services                                    | P3%,P1%,P2%           | optional           |
| C - Measure to promote efficient and sustainable water use                                       | P3%                   | optional           |
| D - Measure to protect drinking water quality and reduce the level of treatment required         | P1%,P2%,P3%,P9        | optional           |
| E - Measure to control abstraction from surface and groundwater, and impoundment of surface water| P3%                   | not applicable     |
| F - Measure to control artificial recharge or augmentation of groundwater                        | P6%                   | not applicable     |
| G - Measure to control point source discharges                                                   | P1%                   | optional           |
| H - Measure to prevent or control inputs of diffuse pollutants                                   | P2%                   | optional           |
| J - Measure to prohibit direct discharges to groundwater                                         | P1%,P2%               | optional           |
| K - Measure to eliminate Priority Substances and reduce pollution by other substances            | P1%,P2%               | optional           |
| L - Measure to prevent accidental pollution                                                      | P1%,P2%,P9            | optional           |
| I2-2 - Measure to address significant impacts on surface waters - Altered habitats (hydrological)| P4-3%                 | not applicable     |
| I2-3 - Measure to address significant impacts on surface waters - Altered habitats (morphology)  | P4%                   | not applicable     |
| I2-4 - Measure to address significant impacts on surface waters - Acidification                  | P2-7, others?         | optional           |
| P - Measure to address significant pressures on surface waters                                   | P%                    | conditional        |
| X01 - Construction or upgrades of wastewater treatment plants                                    | P1%,P2%               | optional           |
| X12 - Advisory services                                                                          | P%                    | optional           |
| X14 - Research, improvement of knowledge base reducing uncertainty                               | P%                    | optional           |
| X23 - Natural water retention measures                                                           | P%                    | optional           |
| X24 - Climate change adaptation measure                                                          | P%                    | optional           |




In the **3ʳᵈ cycle**, the reporting guidance stated that *“the name should reflect the pressure that is being tackled by the measure”* — meaning the pressure(s) should be described textually in the name of the measure. This recommendation was not consistently followed, and an analysis of the measure names across Europe does not yield useful results.

It is easier to keep the **original name of the measure**, and to allow MS to optionally select the **mainPressureType** that the measure addresses, at the adequate level of detail (e.g. a generic measure may address **P2 – Diffuse sources**, while a more targeted measure may address only P2‑5 – Diffuse – Contaminated sites or abandoned industrial sites).

The **mainPressureType** attribute allows more clarity and flexibility and can be applied to supplementary measures too.  
The mainPressureType attribute is optional, except for measures of type **G** and **H**.  
For measures of type G and H, the Commission requires additional information to differentiate measures addressing issues related to Urban Waste Water (**P1‑1**) and diffuse pollution from Agriculture (**P2‑2**).

*If needed and applicable*, a similar approach can be used for **mainSubstanceType**, allowing MS to identify measures targeting specific substances or groups of substances.



The geographical scope of a measure is specified in the **geographicalCoverage** attribute, by selecting the most appropriate option: {‘national’ | ‘riverBasinDistrict’ | ‘waterBody’ | ‘protectedArea’}.

The option **‘national’** should be used for measures that target any waterbody affected by a given significant pressure or substance failing. Similarly, the option **‘riverBasinDistrict’** should be used for measures that target any waterbody affected by a given significant pressure or substance failing within the RBDs indicated in the **euRBDCode** attribute.

If appropriate and necessary, it is possible to specify that a measure only applies to a specific category of waterbodies, using the optional **waterCategory** attribute.

If appropriate and necessary, it is possible to specify that a measure only applies to a specific type of WFD protected area, using the optional **protectedAreaType** attribute.

The option **geographicalCoverage = ‘waterBody’** should be reserved for measures that target specific water bodies (for example, a given river, or a set of lakes).  
The option **geographicalCoverage = ‘protectedArea’** should be reserved for measures that target specific protected areas (for example, a set of bathing waters or a specific UWWTD sensitive area).  
In these cases, it is not requested to individually identify the waterbodies or protected areas.

The temporal scope of a measure is provided in the **implementationPeriod** – the range of years indicated is used to check the reporting of information related to expenditures (e.g. if a measure is yet to start, then no past expenditures exist).  
The **implementationStatus** attribute allows the distinction between planned and ongoing measures – and may also be used for measures planned for the 3ʳᵈ cycle but already executed or cancelled by the end of 2027.

## Economic data in the Programme of Measures

The revision of the electronic reporting focuses on the main issues described in the Note to the CIS Working Group Economics ([^1]) quoted below:

[^1]: P. Arnoldus, “Workstream 1: proposing a simplification and standardisation of the economic data reporting,” note to the CIS Working 
Group Economics, 15 December 2025,[Available](https://circabc.europa.eu/ui/group/9ab5926d-bed4-4322-9aa7-9964bbe8312d/library/2eef1f5c-5df6-41e2-93e8-c0f427d80eb1/details) in Circabc 

“[…] Both the Commission’s 6ᵗʰ and 7ᵗʰ WFD Implementation Reports indicate persistent problems in the (electronic) reporting on the investments and the costs of other measures in the Programme of Measures (PoM).

The 6ᵗʰ WFD Implementation Report notes that the Member States’ reporting on costs and financing of the PoMs appears overall patchy and that a consultant’s study estimate is an underestimation for the total costs, as there are significant data gaps and it excludes operational and infrastructure maintenance costs. The corresponding investment overview table shows indeed large gaps ([^2]) .

[^2]: 6th WFD Implementation Report,[ COM(2021) 970](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:52021DC0970),p15. The table concerns Table 4, p24, of [SWD(2021) 970](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:52021SC0970) – note that the differentiation is based.

The Commission’s evaluation of the 3ʳᵈ River Basin Management Plans ([^3]), as part of the 7ᵗʰ WFD Implementation Report, notes that the “third PoMs presented in the (…) RBMPs show that Member States continue to have different approaches to their design and reporting” and that “the costs and the financing of the planned measures are often missing.” Hence, the Commission recommends that “in order to effectively implement the PoMs, long‑term investment plans should be developed and the source of financing for each measure clearly identified.”  
Good planning is also necessary for the acquisition of support from EU Funds, the EIB, and other promotional banks.


[^3]: Quotes are from 7th WFD Implementation Report,[ COM(2025) 2](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:52025DC0002)(p15, p36) 
*The challenge is thus to improve the reporting of the costs of the PoM measures, including the investment amounts,* and to specify the funding of these investments and other measures. This requires a clear distinction between **capital costs (CAPEX)** and **operational costs (OPEX)**.

The proposal here is to agree on a clear conceptual basis for the PoM costs.

It is natural to consider the PoM as a **budget of government outlays** – however, there can be costs on other economic agents without government payment involved (e.g. banning an activity).

The budget orientation would imply focusing on foreseen *spending amounts*. This has three consequences:

- ‘Welfare costs’ should not be included in the reporting. However, they can be taken up as “negative benefits” in the **CEA (cost‑effectiveness analysis)**.  
- The reporting concerns investment spending (purchases / commitments) and not capital costs (depreciation).  
- To link with financial support from **EU Funds**, **EIB**, and other promotional banks, it is necessary to distinguish OPEX and CAPEX when reporting investment costs.

There is a readily available conceptual basis for the reporting on the PoM investment and other costs, with which the Member States are already familiar, namely the **environmental protection expenditures**. They are required to collect and report this data annually to Eurostat ([^4]), who publishes the **Environmental Protection Expenditures Accounts (EPEA)** as one of the environmental‑economic satellite accounts to the economic National Accounts.The EPEA are based on a clear, publicly available protocol (following UN statistical standards), defining the environmental domains, spending economic sectors, and expenditure types. The latter includes the distinction between **capital** and **current** expenditures. Hence, it meets the features described in the three points above.


[^4]: An obligation under Regulation (EU) No 691/2011, amended by Commission Delegated Regulation (EU) 2022/125; the consolidated 
version can be found [here](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A02011R0691-20250624)


A brief review of the reported data confirms the issues mentioned above.

In the **3ʳᵈ cycle** of reporting, the overall cost of the PoM was reported in the **Costs** class ({ref}`Figure 11 <Figure 11>`). Reporting of costs was, de facto, optional – since all numerical attributes admitted the option **–9999** to denote “data not available”.

 Out of the 146 RBD reported by EU Member States, 24 do not have data on investments, 54 do not have data on operational costs and 64 do not have data on EU funds. 

**Figure 11.** Class diagram for the RBMPPoM_2022 schema: Costs – 3ʳᵈ cycle of reporting.

(Figure 11)=
```{mermaid} /DataModelReview/mmd/MeasuresCosts.mmd
:align: center
```

The variability of the geographical and temporal coverage of the reported data adds to the difficulty in achieving a meaningful analysis.{ref}`Table 4 <Table 4>` illustrates the issues regarding temporal coverage. {ref}`Table 5 <Table 5>` illustrates the issue with geographical coverage.


*Table 4. Temporal coverage: period to which the reported costs refer – 3ʳᵈ RBMP electronic reporting (including Norway).*

(Table 4)=
| costOfMeasurePeriod20152021 | costOfMeasurePeriod20212027 | Number of RBDs |
|------------------------------|------------------------------|----------------|
| 2014--2020                   | 2022--2027                   | 5              |
| 2015--2020                   | 2021--2027                   | 1              |
| 2015--2020                   | 2022--2027                   | 2              |
| 2015--2021                   | 2007--2027                   | 1              |
| 2015--2021                   | 2021--2027                   | 62             |
| 2015--2021                   | 2022--2027                   | 23             |
| 2016--2021                   | 2009--2015                   | 1              |
| 2016--2021                   | 2010--2015                   | 7              |
| 2016--2021                   | 2021--2027                   | 4              |
| 2016--2021                   | 2022--2027                   | 40             |
| 2016--2022                   | 2023--2027                   | 4              |
| 2016--2027                   | 2019                         | 4              |
| 2017--2021                   | 2021--2027                   | 4              |
| 2017--2021                   | 2022--2027                   | 1              |



*Table 5. Geographic coverage: scale to which the reported costs refer – 3ʳᵈ RBMP electronic reporting (including Norway).*

(Table 5)=
| costOfMeasuresScale20152021 | costOfMeasuresScale20212027 | Number of RBDs |
|------------------------------|------------------------------|----------------|
| National                     | National                     | 48             |
| River Basin District         | River Basin District         | 103            |
| National                     | River Basin District         | 4              |
| River Basin District         | National                     | 7              |




### ExpenditurePerMeasurePerSector – 4ᵗʰ cycle of reporting

Figure 12 illustrates the ExpenditurePerMeasurePerSector table proposed for the 4ᵗʰ cycle.

The data is reported for each measure, *if it is available*: the **measureCode** identifier and the **expenditureDataAvailable** attribute are the only mandatory attributes.

The geographical scope of the measure is inherited from the parent record in the **Measure** table and does not need to be reported again. Likewise, the temporal scope is inherited from the parent records and can be used to verify the reported data ([^5]).

[^5]: An error should be raised when there is missing data. In pseudo-code (the && operators tests whether a range of values overlaps):<br>a) IF expenditureDataAvailable = 'Yes' AND Measure.implementationPeriod && '[2022,2027]' AND Measure.implementationStatus IN ('executed', 'ongoing', 'implemented') AND totalCapitalExpenditure3rdCycle IS NULL AND annualCurrentExpenditure3rdCycle IS NULL. <br>b) IF expenditureDataAvailable = 'Yes' AND Measure.implementationPeriod && '[2028,2033]' AND Measure.implementationStatus IN ('ongoing', 'implemented', 'planned') AND totalCapitalExpenditure4thCycle IS NULL AND annualCurrentExpenditure4thCycle IS NULL. 

The attribute **millionUnitsOfNationalCurrency** was introduced to facilitate reporting by MS outside the Euro area, in alignment with common statistical practices ([^6]). It also facilitates human analysis, namely the cross‑checking against the RBMP documentation.

[^6]: Data must be reported in Millions of Euro for Euro Area Member States, and in Millions of National currency for non-Euro Area countries. (The unit multiplier is set to 6 and it is applied to all the data, so it doesn't need to be specified.) Non-Euro Area countries 
hould use the relevant code for its national currency (e.g. BGN, CZK, DKK, HRK, HUF, PLN, RON, SEK) rather than common code for domestic currency (XDC). Euro Area countries must use EUR. Generally, the number of decimal digits is “0”. If a country wants to send a figure lower than 1 million, decimals may be used. In this case, the separator must be a dot (.). (Example: if a country wants to report a value of 10 000 the figure 0.01 must be sent). If necessary the proposal can be modified to use a different multiplier (e.g. thousands). 

**Figure 12.** *ExpenditurePerMeasurePerSector – 4ᵗʰ cycle of reporting.*


```{mermaid} /DataModelReview/mmd/MeasuresExpenditure.mmd
:align: center
```


A clear separation is made between **capital** expenditure vs. **current** expenditure and between the 3ʳᵈ cycle and the 4ᵗʰ cycle data. Only total values are requested.

The **institutionalSector** attribute identifies the institutional sector doing the outlay. This aspect is explained below.

The European System of Accounts (ESA 2010) has a standard classification of institutional sectors (see {ref}`Table 6 <Table 6>`).  
The topmost class (S.1 – Total Economy) encompasses all national institutional sectors; implicitly, the 3ʳᵈ cycle of WFD reporting used it.  
The dichotomous key in Figure 13 clarifies the allocation of units to sectors.

The Environmental Protection Expenditures Accounts (EPEA) uses four groups of sectors ([^7]):

[^7]: See e.g. the Environmental protection expenditure accounts Handbook , 2017 edition [https://ec.europa.eu/eurostat/documents/3859598/7903714/KS-GQ-17-004-EN-N.pdf/7ea9c74b-eda4-4c23-b7bd-897358bfc990?t=1489135578000](https://ec.europa.eu/eurostat/documents/3859598/7903714/KS-GQ-17-004-EN-N.pdf/7ea9c74b-eda4-4c23-b7bd-897358bfc990?t=1489135578000)
- S13 and S15 – General government and **NPISH**  
- S11 and S12 – Corporations
- S14 – Households
- S2 – Rest of the World

*Table 6. European System of Accounts (ESA 2010) sectors.*

(Table 6)=
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



**Figure 13.** *European System of Accounts (ESA 2010) allocation of institutional units to sectors.*

(Figure 13)=
```{mermaid} /DataModelReview/mmd/MeasuresUnitResidentflowchart.mmd
:align: center
```


Table 7 presents a proposed list of institutional sectors that can be used in the **4ᵗʰ cycle** of reporting. The list should be revised and discussed with the CIS WG Economics.

It is also important to provide technical guidance and examples on the proper reporting of expenditures. For example, in the context of the EPEA, research and development (R&D) expenditure is primarily classified as current expenditure, while the National Accounts framework (ESA 2010) typically capitalizes R&D as an investment.

*Table 7. Proposed list of institutional sectors – 4ᵗʰ cycle of reporting.*


(Table 7)=
| ESA Sector*      | Definition and comments |
|------------------|--------------------------|
| S.1              | Total economy. Allows the provision of aggregated data. |
| S.13             | General government. The "default" option, if the RBMPs only include government outlays. |
| S.13_S.15        | General government + NPISH. Aligned with EPEA, can be used if preferred. |
| S.11_S.12        | Corporations. Aligned with EPEA, can be used if preferred. |
| S.11             | Non-financial corporations. Can be used if the distinction of outlays by public and private companies is not relevant. |
| S.11001          | Public non-financial corporations. Can be used if the distinction of outlays by public and private companies is relevant. |
| S.11002_S.11003  | Private non-financial corporations. Can be used if the distinction of outlays by public and private companies is relevant. |
| S.212            | Institutions and bodies of the European Union (e.g. European Central Bank, European Commission). |



It is also important to address the reporting of transfers of EU Funds.  
If institutionalSector = 'S.212' then the value represents a transfer of EU funds into the national economy. Depending on the purpose, it can be a capital transfer (e.g. to build a new UWWT plant), or a current transfer (e.g. a CAP subsidy to pay farmers to reduce or eliminate pesticides). It is not necessary to identify which sector receives the transfer.

A numerical example can be used to illustrate the proposed approach.

A new Urban Waste Water Treatment Plant required a total capital expenditure of 10M€.

• Scenario 1 : the General Government (S.13) built the plant using national funds.  
• Scenario 2 : a public utility company (S.11001) built the plant, using 10M€ of national funds transferred by the government.  
• Scenario 3 : the government built the plant using 8M€ of national funds and 2M€ from the EU Cohesion Fund.  
• Scenario 4 : a public utility company (S.11001) built the plant, using 8M€ of national funds transferred by the General Government (S.13) to the company and 2M€ of EU funds transferred to the company via the national government.  
• Scenario 5 : a public utility company (S.11001) built the plant, using 5M€ of their own funds, 4M€ of national funds transferred by the General Government (S.13) to the company and 1M€ of EU funds transferred to the company via the national government.

Table 8 illustrates the reporting of the different scenarios.

Note that scenario 1 and scenario 2 are identical from a reporting point‑of‑view.  
Likewise, scenario 3 and scenario 4 are identical.

*Table 8. Illustrative example with the reporting of expenditure per sector.*

(Table 8)
| Scenario | Institutional Sector                                   | Total Capital Expenditure |
|----------|---------------------------------------------------------|----------------------------|
| 1        | S.13 – General Government                               | 10 M€                      |
| 2        | S.13 – General Government                               | 10 M€                      |
| 3        | S.13 – General Government                               | 8 M€                       |
| 3        | S.212 – Institutions and bodies of the European Union   | 2 M€                       |
| 4        | S.13 – General Government                               | 8 M€                       |
| 4        | S.212 – Institutions and bodies of the European Union   | 2 M€                       |
| 5        | S.11001 – Public non-financial corporations             | 5 M€                       |
| 5        | S.13 – General Government                               | 4 M€                       |
| 5        | S.212 – Institutions and bodies of the European Union   | 1 M€                       |



The Commission must provide guidance on the reporting of expenditure for measures where 
mainKeyTypeOfMeasure IN ('C - Measure to promote efficient and sustainable water use', 'E - Measure to control abstraction from surface and groundwater, and impoundment of surface 
water') which may be outside the scope of the EPEA.

**Alignment with the Classification of environmental protection activities**

The EPEA categorises activities using the Classification of environmental protection activities (CEPA 2000, {ref}`Table 10 <Table 10>`). The proposed classification of Measures using the mainKeyTypeOfMeasure value ({ref}`Table 3 <Table 3>`) is not based on the CEPA 2000 classification.

Note also that CEPA strictly covers Environmental Protection (preventing pollution and degradation) and excludes Resource Management (saving water or energy), which falls under CReMA([^8])  (Classification of Resource Management Activities).

[^8]: [https://ec.europa.eu/eurostat/documents/1798247/12177560/CEPA+and+CReMA+explanatory+notes++technical+note.pdf/b3517fb9-1cb3-7cd9-85bd-4e3a3807e28a?t=1609863934103](https://ec.europa.eu/eurostat/documents/1798247/12177560/CEPA+and+CReMA+explanatory+notes++technical+note.pdf/b3517fb9-1cb3-7cd9-85bd-4e3a3807e28a?t=1609863934103)

Nevertheless, it seems to be possible to map most of the mainKeyTypeOfMeasure classes to a primary CEPA 2000 class ({ref}`Table 11 <Table 11>`). 

The mapping and post-classification can be done by the Commission, using the reported data per Measure, to analyse and aggregate the data according CEPA classes, if that is required.

## Annexes

### Simplified classification of measures – 4ᵗʰ cycle of reporting

This annex presents the **mainKeyTypeOfMeasure**, a simplified classification of measures that consolidates and replaces the **basicMeasureType** and the **keyTypeOfMeasure** classifications used in the 3ʳᵈ cycle.

The purpose of the simplified classification is:  
• To reduce the number of classes to a manageable set (19 options).  
• To use a single classification scheme applicable to both basic measures and supplementary measures.  
• To avoid redundancy and reporting burden in the classification of the measures.  
• To maintain the options directly linked to the basic measure types in Articles 11(3)(b) to 11(3)(l) of the WFD – see codes B, C, D, E, F, G, H, J, K, L.  
• To maintain the disaggregation in the measures to address significant impacts in the status of water as per Article 11(3)(i) – see codes I2-2, I2-3 and I2-4.  
• To allow flexibility in the reporting of the measures to address significant pressures, when combined with the optional mainPressureType attribute.  
• To maintain the previous KTM that do not fit the criteria above and were reported with high frequency in the 3ʳᵈ cycle – see codes X01, X12, X14, X23 and X24.

Table 9 aligns the **mainKeyTypeOfMeasure** with the previous separate classification 
schemes. It supports MS in the migration to the single simplified codelist to be used in the 
**mainKeyTypeOfMeasure** attribute in the 4ᵗʰ cycle of reporting.

The proposed classification is provisional and can be reviewed by MS to detect potential issues and clarify the scope of the definitions.

Regarding the measures to address significant impacts in the status of water as per Article 11(3)(i) – see codes I2-2, I2-3 and I2-4 note that only some of the impacts applicable to surface water are detailed.


*Table 9. Mapping between the proposed mainKeyTypeOfMeasure (4ᵗʰ cycle) and current basicMeasureType and 
keyTypeOfMeasure (2ⁿᵈ and 3ʳᵈ cycle).*

(Table 9)=
| mainKeyTypeOfMeasure (4th cycle)                                                               | basicMeasureType (2nd and 3rd cycle)                                      | keyTypeOfMeasure (2nd and 3rd cycle) |
|------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|---------------------------------------|
| B - Measure to implement recovery of costs for water services                                  | Measure to implement recovery of costs for water services                 | KTM9 - Water pricing policy measures for the implementation of the recovery of cost of water services from households; KTM10 - Water pricing policy measures for the implementation of the recovery of cost of water services from industry; KTM11 - Water pricing policy measures for the implementation of the recovery of cost of water services from agriculture |
| C - Measure to promote efficient and sustainable water use                                     | Measure to promote efficient and sustainable water use                    | KTM8 - Water efficiency, technical measures for irrigation, industry, energy and households |
| D - Measure to protect drinking water quality and reduce the level of treatment required       | Measure to protect drinking water quality and reduce the level of treatment required | KTM13 - Drinking water protection measures (e.g. establishment of safeguard zones, buffer zones etc) |
| E - Measure to control abstraction from surface and groundwater, and impoundment of surface water | Measure to control abstraction from surface and groundwater               |                                       |
| F - Measure to control artificial recharge or augmentation of groundwater                      | Measure to control recharging of groundwater                              |                                       |
| G - Measure to control point source discharges                                                 | Measure to control point source discharges                                |                                       |
| H - Measure to prevent or control inputs of diffuse pollutants                                 | Measure to prevent or control inputs of diffuse pollutants                | KTM17 - Measures to reduce sediment from soil erosion and surface run-off; KTM2 - Reduce nutrient pollution from agriculture; KTM21 - Measures to prevent or control the input of pollution from urban areas, transport, and built infrastructure; KTM22 - Measures to prevent or control the input of pollution from forestry; KTM7 - Improvements in flow regime and/or establishment of ecological flows |
| I2-2 - Measure to address significant impacts - Altered habitats due to hydrological changes   | Measure to address significant impacts on the hydromorphological conditions | KTM5 - Improving longitudinal continuity (e.g. establishing fish passes, demolishing old dams); KTM6 - Improving hydromorphological conditions of water bodies other than longitudinal continuity |
| I2-4 - Measure to address significant impacts - Acidification                                  |                                                                           | KTM25 - Measures to counteract acidification |
| J - Measure to prohibit direct discharges to groundwater                                       | Measure to prohibit direct discharges to groundwater                      |                                       |
| K - Measure to eliminate by Priority Substances and reduce pollution by other substances       | Measure to eliminate or reduce pollution by Priority Substances           | KTM15 - Measures for the phasing-out of emissions, discharges and losses of Priority Hazardous Substances or for the reduction of emissions, discharges and losses of Priority Substances; KTM3 - Reduce pesticides pollution from agriculture |
| L - Measure to prevent accidental pollution                                                    | Measure to prevent accidental pollution                                   | KTM18 - Measures to prevent or control the adverse impacts of invasive alien species, and introduced diseases; KTM19 - Measures to prevent or control the adverse impacts of recreation including angling; KTM20 - Measures to prevent or control the adverse impacts of fishing and other exploitation/removal of animal and plants; KTM4 - Remediation of contaminated sites (historical pollution including sediments, groundwater, soil) |
| X01 - Construction or upgrades of wastewater treatment plants                                  |                                                                           | KTM1 - Construction or upgrades of wastewater treatment plants; KTM16 - Upgrades or improvements of industrial wastewater treatment plants (including farms) |
| X12 - Advisory services                                                                        |                                                                           | KTM12 - Advisory services for agriculture |
| X14 - Research, improvement of knowledge, base reducing uncertainty                            |                                                                           | KTM14 - Research, improvement of knowledge base reducing uncertainty |
| X23 - Natural water retention measures                                                         |                                                                           | KTM23 - Natural water retention measures |
| X24 - Climate change adaptation measure                                                        |                                                                           | KTM24 - Adaptation to climate change |



## Classification of environmental protection activities (CEPA 2000)

*Table 10. Subset of CEPA classes potentially applicable to the classification of WFD Measures.* 
Based on the information in (http://publications.europa.eu/resource/dataset/cepa2000).  
**Note: this table is not relevant for the reporting process, it is only relevant for the analysis of reported data.**

(Table 10)=
| CODE | NAME | SCOPE |
|------|------|--------|
| CEPA 2 | Wastewater management | Wastewater is defined as water that is of no further immediate value for the purpose for which it was used or in the pursuit of which it was produced because of quality, quantity, or time of its occurrence.<br><br>Wastewater management comprises activities and measures aimed at the prevention of pollution of surface water through the reduction of the release of wastewater into inland surface water and seawater.<br><br>It includes:<br>• the collection, treatment of wastewater;<br>• monitoring and regulation activities;<br>• septic tanks.<br><br>Septic tanks are settling tanks through which wastewater is flowing and the suspended matter is decanted as sludge. Organic matter (in the water and in the sludge) is partly decomposed by anaerobic bacteria and other micro-organisms.<br><br>It excludes:<br>• actions and activities aiming to protect groundwater from pollutant infiltration and the cleaning up of water bodies after pollution (see CEPA 4). |
| CEPA 2.1 | Prevention of pollution through in-process modifications | Activities and measures aimed at reducing the generation of wastewater through IPMs related to:<br>• cleaner and more efficient production processes and other technologies (cleaner technologies);<br>• the consumption or use of ‘cleaner’ (adapted) products.<br><br>It includes:<br>• replacing existing production processes with new processes designed to reduce water pollutants or wastewater generated during production (e.g., separation of networks, treatment and re-use of water used in production processes);<br>• modifying or adapting an existing production process or facilities to enable substitution of raw materials, catalysts and other inputs by non- or less‑polluting products. |
| CEPA 2.2 | Sewerage networks | Activities aimed at the operation, maintenance and repair of sewerage networks.<br><br>Sewerage networks are systems of collectors, pipelines, vehicles, tanks, conduits and pumps used to transport wastewater (rainwater, domestic and other wastewater) from points of generation to a sewage treatment plant or discharge point. |
| CEPA 2.3 | Wastewater treatment | Wastewater treatment is the process which brings wastewater up to environmental standards or other quality norms.<br><br>Three broad types of treatment:<br>1. **Mechanical treatment** – separation of wastewater into treated water and sludge (sedimentation, screening, flotation).<br>2. **Biological treatment** – aerobic or anaerobic microorganisms treat wastewater (activated sludge, anaerobic digestion).<br>3. **Advanced treatment** – removal of specific constituents (metals, nitrates, phosphorous, oxidisable non‑biodegradable matter).<br><br>Also included:<br>• septic tanks, their maintenance and emptying;<br>• construction and operation of sewage treatment plants;<br>• treatment of sewage sludge for disposal or reuse (agriculture, incineration with energy recovery, biogas). |
| CEPA 2.4 | Treatment of cooling water | Processes which bring cooling water up to environmental standards before release.<br><br>Cooling water is used to remove heat. Activities include:<br>• air cooling (extra cost vs. water cooling);<br>• cooling towers (when required for pollution reduction);<br>• cooling circuits for processing water and vapour condensation;<br>• equipment to enhance dispersion of cooling water;<br>• closed cooling circuits;<br>• circuits for using cooling water for heating purposes.<br><br>Includes activities reducing cooling water use and improving efficiency in the energy sector. |
| CEPA 2.5 | Measurement, control, laboratories and the like | Activities aimed at monitoring pollutant concentrations in wastewater and the quality of inland surface water and marine water at discharge points.<br><br>Includes analysis and measurement of pollutants. |
| CEPA 2.6 | Other activities | All other activities and measures aimed at wastewater management, including regulation and ETIGA activities specific to CEPA 2, when separable from other CEPA classes. |
| CEPA 4 | Protection and remediation of soil, groundwater and surface water | Protection and remediation of soil and water concerns surface water, groundwater and marine waters.<br><br>Includes prevention of pollutant infiltration, cleaning up of soils and water bodies, protection of soil from erosion and degradation (including salinisation), and monitoring of soil and groundwater pollution.<br><br>Excludes:<br>• wastewater management (CEPA 2);<br>• soil protection in forests (CReMA 11A);<br>• biodiversity and landscape protection (CEPA 6).<br><br>Aquaculture is excluded except organic aquaculture (CEPA 4.3). |
| CEPA 4.1 | Prevention of pollutant infiltration | Activities and measures aimed at reducing or eliminating penetration of polluting substances into soil and water.<br><br>It includes:<br>• sealing of soils of industrial plants;<br>• installation of catchment for pollutant run-offs and leaks;<br>• strengthening of storage facilities;<br>• transportation of pollutant products. |
| CEPA 4.2 | Cleaning up of soil and water bodies | Processes to reduce pollutants in soil and water bodies either in situ or in installations.<br><br>It includes:<br>• soil decontamination at industrial sites, landfills, black spots;<br>• dredging pollutants from water bodies;<br>• cleaning up surface water after accidental pollution;<br>• cleaning up oil spills on land, inland waters and seas.<br><br>It excludes:<br>• liming of lakes and artificial oxygenation (CEPA 6);<br>• civil protection services (outside CEPA/CReMA). |
| CEPA 4.3 | Protection of soil from erosion and other physical degradation | Activities aimed at protecting soil from erosion and physical/chemical degradation.<br><br>It includes:<br>• restoring protective vegetal cover;<br>• anti‑erosion walls;<br>• organic farming and less harmful agricultural practices;<br>• organic aquaculture.<br><br>It excludes:<br>• conventional agriculture (outside CEPA/CReMA);<br>• protection of settlements against natural hazards.<br><br>Includes definition of soil erosion. |
| CEPA 4.4 | Prevention and remediation of soil salinity | Activities aimed at preventing or reducing soil and groundwater salinity.<br><br>It includes:<br>• increasing groundwater tables to prevent seawater intrusion;<br>• lowering groundwater tables via re‑vegetation, irrigation changes.<br><br>It excludes:<br>• measures for economic purposes (conventional agriculture, land reclamation). |
| CEPA 4.5 | Measurement, control, laboratories and the like | Monitoring soil, groundwater and surface water quality, erosion and salinity.<br><br>It includes:<br>• monitoring systems;<br>• inventories of black spots;<br>• maps and databases of pollution, erosion, salinity. |
| CEPA 4.6 | Other activities | All other activities aimed at protecting and remediating soil, groundwater, surface water and marine waters.<br><br>Includes ETIGA activities specific to CEPA 4. |
| CEPA 6 | Protection of biodiversity and landscapes | Activities aimed at protecting and replenishing wild fauna and flora, habitats, ecosystems, and natural/semi‑natural landscapes.<br><br>Includes rehabilitation of abandoned mining/quarrying sites.<br><br>Excludes:<br>• historic monuments;<br>• weed control for agriculture;<br>• recreational structures (parks, golf courses);<br>• zoos, aquariums, city greenery;<br>• roadside green spaces;<br>• extraction activities (hunting, fishing);<br>• conventional farming/gardening (except organic farming under CEPA 4).<br><br>Forest fire protection is reported under CReMA 11A. |
| CEPA 6.1 | Protection and rehabilitation of species and habitats | Activities aimed at conservation, reintroduction, recovery of species and restoration of habitats.<br><br>It includes:<br>• conserving genetic heritage;<br>• ecological infrastructure (green bridges, passages);<br>• re‑introduction of native species;<br>• control of invasive species;<br>• restoration of wild flora/fauna stocks;<br>• land purchase for habitat protection;<br>• low‑impact fishing nets, pesticides, turbine shutdown algorithms, bat protection systems. |
| CEPA 6.2 | Protection of natural and semi-natural landscapes | Activities aimed at protecting natural and semi‑natural landscapes.<br><br>It includes:<br>• preservation of protected natural objects;<br>• rehabilitation of mining/quarrying sites;<br>• renaturalisation of river banks;<br>• burying electricity lines;<br>• maintenance of traditional landscapes;<br>• restoration of water bodies as habitats;<br>• biodiversity/landscape protection in agriculture.<br><br>It excludes:<br>• protection of historic monuments;<br>• aesthetic landscaping for economic purposes;<br>• protection of built‑up landscapes. |
| CEPA 6.3 | Measurement, control, laboratories and the like | Monitoring, analysis and inspection activities not classified elsewhere.<br><br>Includes censuses, inventories, databases of flora and fauna. |
| CEPA 6.4 | Other activities | All other activities aimed at protecting species, habitats and landscapes.<br><br>Includes ETIGA activities specific to CEPA 6 and government activities for quotas, regulation, monitoring, control (e.g., fishing), management of wild game reserves. |
| CEPA 8 | Research and development | R&D for prevention and elimination of pollution and for pollution measurement and analysis.<br><br>Includes:<br>• identification and analysis of pollution sources, dispersion mechanisms, effects on humans and ecosystems.<br><br>Excludes:<br>• R&D related to natural resource management (CReMA 15). |
| CEPA 8.2 | Protection of water | — |
| CEPA 8.4 | Protection of soil and groundwater | — |
| CEPA 8.6 | Protection of species and habitats | — |
| CEPA 8.8 | Other research on the environment | — |
| CEPA 9 | Other environmental protection activities | Regulation and ETIGA activities not classified elsewhere.<br><br>Includes:<br>• support to environmental decision‑making;<br>• regulation by government bodies;<br>• environmental management by businesses;<br>• activities not elsewhere classified. |
| CEPA 9.1 | General environmental administration and management | Includes:<br>• administration, management and support to environmental protection decisions;<br>• preparation of declarations or requests for permission;<br>• internal environmental management;<br>• environmental certification processes;<br>• consultancy, supervision and analysis;<br>• regulation by government. |
| CEPA 9.1.1 | General administration, regulation and the like | — |
| CEPA 9.1.2 | Environmental management | — |
| CEPA 9.2 | Education, training and information | Activities aimed at providing environmental education, training and information.<br><br>Includes:<br>• high school programs;<br>• university degrees or special courses;<br>• environmental reports and communication. |
| CEPA 9.4 | Activities not elsewhere classified | Environmental protection activities not classifiable under other CEPA classes.<br><br>Includes international financial aid where attribution to specific CEPA classes is difficult. |




## Mapping between mainKeyTypeOfMeasure and CEPA 2000 

*Table 11. Tentative mapping between the proposed mainKeyTypeOfMeasure classification and the CEPA 2000 classification.*
**Note: this table is not relevant for the reporting process, it is only relevant for the analysis of reported data.**

(Table 11)=
| mainKeyTypeOfMeasure (4th cycle)                                                               | Primary CEPA 2000 class | Rationale / Notes |
|------------------------------------------------------------------------------------------------|--------------------------|--------------------|
| B - Measure to implement recovery of costs for water services                                  | 14.2                     | Measures related to the recovery of costs for water services. |
| C - Measure to promote efficient and sustainable water use                                     | 14.2                     | Measures related to the efficient and sustainable use of water. |
| D - Measure to protect drinking water quality and reduce the level of treatment required       | 14.1                     | Measures related to the protection of drinking water quality. |
| E - Measure to control abstraction from surface and groundwater, and impoundment of surface water | 14.1                  | Measures related to abstraction control. |
| F - Measure to control artificial recharge or augmentation of groundwater                      | 14.1                     | Measures related to groundwater recharge. |
| G - Measure to control point source discharges                                                 | 14.1                     | Measures related to point source pollution control. |
| H - Measure to prevent or control inputs of diffuse pollutants                                 | 14.1                     | Measures related to diffuse pollution control. |
| I2-2 - Measure to address significant impacts - Altered habitats due to hydrological changes   | 12.1 / 12.2              | Measures related to hydromorphological pressures. |
| I2-4 - Measure to address significant impacts - Acidification                                  | 14.1                     | Measures related to acidification. |
| J - Measure to prohibit direct discharges to groundwater                                       | 14.1                     | Measures related to groundwater protection. |
| K - Measure to eliminate Priority Substances and reduce pollution by other substances          | 14.1                     | Measures related to Priority Substances and other pollutants. |
| L - Measure to prevent accidental pollution                                                    | 14.1                     | Measures related to accidental pollution. |
| X01 - Construction or upgrades of wastewater treatment plants                                  | 14.1                     | Measures related to wastewater treatment infrastructure. |
| X12 - Advisory services                                                                        | 14.1                     | Measures related to advisory services. |
| X14 - Research, improvement of knowledge, base reducing uncertainty                            | 14.1                     | Measures related to research and knowledge improvement. |
| X23 - Natural water retention measures                                                         | 12.1 / 12.2              | Measures related to natural water retention. |
| X24 - Climate change adaptation measure                                                        | 14.1                     | Measures related to climate change adaptation. |




