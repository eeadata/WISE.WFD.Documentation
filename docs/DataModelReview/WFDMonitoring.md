(heading_wfd_monitoring)=
# WFD monitoring

Last updated: 2026-05-19

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
(see {numref}`ClassDiagram_Monitoring_2016`).

For the 3ʳᵈ cycle reporting, in 2022, 
the analysis of the content of the WISE SoE reporting showed issues 
in the completeness of the voluntary reporting of monitoring results for water quality: 
it would not have been possible to derive the requested monitoring information from the EEA Waterbases.
Therefore, the reporting schema was simplified (see {numref}`ClassDiagram_Monitoring_2022`),
but kept in the WFD 2022 electronic reporting.

In preparation on the 4ᵗʰ cycle reporting,
a similar analysis of the current content of the WISE SoE reporting was done.  
(See examples related to Atrazine in the last section of this document.) 

While the European coverage of the WISE SoE reporting remains fragmentary,
it is clear that some Member States provide detailed and abundant data 
that likely reflects the existing WFD monitoring programmes.  
For such Member States, reporting derived statistics about sampling frequency and period 
in the 4ᵗʰ cycle electronic reporting is duplicate reporting and an unnecessary reporting burden.

```{epigraph}

Reporting should reflect the monitoring carried out that has informed the second RBMPs. 
Given that monitoring programmes are usually dynamic and multi‐annual 
(i.e. in the cases of quality elements with lower frequencies of monitoring), 
reporting should reflect, as accurately as possible, 
the monitoring that has informed the preparation of the second RBMPs. 
Reporting is not intended to include information regarding future monitoring programmes or planned changes.[...]  

The data and information on monitoring to be reported under Article 8 of the WFD 
include a description of the monitoring sites, a specification of the different QEs and chemical substances
monitored at each site, and information relating to the associated monitoring programmes.[...]  

Member States are expected to report to EEA WISE SoE:
* Water quality results including Priority Substances and River Basin Specific Pollutants 
  to EEAs Waterbases on groundwater, rivers, lakes, transitional waters and coastal waters
* Results from monitoring Biological Quality Elements 
  to EEAs Waterbases on rivers, lakes, transitional waters and coastal waters.  

-- *Extracts from 2016 WFD Reporting Guidance for the 2nd cycle (pg. 93-100)*
```

```{figure} img/ClassDiagram_Monitoring_2016.png
:name: ClassDiagram_Monitoring_2016
:align: center
:width: 75%

Monitoring_2016 schema - 2nd cycle - Obsolete
```

```{epigraph}

Reporting should reflect the monitoring that was carried out and informed the third RBMPs. 
It is not intended to include information regarding future monitoring programmes. 
It can include planned changes when sufficient information is already available 
on the QEs, substances or parameters that will be monitored and at which frequency. 
In these cases, the date of the last monitoring should be reported as ‘9999’, as mentioned in the specific guidance below.[...]  

The data and information on monitoring to be reported under Article 8 of the WFD 
include a description of the monitoring sites, a specification of the different QEs and chemical substances
monitored at each site, and information relating to the associated monitoring programmes.[...]  

Member States are expected to report to EEA WISE SoE:
* Water quality results, including Priority Substances and River Basin Specific Pollutants, 
  to Waterbases on groundwater, rivers, lakes, transitional waters and coastal waters
* Results from monitoring Biological Quality Elements to Waterbases on rivers, lakes, transitional waters and coastal waters  

-- *Extracts from the 2022 WFD Reporting Guidance for the 3ʳᵈ cycle (pg. 90-97)*
```

```{figure} img/ClassDiagram_Monitoring_2022.png
:name: ClassDiagram_Monitoring_2022
:align: center
:width: 75%

Monitoring_2022 schema - 3ʳᵈ cycle - Obsolete
```

(heading_wfd_monitoring_4th_cycle)=
## Descriptive data - 4ᵗʰ cycle

For the 4ᵗʰ cycle of reporting, the requested information is further simplified.

* {ref}`heading_wfd_monitoring_monitoring_programmes_table_4th_cycle`
* {ref}`heading_wfd_monitoring_monitoring_table_4th_cycle`

(heading_wfd_monitoring_monitoring_programmes_table_4th_cycle)=
### MonitoringProgrammes table - 4ᵗʰ cycle

The information about the monitoring programmes is provided in the RBMP documents: 
only the reference to the supporting documents is requested 
in the `MonitoringProgrammes` table (see {numref}`DescriptiveMonitoringProgrammes4thcycle`). 

```{mermaid} /DataModelReview/mmd/Monitoring_4thCycle_MonitoringProgrammes_ClassDiagram.mmd
:name: DescriptiveMonitoringProgrammes4thcycle
:caption:  Descriptive data - Monitoring Programmes - 4ᵗʰ cycle
:align: center
:zoom:
```

The following conditions apply:

01. The `MonitoringProgrammes` table *must* have one record 
    for each of the river basin districts being reported.  
    The river basin district is identified by its `euRBDCode` identifier.

03. The `gwChemicalMonitoringReference`  
    *must* be reported for 
    every river basin district with 
    designated groundwater bodies. 

04. The `gwQuantitativeMonitoringReference`  
    *must* be reported for 
    every river basin district with 
    designated groundwater bodies. 

05. The `swChemicalMonitoringReference`  
    *must* be reported for 
    every river basin district with 
    designated surface water bodies. 

06. The `swEcologicalMonitoringReference`  
    *must* be reported for 
    every river basin district with 
    designated surface water bodies 
    that are not territorial waters. 

The `useWaterbaseForMonitoringData` value defines what needs to be reported in the `Monitoring` table.
  * It applies to all surface water monitoring 
    *except Biological Quality Elements (QE1)* 
    and *Hydromorphological Quality Elements (QE2)*
  * It applies to all groundwater monitoring
    *except Quantitative Monitoring* (EEA_00-01-1).

The option `useWaterbaseForMonitoringData = 'yes'` 
indicates that, for all other parameters,
the monitoring data statistics 
should be *derived* from the data reported to Waterbase.  

(heading_wfd_monitoring_monitoring_table_4th_cycle)=
### Monitoring table - 4ᵗʰ cycle

A single simplified **Monitoring** table is proposed (see {numref}`DescriptiveMonitoring4thcycle`). 

* The `frequency` and `cycle` values are codified, 
  to avoid ambiguities in the reporting and interpretation of results, 
  while maintaining the definitions used in the 2nd and 3rd RBMPs. 

* The `lastMonitored` value indicates the last year (until 2027, inclusive) 
  when the parameter was monitored *in situ*, at that site.
  If the parameter *has never been monitored in past*, 
  but *will* be monitored during the 4ᵗʰ cycle, 
  at that site, report the value 9999.
 
* For the 5ᵗʰ cycle of reporting, in 2033, 
  it is expected that information about monitoring parameters, frequency, etc., 
  can be derived from monitoring observations 
  reported under the WISE-2, WISE-6 and WISE-3 dataflows.
  The derived information would then fully replace 
  the Monitoring table in the RBMP electronic reporting.

For the 4ᵗʰ cycle, the following conditions apply:

01. The `Monitoring` table must always 
    list the surface water monitoring sites 
    for Biological Quality Elements (QE1%) 
    for every river basin distric with 
    designated surface water bodies 
    (except territorial waters). 

02. The `Monitoring` table must always 
    list the surface water monitoring sites 
    for Hydromorphological Quality Elements (QE2%)
    for every river basin distric with 
    designated surface water bodies 
    (except territorial waters). 

03. The `Monitoring` table must always 
    list the groundwater monitoring sites 
    for 'EEA_00-01-1 - Quantitative Monitoring'
    for every river basin distric with 
    designated groundwater bodies.
      
04. If, for a given river basin district, 
    the option `useWaterbaseForMonitoringData = 'yes'` 
    is reported in the `MonitoringProgrammes` table, 
    then the monitoring of physico-chemical and chemical parameters *must NOT* 
    be reported in the `Monitoring` table.

05. If, for a given river basin district, 
    the option `useWaterbaseForMonitoringData = 'no'` 
    is reported in the `MonitoringProgrammes` table, 
    then the monitoring of physico-chemical and chemical parameters *must NOT* 
    be reported in the `Monitoring` table.

The quality control requirements defined in the 3ʳᵈ cycle still apply:

06. The option `parameterCode LIKE 'EEA_00-01-1%'`
    (Quantitative monitoring) is only valid 
    for monitoring sites in groundwater bodies.

07. The option `parameterCode LIKE 'QE1-%'`
    (Biological quality elements) is only valid 
    in rivers, lakes, transitional and coastal water bodies.

08. The `parameterCode LIKE 'QE2-%'`
    (Hydromorphological quality elements) is only valid 
    in rivers, lakes, transitional and coastal water bodies.

With regard to chemical monitoring:

09. The `chemicalMatrix` value 
    *must* be reported 
    *if and only if* chemical monitoring occurs. 
   
10. For sites in groundwater bodies 
    where chemical monitoring occurs, 
    `chemicalMatrix = 'water'` 
    is the only valid option.

11. The `chemicalPurpose` value
    *must* be reported 
    *if and only if* chemical monitoring occurs.  

12. For sites in surface water bodies, 
    chemical monitoring includes 
    priority substances and 
    river basin specific pollutants.

13. For sites in groundwater bodies, 
    chemical monitoring includes 
    priority substances,  
    the pollutants designated as "river basin specific pollutants" (for surface waters),
    and any other chemical substances 
    where  `parameterCode LIKE 'CAS%'`.

14. Some parameters applicable to surface water 
    are NOT valid in groundwater monitoring sites:

    * EEA_3133-07-1 - Oxidisability
    * EEA_3133-02-6 - BOD7
    * EEA_3111-01-1 - Secchi depth
    * EEA_3161-04-4 - Particulate organic nitrogen
    * EEA_3164-08-7 - Nitrate to orthophosphate ratio
    * EEA_3164-07-6 - Total nitrogen to total phosphorus ratio
    * EEA_3164-01-0 - Chlorophyll a

See the analysis in {ref}`heading_wfd_monitoring_groundwater_physico_chemical_monitoring_in_waterbase`.

```{mermaid} /DataModelReview/mmd/Monitoring_4thCycle_Monitoring_ClassDiagram.mmd
:name: DescriptiveMonitoring4thcycle
:caption:  Descriptive data - Monitoring - 4ᵗʰ cycle
:align: center
:zoom:
```

(heading_wfd_monitoring_codelists_4th_cycle)=
## Codelists for the Monitoring table - 4ᵗʰ cycle

The diagram below presents the codelists applicable to `Monitoring` table, 
which simplify and clarify codelists adopted in the 3ʳᵈ cycle.  
Note that for quality elements under QE3 (General parameters), 
the CAS code or EEA code must be used.  
Note also that the option `'EEA_00-00-0 - Other parameter'` 
will *not* be available in the 4ᵗʰ cycle of reporting.  

```{mermaid}  /DataModelReview/mmd/Monitoring_4thCycle_Codelists_ClassDiagram.mmd
:name: CodelistsDescriptiveMonitoring4thcycle
:caption:  Codelists - Monitoring - 4ᵗʰ cycle
:align: center
```

(heading_wfd_monitoring_documents_dataset_4th_cycle)=
## Documents dataset - 4ᵗʰ cycle

```{todo}
Review
```

The Documents dataset follows the standard structure used in various WISE dataflows ({numref}`Monitoring_4thCycle_Documents`):

* The `dcMetadata` table is required and contains only one record per delivery (i.e. per country). 
  It provides the basic Dublin Core metadata elements about the delivery.

* If required by the data providers, and especially if spatial data is being reported, 
  the `licenseDocument` and the `metadataDocument` attributes allow the provision of additional information about the dataset.

* The dcMetadata table also functions as a "manifest file" explaining: 

  * if the delivery contains an update of the spatial data (`updateSpatialData = 'yes'`) 
  * and/or if the delivery contains an update of the monitoring data (`updateMonitoringData= 'yes'`). 
  
* The structure of the `Document` table is standard in the WISE dataflows: 
it allows the upload of documents (for example, PDFs) 
or the provision of a hyperlink to a document stored in a publicly accessible national web site.

```{mermaid} /DataModelReview/mmd/Monitoring_4thCycle_Documents_ClassDiagram.mmd
:name: Monitoring_4thCycle_Documents
:caption: Monitoring - 4ᵗʰ cycle - Documents
:align: center
:zoom:
```

## Annexes - Data analysis - 3ʳᵈ cycle

```{include} FragmentAnnexesDataAnalysis3rdCycle
```

```{admonition} About the examples below
:class: dropdown
The SQL queries below illustrate the use of the existing European datasets, 
and do not necessarily match the queries used to obtain the tables 
(although they may be adjusted for that purpose).
```

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
| TeW | 8 | 13 | 37 | 45 |

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

```{dropdown} Show code

  ```{code-block} sql
  :caption: Monitoring programmes for Atrazine - 3ʳᵈ cycle
  :linenos:
  -- https://discodata.eea.europa.eu/

  SELECT [parameterCode],[waterBodyCategory]
      ,count(*) as [numberOfRecords]
      ,count(distinct [euMonitoringSiteCode]) as [numberOfSites]
      ,count(distinct [waterbodyCode]) as [numberOfWaterBodies]
      ,count(distinct [countryCode]) as [numberOfCountries]
  FROM [WISE_WFD].[v2r1].[Monitoring_MonitoringSite_ChemicalEcologicalQuantitativeMonitoring] WITH (NOLOCK)
  WHERE [hasDescriptiveData] = 1
  AND [cYear] = 2022
  AND [waterBodyCategory] IS NOT NULL
  AND [parameterCode] = 'CAS_1912-24-9 - Atrazine'
  GROUP BY [parameterCode],[waterBodyCategory]
  ORDER BY [numberOfRecords] DESC
  ```

```{dropdown} Show code

  ```{code-block} sql
  :caption: Monitoring results for Atrazine - Waterbase
  :linenos:
  -- https://discodata.eea.europa.eu/
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

```{dropdown} Show code

  ```{code-block} sql
  :caption: Monitoring results for Atrazine - EEA Pesticides Indicator
  :linenos:

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

```{dropdown} Show code

  ```{code-block} sql
  :caption: Monitoring results for Atrazine by water category - EEA Pesticides Indicator
  :linenos:

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

### Groundwater quantitative monitoring - 3ʳᵈ cycle

```{dropdown} Show code

  ```{code-block} sql
  :caption: Groundwater quantitative monitoring - 3ʳᵈ cycle
  :linenos:
  --   https://discodata.eea.europa.eu/
  SELECT [parameterCode]
      ,count(*) as [numberOfRecords]
      ,count(distinct [euMonitoringSiteCode]) as [numberOfSites]
      ,count(distinct [waterbodyCode]) as [numberOfWaterBodies]
      ,count(distinct [countryCode]) as [numberOfCountries]
  FROM [WISE_WFD].[v2r1].[Monitoring_MonitoringSite_ChemicalEcologicalQuantitativeMonitoring] WITH (NOLOCK)
  WHERE [hasDescriptiveData] = 1
  AND [cYear] = 2022
  AND [parameterCode] = 'EEA_00-01-1 - Quantitative monitoring'
  AND [waterBodyCategory] = 'GW'
  GROUP BY [parameterCode]
  ```

### Groundwater chemical monitoring - 3ʳᵈ cycle

```{dropdown} Show code

  ```{code-block} sql
  :caption: Groundwater chemical monitoring - 3ʳᵈ cycle
  :linenos:
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
  FROM [WISE_WFD].[v2r1].[Monitoring_MonitoringSite_ChemicalEcologicalQuantitativeMonitoring] WITH (NOLOCK)
  WHERE [hasDescriptiveData] = 1
  AND [cYear] = 2022
  AND [parameterCode] != 'EEA_00-00-0 - Other parameter'
  AND [parameterCode] != 'EEA_00-01-1 - Quantitative monitoring'
  AND [waterBodyCategory] = 'GW'
  GROUP BY [parameterCode]
  ORDER BY [numberOfRecords] DESC
  ```

(heading_wfd_monitoring_groundwater_physico_chemical_monitoring_in_waterbase)=
### Groundwater physico-chemical monitoring - Waterbase

The table below shows the physico-chemical monitoring in **groundwater**, as reported to Waterbase.

All the parameters possible in **surface water** are listed: 
some of them do not make sense in groundwater (e.g. Secchi depth) 
and/or where never reported to Waterbase.

Those parameters will not be accepted in groundwater monitoring sites:
* EEA_3133-07-1 - Oxidisability
* EEA_3133-02-6 - BOD7
* EEA_3111-01-1 - Secchi depth
* EEA_3161-04-4 - Particulate organic nitrogen
* EEA_3164-08-7 - Nitrate to orthophosphate ratio
* EEA_3164-07-6 - Total nitrogen to total phosphorus ratio
* EEA_3164-01-0 - Chlorophyll a

The list may be modified based on the input of the thematic experts.

```{dropdown} Show table

  ```{table} Groundwater physico-chemical monitoring in Waterbase
  :name: groundwater-physico-chemical-monitoring-in-waterbase
  :width: 100%
  :align: center

  | Parameter                                                | Last year reported     | Number of records     | Number of sites     | Number of countries     |
  |:---------------------------------------------------------|:-----------------------|:----------------------|:--------------------|:------------------------|
  | EEA_31-01-6 - Hardness                                   | 2023                   | 68609                 | 7491                | 11                      |
  | EEA_3142-02-7 - Chlorine Cl-                             | 2023                   | 38397                 | 3224                | 9                       |
  | EEA_3142-01-6 - Electrical conductivity                  | 2023                   | 327302                | 25331               | 29                      |
  | EEA_3141-01-3 - Salinity                                 | 2021                   | 186                   | 87                  | 1                       |
  | EEA_3133-07-1 - Oxidisability                            | «none»                 | «none»                | «none»              | «none»                  |
  | EEA_3133-06-0 - Total organic carbon (TOC)               | 2023                   | 106900                | 9383                | 19                      |
  | EEA_3133-05-9 - Dissolved organic carbon (DOC)           | 2023                   | 27020                 | 4564                | 7                       |
  | EEA_3133-04-8 - CODMn                                    | 2023                   | 44504                 | 3549                | 13                      |
  | EEA_3133-03-7 - CODCr                                    | 2023                   | 350                   | 160                 | 5                       |
  | EEA_3133-02-6 - BOD7                                     | «none»                 | «none»                | «none»              | «none»                  |
  | EEA_3133-01-5 - BOD5                                     | 2023                   | 853                   | 111                 | 6                       |
  | EEA_3132-01-2 - Dissolved oxygen                         | 2023                   | 308192                | 22098               | 34                      |
  | EEA_3131-01-9 - Oxygen saturation                        | 2023                   | 34092                 | 4516                | 6                       |
  | EEA_31615-01-7 - Total nitrogen                          | 2023                   | 11928                 | 1503                | 11                      |
  | EEA_31613-01-1 - Non-ionised ammonia                     | 2021                   | 876                   | 131                 | 2                       |
  | EEA_3121-01-5 - Water temperature                        | 2023                   | 217782                | 20414               | 24                      |
  | EEA_31-03-8 - Total dissolved solids                     | 2023                   | 19892                 | 1985                | 8                       |
  | EEA_31-02-7 - Total suspended solids                     | 2023                   | 1639                  | 163                 | 5                       |
  | EEA_3112-01-4 - Turbidity                                | 2023                   | 3640                  | 654                 | 4                       |
  | EEA_3111-01-1 - Secchi depth                             | «none»                 | «none»                | «none»              | «none»                  |
  | EEA_3161-05-5 - Total inorganic nitrogen                 | 2023                   | 2337                  | 65                  | 1                       |
  | EEA_3161-04-4 - Particulate organic nitrogen             | «none»                 | «none»                | «none»              | «none»                  |
  | EEA_3161-03-3 - Total organic nitrogen                   | 2023                   | 2116                  | 65                  | 1                       |
  | EEA_3161-02-2 - Total oxidised nitrogen                  | 2021                   | 10938                 | 1548                | 2                       |
  | EEA_3161-01-1 - Kjeldahl nitrogen                        | 2019                   | 306                   | 31                  | 4                       |
  | EEA_3153-02-4 - Alkalinity                               | 2023                   | 3192                  | 969                 | 3                       |
  | EEA_3153-01-3 - Acid neutralising capacity to pH 4.5     | 2023                   | 2625                  | 797                 | 2                       |
  | EEA_3152-01-0 - pH                                       | 2023                   | 289088                | 22776               | 29                      |
  | EEA_3151-01-7 - Acid neutralising capacity               | 2023                   | 19191                 | 2026                | 3                       |
  | EEA_3164-08-7 - Nitrate to orthophosphate ratio          | «none»                 | «none»                | «none»              | «none»                  |
  | EEA_3164-07-6 - Total nitrogen to total phosphorus ratio | 2015                   | 3                     | 1                   | 1                       |
  | EEA_3164-01-0 - Chlorophyll a                            | «none»                 | «none»                | «none»              | «none»                  |
  | EEA_3163-01-7 - Silicate                                 | 2023                   | 14015                 | 1693                | 6                       |
  ```

```{dropdown} Show code

  ```{code-block} sql
  :caption: Groundwater monitoring - Waterbase
  :linenos:
  SELECT  [observedPropertyDeterminandCode]
          ,MAX(YEAR([phenomenonTimeSamplingDate])) AS [lastYearReportedInGW]
          ,COUNT(*) AS [numberOfRecordsInGW]
          ,COUNT(DISTINCT [monitoringSiteIdentifier]) AS [numberOfSitesInGW]
          ,COUNT(DISTINCT [countryCode]) AS [numberOfCountriesInGW]
    FROM [WISE_SOE].[latest].[T_WISE6_DisaggregatedData]
    WHERE [parameterWaterBodyCategory] = 'GW'
    GROUP BY [observedPropertyDeterminandCode]
  ```

### Surface water chemical monitoring - 3ʳᵈ cycle

The full list of priority substances and river basin specific pollutants (except 'EEA_00-00-0 - Other parameter'), includes 231 substance codes. 
Note, however, that more substances are being monitored, according to the reported data.

```{dropdown} Show code

  ```{code-block} sql
  :caption: Groundwater chemical monitoring - 3ʳᵈ cycle
  :linenos:
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
  FROM [WISE_WFD].[v2r1].[SWB_SurfaceWaterBody_FailingRBSP]
  WHERE [hasDescriptiveData] = 1
  AND [cYear] = 2022
  AND [swFailingRBSP] != 'EEA_00-00-0 - Other parameter'
  AND [swFailingRBSP] != 'None'
  AND [swFailingRBSP] NOT IN ('CAS_14797-55-8 - Nitrate','CAS_14797-65-0 - Nitrite','CAS_14798-03-9 - Ammonium','CAS_18785-72-3 - Sulphate','EEA_31613-01-1 - Non-ionised ammonia')
 
```


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

```{dropdown} Show code

  ```{code-block} sql
  :caption: River Basin Specific Pollutants - 3ʳᵈ cycle
  :linenos:

  --   https://discodata.eea.europa.eu/

  SELECT [swFailingRBSP], [qeCode],
      count(DISTINCT euSurfaceWaterBodyCode) as [numberOfWaterBodiesFailing],
      count(DISTINCT countryCode) as [numberOfCountries],
      max(countryCode) as [exampleCountry]
  FROM [WISE_WFD].[v2r1].[SWB_SurfaceWaterBody_FailingRBSP] a
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

### Surface water ecological monitoring - 3ʳᵈ cycle

See {numref}`sw_ecological_monitoring`: for an overview of the Surface water ecological monitoring reported in the 3ʳᵈ cycle RBMPs.
Note that more than one substance or parameter can be aggregated under each Quality Element code.

For QE3-1 (General parameters), it is preferable to use the substance code and agregate the reported data to the corresponding quality element. 
Given that both options - quality element code and substance code - were used in the reporting, the query is more complex. 

In the 4ᵗʰ cycle, the use of the CAS and EEA codes should be recommended.
At least the use of the 'QE3-3 - River Basin Specific Pollutants' should be avoided.

```{table} Surface water ecological monitoring - 3ʳᵈ cycle
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

```{dropdown} Show code

  ```{code-block} sql
  :caption: Surface water ecological monitoring - 3ʳᵈ cycle
  :linenos:
  --   https://discodata.eea.europa.eu/
  SELECT COALESCE(b.[qeCode], a.[parameterCode]) AS [qeCode]
      ,count(*) as [numberOfRecords]
      ,count(distinct [euMonitoringSiteCode]) as [numberOfSites]
      ,count(distinct [waterbodyCode]) as [numberOfWaterBodies]
      ,count(distinct [countryCode]) as [numberOfCountries]
  FROM [WISE_WFD].[v2r1].[Monitoring_MonitoringSite_ChemicalEcologicalQuantitativeMonitoring] a
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
 
### Assessment method for quality elements - 3ʳᵈ cycle

All the information analysed above refers to "in-situ" data, i.e. conventional monitoring.

```{dropdown} Show code

  ```{code-block} sql
  :caption: Assessment method for quality elements - 3ʳᵈ cycle
  :linenos:

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
 
## Data extraction - pending issues - 3ʳᵈ cycle

During the data analysis, some incorrect data extraction issues where detected.

```{dropdown} [waterBodyCategory] should not be null - affects 19 sites

  ```{code-block} sql
  :caption: Issue: [waterBodyCategory] should not be null
  :linenos:
  SELECT *
  FROM [WISE_WFD].[v2r1].[Monitoring_MonitoringSite_ChemicalEcologicalQuantitativeMonitoring]
  WHERE [cYear] = 2022
  AND [hasDescriptiveData] = 1
  AND [parameterOther] IS NULL
  AND [waterBodyCategory] is NULL
  ```

```{dropdown} Inadequate reclassification to 'Missing', should be 'Inapplicable'

  ```{code-block} sql
  :caption: Issue: [waterBodyCategory] Inadequate reclassification to 'Missing', should be 'Inapplicable'
  :linenos:
  SELECT *
  FROM [WISE_WFD].[v2r1].[Monitoring_MonitoringSite_ChemicalEcologicalQuantitativeMonitoring]
  WHERE [cYear] = 2022
  AND [hasDescriptiveData] = 1
  AND [parameterOther] IS NULL
  AND [waterBodyCategory] is NULL
  ```

(heading_wfd_monitoring_references)=
## References

```{include} FragmentWFD2022ReportingSchemas
```
