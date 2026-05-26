(heading_wfd_pressures)=
# Significant pressure codelist

## Overview

This section describes the review of the `PressureType` codelist used in the 3ʳᵈ cycle reporting.

The review focused on the following aspects:

* to address the issues raised by Member States on the use of option 'P8 - Anthropogenic pressure - Unknown'
* to implement the overall approach of removing textual reporting of 'other' pressures
* to allow flexibility in the level of reporting 
  (e.g. use 'P2 - Diffuse sources' instead of 'P2-10 - Diffuse - Other' if the applicable pressure is not present in the codelist)
* to revise the wording of some of the options (while mantaining the code structure to facilitate the mapping).

(heading_wfd_pressure_type_codelist_4th_cycle)=
### PressureType codelist - 4ᵗʰ cycle

The `PressureType` codelist is a hierarchical codelist (see {numref}`PressureType_4thCycle_Codelists_ClassDiagram`). 

The codelist provides the domain for several attributes related to pressures, in different tables.

Depending on the context, the use of some codes may be restricted by quality control.
(For example, options 'P4-1%', 'P4-2%' or 'P5%' are unlikely to apply to groundwater.)

Regardless of the hierarchical structure, the most detailed applicable option should be selected when reporting.

```{mermaid} /DataModelReview/mmd/PressureType_4thCycle_Codelists_ClassDiagram.mmd
:name: PressureType_4thCycle_Codelists_ClassDiagram
:caption:  Codelist - PressureType - 4ᵗʰ cycle
:align: center
:zoom:
```

The {ref}`PressuresType_3rdCycle_4thCycle_MappingTable` clarifies the correspondence between codelist values.

```{dropdown} Show mapping table
```{include} tables/PressuresType_3rdCycle_4thCycle_MappingTable
```

## Annexes - Data analysis - 3ʳᵈ cycle

```{include} FragmentAnnexesDataAnalysis3rdCycle
```

### Surface water bodies with 'P8 - Anthropogenic pressure - Unknown' and unknown chemical status

```{epigraph}
A Member State flagged that where a water body is reported to be in unknown chemical status, a pressure must also be reported on that water body. This resulted in the Member State reporting 60% of surface water bodies to be affected by unknown anthropogenic pressures. The Member State representative said that in reality, the percentage of waterbodies with an unknown pressure was approximately 10%. I.e. this resulted in a large difference between the data reported electronically, and the actual situation in the Member State.
```

```{todo} 
Significant pressures - Provide link to report 

ASSESSMENT OF THE THIRD RIVER BASIN MANAGEMENT PLANS (RBMPS) - APPENDIX - LESSONS LEARNT - ELECTRONIC REPORTING

```

This was indeed an issue.
The situation described is likely cause by the fact that there is no option 'Unknown' in the 3ʳᵈ cycle codelist.
In fact, the reporting guidance says that 'P8 - Anthropogenic pressure - Unknown' is only relevant where status is lower than good and pressure is unknown.

For the future, the codelist should include the option 'unknown', to be used in this scope.
(Also the option can be used if status is unknown.)

```{dropdown} Show code
```{code-block} sql
:caption: Surface water bodies with unknown chemical status, non-failing ecological status and 'P8 - Anthropogenic pressure - Unknown' - 3ʳᵈ cycle
:linenos:
-- Query 1: unknown chemical status, non-failing ecological status
SELECT a.countryCode,
       a.numberOfWaterBodies,
       b.numberOfWaterBodies_potentiallyWithIssue,
       c.numberOfWaterBodies_actuallyWithIssue,
       round(cast(b.numberOfWaterBodies_potentiallyWithIssue as float) * 100 / a.numberOfWaterBodies, 1) AS percent_potentiallyWithIssue,
       round(cast(c.numberOfWaterBodies_actuallyWithIssue as float) * 100 / a.numberOfWaterBodies, 1) AS percent_actuallyWithIssue
FROM (
    SELECT countryCode, count(distinct euSurfaceWaterBodyCode) AS numberOfWaterBodies
    FROM WISE_WFD.v2r1.SWB_SurfaceWaterBody
    WHERE cYear = 2022
      AND surfaceWaterBodyCategory != 'TeW'
    GROUP BY countryCode
) a
JOIN (
    SELECT countryCode, count(distinct euSurfaceWaterBodyCode) AS numberOfWaterBodies_potentiallyWithIssue
    FROM WISE_WFD.v2r1.SWB_SurfaceWaterBody
    WHERE cYear = 2022
      AND surfaceWaterBodyCategory != 'TeW'
      AND swChemicalStatusValue = 'Unknown'
      AND swEcologicalStatusOrPotentialValue NOT IN ('3','4','5')
    GROUP BY countryCode
) b
  ON a.countryCode = b.countryCode
JOIN (
    SELECT countryCode,
           swSignificantPressureType,
           count(distinct euSurfaceWaterBodyCode) AS numberOfWaterBodies_actuallyWithIssue
    FROM (
        SELECT countryCode,
               euSurfaceWaterBodyCode,
               max(swSignificantPressureType) AS swSignificantPressureType
        FROM WISE_WFD.v2r1.SWB_SurfaceWaterBody_swSignificantPressureType
        WHERE cYear = 2022
          AND surfaceWaterBodyCategory != 'TeW'
          AND swChemicalStatusValue = 'Unknown'
          AND swEcologicalStatusOrPotentialValue NOT IN ('3','4','5')
        GROUP BY countryCode, euSurfaceWaterBodyCode
        HAVING count(DISTINCT swSignificantPressureType) = 1
           AND max(swSignificantPressureType) = 'P8 - Anthropogenic pressure - Unknown'
    ) x
    GROUP BY countryCode, swSignificantPressureType
) c
  ON a.countryCode = c.countryCode
ORDER BY percent_actuallyWithIssue DESC;
```

### Groundwater water bodies with 'P8 - Anthropogenic pressure - Unknown' and unknown chemical status

The issue above didn't appear to affect groundwater bodies.
But nevertheless it will be solved for both.

```{dropdown} Show code
```{code-block} sql
:caption: Groundwater bodies with unknown chemical status, non-failing quantitative status and 'P8 - Anthropogenic pressure - Unknown' - 3ʳᵈ cycle
:linenos:
-- Query 1: unknown chemical status, non-failing quantitative status, and only P8 significant pressure type
SELECT a.countryCode,
       a.numberOfWaterBodies,
       b.numberOfWaterBodies_potentiallyWithIssue,
       c.numberOfWaterBodies_actuallyWithIssue,
       round(cast(b.numberOfWaterBodies_potentiallyWithIssue as float) * 100 / a.numberOfWaterBodies, 1) AS percent_potentiallyWithIssue,
       round(cast(c.numberOfWaterBodies_actuallyWithIssue as float) * 100 / a.numberOfWaterBodies, 1) AS percent_actuallyWithIssue
FROM (
    SELECT countryCode, count(distinct euGroundWaterBodyCode) AS numberOfWaterBodies
    FROM WISE_WFD.v2r1.GWB_GroundWaterBody
    WHERE cYear = 2022
      AND hasDescriptiveData = 1
    GROUP BY countryCode
) a
JOIN (
    SELECT countryCode, count(distinct euGroundWaterBodyCode) AS numberOfWaterBodies_potentiallyWithIssue
    FROM WISE_WFD.v2r1.GWB_GroundWaterBody
    WHERE cYear = 2022
      AND hasDescriptiveData = 1
      AND gwChemicalStatusValue = 'Unknown'
      AND gwQuantitativeStatusValue NOT IN ('3')
    GROUP BY countryCode
) b
  ON a.countryCode = b.countryCode
JOIN (
    SELECT countryCode,
           gwSignificantPressureType,
           count(distinct euGroundWaterBodyCode) AS numberOfWaterBodies_actuallyWithIssue
    FROM (
        SELECT countryCode,
               euGroundWaterBodyCode,
               max(gwSignificantPressureType) AS gwSignificantPressureType
        FROM WISE_WFD.v2r1.GWB_GroundWaterBody_gwSignificantPressureType
        WHERE cYear = 2022
          AND hasDescriptiveData = 1
          AND gwChemicalStatusValue = 'Unknown'
          AND gwQuantitativeStatusValue NOT IN ('3')
        GROUP BY countryCode, euGroundWaterBodyCode
        HAVING count(DISTINCT gwSignificantPressureType) = 1
           AND max(gwSignificantPressureType) = 'P8 - Anthropogenic pressure - Unknown'
    ) x
    GROUP BY countryCode, gwSignificantPressureType
) c
  ON a.countryCode = c.countryCode
ORDER BY percent_actuallyWithIssue DESC;
```

### Groundwater bodies where the single pressure causing failure is 'P6-1 - Groundwater - Recharges'

A total of 124 groundwater bodies have 'P6-1 - Groundwater - Recharges' as a significant pressure.
But only 12 groundwater bodies have 'P6-1 - Groundwater - Recharges' as the *single* significant pressure.

```{dropdown} Show code
```{code-block} sql
:caption: Groundwater bodies where the single pressure causing failure is 'P6-1 - Groundwater - Recharges' - 3ʳᵈ cycle
:linenos:
SELECT euGroundWaterBodyCode, gwChemicalStatusValue, gwQuantitativeStatusValue
FROM [WISE_WFD].[v2r1].[GWB_GroundWaterBody_gwSignificantPressureType]
WHERE [cYear] = 2022 AND [hasDescriptiveData] = 1
AND euGroundWaterBodyCode IN
(
-- Of which only 16 have only P6 significant pressure type and failing chemical or quantitative status, and no other significant pressure types.
SELECT euGroundWaterBodyCode
FROM [WISE_WFD].[v2r1].[GWB_GroundWaterBody_gwSignificantPressureType]
WHERE [cYear] = 2022 AND [hasDescriptiveData] = 1
AND [euGroundWaterBodyCode] in 
  ( -- 124 Ground Water Bodies with P6 significant pressure type and failing chemical or quantitative status
  SELECT euGroundWaterBodyCode
  FROM [WISE_WFD].[v2r1].[GWB_GroundWaterBody_gwSignificantPressureType]
  WHERE [cYear] = 2022 AND [hasDescriptiveData] = 1
  AND [gwSignificantPressureType] LIKE 'P6%'
  AND (gwChemicalStatusValue = '3' or gwQuantitativeStatusValue = '3') 
  ) 
  GROUP BY euGroundWaterBodyCode
  HAVING COUNT(DISTINCT gwSignificantPressureType) = 1
  ) 

```

### Surface bodies where the single pressure causing failure is 'P6-1 - Groundwater - Recharges'

A total of 37 surface water bodies have 'P6-1 - Groundwater - Recharges' as a significant pressure.
But **zero** surface water bodies have 'P6-1 - Groundwater - Recharges' as the *single* significant pressure.

```{dropdown} Show code
```{code-block} sql
:caption: Surface bodies where the single pressure causing failure is 'P6-1 - Groundwater - Recharges' - 3ʳᵈ cycle
:linenos:

SELECT euSurfaceWaterBodyCode, swChemicalStatusValue, swEcologicalStatusOrPotentialValue
FROM [WISE_WFD].[v2r1].[SWB_SurfaceWaterBody_swSignificantPressureType]
WHERE [cYear] = 2022 AND [hasDescriptiveData] = 1
AND euSurfaceWaterBodyCode IN
(
-- Of which ZERO have only P6 significant pressure type and failing chemical or quantitative status, and no other significant pressure types.
SELECT euSurfaceWaterBodyCode
FROM [WISE_WFD].[v2r1].[SWB_SurfaceWaterBody_swSignificantPressureType]
WHERE [cYear] = 2022 AND [hasDescriptiveData] = 1
AND euSurfaceWaterBodyCode in 
  ( -- 37 Surface water Bodies with P6 significant pressure type and failing chemical or ecological status
  SELECT euSurfaceWaterBodyCode
  FROM [WISE_WFD].[v2r1].[SWB_SurfaceWaterBody_swSignificantPressureType]
  WHERE [cYear] = 2022 AND [hasDescriptiveData] = 1
  AND [swSignificantPressureType] LIKE 'P6%'
  AND (swChemicalStatusValue = '3' or swEcologicalStatusOrPotentialValue in ('3','4','5')) 
  ) 
  GROUP BY euSurfaceWaterBodyCode
  HAVING COUNT(DISTINCT swSignificantPressureType) = 1
  ) 
```