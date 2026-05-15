(heading_wfd_economic_analysis)=
# WFD economic analysis

Last update: 2026-05-08

```{warning}
The online version of the text is being reviewed.  
See **PROPOSAL - Version 2026.02.20** {download}`PDF </DataModelReview/pdf/WFD_4th_cycle_EconomicAnalysis_v20260220.pdf>`
```

## Purpose and overview

The document revises the **Economic Analysis & Services** classes used in the 3rd cycle of reporting of the Water Framework Directive River Basin Management Plans ({numref}`EconomicAnalysis_Classdiagram`) and presents a proposal for the electronic reporting in the 4th cycle ({numref}`EconomicAnalysis_RevenueandCosts`).

The former questionnaire in the *EconomicAnalysis* class is removed.

The questionnaire in the *CostRecovery* and *CostRecoveryPerService* tables maintains the same simplified Yes/No approach and requests information only for three collective services (drinking water supply services, irrigation water supply services and wastewater collection and treatment services).

The *Service* table is removed. Information about volumes, revenues and costs is requested in the *VolumeRevenueCostPerService* table, using the standard structure for statistical data commonly used by Eurostat.


```{mermaid} /DataModelReview/mmd/EconomicAnalysisclassDiagram.mmd
:name: EconomicAnalysis_Classdiagram
:align: center
:caption: Partial class diagram for Economic Analysis and Water Services (RBMPPoM_2022) schema.
```


```{mermaid} /DataModelReview/mmd/EconomicAnalysis_RevenueandCosts.mmd
:name: EconomicAnalysis_RevenueandCosts
:align: center
:caption: Cost recovery questionnaire and volume, revenue and costs per service – 4th cycle of reporting
```

## Cost Recovery – 4ᵗʰ cycle

The former questionnaire in the *EconomicAnalysis* class is removed.

The questionnaire in the *CostRecovery* and *CostRecoveryPerService* tables ({numref}`Figure3EconomicAnalysis`) maintains the same simplified Yes/No approach and requests information only for three collective services (drinking water supply services, irrigation water supply services and wastewater collection and treatment services).

({numref}`EconomicAnalysis_CostRecoveryTable`) lists the content of the questionnaire.

```{include} tables/EconomicAnalysis_CostRecoveryTable
```

(Figure 3)=
```{mermaid} /DataModelReview/mmd/Figure3EconomicAnalysis.mmd
:name: Figure3EconomicAnalysis
:align: center
:caption: CostRecovery – 4ᵗʰ cycle of reporting   Figure 4 . CostRecoveryPerService – 4ᵗʰ cycle of reporting*
```

## Water Services Data – 4ᵗʰ cycle

The data structure was simplified to a core set of quantitative data for a limited number of water services and water user sectors. The purpose is to obtain a consistent overview across Europe, at river basin district level.

Information is requested:<br>• about the physical volumes of water, the revenues and the costs ({ref}`Figure 5 <Figure 5>`),<br>• for three water user sectors – agriculture, industry and households ({numref}`EconomicAnalysis_WaterSectors4thcycle _Table`),<br>• and for three water services – public drinking water supply services, public irrigation water supply services and sewerage services.



(Figure 5)=
| a) | b) and c) |
|---------|---------|
| <img src="img/EconomicAnalysisPhysicalvolume.PNG" width="300"> | <img src="img/EconomicAnalysisRevenue.PNG" width="300"> |

*Figure 5.Overview diagram for the requested data on volumes, revenues and costs – 4ᵗʰ cycle of reporting.*

<div style="display: flex; gap: 20px;">

<div style="flex: 1;">
<p><strong>a) Physical volume</strong><br>
The following flows are quantified: volume of water abstraction from the environment (e.g. for self‑supply and for public water supply), volume of water supplied by public water services, and volume of wastewater discharged to the environment by public water services.

The flows represented by grey arrows in the diagram are not required (water returned without use, e.g. due to evaporation or losses during transport, reused/recycled water supplied back to the water user sectors, direct discharges by the water user sectors).

Note that the gross freshwater abstraction includes only water abstracted from inland surface and groundwater bodies – desalinated water and water imports are not quantified. The requested data are the estimated average annual volumes in million cubic metres, over a specified reference period, in the river basin district.</p>
</div>

<div style="flex: 1;">
<p><strong>b) Revenue</strong><br>
For the volumes identified in a), the revenues from water abstraction (e.g. from environmental charges paid to the general government institutional sector as resource taxes), revenues from water supply (e.g. from volumetric service fees paid to the Water collection, treatment and supply (NACE 36.00) sector), revenues from wastewater collection and treatment (for example, from volumetric service fees paid to the Sewerage (NACE 37.00) sector) and revenues from discharges to the environment, including emissions to water (for example, from environmental charges paid to the general government, which in this case may include pollution taxes).

The requested data are the estimated average annual total revenue in million units of the national currency, in the river basin district, for the volumes quantified in a).<br>
<strong>c) Cost</strong><br>
For the provision of the services quantified in a) and b), the total costs are to be quantified, distinguishing between CAPEX and OPEX.

</p>
</div>

</div>

The requested data on water volumes is detailed in ({numref}`conceptualvolume`). The relevant concepts are aligned with the OECconceptualvolumeD/Eurostat Joint Questionnaire on Inland Waters and the Eurostat Regional Water Questionnaire and defined in ({numref}`EconomicAnalysis_Conceptsanddefinitions`).

```{figure} img/EconomicAnalysisConceptualVolume.PNG
:name: conceptualvolume
:align: center
:width: 100%
Conceptual diagram for the requested data on volumes – 4ᵗʰ cycle of reporting.
```



```{include} tables/EconomicAnalysis_WaterSectors4thcycle _Table
```                                                                                                                                              


```{include} tables/EconomicAnalysis_WaterServices_Table
```  


All the information is requested at river basin district level and must refer to the same reference year, preferably close to the programming period.

The following generic guidelines apply to the reporting of volumes:<br>• Volumes related to **water abstraction** (V1, V2, V3, V4, V5 in ({numref}`conceptualvolume`)) are reported based on the location of the point of abstraction. Only abstractions from freshwater surface water bodies (rivers and lakes, including reservoirs) and groundwater bodies are considered.<br>• Volumes related to **water use** (V41, V52, V53 in ({numref}`conceptualvolume`)) are reported based on the location of the point of use/consumption. In other words, the volumes refer to water used in the river basin district.<br>• Volumes related to **water returns** (V6 in ({numref}`conceptualvolume`) are reported based on the location of the point of wastewater discharge. This includes discharges also to transitional and coastal water bodies located in the river basin district.<br>

Given the guidelines above, and the fact that the data is requested at river basin district level (RBD), the following corollaries apply:
<br>• The balance condition V4 ≈ V41 is not expected to hold, due to losses during transport and water returned without use (which result in V4 > V41) or due to transfers between river basin districts (which may result in V41 > V4).<br>• The balance condition V5 ≈ V52 + V53 is not expected to hold, again due to losses and transfers between river basin districts, including the cases where the user/consumer is outside the river basin district where the water is abstracted.<br>• Note that V62 and V63 refer to the volume of wastewater collected and treated by the sanitary services, and not to the amount of wastewater generated by the manufacturing industry and household sectors. Note also that the condition V62 + V63 ⪅ V6 is expected to hold, because V62 and V63 represent a partial apportionment of V6, i.e. of the total volume of treated effluents discharged in the river basin district. The equality V62 + V63 ≈ V6 is not expected to hold (it would only hold if the contribution both of urban run‑off and wastewater from other water user sectors were negligible).<br>• Finally, the condition V52 + V53 ≈ V62 + V63 is not expected to hold if the discharges include a significant amount of wastewater collected from users located outside the basin.



```{include} tables/EconomicAnalysis_Conceptsanddefinitions
```


*Adapted from: Eurostat & OECD. (2024). Data Collection Manual for the OECD/Eurostat Joint Questionnaire on Inland Waters and Eurostat Regional Water Questionnaire (Version 5). Eurostat.*

The requested data on revenues is detailed in {numref}`Economic_Analysis_ConceptualRevenue`). The information must refer to the same year and to the same totals reported for the volumes of water.

The following generic guidelines apply to the reporting of revenues:<br>• **Water abstraction** revenues (R1, R2, R3, R4, R5 in {numref}`Economic_Analysis_ConceptualRevenue`) must include all environmental/resource taxes and administrative fees paid (directly or indirectly) to the general government.<br>• **Water supply** revenues (R41, R52, R53 in {numref}`Economic_Analysis_ConceptualRevenue`) represent the gross revenue of the irrigation water service providers and the drinking water service providers from fees charged to the end‑user sector (agriculture, manufacturing industry and households). The gross revenue must include the base service fee plus any environmental or resource costs incurred during abstraction that are passed through to the consumer to ensure an adequate contribution from that sector.<br>• **Wastewater discharges** revenues (R6 in {numref}`Economic_Analysis_ConceptualRevenue`) must include all environmental taxes and pollution levies paid directly or indirectly to the government for the emission of pollutants back into the environment.<br>• **Sewerage services** revenues (R62 and R63 in {numref}`Economic_Analysis_ConceptualRevenue`) represent gross revenue for wastewater collection and treatment services. The revenue must include the service fees charged to users plus any internalised environmental charges related to the final discharge that are passed on to the households or industrial users.


```{figure} img/EconomicAnalysisConceptualRevenue.PNG
:name: Economic_Analysis_ConceptualRevenue
:align: center
:width: 100%
Conceptual diagram for the requested data on revenues – 4ᵗʰ cycle of reporting.
```
Regarding the costs, the data is again requested for the same year for which volumes and revenues are reported. The total costs, OPEX and CAPEX should be reported for each of the three services in ({numref}`Economic_Analysis_ConceptualRevenue`), as well as the estimated global cost recovery rate.

The following generic guidelines apply to the reporting of costs:<br>• Grant‑financed assets should be included in capital expenditure (CAPEX) estimates for the water service that acquires and owns the asset, and regardless of the source of funding ([^1]).<br>• Environmental taxes should be included in the current expenditure (OPEX) estimates for the water services ([^2]).<br>


[^1]: According to Eurostat’s methodological frameworks, specifically the Environmental Protection Expenditure Accounts (EPEA) and the European System of Accounts (ESA 2010), grant-financed assets should be included in capital expenditure (CAPEX) estimates for the sector that acquires and owns the asset. In Eurostat statistics, CAPEX is primarily measured as Gross Fixed Capital Formation (GFCF). GFCF consists of resident producers' acquisitions, less disposals, of fixed assets during a given period. The recording of an asset's acquisition in GFCF is based on the change of ownership and the total value of the asset at the time of purchase. It does not depend on whether the purchase was funded through internal cash flow, loans, or external grants.
[^2]: Current expenditure includes intermediate consumption (goods and services used in production), compensation of employees, and other taxes on production. Taxes such as those on water abstraction or pollution discharges are considered "taxes on production" because they are unrequited payments to the government linked to the ongoing activity of the utility.

({numref}`EconomicAnalysis_Volume`) presents the standardised structure for the reporting of volumes, revenues and costs per water service. Volumes must be reported in million cubic metre, revenues and costs must be reported in million units of national currency (except for the cost recovery rate, which is reported as a percentage).

The dimension codes for the reporting of costs per water service are presented in {numref}`EconomicAnalysis_Volume`.  
The dimension codes for the reporting of volumes and revenues are presented in ({numref}`EconomicAnalysis_VolumesandRevenues_4thcycle`).


(Figure)=
```{mermaid} /DataModelReview/mmd/EconomicAnalysis_Volume.mmd
:name: EconomicAnalysis_Volume
:caption: Reporting of volume, revenue and costs per water service – 4ᵗʰ cycle of reporting  
:align: center
```
See also in ([^3])
[^3]: ({numref}`EconomicAnalysis_Volume`) presents a structure for the ServiceVolumeRevenueCost table where the column names reflect the SDMX designations (geo, time, dimension, obs_value, obs_unit, obs_status, obs_comment) typically used by Eurostat. The diagram below is merely illustrative: for data reporters involved in the EIONET WISE SoE dataflows, it shows that there is a one-to-one equivalence with the column names used in many of the EIONET dataflows (which reflect the OGC Observations and Measurements conceptual model).


```{table} Dimension codes for the reporting of costs per water service – 4ᵗʰ cycle of reporting
:name: measures_4th cycle reportingcosts_table
:width: 100%

| Dimension     | Description                                                |
|---------------|------------------------------------------------------------|
| CST_IRR_TOT   | Irrigation water services – Total cost                     |
| CST_IRR_CAP   | Irrigation water services – Capital expenditure            |
| CST_IRR_OPE   | Irrigation water services – Operational expenditure        |
| CST_IRR_CRR   | Irrigation water services – Cost recovery rate             |
| CST_DRI_TOT   | Drinking water services – Total cost                       |
| CST_DRI_CAP   | Drinking water services – Capital expenditure              |
| CST_DRI_OPE   | Drinking water services – Operational expenditure          |
| CST_DRI_CRR   | Drinking water services – Cost recovery rate               |
| CST_WWT_TOT   | Sewerage services – Total cost                             |
| CST_WWT_CAP   | Sewerage services – Capital expenditure                    |
| CST_WWT_OPE   | Sewerage services – Operational expenditure                |
| CST_WWT_CRR   | Sewerage services – Cost recovery rate                     |
```

```{mermaid} /DataModelReview/mmd/EconomicAnalysis_VolumeRevenueCost.mmd
:align: center
```


```{include} tables/EconomicAnalysis_VolumesandRevenues_4thcycle
```


*Includes both direct and indirect payments to the general government institutional sector. May also include payments to private sector owners.*  

**Codes used in the diagrams of ({numref}`conceptualvolume`) and ({numref}`Economic_Analysis_ConceptualRevenue`).**

## Ancillary Data Sources

Information about annual volumes is reported voluntarily by MS under the OECD/Eurostat Joint Questionnaire on Inland Waters and Eurostat Regional Water Questionnaire ([^4],[^5]). Although the questionnaires have a much higher level of detail than required for the 4ᵗʰ cycle of electronic reporting, it is important that MS provide consistent data, which may allow more detailed analysis to be performed if necessary.

[^4]: See [https://ec.europa.eu/eurostat/cache/metadata/en/env_nwat_esms.htm](https://ec.europa.eu/eurostat/cache/metadata/en/env_nwat_esms.htm)

[^5]: See [https://ec.europa.eu/eurostat/cache/metadata/en/env_rwat_esms.htm](https://ec.europa.eu/eurostat/cache/metadata/en/env_rwat_esms.htm)

Tables {numref}`measures_freshwater_abstraction`,{numref}`measures_supplycategory`,{numref}`measures_Wastewater` provides an overview of some of the OECD/Eurostat Joint Questionnaire tables and dimensions that are directly related to the data requested for the WFD 4ᵗʰ cycle of reporting.

Overview of relevant tables and dimensions in the OECD/Eurostat Joint Questionnaire.  



```{table} Annual freshwater abstraction by source (dimension 1) and by sector (dimension 2).
:name: measures_freshwater_abstraction
:width: 100%

| Dimension 1 | Dimension 2   | Description                                                     |
|-------------|----------------|-----------------------------------------------------------------|
| FSW         | ABST           | 1. Fresh surface water total gross abstraction (NACE 01–99)     |
| FSW         | ABS_PWS        | by Public water supply                                          |
| FSW         | ABS_AGR        | by Agriculture, forestry, fishing (NACE 01–03)                  |
| FSW         | ABS_AGR_IR     | of which for irrigation                                         |
| FSW         | ABS_IND        | by Manufacturing industry (NACE 10–33)                          |
| FSW         | ABS_HH         | by Private households                                           |
| FGW         | ABST           | 2. Fresh groundwater total gross abstraction (NACE 01–99)       |
| FGW         | ABS_PWS        | by Public water supply                                          |
| FGW         | ABS_AGR        | by Agriculture, forestry, fishing (NACE 01–03)                  |
| FGW         | ABS_AGR_IR     | of which for irrigation                                         |
| FGW         | ABS_IND        | by Manufacturing industry (NACE 10–33)                          |
| FGW         | ABS_HH         | by Private households                                           |
```



```{table} Water use by supply category (dimension 1) and by sector (dimension 2).
:name: measures_supplycategory
:width: 100%

| Dimension 1 | Dimension 2 | Description                                      |
|-------------|-------------|--------------------------------------------------|
| PWS         | TOTAL_HH    | 1. Public water supply – TOTAL (NACE 01–99)      |
| PWS         | A           | Agriculture, forestry, fishing (NACE 01–03)      |
| PWS         | C           | – Manufacturing industry (NACE 10–33)            |
| PWS         | EP_HH       | Private households                               |
| SOWS        | TOTAL_HH    | 2. Self and other water supply – TOTAL (NACE 01–99) |
| SOWS        | A           | Agriculture, forestry, fishing (NACE 01–03)      |
| SOWS        | C           | – Manufacturing industry (NACE 10–33)            |
| SOWS        | EP_HH       | Private households                               |
```

```{table} Generation, treatment and discharges of wastewater: volumes (dimension 1).
:name: measures_Wastewater
:width: 100%

| Dimension 1 | Dimension 2      | Description                                                             |
|-------------|------------------|-------------------------------------------------------------------------|
| VOL_WWV     | GEN_PS           | GENERATION OF WASTEWATER – POINT SOURCES – Total (NACE 01–99)          |
| VOL_WWV     | GEN_AGR          | Agriculture, forestry, fishing (NACE 01–03)                             |
| VOL_WWV     | GEN_IND          | Industry – total (NACE 05–43)                                           |
| VOL_WWV     | GEN_MAN          | – Manufacturing industry (NACE 10–33)                                   |
| VOL_WWV     | GEN_DOM          | Domestic sources – total                                                |
| VOL_WWV     | GEN_HH           | – Private households                                                    |
| VOL_WWV     | GEN_URB          | Urban wastewater – total generated                                      |
| VOL_WWV     | TRT_URB_IF       | – Treatment in WWTPs – total inflow                                     |
| VOL_WWV     | GEN_IND_XURB     | Industrial wastewater (not part of Urban WWV) – total generated         |
| VOL_WWV     | DIS_IND_IW       | – Discharges to inland waters – Total                                   |
| VOL_WWV     | DIS_IND_IW_AT    | of which: Discharges to inland waters after treatment                   |
| VOL_WWV     | DIS_IND_IW_NT    | of which: Discharges to inland waters without treatment                 |
| VOL_WWV     | DIS              | Total discharges of WWTP’s (urban and other) – after treatment          |
```
