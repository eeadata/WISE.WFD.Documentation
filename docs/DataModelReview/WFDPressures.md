(heading_wfd_pressure_type_codelist_4th_cycle)=
# PressureType codelist - 4th cycle

The review of the pressure types codelist used in the 3rd cycle of reporting 
is detailed in the {ref}`heading_wfd_pressures_annexes` and resulted in the following changes:

* A generic option 'unknown' was added.
* A generic option 'none' was added.
* The wording of some of the options was revised (while mantaining the code structure to facilitate the mapping).
* The option 'P7 - Anthropogenic pressure - Other' was removed.
* The option 'P8 - Anthropogenic pressure - Unknown' was removed.
* The option 'P9 - Anthropogenic pressure - Historical pollution' was removed.
* The option 'P1-9 - Point - Other' was replaced by 'P1 - Point'
* The option 'P2-10 - Diffuse - Other' was replaced by 'P2 - Diffuse'
* The option 'P3-7 - Abstraction - Other' was replaced by 'P3 - Abstraction'
* The option 'P4-1-4 - Physical alteration of channel/bed/riparian area/shore - Other' was replaced by 'P4-1 - Longitudinal barrier'
* The option 'P4-2-8 - Dams, barriers and locks - Other' was replaced by 'P4-2 - Transversal barrier'
* The option 'P4-3-6 - Hydrological alteration - Other' was replaced by 'P4-3 - Hydrological alteration'
* The option 'P4-5 - Hydromorphological alteration - Other' was replaced by 'P4-5 - Hydromorphological alteration'

The revised `PressureType` codelist is a hierarchical codelist 
(see {numref}`Codelist_4thCycle_PressureType_ClassDiagram`).  
It provides a controlled list of values for different attributes related to pressures.  
Depending on the attribute and the context, the use of some values may be restricted by the quality control. For example: options 'P4-1%', 'P4-2%' or 'P5%' are unlikely to apply to groundwater, options like 'P6%' are unlike to apply to surface water bodies.

```{mermaid} /DataModelReview/mmd/Codelist_4thCycle_PressureType_ClassDiagram.mmd
:name: Codelist_4thCycle_PressureType_ClassDiagram
:caption:  Codelist - PressureType - 4th cycle
:align: center
:zoom:
```

In the pressures codelist used in the 2nd and 3rd cycle of reporting,
most options combined both a pressure and a driver (see {numref}`PressuresAndImpacts_DPSIRFramework_Table`).
For example: abstraction + agriculture = 'P3-1 - Abstraction - Agriculture'.

This structure was kept in the current codelist. Regardless of the hierarchical structure, the most detailed applicable option should be selected when reporting. If the specific driver is not in the codelist, the higher level code can be used.
Note that not all the drivers defined in the 3rd cycle reporting guidance (see {numref}`Codelist_3rdCycle_DriverType_Table`) are listed.

```{include} tables/PressuresAndImpacts_DPSIRFramework_Table
```

```{include} tables/Codelist_3rdCycle_DriverType_Table
```

```{todo}
Pressures codelist - Definition of the drivers
ENV or EEA Water to complete, and define if any should be added.
```

The {ref}`PressuresType_3rdCycle_4thCycle_MappingTable` clarifies the correspondence 
between the codelist values in the 3rd cycle and in the 4th cycle.

```{dropdown} Show mapping table
```{include} tables/PressuresType_3rdCycle_4thCycle_MappingTable
```

(heading_wfd_pressures_annexes)=
## Annexes - Data analysis - 3rd cycle

```{include} FragmentAnnexesDataAnalysis3rdCycle
```

The codelist of significant pressures used in the 3rd cycle 
includes three options generic values:

*  'P7 - Anthropogenic pressure - Other', which then requires a textual explanation to be provided;
*  'P8 - Anthropogenic pressure - Unknown'
*  'P9 - Anthropogenic pressure - Historical pollution'

The options P7, P8 and P9 are problematic:

* P7 can potentially be used as a "catch-all" option, 
  that requires human analysis to understand what is reported in the text.
* P8 was flagged has problematic by Member States. 
  It is reasonable to have an 'unknown' option, if the water body status is itself unknown, but perhaps not in other circunstances.
* P9 is not informative because it does not clarify 
  what type of historical pollution is actually being reported.

The codelist includes several options that reduce the need for the P7 option:

*  'P1-9 - Point - Other'
*  'P2-10 - Diffuse - Other'
*  'P3-7 - Abstraction - Other'
*  'P4-1-4 - Physical alteration of channel/bed/riparian area/shore - Other'
*  'P4-2-8 - Dams, barriers and locks - Other'
*  'P4-3-6 - Hydrological alteration - Other'
*  'P4-5 - Hydromorphological alteration - Other'

### Number of groundwater bodies by pressure type

See {ref}`PressuresType_NumberOfGWBByPressureType_3rdCycle`.

```{dropdown} Show frequency table
```{include} tables/PressuresType_NumberOfGWBByPressureType_3rdCycle
```

```{dropdown} Show code
```{code-block} sql
:caption: Number of groundwater bodies by pressure type - 3rd cycle
:linenos:
SELECT [gwSignificantPressureTypeGroup]
      ,[gwSignificantPressureType]
      ,count(distinct euGroundWaterBodyCode) numberOfWaterBodies
  FROM [WISE_WFD].[v2r1].[GWB_GroundWaterBody_gwSignificantPressureType] 
  WHERE [cYear] = 2022 AND [hasDescriptiveData] = 1
  AND [gwSignificantPressureType] != 'None'
  GROUP BY [gwSignificantPressureTypeGroup]
      ,[gwSignificantPressureType]
  ORDER BY [gwSignificantPressureTypeGroup]
      ,[gwSignificantPressureType]
```

### Groundwater bodies with 'P7 - Anthropogenic pressure - Other'

Can the option 'P7 - Anthropogenic pressure - Other' be removed from the list of pressures?

* Only 5 groundwater bodies list 'P7 - Anthropogenic pressure - Other' 
  as the single [gwSignificantPressureType] pressure,
  and those 5 waterbodies are in good chemical and quantitative status.

* *Proposal*:
  The option P7 can be safely removed. 
  The [gwSignificantPressureOther] attribute can also be removed.  
  Textual descriptions of other pressures can remain the the RBMP documents.

```{dropdown} Show code
```{code-block} sql
:caption: Groundwater bodies where 'P7 - Anthropogenic pressure - Other' is the single [gwSignificantPressureType] pressure - 3rd cycle
:linenos:
SELECT [gwSignificantPressureOther], count(DISTINCT [euGroundWaterBodyCode]) numberOfWaterBodies
FROM (
    SELECT a.* , c.numberOfPressures
    FROM (
        SELECT [cYear]
              ,[countryCode]
              ,[euRBDCode]
              ,[euGroundWaterBodyCode]
              ,[gwSignificantPressureOther]
              ,[gwQuantitativeStatusValue]
              ,[gwChemicalStatusValue]
              ,[gwSignificantPressureType]
              ,[gwSignificantPressureTypeGroup]
        FROM [WISE_WFD].[v2r1].[GWB_GroundWaterBody_gwSignificantPressureType] 
        WHERE [cYear] = 2022 AND [hasDescriptiveData] = 1
        AND [gwSignificantPressureType] != 'None'
    ) a
    JOIN (
        SELECT euGroundWaterBodyCode 
        FROM (
            SELECT [cYear]
                  ,[countryCode]
                  ,[euRBDCode]
                  ,[euGroundWaterBodyCode]
                  ,[gwSignificantPressureOther]
                  ,[gwQuantitativeStatusValue]
                  ,[gwChemicalStatusValue]
                  ,[gwSignificantPressureType]
                  ,[gwSignificantPressureTypeGroup]
            FROM [WISE_WFD].[v2r1].[GWB_GroundWaterBody_gwSignificantPressureType] 
            WHERE [cYear] = 2022 AND [hasDescriptiveData] = 1
            AND [gwSignificantPressureType] != 'None'
        ) vRelevantData
        WHERE [gwSignificantPressureType] = 'P7 - Anthropogenic pressure - Other'
    ) b ON a.euGroundWaterBodyCode = b.euGroundWaterBodyCode
    JOIN (
        SELECT euGroundWaterBodyCode, count(*) AS numberOfPressures  
        FROM (
            SELECT [cYear]
                  ,[countryCode]
                  ,[euRBDCode]
                  ,[euGroundWaterBodyCode]
                  ,[gwSignificantPressureOther]
                  ,[gwQuantitativeStatusValue]
                  ,[gwChemicalStatusValue]
                  ,[gwSignificantPressureType]
                  ,[gwSignificantPressureTypeGroup]
            FROM [WISE_WFD].[v2r1].[GWB_GroundWaterBody_gwSignificantPressureType] 
            WHERE [cYear] = 2022 AND [hasDescriptiveData] = 1
            AND [gwSignificantPressureType] != 'None'
        ) vRelevantData
        GROUP BY euGroundWaterBodyCode
    ) c ON a.euGroundWaterBodyCode = c.euGroundWaterBodyCode
    WHERE c.numberOfPressures = 1
) vOnlyOtherPressure
GROUP BY [gwSignificantPressureOther] WITH ROLLUP
ORDER BY numberOfWaterBodies DESC
```

###  Groundwater bodies with 'P8 - Anthropogenic pressure - Unknown'

If the option 'P7 - Anthropogenic pressure - Other' 
is removed from the list of pressures, 
can the option 'P8 - Anthropogenic pressure - Unknown' also be removed?

* There are 50 groundwater bodies listing 'P8 - Anthropogenic pressure - Unknown' 
  as the single [gwSignificantPressureType] pressure causing failure.

* *Proposal*:  
  Remove the option 'P8 - Anthropogenic pressure - Unknown' 
  from the list of options.  
  A generic 'unknown' option will be available.
  It is mandatory to assess the pressures for water bodies not achieving good status, but Member States may still choose the option 'unknown'
  and effectively report that the pressures were not assessed.  

```{dropdown} Show code
```{code-block} sql
:caption: Groundwater bodies where 'P8 - Anthropogenic pressure - Unknown' is the single remaining [gwSignificantPressureType] pressure - 3rd cycle
:linenos:
SELECT *
FROM (
    SELECT a.* , c.numberOfPressures
    FROM (
        SELECT [cYear]
              ,[countryCode]
              ,[euRBDCode]
              ,[euGroundWaterBodyCode]
              ,[gwSignificantPressureOther]
              ,[gwQuantitativeStatusValue]
              ,[gwChemicalStatusValue]
              ,[gwSignificantPressureType]
              ,[gwSignificantPressureTypeGroup]
        FROM [WISE_WFD].[v2r1].[GWB_GroundWaterBody_gwSignificantPressureType] 
        WHERE [cYear] = 2022 AND [hasDescriptiveData] = 1
        AND [gwSignificantPressureType] NOT IN ('None','P7 - Anthropogenic pressure - Other')
    ) a
    JOIN (
        SELECT euGroundWaterBodyCode 
        FROM (
            SELECT [cYear]
                  ,[countryCode]
                  ,[euRBDCode]
                  ,[euGroundWaterBodyCode]
                  ,[gwSignificantPressureOther]
                  ,[gwQuantitativeStatusValue]
                  ,[gwChemicalStatusValue]
                  ,[gwSignificantPressureType]
                  ,[gwSignificantPressureTypeGroup]
            FROM [WISE_WFD].[v2r1].[GWB_GroundWaterBody_gwSignificantPressureType] 
            WHERE [cYear] = 2022 AND [hasDescriptiveData] = 1
            AND [gwSignificantPressureType] NOT IN ('None','P7 - Anthropogenic pressure - Other')
        ) vRelevantData
        WHERE [gwSignificantPressureType] = 'P8 - Anthropogenic pressure - Unknown'
    ) b ON a.euGroundWaterBodyCode = b.euGroundWaterBodyCode
    JOIN (
        SELECT euGroundWaterBodyCode, count(*) AS numberOfPressures  
        FROM (
            SELECT [cYear]
                  ,[countryCode]
                  ,[euRBDCode]
                  ,[euGroundWaterBodyCode]
                  ,[gwSignificantPressureOther]
                  ,[gwQuantitativeStatusValue]
                  ,[gwChemicalStatusValue]
                  ,[gwSignificantPressureType]
                  ,[gwSignificantPressureTypeGroup]
            FROM [WISE_WFD].[v2r1].[GWB_GroundWaterBody_gwSignificantPressureType] 
            WHERE [cYear] = 2022 AND [hasDescriptiveData] = 1
            AND [gwSignificantPressureType] NOT IN ('None','P7 - Anthropogenic pressure - Other')
        ) vRelevantData
        GROUP BY euGroundWaterBodyCode
    ) c ON a.euGroundWaterBodyCode = c.euGroundWaterBodyCode
    WHERE c.numberOfPressures = 1
) vOnlyUnknownPressure
WHERE NOT (gwChemicalStatusValue = '2' AND gwQuantitativeStatusValue = '2')
```

### Groundwater bodies with 'P9 - Anthropogenic pressure - Historical pollution'

If the option 'P7 - Anthropogenic pressure - Other' 
and the option 'P8 - Anthropogenic pressure - Unknown' 
are removed from the list of pressures, 
can the option 'P9 - Anthropogenic pressure - Historical pollution' also be removed?

* There are 102 GWB (out of 5605 not achieving good status) 
  that list 'P9 - Anthropogenic pressure - Historical pollution'
  as the single [gwSignificantPressureType] pressure causing failure.
  It is important to note that 75 of those 102 GWB are in Denmark.

* *Proposal*:  
  Remove the option 'P9 - Anthropogenic pressure - Historical pollution'
  from the list of [gwSignificantPressureType] options,
  because it is seldom used and not very informative.

* Inform Member States, specially those that used the P9 option 
  in the 3rd cycle electronic reporting.

```{dropdown} Show code
```{code-block} sql
:caption: Groundwater bodies where 'P9 - Anthropogenic pressure - Historical pollution' is the single remaining [gwSignificantPressureType] pressure - 3rd cycle
:linenos:
SELECT countryCode, count(*) n
FROM (
    SELECT a.* , c.numberOfPressures
    FROM (
        SELECT [cYear]
              ,[countryCode]
              ,[euRBDCode]
              ,[euGroundWaterBodyCode]
              ,[gwSignificantPressureOther]
              ,[gwQuantitativeStatusValue]
              ,[gwChemicalStatusValue]
              ,[gwSignificantPressureType]
              ,[gwSignificantPressureTypeGroup]
        FROM [WISE_WFD].[latest].[GWB_GroundWaterBody_gwSignificantPressureType] 
        WHERE [cYear] = 2022 AND [hasDescriptiveData] = 1
        AND [gwSignificantPressureType] 
          NOT IN ('None',
                'P7 - Anthropogenic pressure - Other',
                'P8 - Anthropogenic pressure - Unknown')
    ) a
    JOIN (
        SELECT euGroundWaterBodyCode 
        FROM (
            SELECT [cYear]
                  ,[countryCode]
                  ,[euRBDCode]
                  ,[euGroundWaterBodyCode]
                  ,[gwSignificantPressureOther]
                  ,[gwQuantitativeStatusValue]
                  ,[gwChemicalStatusValue]
                  ,[gwSignificantPressureType]
                  ,[gwSignificantPressureTypeGroup]
            FROM [WISE_WFD].[latest].[GWB_GroundWaterBody_gwSignificantPressureType] 
            WHERE [cYear] = 2022 AND [hasDescriptiveData] = 1
            AND [gwSignificantPressureType] 
              NOT IN ('None',
                    'P7 - Anthropogenic pressure - Other',
                    'P8 - Anthropogenic pressure - Unknown')
        ) vRelevantData
        WHERE [gwSignificantPressureType] = 'P9 - Anthropogenic pressure - Historical pollution'
    ) b ON a.euGroundWaterBodyCode = b.euGroundWaterBodyCode
    JOIN (
        SELECT euGroundWaterBodyCode, count(*) AS numberOfPressures  
        FROM (
            SELECT [cYear]
                  ,[countryCode]
                  ,[euRBDCode]
                  ,[euGroundWaterBodyCode]
                  ,[gwSignificantPressureOther]
                  ,[gwQuantitativeStatusValue]
                  ,[gwChemicalStatusValue]
                  ,[gwSignificantPressureType]
                  ,[gwSignificantPressureTypeGroup]
            FROM [WISE_WFD].[latest].[GWB_GroundWaterBody_gwSignificantPressureType] 
            WHERE [cYear] = 2022 AND [hasDescriptiveData] = 1
            AND [gwSignificantPressureType] 
              NOT IN ('None',
                    'P7 - Anthropogenic pressure - Other',
                    'P8 - Anthropogenic pressure - Unknown')
        ) vRelevantData
        GROUP BY euGroundWaterBodyCode
    ) c ON a.euGroundWaterBodyCode = c.euGroundWaterBodyCode
    WHERE c.numberOfPressures = 1
) vOnlyHistoricalPressure
WHERE NOT (gwChemicalStatusValue = '2' AND gwQuantitativeStatusValue = '2')
GROUP BY countryCode
ORDER BY countryCode
```

### Number of surface bodies by pressure type

See {ref}`PressuresType_NumberOfSWBByPressureType_3rdCycle`.

```{dropdown} Show frequency table
```{include} tables/PressuresType_NumberOfSWBByPressureType_3rdCycle
```

```{dropdown} Show code
```{code-block} sql
:caption: Number of surface bodies by pressure type - 3rd cycle
:linenos:
SELECT [swSignificantPressureTypeGroup]
      ,[swSignificantPressureType]
      ,count(distinct [euSurfaceWaterBodyCode] ) numberOfWaterBodies
  FROM [WISE_WFD].[latest].[SWB_SurfaceWaterBody_swSignificantPressureType] 
  WHERE [cYear] = 2022 AND [hasDescriptiveData] = 1
  AND [swSignificantPressureType] != 'None'
  GROUP BY [swSignificantPressureTypeGroup]
      ,[swSignificantPressureType]
  ORDER BY [swSignificantPressureTypeGroup]
      ,[swSignificantPressureType]
```

### Surface water bodies with 'P7 - Anthropogenic pressure - Other'

Can the option 'P7 - Anthropogenic pressure - Other' be removed from the list of pressures?

* Only 237 surface water bodies list 'P7 - Anthropogenic pressure - Other' 
  as the single [swSignificantPressureType] pressure,
  of which 235 fail to achieve good status.
  A total of 137 of these water bodies report 
  "gold mining activity (legal and illegal)" 
  as the 'other' pressure - 
  but there is pressure code for this situation
  (i.e. there is not need for a textual description).

* *Proposal*:
  Remove the option 'P7 - Anthropogenic pressure - Other' 
  from the list of [swSignificantPressureType] options.  
  Remove the [swSignificantPressureOther] column.  
  Inform Member States, specially those that used the P7 option 
  in the 3rd cycle electronic reporting.

```{dropdown} Show code
```{code-block} sql
:caption: Surface water bodies where 'P7 - Anthropogenic pressure - Other' is the single [gwSignificantPressureType] pressure - 3rd cycle
:linenos:
SELECT swSignificantPressureOther, count(DISTINCT [euSurfaceWaterBodyCode]) numberOfWaterBodies
FROM (
    SELECT a.* , c.numberOfPressures, d.swSignificantPressureOther
    FROM (
        SELECT [cYear]
              ,[countryCode]
              ,[euRBDCode]
              ,[euSurfaceWaterBodyCode]
              ,[swEcologicalStatusOrPotentialValue]
              ,[swChemicalStatusValue]
              ,[swSignificantPressureType]
              ,[swSignificantPressureTypeGroup]
        FROM [WISE_WFD].[latest].[SWB_SurfaceWaterBody_swSignificantPressureType] 
        WHERE [cYear] = 2022 AND [hasDescriptiveData] = 1
        AND [swSignificantPressureType] != 'None'
    ) a
    JOIN (
        SELECT [euSurfaceWaterBodyCode] 
        FROM (
            SELECT [cYear]
                  ,[countryCode]
                  ,[euRBDCode]
                  ,[euSurfaceWaterBodyCode]
                  ,[swEcologicalStatusOrPotentialValue]
                  ,[swChemicalStatusValue]
                  ,[swSignificantPressureType]
                  ,[swSignificantPressureTypeGroup]
            FROM [WISE_WFD].[latest].[SWB_SurfaceWaterBody_swSignificantPressureType] 
            WHERE [cYear] = 2022 AND [hasDescriptiveData] = 1
            AND [swSignificantPressureType] != 'None'
        ) vRelevantData
        WHERE [swSignificantPressureType] = 'P7 - Anthropogenic pressure - Other'
    ) b ON a.[euSurfaceWaterBodyCode] = b.[euSurfaceWaterBodyCode]
    JOIN (
        SELECT [euSurfaceWaterBodyCode], count(*) AS numberOfPressures  
        FROM (
            SELECT [cYear]
                  ,[countryCode]
                  ,[euRBDCode]
                  ,[euSurfaceWaterBodyCode]
                  ,[swEcologicalStatusOrPotentialValue]
                  ,[swChemicalStatusValue]
                  ,[swSignificantPressureType]
                  ,[swSignificantPressureTypeGroup]
            FROM [WISE_WFD].[latest].[SWB_SurfaceWaterBody_swSignificantPressureType] 
            WHERE [cYear] = 2022 AND [hasDescriptiveData] = 1
            AND [swSignificantPressureType] != 'None'
        ) vRelevantData
        GROUP BY [euSurfaceWaterBodyCode]
    ) c ON a.[euSurfaceWaterBodyCode] = c.[euSurfaceWaterBodyCode]
    JOIN [WISE_WFD].[latest].[SWB_SurfaceWaterBody_swSignificantPressureOther] d
    ON a.[euSurfaceWaterBodyCode] = d.[euSurfaceWaterBodyCode]
        AND d.[cYear] = 2022
    WHERE c.numberOfPressures = 1
) vOnlyOtherPressure
WHERE NOT (swEcologicalStatusOrPotentialValue IN ('1','2') AND swChemicalStatusValue IN ('2'))
GROUP BY swSignificantPressureOther WITH ROLLUP
ORDER BY numberOfWaterBodies DESC
```

### Surface water bodies with 'P8 - Anthropogenic pressure - Unknown'

If the option 'P7 - Anthropogenic pressure - Other' is removed from the list of  pressures, can the option 'P8 - Anthropogenic pressure - Unknown' also be removed?

* There are 7 surface water bodies listing 'P8 - Anthropogenic pressure - Unknown' 
  as the single [swSignificantPressureType] pressure causing failure.

* *Proposal*:  
  Remove the option 'P8 - Anthropogenic pressure - Unknown' 
  from the list of [swSignificantPressureType] options.  
  Inform Member States, specially those that used the P8 option in the 3rd cycle electronic reporting.  
  A generic 'unknown' option will be available.
  It is mandatory to assess the pressures for water bodies not achieving good status, but Member States may still choose the option 'unknown'
  and effectively report that the pressures were not assessed.  

```{dropdown} Show code
```{code-block} sql
:caption: Surface water bodies where 'P8 - Anthropogenic pressure - Unknown' is the single remaining [gwSignificantPressureType] pressure - 3rd cycle
:linenos:
SELECT *
FROM (
    SELECT a.* , c.numberOfPressures, d.swSignificantPressureOther
    FROM (
        SELECT [cYear]
              ,[countryCode]
              ,[euRBDCode]
              ,[euSurfaceWaterBodyCode]
              ,[swEcologicalStatusOrPotentialValue]
              ,[swChemicalStatusValue]
              ,[swSignificantPressureType]
              ,[swSignificantPressureTypeGroup]
        FROM [WISE_WFD].[latest].[SWB_SurfaceWaterBody_swSignificantPressureType] 
        WHERE [cYear] = 2022 AND [hasDescriptiveData] = 1
        AND [swSignificantPressureType] NOT IN ('None','P7 - Anthropogenic pressure - Other')
    ) a
    JOIN (
        SELECT [euSurfaceWaterBodyCode] 
        FROM (
            SELECT [cYear]
                  ,[countryCode]
                  ,[euRBDCode]
                  ,[euSurfaceWaterBodyCode]
                  ,[swEcologicalStatusOrPotentialValue]
                  ,[swChemicalStatusValue]
                  ,[swSignificantPressureType]
                  ,[swSignificantPressureTypeGroup]
            FROM [WISE_WFD].[latest].[SWB_SurfaceWaterBody_swSignificantPressureType] 
            WHERE [cYear] = 2022 AND [hasDescriptiveData] = 1
            AND [swSignificantPressureType] NOT IN ('None','P7 - Anthropogenic pressure - Other')
        ) vRelevantData
        WHERE [swSignificantPressureType] = 'P8 - Anthropogenic pressure - Unknown'
    ) b ON a.[euSurfaceWaterBodyCode] = b.[euSurfaceWaterBodyCode]
    JOIN (
        SELECT [euSurfaceWaterBodyCode], count(*) AS numberOfPressures  
        FROM (
            SELECT [cYear]
                  ,[countryCode]
                  ,[euRBDCode]
                  ,[euSurfaceWaterBodyCode]
                  ,[swEcologicalStatusOrPotentialValue]
                  ,[swChemicalStatusValue]
                  ,[swSignificantPressureType]
                  ,[swSignificantPressureTypeGroup]
            FROM [WISE_WFD].[latest].[SWB_SurfaceWaterBody_swSignificantPressureType] 
            WHERE [cYear] = 2022 AND [hasDescriptiveData] = 1
            AND [swSignificantPressureType] NOT IN ('None','P7 - Anthropogenic pressure - Other')
        ) vRelevantData
        GROUP BY [euSurfaceWaterBodyCode]
    ) c ON a.[euSurfaceWaterBodyCode] = c.[euSurfaceWaterBodyCode]
    JOIN [WISE_WFD].[latest].[SWB_SurfaceWaterBody_swSignificantPressureOther] d
    ON a.[euSurfaceWaterBodyCode] = d.[euSurfaceWaterBodyCode]
        AND d.[cYear] = 2022
    WHERE c.numberOfPressures = 1
) vOnlyUnknownPressure
WHERE NOT (swEcologicalStatusOrPotentialValue IN ('1','2') AND swChemicalStatusValue IN ('2'))
```

### Surface water bodies with 'P9 - Anthropogenic pressure - Historical pollution'

If the option 'P7 - Anthropogenic pressure - Other' 
and the option 'P8 - Anthropogenic pressure - Unknown' 
are removed from the list of pressures, 
can the option 'P9 - Anthropogenic pressure - Historical pollution' also be removed?

* There are zero water bodies listing this pressure as the single pressure.

* *Proposal*:  
  Remove the option 'P9 - Anthropogenic pressure - Historical pollution'
  from the list of [swSignificantPressureType] options,
  because it is seldom used and not very informative.

```{dropdown} Show code
```{code-block} sql
:caption: Surface water bodies where 'P9 - Anthropogenic pressure - Historical pollution' is the single remaining [gwSignificantPressureType] pressure - 3rd cycle
:linenos:
SELECT *
FROM (
    SELECT a.* , c.numberOfPressures, d.swSignificantPressureOther
    FROM (
        SELECT [cYear]
              ,[countryCode]
              ,[euRBDCode]
              ,[euSurfaceWaterBodyCode]
              ,[swEcologicalStatusOrPotentialValue]
              ,[swChemicalStatusValue]
              ,[swSignificantPressureType]
              ,[swSignificantPressureTypeGroup]
        FROM [WISE_WFD].[latest].[SWB_SurfaceWaterBody_swSignificantPressureType] 
        WHERE [cYear] = 2022 AND [hasDescriptiveData] = 1
        AND [swSignificantPressureType] 
          NOT IN ('None',
                  'P7 - Anthropogenic pressure - Other',
                  'P8 - Anthropogenic pressure - Unknown')
    ) a
    JOIN (
        SELECT [euSurfaceWaterBodyCode] 
        FROM (
            SELECT [cYear]
                  ,[countryCode]
                  ,[euRBDCode]
                  ,[euSurfaceWaterBodyCode]
                  ,[swEcologicalStatusOrPotentialValue]
                  ,[swChemicalStatusValue]
                  ,[swSignificantPressureType]
                  ,[swSignificantPressureTypeGroup]
            FROM [WISE_WFD].[latest].[SWB_SurfaceWaterBody_swSignificantPressureType] 
            WHERE [cYear] = 2022 AND [hasDescriptiveData] = 1
            AND [swSignificantPressureType] 
              NOT IN ('None',
                      'P7 - Anthropogenic pressure - Other',
                      'P8 - Anthropogenic pressure - Unknown')
        ) vRelevantData
        WHERE [swSignificantPressureType] = 'P9 - Anthropogenic pressure - Historical pollution'
    ) b ON a.[euSurfaceWaterBodyCode] = b.[euSurfaceWaterBodyCode]
    JOIN (
        SELECT [euSurfaceWaterBodyCode], count(*) AS numberOfPressures  
        FROM (
            SELECT [cYear]
                  ,[countryCode]
                  ,[euRBDCode]
                  ,[euSurfaceWaterBodyCode]
                  ,[swEcologicalStatusOrPotentialValue]
                  ,[swChemicalStatusValue]
                  ,[swSignificantPressureType]
                  ,[swSignificantPressureTypeGroup]
            FROM [WISE_WFD].[latest].[SWB_SurfaceWaterBody_swSignificantPressureType] 
            WHERE [cYear] = 2022 AND [hasDescriptiveData] = 1
            AND [swSignificantPressureType] 
              NOT IN ('None',
                      'P7 - Anthropogenic pressure - Other',
                      'P8 - Anthropogenic pressure - Unknown')
        ) vRelevantData
        GROUP BY [euSurfaceWaterBodyCode]
    ) c ON a.[euSurfaceWaterBodyCode] = c.[euSurfaceWaterBodyCode]
    JOIN [WISE_WFD].[latest].[SWB_SurfaceWaterBody_swSignificantPressureOther] d
    ON a.[euSurfaceWaterBodyCode] = d.[euSurfaceWaterBodyCode]
        AND d.[cYear] = 2022
    WHERE c.numberOfPressures = 1
) vOnlyHistoricalPressure
WHERE NOT (swEcologicalStatusOrPotentialValue IN ('1','2') AND swChemicalStatusValue IN ('2'))
```


### Surface water bodies with 'P8 - Anthropogenic pressure - Unknown' and unknown chemical status

This specific situation was detected during the Assessment of the 3rd RBMPs:

```{epigraph}
A Member State flagged that where a water body is reported to be in unknown chemical status, a pressure must also be reported on that water body. This resulted in the Member State reporting 60% of surface water bodies to be affected by unknown anthropogenic pressures. The Member State representative said that in reality, the percentage of waterbodies with an unknown pressure was approximately 10%. I.e. this resulted in a large difference between the data reported electronically, and the actual situation in the Member State.
```

```{todo} 
Significant pressures - Provide link to report 

ASSESSMENT OF THE THIRD RIVER BASIN MANAGEMENT PLANS (RBMPS) - APPENDIX - LESSONS LEARNT - ELECTRONIC REPORTING

```

This was indeed an issue.
The situation described is likely cause by the fact that there is no option 'Unknown' in the 3rd cycle codelist.
In fact, the reporting guidance says that 'P8 - Anthropogenic pressure - Unknown' is only relevant where status is lower than good and pressure is unknown.

For the future, the codelist should include the option 'unknown', to be used in this scope.
(Also the option can be used if status is unknown.)

```{dropdown} Show code
```{code-block} sql
:caption: Surface water bodies with unknown chemical status, non-failing ecological status and 'P8 - Anthropogenic pressure - Unknown' - 3rd cycle
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
:caption: Groundwater bodies with unknown chemical status, non-failing quantitative status and 'P8 - Anthropogenic pressure - Unknown' - 3rd cycle
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
:caption: Groundwater bodies where the single pressure causing failure is 'P6-1 - Groundwater - Recharges' - 3rd cycle
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
:caption: Surface bodies where the single pressure causing failure is 'P6-1 - Groundwater - Recharges' - 3rd cycle
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