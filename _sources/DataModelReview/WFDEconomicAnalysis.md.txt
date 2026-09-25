(heading_wfd_economic_analysis)=
# Economic analysis

Last update: 2026-05-08

## Purpose and overview

The document revises the **Economic Analysis & Services** classes used in the 3rd cycle of reporting
of the Water Framework Directive River Basin Management Plans ({numref}`EconomicAnalysis_3rdCycle_ClassDiagram`)
and presents a proposal for the electronic reporting in the 4th cycle.

```{mermaid} /DataModelReview/mmd/EconomicAnalysis_3rdCycle_ClassDiagram.mmd
:name: EconomicAnalysis_3rdCycle_ClassDiagram
:align: center
:caption: Partial diagram for Economic Analysis and Water Services (RBMPPoM_2022) schema - 3rd cycle
```

## Proposed structure - 4th cycle

For the 4th cycle of reporting, the requested information detailed in (see also {numref}`EconomicAnalysis_4thCycle_Overview_ClassDiagram`):

```{mermaid} /DataModelReview/mmd/EconomicAnalysis_4thCycle_Overview_ClassDiagram.mmd
:name: EconomicAnalysis_4thCycle_Overview_ClassDiagram
:align: center
:caption: WFD Economic Analysis dataflow - 4th cycle
```

* The former questionnaire in the *EconomicAnalysis* class is removed.  

* The questionnaires in the new `CostRecovery` and `CostRecoveryPerService` tables maintains
  the same simplified Yes/No approach and requests information only for three collective services
  (drinking water supply services, irrigation water supply services and
  wastewater collection and treatment services).

* The *Service* table is removed. Information about volumes, revenues and costs is requested
  in the `VolumeRevenueCostPerService` table, using the standard structure for statistical data
  commonly used by Eurostat.

## Descriptive data - 4th cycle

### CostRecovery table

The questionnaire in the `CostRecovery` table
requests information at River Basin District level.
See {numref}`EconomicAnalysis_4thCycle_CostRecovery_ClassDiagram`
and {numref}`EconomicAnalysis_CostRecovery_Table`.

```{mermaid} /DataModelReview/mmd/EconomicAnalysis_4thCycle_CostRecovery_ClassDiagram.mmd
:name: EconomicAnalysis_4thCycle_CostRecovery_ClassDiagram
:align: center
:caption: CostRecovery table - 4th cycle
```

```{include} tables/EconomicAnalysis_CostRecovery_Table
```

### CostRecoveryPerService table

The questionnaire in the `CostRecoveryPerService` table
maintains the same simplified Yes/No approach and requests information
only for three collective services (drinking water supply services,
irrigation water supply services and wastewater collection and treatment services).
See {numref}`EconomicAnalysis_4thCycle_CostRecoveryPerService_ClassDiagram`
and {numref}`EconomicAnalysis_CostRecoveryPerService_Table`.

```{mermaid} /DataModelReview/mmd/EconomicAnalysis_4thCycle_CostRecoveryPerService_ClassDiagram.mmd
:name: EconomicAnalysis_4thCycle_CostRecoveryPerService_ClassDiagram
:align: center
:caption: CostRecoveryPerService table - 4th cycle
```

```{include} tables/EconomicAnalysis_CostRecoveryPerService_Table
```

### Data at water service level - overview

The data structure was simplified to a core set of quantitative data
for a limited number of water services and water user sectors.
The purpose is to obtain a consistent overview across Europe, at river basin district level.

Information is requested:

* about the physical volumes of water, the revenues and the costs
* for three water user sectors – agriculture, industry and households
  (see {numref}`EconomicAnalysis_Concepts_WaterUserSectors_Table`)
* and for three water services – public drinking water supply services,
  public irrigation water supply services and sewerage services
  (see {numref}`EconomicAnalysis_Concepts_WaterServices_Table`).

```{include} tables/EconomicAnalysis_Concepts_WaterUserSectors_Table
```

```{include} tables/EconomicAnalysis_Concepts_WaterServices_Table
```  

```{list-table} Overview diagram for the requested data on volumes, revenues and costs - 4th cycle
:name: EconomicAnalysis_Overview_PhysicalVolumeRevenueCost
:widths: 50 50
:width: 100%
:align: center

* - **a)**
  - **b)** and **c)**

* - ```{image} img/EconomicAnalysis_Overview_PhysicalVolume.png
    :width: 70%
    :align: center
    ```
  - ```{image} img/EconomicAnalysis_Overview_RevenueCost.png
    :width: 70%
    :align: center
    ```
* - **a) physical volumes of water**  
    The following flows are quantified:

    * volume of water abstraction from the environment (e.g. for self-supply and for public water supply),
    * volume of water supplied by public water services, 
    * and volume of wastewater discharged to the environment by public water services.

    The flows represented by grey arrows in the diagram are not required
    (water returned without use, e.g. due to evaporation or losses during transport,
    reused/recycled water supplied back to the water user sectors,
    direct discharges by the water user sectors).

    Note that the gross freshwater abstraction includes only
    water abstracted from inland surface and groundwater bodies –
    desalinated water and water imports are not quantified.
    The requested data are the estimated average annual volumes in million cubic metre,
    over a specified reference period, in the river basin district.

  - **b) revenues**  
    For the volumes in **a)**, the revenues are quantified:

    * from water abstraction (e.g. from environmental charges paid
      to the general government institutional sector as resource taxes),
    * from water supply (e.g. from volumetric service fees paid
      to the Water collection, treatment and supply (NACE 36.00) sector)
    * from wastewater collection and treatment (for example,
      from volumetric service fees paid to the Sewerage (NACE 37.00) sector)
    * and revenues from discharges to the environment, including emissions to water
      (for example, from environmental charges paid to the general government,
      which in this case may include pollution taxes).

    The requested data are the estimated average annual total revenue
    in million units of the national currency, in the river basin district,
    for the volumes quantified in **a)**.  

    **c) costs**  
    For the provision of the services quantified in **b)**,
    the total costs are to be quantified, distinguishing between CAPEX and OPEX.

```

The requested data on water volumes is detailed in {numref}`EconomicAnalysis_Conceptual_PhysicalVolume`.
The relevant concepts are aligned with the OECD/Eurostat Joint Questionnaire on Inland Waters
and the Eurostat Regional Water Questionnaire and defined in {numref}`EconomicAnalysis_Concepts_Volumes_Table`.

```{figure} img/EconomicAnalysis_Conceptual_PhysicalVolume.png
:name: EconomicAnalysis_Conceptual_PhysicalVolume
:align: center
:width: 70%
Conceptual diagram for the requested data on volumes - 4th cycle
```

```{include} tables/EconomicAnalysis_Concepts_Volumes_Table
```

All the information is requested at river basin district level
and must refer to the same reference year, preferably close to the programming period.

The following generic guidelines apply to the reporting of volumes:

* Volumes related to **water abstraction**
  (V1, V2, V3, V4, V5 in {numref}`EconomicAnalysis_Conceptual_PhysicalVolume`)
  are reported based on the location of the point of abstraction.
  Only abstractions from freshwater surface water bodies (rivers and lakes, including reservoirs)
  and groundwater bodies are considered.
* Volumes related to **water use**
  (V41, V52, V53 in {numref}`EconomicAnalysis_Conceptual_PhysicalVolume`)
  are reported based on the location of the point of use/consumption.
  In other words, the volumes refer to water used in the river basin district.
* Volumes related to **water returns**
  (V6 in {numref}`EconomicAnalysis_Conceptual_PhysicalVolume`)
  are reported based on the location of the point of wastewater discharge.
  This includes discharges also to transitional and coastal water bodies
  located in the river basin district.  

Given the guidelines above, and the fact that the data is requested
at river basin district level (RBD), the following corollaries apply:

* The balance condition **V4 ≈ V41** is not expected to hold,
  due to losses during transport and water returned without use (which result in V4 > V41)
  or due to transfers between river basin districts (which may result in V41 > V4).  
* The balance condition **V5 ≈ V52 + V53** is not expected to hold,
  again due to losses and transfers between river basin districts,
  including the cases where the user/consumer is outside the river basin district
  where the water is abstracted.  
* Note that V62 and V63 refer
  to the volume of wastewater collected and treated by the sanitary services,
  and not to the amount of wastewater generated by the manufacturing industry and household sectors.
  Note also that the condition **V62 + V63 ⪅ V6** is expected to hold,
  because V62 and V63 represent a partial apportionment of V6,
  i.e. of the total volume of treated effluents discharged in the river basin district.
  The equality **V62 + V63 ≈ V6** is not expected to hold
  (it would only hold if the contribution both of urban run‑off
  and wastewater from other water user sectors were negligible).  
* Finally, the condition **V52 + V53 ≈ V62 + V63** is not expected to hold
  if the discharges include a significant amount of wastewater collected
  from users located outside the basin.

The requested data on revenues is detailed in {numref}`EconomicAnalysis_Conceptual_Revenue`.
The information must refer to the same year and to the same totals reported for the volumes of water.

The following generic guidelines apply to the reporting of revenues:

* **Water abstraction** revenues
  (R1, R2, R3, R4, R5 in {numref}`EconomicAnalysis_Conceptual_Revenue`)
  must include all environmental/resource taxes and administrative fees paid
  (directly or indirectly) to the general government.  
* **Water supply** revenues
  (R41, R52, R53 in {numref}`EconomicAnalysis_Conceptual_Revenue`)
  represent the gross revenue of the irrigation water service providers
  and the drinking water service providers from fees charged to the end‑user sector
  (agriculture, manufacturing industry and households).
  The gross revenue must include the base service fee plus any environmental or resource costs
  incurred during abstraction that are passed through to the consumer
  to ensure an adequate contribution from that sector.  
* **Wastewater discharges** revenues
  (R6 in {numref}`EconomicAnalysis_Conceptual_Revenue`)
  must include all environmental taxes and pollution levies
  paid directly or indirectly to the government
  for the emission of pollutants back into the environment.  
* **Sewerage services** revenues
  (R62 and R63 in {numref}`EconomicAnalysis_Conceptual_Revenue`)
  represent gross revenue for wastewater collection and treatment services.
  The revenue must include the service fees charged to users
  plus any internalised environmental charges related to the final discharge
  that are passed on to the households or industrial users.

```{figure} img/EconomicAnalysis_Conceptual_Revenue.png
:name: EconomicAnalysis_Conceptual_Revenue
:align: center
:width: 75%
Conceptual diagram for the requested data on revenues - 4th cycle
```

Regarding the costs, the data is again requested for the same year
for which volumes and revenues are reported.
The total costs, OPEX and CAPEX should be reported for each of the three services
in {numref}`EconomicAnalysis_Conceptual_Revenue`, as well as the estimated global cost recovery rate.

The following generic guidelines apply to the reporting of costs:

* Grant‑financed assets should be included in capital expenditure (CAPEX)
  estimates for the water service that acquires and owns the asset,
  and regardless of the source of funding [^CAPEX].  
* Environmental taxes should be included in the current expenditure (OPEX)
  estimates for the water services [^OPEX].

[^CAPEX]: According to Eurostat’s methodological frameworks,
specifically the Environmental Protection Expenditure Accounts (EPEA)
and the European System of Accounts (ESA 2010),
grant-financed assets should be included in capital expenditure (CAPEX) estimates
for the sector that acquires and owns the asset.
In Eurostat statistics, CAPEX is primarily measured as Gross Fixed Capital Formation (GFCF).
GFCF consists of resident producers' acquisitions, less disposals, of fixed assets during a given period.
The recording of an asset's acquisition in GFCF is based
on the change of ownership and the total value of the asset at the time of purchase.
It does not depend on whether the purchase was funded through internal cash flow, loans, or external grants.

[^OPEX]: Current expenditure includes intermediate consumption (goods and services used in production),
compensation of employees, and other taxes on production.
Taxes such as those on water abstraction or pollution discharges are considered "taxes on production"
because they are unrequited payments to the government linked to the ongoing activity of the utility.

### VolumeRevenueCostPerService table

{numref}`EconomicAnalysis_4thCycle_VolumeRevenueCostPerService_ClassDiagram` presents
the standardised structure for the reporting of volumes, revenues and costs per water service,
using the `ServiceVolumeRevenueCost` table. The column names reflect the SDMX designations
(geo, time, dimension, obs_value, obs_unit, obs_status, obs_comment) typically used by Eurostat.

* Volumes must be reported in million cubic metre, revenues and costs
  must be reported in million units of national currency
  (except for the cost recovery rate, which is reported as a percentage).

* The dimension codes for the reporting of costs per water service
  are presented in {numref}`Codelist_4thCycle_EconomicAnalysis_Dimension_Costs_Table`.

* The dimension codes for the reporting of volumes and revenues
  are presented in {numref}`Codelist_4thCycle_EconomicAnalysis_Dimension_VolumesRevenues_Table`.

```{mermaid} /DataModelReview/mmd/EconomicAnalysis_4thCycle_VolumeRevenueCostPerService_ClassDiagram.mmd
:name: EconomicAnalysis_4thCycle_VolumeRevenueCostPerService_ClassDiagram
:caption:  VolumeRevenueCostPerService table - volume, revenue and costs per water service – 4th cycle
:align: center
```

```{include} tables/Codelist_4thCycle_EconomicAnalysis_Dimension_Costs_Table
```

```{include} tables/Codelist_4thCycle_EconomicAnalysis_Dimension_VolumesRevenues_Table
```

(heading_wfd_economic_analysis_documents_dataset_4th_cycle)=
## Documents dataset - 4th cycle

The Documents dataset follows the standard structure used in various WISE dataflows
({numref}`EconomicAnalysis_4thCycle_Documents_ClassDiagram`):

* The `dcMetadata` table provides the basic Dublin Core metadata elements about the delivery.
  
  - If required by the data providers,
    the `licenseDocument` attribute allow the provision
    of additional information about the dataset.
  - The `dcMetadata` table also functions as a "manifest file"
    explaining if the delivery contains data for a given river basin district or not.

* The `Document` table allows the upload of documents (for example, PDFs)
  or the provision of a `hyperlink` to a document stored in a publicly accessible national web site.

```{mermaid} /DataModelReview/mmd/EconomicAnalysis_4thCycle_Documents_ClassDiagram.mmd
:name: EconomicAnalysis_4thCycle_Documents_ClassDiagram
:caption: WFD EconomicAnalysis dataflow - 4th cycle - Documents
:align: center
```

The following criteria apply:

01. The `dcMetadata` table must contain *one and only one* record
    for each of the country's river basin districts, identified by the `euRBDCode`.

02. The descriptive dataset tables are **national**,
    but the quality control will allow deliveries
    where some of the river basin districts have `includesDescriptiveData = no`.

## Annexes - Ancillary data sources

Information about annual volumes is reported voluntarily by MS
under the OECD/Eurostat Joint Questionnaire
on Inland Waters and Eurostat Regional Water Questionnaire [^NWAT] [^RWAT].
Although the questionnaires have a much higher level of detail
than required for the 4th cycle of electronic reporting,
it is important that MS provide consistent data,
which may allow more detailed analysis to be performed if necessary.

{numref}`EconomicAnalysis_OECDEurostat_AnnualFreshwaterAbstraction`,
{numref}`EconomicAnalysis_OECDEurostat_WaterUseBySupplyCategory` and
{numref}`EconomicAnalysis_OECDEurostat_WasteWater` provide an overview
of some of the OECD/Eurostat Joint Questionnaire tables and dimensions
that are directly related to the data requested for the WFD 4th cycle of reporting.

```{include} tables/EconomicAnalysis_OECDEurostat_AnnualFreshwaterAbstraction
```

```{include} tables/EconomicAnalysis_OECDEurostat_WaterUseBySupplyCategory
```

```{include} tables/EconomicAnalysis_OECDEurostat_WasteWater
```

[^NWAT]: See [https://ec.europa.eu/eurostat/cache/metadata/en/env_nwat_esms.htm](https://ec.europa.eu/eurostat/cache/metadata/en/env_nwat_esms.htm)

[^RWAT]: See [https://ec.europa.eu/eurostat/cache/metadata/en/env_rwat_esms.htm](https://ec.europa.eu/eurostat/cache/metadata/en/env_rwat_esms.htm)

## References

```{footbibliography}
```

```{warning}
The original document containing this revised model
can still be downloaded but should no longer be used.
See **PROPOSAL - Version 2026.02.20** 
{download}`PDF </DataModelReview/pdf/WFD_4th_cycle_EconomicAnalysis_v20260220.pdf>`
```
