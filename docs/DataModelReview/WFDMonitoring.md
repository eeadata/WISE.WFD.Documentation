(heading_wfd_monitoring)=
# WFD - Monitoring

```{warning}
The online version of the text is being reviewed.  
It will be modified to include the combined reporting of the MonitoringSite dataset and the Monitoring data.
```
(heading_wfd_monitoring_3rd_cycle)=
## Monitoring schema - 3ʳᵈ cycle

The 2016 and 2022 WFD reporting guidance documents 
clarify the content of the information requested in the **Monitoring** schema, in accordance to Article 8 of the WFD.  
The information requested in the electronic reporting refers to past monitoring, and not to planned monitoring, 
with exceptional cases allowed for in the 3ʳᵈ cycle reporting guidance (see excerpts below).

The 2016 and 2022 WFD reporting guidance documents also highlight the connection to the EEA voluntary dataflows,
and the expectation that Member States report the monitoring results under the WISE SoE dataflows.
This would have allowed the requested information to be derived from the WISE SoE dataflows, 
thus making redundant the electronic reporting under the RBMPs.

Given that, in 2016, the WISE SoE dataflows were under revision, 
information about the 2nd cycle monitoring programmes was requested in the WFD 2016 electronic reporting 
(see {numref}`Monitoring_2016`).

For the 3ʳᵈ cycle reporting, in 2022, 
the analysis of the content of the WISE SoE reporting showed issues 
in the completeness of the voluntary reporting of monitoring results for water quality: 
it would not have been possible to derive the requested monitoring information from the EEA Waterbases.
Therefore, the reporting schema was simplified (see {numref}`Monitoring_2022`),
but kept in the WFD 2022 electronic reporting.

In preparation on the 4ᵗʰ cycle reporting,
a similar analysis of the current content of the WISE SoE reporting was done.  
(See examples related to Atrazine in the last section of this document.) 

While the European coverage of the WISE SoE reporting remains fragmentary,
it is clear that some Member States provide detailed and abundant data 
that likely reflects the existing WFD monitoring programmes.  
For such Member States, reporting derived statistics about sampling frequency and period 
in the 4ᵗʰ cycle electronic reporting is duplicate reporting and an unnecessary reporting burden.


***Extracts from 2016 WFD Reporting Guidance for the 2nd cycle (pg. 93-100)***

> "Reporting should reflect the monitoring carried out that has informed the second RBMPs. 
> Given that monitoring programmes are usually dynamic and multi‐annual 
> (i.e. in the cases of quality elements with lower frequencies of monitoring), 
> reporting should reflect, as accurately as possible, 
> the monitoring that has informed the preparation of the second RBMPs. 
> Reporting is not intended to include information regarding future monitoring programmes or planned changes."
  
> "The data and information on monitoring to be reported under Article 8 of the WFD 
> include a description of the monitoring sites, a specification of the different QEs and chemical substances
> monitored at each site, and information relating to the associated monitoring programmes."
  
> "Member States are expected to report to EEA WISE SoE:
> * Water quality results including Priority Substances and River Basin Specific Pollutants 
>   to EEAs Waterbases on groundwater, rivers, lakes, transitional waters and coastal waters
> * Results from monitoring Biological Quality Elements 
>   to EEAs Waterbases on rivers, lakes, transitional waters and coastal waters."

```{figure} img/Monitoring_2016.png
:name: Monitoring_2016
:align: center
:width: 75%

Monitoring_2016 Schema - 2nd cycle - Obsolete
```


***Extracts from the 2022 WFD Reporting Guidance for the 3ʳᵈ cycle (pg. 90-97)***

> "Reporting should reflect the monitoring that was carried out and informed the third RBMPs. 
> It is not intended to include information regarding future monitoring programmes. 
> It can include planned changes when sufficient information is already available 
> on the QEs, substances or parameters that will be monitored and at which frequency. 
> In these cases, the date of the last monitoring should be reported as ‘9999’, as mentioned in the specific guidance below."
  
> "The data and information on monitoring to be reported under Article 8 of the WFD 
> include a description of the monitoring sites, a specification of the different QEs and chemical substances
> monitored at each site, and information relating to the associated monitoring programmes."
  
> "Member States are expected to report to EEA WISE SoE:
> * Water quality results, including Priority Substances and River Basin Specific Pollutants, 
>   to Waterbases on groundwater, rivers, lakes, transitional waters and coastal waters
> * Results from monitoring Biological Quality Elements to Waterbases on rivers, lakes, transitional waters and coastal waters"


```{figure} img/Monitoring_2022.png
:name: Monitoring_2022
:align: center
:width: 75%

Monitoring_2022 Schema - 3ʳᵈ cycle - Obsolete
```

(heading_wfd_monitoring_4th_cycle)=
## Monitoring table - 4ᵗʰ cycle

For the 4ᵗʰ cycle of reporting, the requested information is further simplified (see {numref}`DescriptiveMonitoring4thcycle`):

* Information about the monitoring programmes is provided in the RBMP documents only: 
  only the reference to the supporting documents is requested in the **MonitoringProgrammes** table. 

  The information can be provided at national level (by ommitting the euRBDCode), 
  or the River Basin District level (by providing the euRBDCode each of the national RBDs). 

  Note that:

  * the options **gwChemicalMonitoringReference = NULL** and **gwQuantitativeMonitoringReference =  NULL** 
    are only valid if applied to River Basin Districts without designated groundwater bodies;
  * the options **swChemicalMonitoringReference =  NULL** and **swEcologicalMonitoringReference =  NULL** 
   are only valid  if applied to River Basin Districts without designated surface water bodies (if any).
   
* The **useWaterbaseForMonitoringData** attribute allows data provider to indicate that the monitoring data statistics 
  should be derived from the data reported to Waterbase.
  
  Note that:
  
  * This applies to all surface water monitoring 
    *except Biological Quality Elements (QE1) and Hydromorphological Quality Elements (QE2)*
    
  * This applies to all groundwater monitoring
    *except Quantitative Monitoring*

* Finally, a single simplified **Monitoring** table is proposed.

  For the 5th cycle of reporting, in 2033, it is expected that information about monitoring parameters, frequency, etc., 
  can be derived from monitoring observations reported under the WISE-2, WISE-6 and WISE-3 dataflow.
  The derived information would then fully replace the Monitoring table in the RBMP electronic reporting.
  
  * The **frequency** and **cycle** values are codified, to avoid ambiguities in the reporting and interpretation of results,
    while mantaining the definitions used in the 2nd and 3rd RBMPs.

```{mermaid}
:name: DescriptiveMonitoring4thcycle
:caption:  Descriptive data - Monitoring - 4ᵗʰ cycle
:align: center
:zoom:
%%{init: {'theme': 'neutral'}}%%
classDiagram
direction LR

namespace Reporting{

  class MonitoringProgrammes{
    + euRBDCode : wiseIdentifier [0..1]
    + useWaterbaseForMonitoringData : YesNo
    + programmesReference : referenceIdentifier
    + investigativeMonitoringReference : referenceIdentifier
    + operationalMonitoringReference : referenceIdentifier
    + surveillanceMonitoringReference : referenceIdentifier
    + gwChemicalMonitoringReference : referenceIdentifier [0..1]
    + gwQuantitativeMonitoringReference : referenceIdentifier [0..1]
    + swChemicalMonitoringReference : referenceIdentifier [0..1]
    + swEcologicalMonitoringReference : referenceIdentifier [0..1]
  }

  class Monitoring{
    + euMonitoringSiteCode : wiseIdentifier
    + parameterCode : ParameterCode
    + chemicalMatrix : ChemicalMatrixType [0..1]
    + chemicalPurpose : ChemicalPurpose [0..1]
    + frequency : FrequencyCode
    + cycle : CycleCode
    + lastMonitored : Year
  }
}

```
(heading_wfd_monitoring_codelists_4th_cycle)=
## Codelists associated with the Monitoring table - 4ᵗʰ cycle

The diagram below present the codelists applicable to **Monitoring** table, which simplify and clarify codelists adopted in the 3ʳᵈ cycle.

Note that for quality elements under QE3 (General parameters), the CAS code or EEA code must be used.
Note also that the option 'EEA_00-00-0 - Other parameter' will *not* be available in the 4ᵗʰ cycle of reporting.

```{mermaid}
:name: CodelistsDescriptiveMonitoring4thcycle
:caption:  Codelists - Monitoring - 4ᵗʰ cycle
:align: center
:zoom:
%%{init: {'theme': 'neutral'}}%%
classDiagram
direction LR
namespace Codelist{

    class ParameterCode{
      <<enumeration>>

      «quantitative monitoring»
      EEA_00-01-1 - Quantitative monitoring

      «biological quality elements»
      QE1-1 - Phytoplankton
      QE1-2 - Other aquatic flora
      QE1-2-1 - Macroalgae
      QE1-2-2 - Angiosperms
      QE1-2-3 - Macrophytes
      QE1-2-4 - Phytobenthos
      QE1-3 - Benthic invertebrates
      QE1-4 - Fish

      «hydromorphological quality elements»
      QE2-1 - Hydrological or tidal regime
      QE2-2 - River continuity conditions
      QE2-3 - Morphological conditions

      «CAS codes and EEA codes under WISE-6»
      ...
    }

    class ChemicalMatrixType{
        <<enumeration>>
        water
        biota
        sediment
        }

    class ChemicalPurpose{
        <<enumeration>>
        status
        trend
        both
        }   

    class FrequencyCode{
        <<enumeration>>
        continuousSampling
        1samplePerMonitoringYear
        2to6samplesPerMonitoringYear
        7to12SamplesPerMonitoringYear
        13To24SamplesPerMonitoringYear
        moreThan24SamplesPerMonitoringYear
        unknown
        }   

    class CycleCode{
        <<enumeration>>
        singleCampaign
        onceEvery1Year
        onceEvery2Years
        onceEvery3Years
        onceEvery4Years
        onceEvery5Years
        onceEvery6Years
        onceEvery12Years
        onceEvery18Years
        unknown
        }   
}

```


## Annex - Exploratory analysis of data reported in the 3ʳᵈ cycle

This section is not relevant for the understanding of the proposed model. 
It contains some of the data analysis that supported the revision of the data model.

Note that the execution of the queries is slow and may timeout for the entire European dataset in the discodata service. 

### Monitoring of CAS_1912-24-9 - Atrazine 

See {numref}`atrazine_wfd2022` for the information about the monitoring of Atrazine in the period 2016-2021, by water body category, in all matrices, according to the data reported under the WFD2022 Monitoring schema.

See {numref}`atrazine_2016_2021_waterbase` for the monitoring results for Atrazine in the period 2016-2021, by water body category, in water, according to the data available in the Waterbase_T_WISE6_DisaggregatedData table (reported under WISE SoE Water Quality - WISE-6).

See {numref}`atrazine_2016_2021_waterbase_country` for the monitoring results for Atrazine in the period 2016-2021, by water body category **and country**, in water, according to the data available in the Waterbase_T_WISE6_DisaggregatedData table (reported under WISE SoE Water Quality - WISE-6). *Note that over 61% of the data was reported by Italy and France.*

See {numref}`atrazine_2022_2027_waterbase` for the monitoring results for Atrazine in the period 2022-2027, by water body category, in water, according to the data available in the Waterbase_T_WISE6_DisaggregatedData table (reported under WISE SoE Water Quality - WISE-6). *Note that only data until 2023 has been reported so far.*

See {numref}`atrazine_2022_2027_waterbase_country` for the monitoring results for Atrazine in the period 2016-2021, by water body category **and country**, in water, according to the data available in the Waterbase_T_WISE6_DisaggregatedData table (reported under WISE SoE Water Quality - WISE-6). *Note that over 64% of the data was reported by Italy and France.*


```{table} Monitoring of Atrazine in the period 2016-2021, according to the WFD2022 reporting.
:name: atrazine_wfd2022
:width: 100%
:align: center

| wbCategory | countries | waterBodies | sites | **records** |
| --- | --- | --- | --- | --- |
| GW | 18 | 2764 | 16028 | 16028 |
| LW | 23 | 2658 | 2798 | 2975 |
| RW | 26 | 14990 | 16880 | 17217 |
| TW | 14 | 393 | 481 | 532 |
| CW | 18 | 591 | 859 | 1017 |
| TeW | 8 | 13 | 37 | 45 |`

```

```{table} Data related to Atrazine in the period 2016-2021, in Waterbase_T_WISE6_DisaggregatedData, by water category.
:name: atrazine_2016_2021_waterbase
:width: 100%
:align: center

| wbCategory | countries | waterBodies | sites |  **samples** |
| --- | --- | --- | --- | --- |
|GW | 15 | 2302 | 8351 | 59586 |
| LW | 15 | 738 | 782 | 10484 |
| RW | 19 | 4062 | 4380 | 114545 |
| TW | 11 | 134 | 178 | 3124 |
| CW | 7 | 238 | 337 | 3586 |
| TeW | 1 | 1 | 1 | 12 |

```

```{table} Data related to Atrazine in the period 2016-2021, in Waterbase_T_WISE6_DisaggregatedData, by country and water category.
:name: atrazine_2016_2021_waterbase_country
:width: 100%
:align: center

| country | GW | LW | RW | TW | CW | total |
| --- | --- | --- | --- | --- | --- | --- |
| IT | 2925 | 144 | 1828 | 84 | 185 | 5166 |
| FR | 1703 | 137 | 1605 | 6 |  | 3451 |
| DE | 853 | 1 | 142 | 1 |  | 997 |
| DK | 770 |  |  |  |  | 770 |
| CZ | 651 |  |  |  |  | 651 |
| BE | 396 |  | 44 | 3 |  | 443 |
| IE | 111 | 79 | 167 |  |  | 357 |
| PL | 180 | 134 | 1 |  |  | 315 |
| PT | 176 | 20 | 72 | 31 | 9 | 308 |
| EL |  | 24 | 210 | 27 | 35 | 296 |
| NL |  | 164 | 61 | 9 | 8 | 242 |
| SK | 194 |  | 16 |  |  | 210 |
| LV | 156 | 8 | 22 |  |  | 186 |
| BG | 89 | 13 | 57 | 6 |  | 165 |
| CY | 80 | 10 | 13 |  |  | 103 |
| EE |  | 35 | 54 |  | 10 | 99 |
| ES |  |  |  | 4 | 86 | 90 |
| SI | 44 | 8 | 20 |  | 4 | 76 |
| HR | 23 | 4 | 33 | 1 |  | 61 |
| LT |  | 1 | 19 | 6 |  | 26 |
| FI |  |  | 14 |  |  | 14 |
| SE |  |  | 2 |  |  | 2 |
| total | 8351 | 782 | 4380 | 178 | 337 | 14028 |

```

```{table} Provisional data related to Atrazine in the period 2022-2027, in Waterbase_T_WISE6_DisaggregatedData, by water category.
:name: atrazine_2022_2027_waterbase
:width: 100%
:align: center

| wbCategory | countries | waterBodies | sites |  **samples** |
| --- | --- | --- | --- | --- |
| GW | 15 | 2271 | 7991 | 23378 |
| LW | 11 | 314 | 343 | 2811 |
| RW | 16 | 3297 | 3503 | 36323 |
| TW | 8 | 89 | 122 | 1621 |
| CW | 6 | 116 | 145 | 1129 |

```

```{table} Provisional data related to Atrazine in the period 2022-2027, in Waterbase_T_WISE6_DisaggregatedData, by water category and country
:name: atrazine_2022_2027_waterbase_country
:width: 100%
:align: center

| country | GW | LW | RW | TW | CW | total |
| --- | --- | --- | --- | --- | --- | --- |
| IT | 2552 | 104 | 1649 | 96 | 106 | 4507 |
| FR | 1942 | 51 | 1277 |  |  | 3270 |
| DK | 1018 |  |  |  |  | 1018 |
| DE | 749 | 2 | 174 | 4 |  | 929 |
| CZ | 654 |  |  |  |  | 654 |
| BE | 231 |  | 38 | 3 |  | 272 |
| SK | 239 |  | 24 |  |  | 263 |
| PL | 178 |  |  |  |  | 178 |
| PT | 136 | 11 | 23 | 1 | 4 | 175 |
| LV | 111 | 10 | 29 |  |  | 150 |
| NL |  | 89 | 34 | 9 | 8 | 140 |
| BG | 59 | 9 | 59 | 2 |  | 129 |
| IE | 35 | 35 | 59 |  |  | 129 |
| EE |  | 27 | 60 |  | 18 | 105 |
| CY | 61 | 1 | 8 |  |  | 70 |
| HR | 21 | 4 | 34 | 1 | 7 | 67 |
| LT |  |  | 27 | 6 | 2 | 35 |
| SI | 5 |  | 6 |  |  | 11 |
| SE |  |  | 2 |  |  | 2 |
| total | 7991 | 343 | 3503 | 122 | 145 | 12104 |

```

```{table} Data related to Atrazine in the period 2016-2021, by country and water body category, in the EEA pesticides indicator.
:name: atrazine_2016_2021_pesticides
:width: 100%
:align: center

| wbCategory | countries | waterBodies | sites |  **samples** |
| --- | --- | --- | --- | --- |
| GW | 17 | 2973 | 11871 | 82989 |
| LW | 16 | 1176 | 1275 | 16841 |
| RW | 21 | 6553 | 7023 | 152628 |

```

*Note* - The queries below illustrate the use of the existing European datasets, and do not necessarily match the queries used to obtain the tables above (although they may be adjusted for that purpose).

<details>
<summary>Show code</summary>

```sql

-- https://discodata.eea.europa.eu
-- Warning: the query may timeout in the public interface.

/**
    Monitoring programmes reported in WFD2022 for CAS_1912-24-9 - Atrazine
**/

  SELECT [parameterCode],[waterBodyCategory]
      ,count(*) as [numberOfRecords]
      ,count(distinct [euMonitoringSiteCode]) as [numberOfSites]
      ,count(distinct [waterbodyCode]) as [numberOfWaterBodies]
      ,count(distinct [countryCode]) as [numberOfCountries]
  FROM [WISE_WFD].[latest].[Monitoring_MonitoringSite_ChemicalEcologicalQuantitativeMonitoring] WITH (NOLOCK)
  WHERE [hasDescriptiveData] = 1
  AND [cYear] = 2022
  AND [waterBodyCategory] IS NOT NULL
  AND [parameterCode] = 'CAS_1912-24-9 - Atrazine'
  GROUP BY [parameterCode],[waterBodyCategory]
  ORDER BY [numberOfRecords] DESC
```
</details><br/>


<details>
<summary>Show code</summary>

```sql
-- https://discodata.eea.europa.eu
-- Warning: the query may timeout in the public interface.

/**
    Monitoring results for CAS_1912-24-9 - Atrazine available in [Waterbase_T_WISE6_DisaggregatedData].
    Monitoring sites with at least 1 valid observation of Atrazine in the period 2016-2021, by water body category,
    where the analysed matrix is Water (total or dissolved fraction).
**/

SELECT [parameterWaterBodyCategory] AS [waterBodyCategory],
       count(distinct a.[countryCode]) as [numberOfCountries],
       count(distinct b.[waterBodyIdentifier]) numberOfWaterBodies,
       count(distinct a.[monitoringSiteIdentifier]) numberOfMonitoringSites,
       count(*) as numberOfSamples

  FROM [WISE_SOE].[latest].[Waterbase_T_WISE6_DisaggregatedData] a
  JOIN [WISE_SOE].[latest].[Waterbase_S_WISE_SpatialObject_DerivedData] b
  ON a.monitoringSiteIdentifier = b.monitoringSiteIdentifier
  AND a.monitoringSiteIdentifierScheme = b.monitoringSiteIdentifierScheme
  WHERE [observedPropertyDeterminandCode] = 'CAS_1912-24-9' -- Atrazine
  AND [phenomenonTimeReferenceYear] BETWEEN 2016 AND 2021 -- 2nd cycle
  AND [procedureAnalysedMatrix] IN ( 'W', 'W-DIS')  -- Water (total or dissolved)
  AND [metadata_statusCode] in ('accepted', 'valid', 'experimental', 'stable','derived')
  AND ISNULL([resultObservationStatus],'') NOT IN ('L','M','N','O','Z')
  AND a.[monitoringSiteIdentifierScheme] = 'euMonitoringSiteCode' -- WFD monitoring sites
  AND a.[countryCode] != 'UK' -- Exclude the UK 
  GROUP BY [parameterWaterBodyCategory]

```
</details><br/>


<details>
<summary>Show code</summary>

```sql
-- https://discodata.eea.europa.eu
-- Warning: the query may timeout in the public interface.

/**
    Monitoring results for CAS_1912-24-9 - Atrazine used in the EEA pesticides indicator.
**/

SELECT [waterBodyCategory],
       [countryCode],
       [waterBodyIdentifier],
       [monitoringSiteIdentifier],
       sum([resultNumberOfSamples]) as [totalNumberOfSamples],
       max([resultNumberOfSamples]) as [maximumNumberOfSamplesPerYear],
       count(distinct [phenomenonTimeReferenceYear]) as [numberOfSamplingYears]
FROM
(SELECT [countryCode]
      ,[monitoringSiteIdentifier]
      ,[waterBodyIdentifier]
      ,[waterBodyCategory]
      ,[phenomenonTimeReferenceYear]
      ,[eeaIndicator]
      ,[resultNumberOfSamples]
      
  FROM [WISE_Indicators].[latest].[AggregatedData_Pesticides]
  WHERE [eeaIndicator] = 'CAS_1912-24-9 - Atrazine'
  AND [phenomenonTimeReferenceYear] BETWEEN 2016 AND 2021 -- 2nd cycle
  AND [monitoringSiteIdentifierScheme] = 'euMonitoringSiteCode' -- WFD monitoring sites

  ) AS t
  GROUP BY [waterBodyCategory],[countryCode],[waterBodyIdentifier],[monitoringSiteIdentifier]
  ORDER BY [waterBodyCategory],[countryCode],[waterBodyIdentifier],[monitoringSiteIdentifier]
```
</details><br/>
  
<details>
<summary>Show code</summary>
  
```sql
-- https://discodata.eea.europa.eu
-- Warning: the query may timeout in the public interface.

/**
    Monitoring results for CAS_1912-24-9 - Atrazine used in the EEA pesticides indicator.
    RESULTS BY WATER CATEGORY

**/

SELECT [waterBodyCategory],
       count(distinct [countryCode]) numberOfCountries,
       count(distinct [waterBodyIdentifier]) numberOfWaterBodies,
       count(distinct [monitoringSiteIdentifier]) numberOfMonitoringSites,
       sum([resultNumberOfSamples]) as numberOfSamples
FROM
(SELECT [countryCode]
      ,[monitoringSiteIdentifier]
      ,[waterBodyIdentifier]
      ,[waterBodyCategory]
      ,[phenomenonTimeReferenceYear]
      ,[eeaIndicator]
      ,[resultNumberOfSamples]
      
  FROM [WISE_Indicators].[latest].[AggregatedData_Pesticides]
  WHERE [eeaIndicator] = 'CAS_1912-24-9 - Atrazine'
  AND [phenomenonTimeReferenceYear] BETWEEN 2016 AND 2021 -- 2nd cycle
  AND [monitoringSiteIdentifierScheme] = 'euMonitoringSiteCode' -- WFD monitoring sites

  ) AS t
  GROUP BY [waterBodyCategory]
  ORDER BY [waterBodyCategory]
```
</details><br/>

### Monitoring - Groundwater quantitative monitoring - 3ʳᵈ cycle

<details>
<summary>Show code</summary>

```sql
  --   https://discodata.eea.europa.eu/
  SELECT [parameterCode]
      ,count(*) as [numberOfRecords]
      ,count(distinct [euMonitoringSiteCode]) as [numberOfSites]
      ,count(distinct [waterbodyCode]) as [numberOfWaterBodies]
      ,count(distinct [countryCode]) as [numberOfCountries]
  FROM [WISE_WFD].[latest].[Monitoring_MonitoringSite_ChemicalEcologicalQuantitativeMonitoring] WITH (NOLOCK)
  WHERE [hasDescriptiveData] = 1
  AND [cYear] = 2022
  AND [parameterCode] = 'EEA_00-01-1 - Quantitative monitoring'
  AND [waterBodyCategory] = 'GW'
  GROUP BY [parameterCode]

```
</details><br/>  

### Monitoring - Groundwater chemical monitoring - 3ʳᵈ cycle

<details>
<summary>Show code</summary>

```sql
  --   https://discodata.eea.europa.eu/

  /**

  Groundwater chemical monitoring programmes reported in WFD2022 
  Except 'EEA_00-00-0 - Other parameter'.

  **/

  SELECT [parameterCode]
      ,count(*) as [numberOfRecords]
      ,count(distinct [euMonitoringSiteCode]) as [numberOfSites]
      ,count(distinct [waterbodyCode]) as [numberOfWaterBodies]
      ,count(distinct [countryCode]) as [numberOfCountries]
  FROM [WISE_WFD].[latest].[Monitoring_MonitoringSite_ChemicalEcologicalQuantitativeMonitoring] WITH (NOLOCK)
  WHERE [hasDescriptiveData] = 1
  AND [cYear] = 2022
  AND [parameterCode] != 'EEA_00-00-0 - Other parameter'
  AND [parameterCode] != 'EEA_00-01-1 - Quantitative monitoring'
  AND [waterBodyCategory] = 'GW'
  GROUP BY [parameterCode]
  ORDER BY [numberOfRecords] DESC

```
</details><br/>  

### Monitoring - Surface water chemical monitoring - 3ʳᵈ cycle

The full list of priority substances and river basin specific pollutants (except 'EEA_00-00-0 - Other parameter'), includes 231 substance codes. 
Note, however, that more substances are being monitored, according to the reported data.

<details>
<summary>Show code</summary>

```sql
  --   https://discodata.eea.europa.eu/

  /**

  List of priority substances and river basin specific pollutants reported in WFD2022.
  Except 'EEA_00-00-0 - Other parameter'.

  **/

  SELECT DISTINCT [swPrioritySubstanceCode]  AS [substanceCode] , 'ps' as [substanceType]
  FROM [WISE_WFD].[latest].[SWB_SurfaceWaterBody_SWPrioritySubstance]
  WHERE [hasDescriptiveData] = 1
  AND [cYear] = 2022
  AND [swPrioritySubstanceCode] != 'None'

  UNION

  SELECT DISTINCT [swFailingRBSP] AS [substanceCode] , 'rbsp' as [parameterType]
  FROM [WISE_WFD].[latest].[SWB_SurfaceWaterBody_FailingRBSP]
  WHERE [hasDescriptiveData] = 1
  AND [cYear] = 2022
  AND [swFailingRBSP] != 'EEA_00-00-0 - Other parameter'
  AND [swFailingRBSP] != 'None'
  AND [swFailingRBSP] NOT IN ('CAS_14797-55-8 - Nitrate','CAS_14797-65-0 - Nitrite','CAS_14798-03-9 - Ammonium','CAS_18785-72-3 - Sulphate','EEA_31613-01-1 - Non-ionised ammonia')
 
```
</details><br/>  

See {numref}`rbsp_qe31`: note that substances like Nitrate, Nitrite, Ammonium, Sulphate, and Non-ionised ammonia are sometimes reported 
both as quality elements, and as river basin specific pollutants. There are additional substances in the 2nd cycle.

These situations should be clarified with MS (and clear guidelines provided so that the quality control is implemented correctly).

```{table} Substances reported as River Basin Specific Pollutants that are also classified as QE3-1.
:name: rbsp_qe31
:width: 100%
:align: center

| swFailingRBSP | qeCode | waterBodiesFailing | countries | country |
| --- | --- | --- | --- | --- |
| CAS_14797-55-8 - Nitrate | QE3-1-6-1-1 - Nitrate | 57 | 1 | SE |
| CAS_14797-65-0 - Nitrite | QE3-1-6-1-2 - Nitrite | 23 | 1 | BE |
| CAS_14798-03-9 - Ammonium | QE3-1-6-1-4 - Ammonium | 510 | 1 | NL |
| CAS_18785-72-3 - Sulphate | QE3-1-4-2 - Other determinand for salinity | 3 | 1 | SI |
| EEA_31613-01-1 - Non-ionised ammonia | QE3-1-6-1-3 - Non-ionised ammonia | 126 | 1 | SE |
```

<details>
<summary>Show code</summary>

```sql
  --   https://discodata.eea.europa.eu/

SELECT [swFailingRBSP], [qeCode],
     count(DISTINCT euSurfaceWaterBodyCode) as [numberOfWaterBodiesFailing],
     count(DISTINCT countryCode) as [numberOfCountries],
     max(countryCode) as [exampleCountry]
FROM [WISE_WFD].[LATEST].[SWB_SurfaceWaterBody_FailingRBSP] a
JOIN 
(SELECT *
FROM (VALUES
('EEA_11-01-8 - PhytoplanktonEQR_G','QE1-1 - Phytoplankton'),
('EEA_11-02-9 - PhytoplanktonEQR_H','QE1-1 - Phytoplankton'),
('EEA_11-03-0 - PhytoplanktonEQR_A','QE1-1 - Phytoplankton'),
('EEA_11-04-1 - PhytoplanktonEQR_E','QE1-1 - Phytoplankton'),
('EEA_11-05-2 - Total phytoplankton biomass','QE1-1 - Phytoplankton'),
('EEA_11-06-3 - Cyanobacteria biomass','QE1-1 - Phytoplankton'),
('EEA_11-07-4 - Cyanobacteria proportion','QE1-1 - Phytoplankton'),
('EEA_11-08-5 - PhytoplanktonEQR','QE1-1 - Phytoplankton'),
('EEA_121-01-7 - MacroalgaeEQR','QE1-2-1 - Macroalgae'),
('EEA_122-02-1 - AngiospermsEQR','QE1-2-2 - Angiosperms'),
('EEA_123-01-3 - MacrophyteEQR_G','QE1-2-3 - Macrophytes'),
('EEA_123-02-4 - MacrophyteEQR_H','QE1-2-3 - Macrophytes'),
('EEA_123-03-5 - MacrophyteEQR_A','QE1-2-3 - Macrophytes'),
('EEA_123-04-6 - MacrophyteEQR_E','QE1-2-3 - Macrophytes'),
('EEA_123-05-7 - Macrophyte depth limit','QE1-2-3 - Macrophytes'),
('EEA_123-06-8 - Charaphytes presence','QE1-2-3 - Macrophytes'),
('EEA_123-07-9 - Isoetides presence','QE1-2-3 - Macrophytes'),
('EEA_124-01-6 - PhytobenthosEQR_G','QE1-2-4 - Phytobenthos'),
('EEA_124-02-7 - PhytobenthosEQR_H','QE1-2-4 - Phytobenthos'),
('EEA_124-03-8 - PhytobenthosEQR_A','QE1-2-4 - Phytobenthos'),
('EEA_124-04-9 - PhytobenthosEQR_E','QE1-2-4 - Phytobenthos'),
('EEA_13-01-4 - InvertebrateEQR_G','QE1-3 - Benthic invertebrates'),
('EEA_13-02-5 - InvertebrateEQR_H','QE1-3 - Benthic invertebrates'),
('EEA_13-03-6 - InvertebrateEQR_A','QE1-3 - Benthic invertebrates'),
('EEA_13-04-7 - InvertebrateEQR_E','QE1-3 - Benthic invertebrates'),
('EEA_13-05-8 - InvertebrateEQR','QE1-3 - Benthic invertebrates'),
('EEA_14-01-7 - FishEQR_G','QE1-4 - Fish'),
('EEA_14-02-8 - FishEQR_H','QE1-4 - Fish'),
('EEA_14-03-9 - FishEQR_A','QE1-4 - Fish'),
('EEA_14-04-0 - FishEQR_E','QE1-4 - Fish'),
('EEA_14-05-1 - FishEQR','QE1-4 - Fish'),
('EEA_15-01-0 - Escherichia coli','QE1-5 - Other species'),
('EEA_15-02-1 - Intestinal enterococci','QE1-5 - Other species'),
('EEA_15-03-2 - Clostridium perfringens','QE1-5 - Other species'),
('EEA_15-04-3 - Coliform bacteria','QE1-5 - Other species'),
('EEA_15-05-4 - Legionella','QE1-5 - Other species'),
('EEA_15-06-5 - Intestinal nematodes','QE1-5 - Other species'),
('EEA_3111-01-1 - Secchi depth','QE3-1-1-1 - Secchi disk depth'),
('EEA_31-02-7 - Total suspended solids','QE3-1-1-2 - Other determinand for transparency'),
('EEA_31-03-8 - Total dissolved solids','QE3-1-1-2 - Other determinand for transparency'),
('EEA_3112-01-4 - Turbidity','QE3-1-1-2 - Other determinand for transparency'),
('EEA_3121-01-5 - Water temperature','QE3-1-2-1 - Water temperature'),
('EEA_3131-01-9 - Oxygen saturation','QE3-1-3-1 - Oxygen saturation'),
('EEA_3132-01-2 - Dissolved oxygen','QE3-1-3-2 - Dissolved oxygen'),
('EEA_3133-01-5 - BOD5','QE3-1-3-3 - Other determinand for oxygenation conditions'),
('EEA_3133-02-6 - BOD7','QE3-1-3-3 - Other determinand for oxygenation conditions'),
('EEA_3133-03-7 - CODCr','QE3-1-3-3 - Other determinand for oxygenation conditions'),
('EEA_3133-04-8 - CODMn','QE3-1-3-3 - Other determinand for oxygenation conditions'),
('EEA_3133-05-9 - Dissolved organic carbon (DOC)','QE3-1-3-3 - Other determinand for oxygenation conditions'),
('EEA_3133-06-0 - Total organic carbon (TOC)','QE3-1-3-3 - Other determinand for oxygenation conditions'),
('EEA_3133-07-1 - Oxidisability','QE3-1-3-3 - Other determinand for oxygenation conditions'),
('EEA_3141-01-3 - Salinity','QE3-1-4-1 - Practical salinity units'),
('CAS_16887-00-6 - Chloride','QE3-1-4-2 - Other determinand for salinity'),
('CAS_18785-72-3 - Sulphate','QE3-1-4-2 - Other determinand for salinity'),
('EEA_31-01-6 - Hardness','QE3-1-4-2 - Other determinand for salinity'),
('EEA_3142-01-6 - Electrical conductivity','QE3-1-4-2 - Other determinand for salinity'),
('EEA_3142-02-7 - Chlorine Cl-','QE3-1-4-2 - Other determinand for salinity'),
('EEA_3151-01-7 - Acid neutralising capacity','QE3-1-5-1 - Acid neutralising capacity'),
('EEA_3152-01-0 - pH','QE3-1-5-2 - pH'),
('CAS_71-52-3 - Hydrogen Carbonate (Bicarbonate) HCO3','QE3-1-5-3 - Other determinand for acidification status'),
('EEA_3153-01-3 - Acid neutralising capacity to pH 4.5','QE3-1-5-3 - Other determinand for acidification status'),
('EEA_3153-02-4 - Alkalinity','QE3-1-5-3 - Other determinand for acidification status'),
('EEA_3161-01-1 - Kjeldahl nitrogen','QE3-1-6-1 - Nitrogen conditions'),
('EEA_3161-02-2 - Total oxidised nitrogen','QE3-1-6-1 - Nitrogen conditions'),
('EEA_3161-03-3 - Total organic nitrogen','QE3-1-6-1 - Nitrogen conditions'),
('EEA_3161-04-4 - Particulate organic nitrogen','QE3-1-6-1 - Nitrogen conditions'),
('EEA_3161-05-5 - Total inorganic nitrogen','QE3-1-6-1 - Nitrogen conditions'),
('CAS_14797-55-8 - Nitrate','QE3-1-6-1-1 - Nitrate'),
('CAS_14797-65-0 - Nitrite','QE3-1-6-1-2 - Nitrite'),
('EEA_31613-01-1 - Non-ionised ammonia','QE3-1-6-1-3 - Non-ionised ammonia'),
('CAS_14798-03-9 - Ammonium','QE3-1-6-1-4 - Ammonium'),
('EEA_31615-01-7 - Total nitrogen','QE3-1-6-1-5 - Total nitrogen'),
('CAS_14265-44-2 - Phosphate','QE3-1-6-2-1 - Orthophosphate'),
('CAS_7723-14-0 - Total phosphorus','QE3-1-6-2-2 - Total phosphorus'),
('EEA_3163-01-7 - Silicate','QE3-1-6-3 - Silicate'),
('EEA_3164-01-0 - Chlorophyll a','QE3-1-6-4 - Other determinand for nutrient conditions'),
('EEA_3164-07-6 - Total nitrogen to total phosphorus ratio','QE3-1-6-4 - Other determinand for nutrient conditions'),
('EEA_3164-08-7 - Nitrate to orthophosphate ratio','QE3-1-6-4 - Other determinand for nutrient conditions')
) AS t(parameterCode, qeCode))

  b
  on a.[swFailingRBSP] = b.[parameterCode]
  WHERE [hasDescriptiveData] = 1
  AND [cYear] = 2022
  AND [swFailingRBSP] != 'EEA_00-00-0 - Other parameter'
  AND [swFailingRBSP] != 'None'
  GROUP BY [swFailingRBSP], [qeCode]

```
</details><br/>  

### Monitoring - Surface water ecological monitoring - 3ʳᵈ cycle

See {numref}`sw_ecological_monitoring`: for an overview of the Surface water ecological monitoring reported in the 3ʳᵈ cycle RBMPs.
Note that more than one substance or parameter can be aggregated under each Quality Element code.

For QE3-1 (General parameters), it is preferable to use the substance code and agregate the reported data to the corresponding quality element. 
Given that both options - quality element code and substance code - were used in the reporting, the query is more complex. 

In the 4ᵗʰ cycle, the use of the CAS and EEA codes should be recommended.
At least the use of the 'QE3-3 - River Basin Specific Pollutants' should be avoided.

```{table} Surface water ecological monitoring, as reported in the 3ʳᵈ cycle RBMPs.
:name: sw_ecological_monitoring
:width: 100%
:align: center

| qeCode | records | sites | waterBodies | countries |
| --- | --- | --- | --- | --- |
| QE1-1 - Phytoplankton | 10751 | 10751 | 8168 | 25 |
| QE1-2 - Other aquatic flora | 10582 | 10582 | 7864 | 7 |
| QE1-2-1 - Macroalgae | 1305 | 1305 | 738 | 13 |
| QE1-2-2 - Angiosperms | 1160 | 1160 | 505 | 12 |
| QE1-2-3 - Macrophytes | 15491 | 15491 | 12195 | 24 |
| QE1-2-4 - Phytobenthos | 22475 | 22475 | 18781 | 24 |
| QE1-3 - Benthic invertebrates | 46693 | 46693 | 36673 | 25 |
| QE1-4 - Fish | 26509 | 26509 | 20455 | 24 |
| QE2-1 - Hydrological or tidal regime | 13196 | 13196 | 11339 | 17 |
| QE2-2 - River continuity conditions | 12158 | 12158 | 10416 | 14 |
| QE2-3 - Morphological conditions | 20428 | 20428 | 17332 | 17 |
| QE3-1-1 - Transparency conditions | 4519 | 4519 | 3577 | 11 |
| QE3-1-1-1 - Secchi disk depth | 4430 | 4430 | 3294 | 16 |
| QE3-1-1-2 - Other determinand for transparency | 15354 | 14175 | 11711 | 15 |
| QE3-1-2 - Thermal conditions | 14156 | 14156 | 11983 | 10 |
| QE3-1-2-1 - Water temperature | 25894 | 25620 | 21364 | 20 |
| QE3-1-3 - Oxygenation conditions | 17869 | 17869 | 14781 | 14 |
| QE3-1-3-1 - Oxygen saturation | 15724 | 15538 | 12250 | 14 |
| QE3-1-3-2 - Dissolved oxygen | 21166 | 20892 | 17793 | 20 |
| QE3-1-3-3 - Other determinand for oxygenation conditions | 39655 | 25007 | 20888 | 19 |
| QE3-1-4 - Salinity conditions | 12965 | 12965 | 10871 | 14 |
| QE3-1-4-1 - Practical salinity units | 3176 | 3170 | 2059 | 10 |
| QE3-1-4-2 - Other determinand for salinity | 36683 | 21167 | 17308 | 18 |
| QE3-1-5 - Acidification status | 15457 | 15457 | 12622 | 11 |
| QE3-1-5-1 - Acid neutralising capacity | 2896 | 2896 | 1883 | 4 |
| QE3-1-5-2 - pH | 30704 | 30358 | 24288 | 20 |
| QE3-1-5-3 - Other determinand for acidification status | 12034 | 11910 | 9497 | 10 |
| QE3-1-6-1 - Nitrogen conditions | 20651 | 20601 | 16353 | 18 |
| QE3-1-6-1-1 - Nitrate | 27391 | 26992 | 21881 | 20 |
| QE3-1-6-1-2 - Nitrite | 16495 | 16270 | 13926 | 17 |
| QE3-1-6-1-3 - Non-ionised ammonia | 1947 | 1822 | 1669 | 6 |
| QE3-1-6-1-4 - Ammonium | 27948 | 27573 | 23310 | 21 |
| QE3-1-6-1-5 - Total nitrogen | 21694 | 21123 | 17336 | 17 |
| QE3-1-6-2 - Phosphorus conditions | 17255 | 17255 | 14136 | 15 |
| QE3-1-6-2-1 - Orthophosphate | 24756 | 24458 | 20381 | 21 |
| QE3-1-6-2-2 - Total phosphorus | 28109 | 27460 | 22850 | 19 |
| QE3-1-6-3 - Silicate | 2001 | 2001 | 1483 | 10 |
| QE3-1-6-4 - Other determinand for nutrient conditions | 818 | 818 | 487 | 8 |
| QE3-3 - River Basin Specific Pollutants | 9174 | 9174 | 7591 | 14 |
```

<details>
<summary>Show code</summary>

```sql
  --   https://discodata.eea.europa.eu/
  SELECT COALESCE(b.[qeCode], a.[parameterCode]) AS [qeCode]
      ,count(*) as [numberOfRecords]
      ,count(distinct [euMonitoringSiteCode]) as [numberOfSites]
      ,count(distinct [waterbodyCode]) as [numberOfWaterBodies]
      ,count(distinct [countryCode]) as [numberOfCountries]
  FROM [WISE_WFD].[latest].[Monitoring_MonitoringSite_ChemicalEcologicalQuantitativeMonitoring] a
  LEFT JOIN 
  (
    SELECT *
    FROM (VALUES
    ('EEA_11-01-8 - PhytoplanktonEQR_G','QE1-1 - Phytoplankton'),
    ('EEA_11-02-9 - PhytoplanktonEQR_H','QE1-1 - Phytoplankton'),
    ('EEA_11-03-0 - PhytoplanktonEQR_A','QE1-1 - Phytoplankton'),
    ('EEA_11-04-1 - PhytoplanktonEQR_E','QE1-1 - Phytoplankton'),
    ('EEA_11-05-2 - Total phytoplankton biomass','QE1-1 - Phytoplankton'),
    ('EEA_11-06-3 - Cyanobacteria biomass','QE1-1 - Phytoplankton'),
    ('EEA_11-07-4 - Cyanobacteria proportion','QE1-1 - Phytoplankton'),
    ('EEA_11-08-5 - PhytoplanktonEQR','QE1-1 - Phytoplankton'),
    ('EEA_121-01-7 - MacroalgaeEQR','QE1-2-1 - Macroalgae'),
    ('EEA_122-02-1 - AngiospermsEQR','QE1-2-2 - Angiosperms'),
    ('EEA_123-01-3 - MacrophyteEQR_G','QE1-2-3 - Macrophytes'),
    ('EEA_123-02-4 - MacrophyteEQR_H','QE1-2-3 - Macrophytes'),
    ('EEA_123-03-5 - MacrophyteEQR_A','QE1-2-3 - Macrophytes'),
    ('EEA_123-04-6 - MacrophyteEQR_E','QE1-2-3 - Macrophytes'),
    ('EEA_123-05-7 - Macrophyte depth limit','QE1-2-3 - Macrophytes'),
    ('EEA_123-06-8 - Charaphytes presence','QE1-2-3 - Macrophytes'),
    ('EEA_123-07-9 - Isoetides presence','QE1-2-3 - Macrophytes'),
    ('EEA_124-01-6 - PhytobenthosEQR_G','QE1-2-4 - Phytobenthos'),
    ('EEA_124-02-7 - PhytobenthosEQR_H','QE1-2-4 - Phytobenthos'),
    ('EEA_124-03-8 - PhytobenthosEQR_A','QE1-2-4 - Phytobenthos'),
    ('EEA_124-04-9 - PhytobenthosEQR_E','QE1-2-4 - Phytobenthos'),
    ('EEA_13-01-4 - InvertebrateEQR_G','QE1-3 - Benthic invertebrates'),
    ('EEA_13-02-5 - InvertebrateEQR_H','QE1-3 - Benthic invertebrates'),
    ('EEA_13-03-6 - InvertebrateEQR_A','QE1-3 - Benthic invertebrates'),
    ('EEA_13-04-7 - InvertebrateEQR_E','QE1-3 - Benthic invertebrates'),
    ('EEA_13-05-8 - InvertebrateEQR','QE1-3 - Benthic invertebrates'),
    ('EEA_14-01-7 - FishEQR_G','QE1-4 - Fish'),
    ('EEA_14-02-8 - FishEQR_H','QE1-4 - Fish'),
    ('EEA_14-03-9 - FishEQR_A','QE1-4 - Fish'),
    ('EEA_14-04-0 - FishEQR_E','QE1-4 - Fish'),
    ('EEA_14-05-1 - FishEQR','QE1-4 - Fish'),
    ('EEA_15-01-0 - Escherichia coli','QE1-5 - Other species'),
    ('EEA_15-02-1 - Intestinal enterococci','QE1-5 - Other species'),
    ('EEA_15-03-2 - Clostridium perfringens','QE1-5 - Other species'),
    ('EEA_15-04-3 - Coliform bacteria','QE1-5 - Other species'),
    ('EEA_15-05-4 - Legionella','QE1-5 - Other species'),
    ('EEA_15-06-5 - Intestinal nematodes','QE1-5 - Other species'),
    ('EEA_3111-01-1 - Secchi depth','QE3-1-1-1 - Secchi disk depth'),
    ('EEA_31-02-7 - Total suspended solids','QE3-1-1-2 - Other determinand for transparency'),
    ('EEA_31-03-8 - Total dissolved solids','QE3-1-1-2 - Other determinand for transparency'),
    ('EEA_3112-01-4 - Turbidity','QE3-1-1-2 - Other determinand for transparency'),
    ('EEA_3121-01-5 - Water temperature','QE3-1-2-1 - Water temperature'),
    ('EEA_3131-01-9 - Oxygen saturation','QE3-1-3-1 - Oxygen saturation'),
    ('EEA_3132-01-2 - Dissolved oxygen','QE3-1-3-2 - Dissolved oxygen'),
    ('EEA_3133-01-5 - BOD5','QE3-1-3-3 - Other determinand for oxygenation conditions'),
    ('EEA_3133-02-6 - BOD7','QE3-1-3-3 - Other determinand for oxygenation conditions'),
    ('EEA_3133-03-7 - CODCr','QE3-1-3-3 - Other determinand for oxygenation conditions'),
    ('EEA_3133-04-8 - CODMn','QE3-1-3-3 - Other determinand for oxygenation conditions'),
    ('EEA_3133-05-9 - Dissolved organic carbon (DOC)','QE3-1-3-3 - Other determinand for oxygenation conditions'),
    ('EEA_3133-06-0 - Total organic carbon (TOC)','QE3-1-3-3 - Other determinand for oxygenation conditions'),
    ('EEA_3133-07-1 - Oxidisability','QE3-1-3-3 - Other determinand for oxygenation conditions'),
    ('EEA_3141-01-3 - Salinity','QE3-1-4-1 - Practical salinity units'),
    ('CAS_16887-00-6 - Chloride','QE3-1-4-2 - Other determinand for salinity'),
    ('CAS_18785-72-3 - Sulphate','QE3-1-4-2 - Other determinand for salinity'),
    ('EEA_31-01-6 - Hardness','QE3-1-4-2 - Other determinand for salinity'),
    ('EEA_3142-01-6 - Electrical conductivity','QE3-1-4-2 - Other determinand for salinity'),
    ('EEA_3142-02-7 - Chlorine Cl-','QE3-1-4-2 - Other determinand for salinity'),
    ('EEA_3151-01-7 - Acid neutralising capacity','QE3-1-5-1 - Acid neutralising capacity'),
    ('EEA_3152-01-0 - pH','QE3-1-5-2 - pH'),
    ('CAS_71-52-3 - Hydrogen Carbonate (Bicarbonate) HCO3','QE3-1-5-3 - Other determinand for acidification status'),
    ('EEA_3153-01-3 - Acid neutralising capacity to pH 4.5','QE3-1-5-3 - Other determinand for acidification status'),
    ('EEA_3153-02-4 - Alkalinity','QE3-1-5-3 - Other determinand for acidification status'),
    ('EEA_3161-01-1 - Kjeldahl nitrogen','QE3-1-6-1 - Nitrogen conditions'),
    ('EEA_3161-02-2 - Total oxidised nitrogen','QE3-1-6-1 - Nitrogen conditions'),
    ('EEA_3161-03-3 - Total organic nitrogen','QE3-1-6-1 - Nitrogen conditions'),
    ('EEA_3161-04-4 - Particulate organic nitrogen','QE3-1-6-1 - Nitrogen conditions'),
    ('EEA_3161-05-5 - Total inorganic nitrogen','QE3-1-6-1 - Nitrogen conditions'),
    ('CAS_14797-55-8 - Nitrate','QE3-1-6-1-1 - Nitrate'),
    ('CAS_14797-65-0 - Nitrite','QE3-1-6-1-2 - Nitrite'),
    ('EEA_31613-01-1 - Non-ionised ammonia','QE3-1-6-1-3 - Non-ionised ammonia'),
    ('CAS_14798-03-9 - Ammonium','QE3-1-6-1-4 - Ammonium'),
    ('EEA_31615-01-7 - Total nitrogen','QE3-1-6-1-5 - Total nitrogen'),
    ('CAS_14265-44-2 - Phosphate','QE3-1-6-2-1 - Orthophosphate'),
    ('CAS_7723-14-0 - Total phosphorus','QE3-1-6-2-2 - Total phosphorus'),
    ('EEA_3163-01-7 - Silicate','QE3-1-6-3 - Silicate'),
    ('EEA_3164-01-0 - Chlorophyll a','QE3-1-6-4 - Other determinand for nutrient conditions'),
    ('EEA_3164-07-6 - Total nitrogen to total phosphorus ratio','QE3-1-6-4 - Other determinand for nutrient conditions'),
    ('EEA_3164-08-7 - Nitrate to orthophosphate ratio','QE3-1-6-4 - Other determinand for nutrient conditions')
    ) AS t(parameterCode, qeCode)) AS b

  ON a.[parameterCode] = b.[parameterCode] 
  
  WHERE [hasDescriptiveData] = 1
  AND [cYear] = 2022
  AND [waterBodyCategory] != 'GW'
  AND (a.[parameterCode] LIKE 'QE%' OR b.[qeCode] IS NOT NULL)
  GROUP BY COALESCE(b.[qeCode], a.[parameterCode])
```
</details><br/>  

### Assessment method for quality elements - 3ʳᵈ cycle

All the information analysed above refers to "in-situ" data, i.e. conventional monitoring.

<details>
<summary>Show code</summary>

```sql
  --   https://discodata.eea.europa.eu/

  /**
  
  For the 4ᵗʰ cycle, the assessment methods codelist provided with QualityElement table must also include non-conventional monitoring. 
  
  **/

SELECT [qeCode]
      ,[qeMonitoringResults]
      ,count(*) as [numberOfWaterBodies]
      ,count(distinct [countryCode]) as [numberOfCountries]
  FROM [WISE_WFD].[latest].[SWB_SurfaceWaterBody_QualityElement]
  WHERE [hasDescriptiveData] = 1
  AND [cYear] = 2022
  AND [qeStatusOrPotentialValue] IN ('1', '2', '3', '4','5')
  GROUP BY [qeCode], [qeMonitoringResults]
  ORDER BY [qeCode], [qeMonitoringResults]
  ```
</details><br/>  