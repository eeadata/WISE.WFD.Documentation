##### Field QCs

###### lastMonitored

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V415
  - BLOCKER
  - The value is not a valid whole number [V415]
* - V421
  - BLOCKER
  - The value must not be missing or empty [V421]
* - V426
  - BLOCKER
  - The value must follow the YYYY format. [V426]
* - V430
  - BLOCKER
  - lastMonitored must be a year <= 2027 or 9999 (only when the parameter has never been monitored before but will be monitored during the 4th cycle). Any other value is invalid.[V430]
* - R406
  - BLOCKER
  - Unknown option in cycle is valid if and only if: lastMonitored = 9999 [R406]
* - R405
  - BLOCKER
  - Unknown option in frequency is valid if and only if:lastMonitored = 9999 or monitoringCycle = 'once' [R405]
* - R405
  - BLOCKER
  - Unknown option in frequency is valid if and only if:lastMonitored = 9999 or monitoringCycle = 'once' [R405]
```

###### euMonitoringSiteCode

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V416
  - BLOCKER
  - The value must not be missing or empty [V416]
* - RF406\_WFD
  - BLOCKER
  - The value euMonitoringSiteCode must exist in reference dataset with wiseevolutiontype != 'deletion' [RF406\_WFD]
* - XC401
  - BLOCKER
  - The value euMonitoringSiteCode must exist in Spatial dataset with wiseevolutiontype != 'deletion' [XC401]
* - RF406\_WISE5
  - BLOCKER
  - The value euMonitoringSiteCode must exist in reference dataset with wiseevolutiontype != 'deletion' [RF406\_WISE5]
```

###### parameterCode

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V417
  - BLOCKER
  - The value must not be missing or empty [V417]
* - V418
  - BLOCKER
  - The value is not a valid member of the referenced list. [V418]
* - R403\_WFD
  - BLOCKER
  - Seven physico-chemical parameters applicable to surface water are NOT valid in groundwater monitoring sites. List includes: EEA\_3133-07-1 (Oxidisability), EEA\_3133-02-6 (BOD7), EEA\_3111-01-1 (Secchi depth), EEA\_3161-04-4 (Particulate organic nitrogen), EEA\_3164-08-7 (Nitrate to orthophosphate ratio), EEA\_3164-07-6 (Total N to total P ratio), EEA\_3164-01-0 (Chlorophyll a). [R403\_WFD]
* - R404\_WFD
  - BLOCKER
  - The option parameterCode LIKE 'EEA\_00-01-1%' (Quantitative monitoring) is only valid for monitoring sites in groundwater bodies. [R404\_WFD]
* - XC404\_WFD
  - BLOCKER
  - parameterCode LIKE 'QE1-%' (Biological quality elements) is only valid in rivers, lakes, transitional and coastal water bodies. [XC404\_WFD]
* - XC405\_WFD
  - BLOCKER
  - parameterCode LIKE 'QE2-%' (Hydromorphological quality elements) is only valid in rivers, lakes, transitional and coastal water bodies. [XC405\_WFD]
* - XC402\_WFD
  - BLOCKER
  - For sites in surface water bodies, chemical monitoring includes priority substances and river basin specific pollutants. [XC402\_WFD]
* - XC403\_WFD
  - BLOCKER
  - For sites in groundwater bodies, chemical monitoring includes priority substances, the pollutants designated as “river basin specific pollutants” (for surface waters), and any other chemical substances where parameterCode LIKE 'CAS%' [XC403\_WFD]
* - R403\_WISE5
  - BLOCKER
  - Seven physico-chemical parameters applicable to surface water are NOT valid in groundwater monitoring sites. List includes: EEA\_3133-07-1 (Oxidisability), EEA\_3133-02-6 (BOD7), EEA\_3111-01-1 (Secchi depth), EEA\_3161-04-4 (Particulate organic nitrogen), EEA\_3164-08-7 (Nitrate to orthophosphate ratio), EEA\_3164-07-6 (Total N to total P ratio), EEA\_3164-01-0 (Chlorophyll a). [R403\_WISE5]
* - R404\_WISE5
  - BLOCKER
  - The option parameterCode LIKE 'EEA\_00-01-1%' (Quantitative monitoring) is only valid for monitoring sites in groundwater bodies. [R404\_WISE5]
* - XC404\_WISE5
  - BLOCKER
  - parameterCode LIKE 'QE1-%' (Biological quality elements) is only valid in rivers, lakes, transitional and coastal water bodies. [XC404\_WISE5]
* - XC405\_WISE5
  - BLOCKER
  - parameterCode LIKE 'QE2-%' (Hydromorphological quality elements) is only valid in rivers, lakes, transitional and coastal water bodies. [XC405\_WISE5]
* - XC413\_WISE5
  - BLOCKER
  - If a monitoring site is associated with a territorialwater, it must NOT report any parameter codes matching -- 'QE1%' or 'QE2%'. [XC413\_WISE5]
```

###### frequency

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V419
  - BLOCKER
  - The value must not be missing or empty [V419]
* - V420
  - BLOCKER
  - The value is not a valid member of the referenced list. [V420]
```

###### cycle

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V422
  - BLOCKER
  - The value must not be missing or empty [V422]
* - V423
  - BLOCKER
  - The value is not a valid member of the referenced list. [V423]
```

###### chemicalMatrix

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - R400\_WFD
  - BLOCKER
  - The chemicalMatrix value must be reported if and only if chemical monitoring occurs. [R400\_WFD]
* - R402\_WFD
  - BLOCKER
  - For groundwater sites with chemical monitoring, the only valid value for chemicalMatrix is 'water'. [R402\_WFD]
* - V413
  - BLOCKER
  - The value is not a valid member of the referenced list. [V413]
* - V433
  - BLOCKER
  - chemicalMatrix contains duplicate values [V433]
* - R400\_WISE5
  - BLOCKER
  - The chemicalMatrix value must be reported if and only if chemical monitoring occurs. [R400\_WISE5]
* - XC402\_WISE5
  - BLOCKER
  - For sites in surface water bodies, chemical monitoring includes priority substances and river basin specific pollutants. [XC402\_WISE5]
* - XC403\_WISE5
  - BLOCKER
  - For sites in groundwater bodies, chemical monitoring includes priority substances, the pollutants designated as “river basin specific pollutants” (for surface waters), and any other chemical substances where parameterCode LIKE 'CAS%' [XC403\_WISE5]
* - R402\_WISE5
  - BLOCKER
  - For groundwater sites with chemical monitoring, the only valid value for chemicalMatrix is 'water'. [R402\_WISE5]
```

###### chemicalPurpose

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - R401\_WFD
  - BLOCKER
  - The chemicalPurpose value must be reported if and only if chemical monitoring occurs. [R401\_WFD]
* - V414
  - BLOCKER
  - The value is not a valid member of the referenced list. [V414]
* - V434
  - BLOCKER
  - chemicalPurpose contains duplicate values [V434]
* - R401\_WISE5
  - BLOCKER
  - The chemicalPurpose value must be reported if and only if chemical monitoring occurs. [R401\_WISE5]
```

###### monitoringCycle

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - XC413\_WFD
  - BLOCKER
  - If a monitoring site is associated with a territorialwater, it must NOT report any parameter codes matching -- 'QE1%' or 'QE2%'. [XC413\_WFD]
```
