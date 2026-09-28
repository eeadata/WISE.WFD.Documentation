(heading_wfd_grouping)=
# Grouping

## Annexes - Data analysis - 3rd cycle

```{include} FragmentAnnexesDataAnalysis3rdCycle
```

The data for this section can be derived from the following tables:

* [WISE_WFD].[v2r1].[SWB_SurfaceWaterBody_QualityElement]
* [WISE_WFD].[v2r1].[SWB_SurfaceWaterBody_QualityElement_qeGrouping]
* [WISE_WFD].[v2r1].[Monitoring_MonitoringSite_ChemicalEcologicalQuantitativeMonitoring]
* Published WISE Spatial datasets

To simplify the analysis, the information
was extracted into a graph structure
with *nodes* representing water bodies,
and *edges* representing the link
between monitored water bodies and
the water bodies with grouping.

```{dropdown} Show description
```{code-block} sql
:caption: Grouping - description of the tables used for analysis

SELECT [countryCode]
      ,[fromNodeId]   -- water body providing the monitoring data
      ,[toNodeId]     -- water body being assessed
      ,[qeCode]       -- quality element being assessed 
  FROM [edges]

-- Water bodies as "nodes"
SELECT [countryCode]    -- country code
      ,[nodeId]         -- water body identifier
      ,[waterCategory]  -- RW, LW, TW, CW
      ,[lat]            -- latitude in WGS84
      ,[lon]            -- longitude in WGS84
      ,[outDegree]      -- number of water body X QE using monitoring data from this water body
      ,[inDegree]       -- number of water body X QE providing monitoring data for the assessment of this water body
  FROM [nodes]

-- "nodes" with qeStatus plus derived information
SELECT [countryCode]      -- country code
      ,[nodeId]           -- water body identifier
      ,[waterCategory]    -- water body category
      ,[qeCode]           -- quality element code
      ,[qeStatus]         -- quality element status ('1','2','3','4','5','unknown',...)
      ,[assessmentMethod] -- assessment method
      ,[outDegree]        -- number of water bodies that are assessed based on data from this water body for the quality element
      ,[inDegree]         -- number of water bodies provide data for the assessment of this water body and quality element
      ,[isMonitored]      -- Monitoring schema: 1 if the water body is monitored for the quality element, 0 otherwise,
  FROM [nodes_qeStatus]

-- data from the Monitoring schema reporting
SELECT [countryCode] -- country code
      ,[nodeId]      -- water body identifier
      ,[qeCode]      -- quality element code
      ,[isMonitored] -- Monitoring schema: 1 if the water body is monitored for the quality element, 0 otherwise 
  FROM [nodes_qeCode_isMonitored]

```

(heading_wfd_quality_elements_grouping)=
## Grouping and quality elements

```{epigraph}
"Reporting on the status assessment of Quality Elements (QEs) 
is expected not only where monitoring results are available for specific water bodies 
but also for all water bodies for which this information is available (e.g. through grouping). 
A status value should, therefore, be given for each of the relevant QEs 
that have been assessed for the water body 
and subsequently used to classify the ecological status or potential of the water body."
-- From the WFD Reporting Guidance 2022 
```

## Grouping with water bodies that were not assessed by monitoring

```{epigraph}
"Schema element: qeGrouping  
Guidance on completion of schema element: Conditional. 
If no monitoring data is available for this quality element in this surface water body 
and status has been derived through grouping 
by extrapolating monitoring data from other surface water bodies,
indicate the codes of the surface water bodies which have been monitored
and used for the classification of this water body.
For example, if the status of surface water body A has been determined
by extrapolating monitoring data from surface water bodies B and C, 
then the euSurfaceWaterBodyCode for surface water bodies B and C should be reported in this element.
Quality checks: Conditional check: Report if and only if qeMonitoringResults is ‘Grouping’.
Within-schema check: Each water body code reported must be identical to a thematicIdIdentifier
reported for surface water bodies in spatial data.
Cross-schema check: The SurfaceWaterBodyCode belongs to a different RBD. 
Please check that for that euSurfaceWaterBodyCode and qeCode, the value of qeMonitoringResults is 'Grouping'.
Cross-schema check: If a euSurfaceWaterBodyCode is valid and belongs to the same RBD, 
then the following condition must be true: for that euSurfaceWaterBodyCode and qeCode, 
the value of qeMonitoringResults must be 'Grouping'."
-- From the WFD Reporting Guidance 2022 
```

The "Cross-schema check" specifications are incorrect
and inconsistent with the "Guidance on completion of schema element"
that requires the extrapolation to be made from a water body
with qeMonitoringResults = 'Monitoring' (and not 'Grouping').
The implementation of the quality control (i.e. the code base) was imperfect:

* For grouping across water bodies in different river basin districts,
  only an indicative ERROR could be flagged (because the reporting was done at RBD scale).
  The resulting inconsistencies affect 11861 of 230115 records (5.2%), mostly in Greece.
* For grouping with water bodies in the same river basin district,
  the inconsistencies affect only 669 records (0.3%).
  The cause was possibly a failure in the quality control process,
  but it is not possible to trace it back at this point.

```{dropdown} Show results
```{csv-table} Grouping - inconsistencies due to inadequate quality control - 3rd cycle
:name: Grouping_water_bodies_inconsistencies_due_to_quality_control_3rdCycle_Table
:header-rows: 1
:delim: "|"
country|qeCode|wb in different RBD |wb in same RBD|water bodies
BE|QE1-1 - Phytoplankton|0|1|1
BE|QE3-1-6-2 - Phosphorus conditions|0|1|1
BG|QE1-2-3 - Macrophytes|0|2|2
BG|QE1-2-4 - Phytobenthos|0|1|1
BG|QE1-4 - Fish|0|1|1
EL|QE1-1 - Phytoplankton|0|2|2
EL|QE1-2-1 - Macroalgae|0|2|2
EL|QE1-2-2 - Angiosperms|0|9|9
EL|QE1-2-3 - Macrophytes|1577|1|1578
EL|QE1-2-4 - Phytobenthos|985|26|1011
EL|QE1-3 - Benthic invertebrates|1155|59|1214
EL|QE1-4 - Fish|1100|53|1153
EL|QE2-2 - River continuity conditions|1801|78|1879
EL|QE2-3 - Morphological conditions|977|104|1081
EL|QE3-1-1 - Transparency conditions|0|76|76
EL|QE3-1-3 - Oxygenation conditions|931|6|937
EL|QE3-1-6-1 - Nitrogen conditions|931|6|937
EL|QE3-1-6-2 - Phosphorus conditions|821|6|827
EL|QE3-3 - River Basin Specific Pollutants|1574|22|1596
ES|QE1-2-3 - Macrophytes|0|13|13
ES|QE1-2-4 - Phytobenthos|0|6|6
ES|QE1-3 - Benthic invertebrates|0|5|5
ES|QE1-4 - Fish|0|1|1
ES|QE2-3 - Morphological conditions|0|3|3
ES|QE3-1-3 - Oxygenation conditions|0|4|4
ES|QE3-1-4 - Salinity conditions|0|6|6
ES|QE3-1-5 - Acidification status|0|2|2
ES|QE3-3 - River Basin Specific Pollutants|0|3|3
HR|QE1-2-1 - Macroalgae|0|2|2
IE|QE1-2 - Other aquatic flora|0|36|36
IT|QE1-2-3 - Macrophytes|1|5|6
IT|QE1-2-4 - Phytobenthos|0|3|3
IT|QE1-3 - Benthic invertebrates|1|7|8
IT|QE1-4 - Fish|0|4|4
IT|QE2-1 - Hydrological or tidal regime|1|1|2
IT|QE2-2 - River continuity conditions|0|1|1
IT|QE2-3 - Morphological conditions|0|1|1
IT|QE3-1-2 - Thermal conditions|0|1|1
IT|QE3-1-3 - Oxygenation conditions|1|3|4
IT|QE3-1-5 - Acidification status|0|1|1
IT|QE3-1-6-1 - Nitrogen conditions|1|3|4
IT|QE3-1-6-2 - Phosphorus conditions|1|3|4
IT|QE3-3 - River Basin Specific Pollutants|3|7|10
LT|QE2-2 - River continuity conditions|0|1|1
LT|QE3-1-3 - Oxygenation conditions|0|1|1
LV|QE3-1-6-1 - Nitrogen conditions|0|1|1
LV|QE3-1-6-2 - Phosphorus conditions|0|1|1
SE|QE1-1 - Phytoplankton|0|7|7
SE|QE1-4 - Fish|0|3|3
SE|QE3-1-1 - Transparency conditions|0|4|4
SE|QE3-1-5 - Acidification status|0|58|58
SE|QE3-1-6-2 - Phosphorus conditions|0|14|14
SK|QE3-3 - River Basin Specific Pollutants|0|2|2
```

```{dropdown} Show code
```{code-block} sql
:caption: Grouping - inconsistencies due to inadequate quality control - 3rd cycle
:linenos:
SELECT [countryCode]
      ,[qeCode]
      ,SUM(IIF([to_euRBDCode] != [from_euRBDCode],1,0)) AS [numberInDifferentBasin]
      ,SUM(IIF([to_euRBDCode] = [from_euRBDCode],1,0)) AS [numberInSameBasin]
      ,COUNT(*) AS [totalNumber]
      FROM 
(SELECT -- toNode

       a.[countryCode]
      ,a.[qeCode]

      ,a.[euRBDCode] as [to_euRBDCode]
      ,a.[euSurfaceWaterBodyCode] as [to_euSurfaceWaterBodyCode]
      ,a.[surfaceWaterBodyCategory] as [to_surfaceWaterBodyCategory]
      ,a.[qeMonitoringResults] as [to_qeMonitoringResults]
      ,a.[qeGrouping] as [to_qeGrouping]
      
      -- fromNode
      ,b.[euRBDCode] as [from_euRBDCode]
      ,b.[surfaceWaterBodyCategory] as [from_surfaceWaterBodyCategory]
      ,b.[qeCode] as [from_qeCode]
      ,b.[qeMonitoringResults] as [from_qeMonitoringResults]
      ,b.[qeGrouping] as [from_qeGrouping]
      
  FROM [WISE_WFD].[v2r1].[SWB_SurfaceWaterBody_QualityElement_qeGrouping] a
  
  LEFT JOIN [WISE_SOW].[v2r1].[SWB_SurfaceWaterBody_QualityElement_qeGrouping] b
    ON a.[countryCode] = b.[countryCode]
    AND a.[qeGrouping] = b.[euSurfaceWaterBodyCode]
    AND a.[qeCode] = b.[qeCode]
    AND a.[cYear] = b.[cYear] 
    
  WHERE a.[cYear] = 2022 AND a.[hasDescriptiveData] = 1
  AND a.[qeMonitoringResults] = 'Grouping' 
  --AND a.[qeCode] != 'QE3-3 - River Basin Specific Pollutants'
  ) a

  WHERE [from_qeMonitoringResults] != 'Monitoring'
  GROUP BY [countryCode], [qeCode]
  ORDER BY [countryCode], [qeCode]
  ```

### Inconsistencies with the data in the Monitoring schema

The information provided in the Monitoring schema
might have provided an alternative data source
to understand which water bodies where actually monitored.

However, in that specific case there was no quality control specified
between the grouping data and the Monitoring schema data.

Therefore, and as the results of the {numref}`Grouping_water_bodies_inconsistencies_with_the_monitoring_schema_data_3rdCycle_Table`
show, the inconsistencies between the grouping data and the monitoring schema data are high.
According to the grouping data, 3550 monitored water bodies had their data
extrapolated for the assessment of water bodies not monitored.
However, for 2225 of those water bodies (62%)
there is no evidence (in the Monitoring schema) of the water body having been monitored
for (at least one of) the expected Quality Element.

```{csv-table} Grouping - inconsistencies with the Monitoring schema data - 3rd cycle
:name: Grouping_water_bodies_inconsistencies_with_the_monitoring_schema_data_3rdCycle_Table
:header-rows: 1
:delim: "|"
qeCode|countries|waterBodies|with inconsistency|percentage
QE1-1 - Phytoplankton|13|247|29|11
QE1-2 - Other aquatic flora|4|45|22|48
QE1-2-1 - Macroalgae|3|29|3|10
QE1-2-2 - Angiosperms|3|44|5|11
QE1-2-3 - Macrophytes|11|684|125|18
QE1-2-4 - Phytobenthos|11|1643|351|21
QE1-3 - Benthic invertebrates|15|1875|306|16
QE1-4 - Fish|14|1022|108|10
QE2-1 - Hydrological or tidal regime|6|250|12|4
QE2-2 - River continuity conditions|7|325|99|30
QE2-3 - Morphological conditions|8|441|126|28
QE3-1-1 - Transparency conditions|8|66|55|83
QE3-1-2 - Thermal conditions|7|386|171|44
QE3-1-3 - Oxygenation conditions|16|1616|1034|63
QE3-1-4 - Salinity conditions|9|374|161|43
QE3-1-5 - Acidification status|11|644|369|57
QE3-1-6-1 - Nitrogen conditions|16|1717|1058|61
QE3-1-6-2 - Phosphorus conditions|17|1800|1189|66
QE3-3 - River Basin Specific Pollutants|13|1820|544|29
«all»|19|3550|2225|62
```

```{dropdown} Show code
```{code-block} sql
:caption: Grouping_water_bodies_grouped_with_themselves_3rdCycle_Table
:linenos:

SELECT [qeCode]
      ,COUNT(DISTINCT [countryCode]) AS [numberOfCountries]
      ,COUNT(DISTINCT [nodeId]) AS [numberOfWaterBodies]
      ,COUNT(DISTINCT IIF([isMonitored] = 0,[nodeId],NULL)) AS [number_withInconsistency]
      ,COUNT(DISTINCT IIF([isMonitored] = 0,[nodeId],NULL))*100/ COUNT(DISTINCT [nodeId]) AS [percentage_withInconsistency]
  FROM [nodes_qeStatus]
  WHERE NOT ([outDegree] > 0 AND [inDegree] > 0)
  AND [outDegree] > 0
  GROUP BY [qeCode] WITH ROLLUP
  ORDER BY [qeCode]

```

#### Basic errors

```{csv-table} Grouping - water bodies grouped with themselves - 3rd cycle
:name: Grouping_water_bodies_grouped_with_themselves_3rdCycle_Table
:header-rows: 1
:delim: "|"

countryCode|from|to|qeCode
IE|IEWE_160_0700|IEWE_160_0700|QE1-2 - Other aquatic flora
IT|IT19CW04794|IT19CW04794|QE3-1-3 - Oxygenation conditions
IT|IT19CW04794|IT19CW04794|QE3-1-6-1 - Nitrogen conditions
IT|IT19CW04794|IT19CW04794|QE3-1-6-2 - Phosphorus conditions
IT|ITF015RWN011012156SABATO18SS3|ITF015RWN011012156SABATO18SS3|QE1-2-4 - Phytobenthos
IT|ITF015RWN011012156SABATO18SS3|ITF015RWN011012156SABATO18SS3|QE1-3 - Benthic invertebrates
```

```{dropdown} Show code
```{code-block} sql
:caption: Grouping - water bodies grouped with themselves - 3rd cycle
:linenos:

SELECT [countryCode]
      ,[fromNodeId]
      ,[toNodeId]
      ,[qeCode]
  FROM [edges]
  WHERE [fromNodeId] = [toNodeId];
```

```{csv-table} Grouping - water bodies both receiving and providing data of a given quality element - 3rd cycle
:name: Grouping_water_bodies_both_receiving_and_providing_data_for_a_qe_3rdCycle_Table
:header-rows: 1
:delim: "|"

country|nodeId|waterCategory|qeCode|qeStatus|outDegree|inDegree|isMonitored
IE|IESW_060_0100|TW|QE1-2 - Other aquatic flora|3|1|1|0
IE|IEWE_160_0700|CW|QE1-2 - Other aquatic flora|3|3|1|0
IT|IT09CI_R000OM173CA|RW|QE3-1-6-2 - Phosphorus conditions|2|1|1|0
IT|IT09CI_R000OM173CA|RW|QE3-1-3 - Oxygenation conditions|2|1|1|0
IT|IT09CI_R000OM173CA|RW|QE3-1-6-1 - Nitrogen conditions|2|1|1|0
IT|IT10N0100121AF|RW|QE3-1-5 - Acidification status|1|1|1|0
IT|IT10N0100121AF|RW|QE3-1-2 - Thermal conditions|1|1|1|0
IT|IT10N0100121AF|RW|QE3-1-3 - Oxygenation conditions|1|1|1|0
IT|IT10N0100121AF|RW|QE1-3 - Benthic invertebrates|2|1|1|0
IT|IT10N0100121AF|RW|QE3-1-6-2 - Phosphorus conditions|1|1|1|0
IT|IT10N0100121AF|RW|QE3-1-6-1 - Nitrogen conditions|1|1|1|0
IT|IT10N0100121AF|RW|QE3-3 - River Basin Specific Pollutants|1|1|1|0
IT|IT19CW04794|CW|QE3-1-6-2 - Phosphorus conditions|2|1|1|0
IT|IT19CW04794|CW|QE3-3 - River Basin Specific Pollutants|2|1|1|0
IT|IT19CW04794|CW|QE3-1-3 - Oxygenation conditions|2|1|1|0
IT|IT19CW04794|CW|QE3-1-6-1 - Nitrogen conditions|2|1|1|0
IT|ITF015RWN011012156SABATO18SS3|RW|QE1-3 - Benthic invertebrates|5|1|1|0
IT|ITF015RWN011012156SABATO18SS3|RW|QE1-2-4 - Phytobenthos|1|1|1|0
HR|HRJMO013|CW|QE1-2-1 - Macroalgae|1|2|1|1
IT|IT09CI_R000OM173CA|RW|QE3-3 - River Basin Specific Pollutants|3|1|1|1
```

```{dropdown} Show code
```{code-block} sql
:caption: Grouping - water bodies both receiving and providing data - 3rd cycle
:linenos:
  SELECT [countryCode]
      ,[nodeId]
      ,[waterCategory]
      ,[qeCode]
      ,[qeStatus]
      ,[outDegree]
      ,[inDegree]
      ,[isMonitored]
  FROM [WISE_Sandbox].[tmp_grouping].[nodes_qeStatus]
  WHERE [outDegree] > 0 AND [inDegree] > 0
  ORDER BY [isMonitored],[nodeId];
```

### Subset of countries for further analysis

The proportion of problematic records is relatively low:
1081 out of 88156 records (1.2%) and 343 out of 16958 water bodies (2%).

Nevertheless, a decision was taken to further analyse
only a subset of 8 countries that have data regarding grouping
where none of above issues was detected.

From the subset of countries:

1. Austria, Romania and Portugal have the highest absolute number of water bodies
   where grouping was applied,
2. Austria uses several monitored water bodies for the assessment of a given water body.
   Other countries reported similar approaches (EL,ES,IT,SE,SK),
   but were not included in the subset, due to data quality issues.
3. The remaining countries use only one monitored water body for each water body assessed via grouping.
   Monitored water bodies may supply data for the assessment of several non-monitored water bodies.

```{dropdown} Show results
```{csv-table} Grouping - Countries with grouping data, and no detected issues - 3rd cycle
:name: Grouping_countries_with_grouping_and_no_issues_3rdCycle_Table
:header-rows: 1
:delim: "|"
country|qeCount|wbMonitoring|wbGrouping|wbEither|maxOutDegree|maxInDegree
AT|6|1278|8002|8076|1718|25
CZ|11|24|29|53|3|1
DK|9|10|13|23|3|1
HU|6|72|78|149|2|1
NL|11|31|61|88|14|1
PT|16|148|228|376|7|1
RO|15|318|1497|1760|145|1
SI|6|2|3|5|2|1
```

```{dropdown} Show code
```{code-block} sql
:caption: Grouping - Countries with available data, and no detected issues - 3rd cycle
:linenos:
SELECT [countryCode]
      ,COUNT(DISTINCT qeCode) AS [qeCount]
      ,COUNT(DISTINCT IIF([outDegree] > 0, nodeId,NULL)) AS [wbMonitoring]
      ,COUNT(DISTINCT IIF([inDegree] > 0, nodeId,NULL))  AS [wbGrouping]
      ,COUNT(DISTINCT nodeId)  AS [wbEither]
      ,MAX(outDegree) AS [maxOutDegree]
      ,MAX(inDegree) AS [maxInDegree]
  FROM [nodes_qeStatus]
  WHERE [countryCode] NOT IN
  (
    SELECT [countryCode]
          -- ,COUNT(*) as [count]
      FROM [WISE_Sandbox].[tmp_grouping].[nodes_qeStatus]
      WHERE ([outDegree] > 0 AND [inDegree] > 0)      -- error
      OR ([outDegree] > 0 AND [assessmentMethod] != 'Monitoring')  -- also an error
      GROUP BY [countryCode] )
  GROUP BY [countryCode]
  ```
