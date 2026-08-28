##### Field QCs

###### gwChemicalMonitoringReference
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V401
  - BLOCKER
  - The value is not a valid member of the referenced list. [V401]
* - RF402\_WFD
  - BLOCKER
  - gwChemicalMonitoringReference Must be reported for every RBD with designated groundwater bodies. [RF402\_WFD]
* - RF402\_WISE5
  - BLOCKER
  - gwChemicalMonitoringReference Must be reported for every RBD with designated groundwater bodies. [RF402\_WISE5]
```

###### gwQuantitativeMonitoringReference
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V402
  - BLOCKER
  - The value is not a valid member of the referenced list. [V402]
* - RF403\_WFD
  - BLOCKER
  - gwQuantitativeMonitoringReference Must be reported for every RBD with designated groundwater bodies. [RF403\_WFD]
* - RF403\_WISE5
  - BLOCKER
  - gwQuantitativeMonitoringReference Must be reported for every RBD with designated groundwater bodies. [RF403\_WISE5]
```

###### swChemicalMonitoringReference
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V403
  - BLOCKER
  - The value is not a valid member of the referenced list. [V403]
* - RF404\_WFD
  - BLOCKER
  - swChemicalMonitoringReference Must be reported for every RBD with designated surface water bodies. [RF404\_WFD]
* - RF404\_WISE5
  - BLOCKER
  - swChemicalMonitoringReference Must be reported for every RBD with designated surface water bodies. [RF404\_WISE5]
```

###### swEcologicalMonitoringReference
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V404
  - BLOCKER
  - The value is not a valid member of the referenced list. [V404]
* - RF405\_WFD
  - BLOCKER
  - swEcologicalMonitoringReference Must be reported for every RBD with designated surface water bodies that are not territorial waters.[RF405\_WFD]
* - RF405\_WISE5
  - BLOCKER
  - swEcologicalMonitoringReference Must be reported for every RBD with designated surface water bodies that are not territorial waters. [RF405\_WISE5]
```

###### programmesReference
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V405
  - BLOCKER
  - The value must not be missing or empty [V405]
* - V406
  - BLOCKER
  - The value is not a valid member of the referenced list. [V406]
```

###### investigativeMonitoringReference
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V407
  - BLOCKER
  - The value must not be missing or empty [V407]
* - V408
  - BLOCKER
  - The value is not a valid member of the referenced list. [V408]
```

###### surveillanceMonitoringReference
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V409
  - BLOCKER
  - The value must not be missing or empty [V409]
* - V410
  - BLOCKER
  - The value is not a valid member of the referenced list. [V410]
```

###### operationalMonitoringReference
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V411
  - BLOCKER
  - The value must not be missing or empty [V411]
* - V412
  - BLOCKER
  - The value is not a valid member of the referenced list. [V412]
```

###### euRBDCode
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - RF401\_WFD
  - BLOCKER
  - The euRBDCode must match a RiverBasinDistrict in the reference where wiseevolutiontype != 'deletion' [RF401\_WFD]
* - V431
  - BLOCKER
  - The value must not be missing or empty [V431]
* - T405\_WFD
  - BLOCKER
  - If, for a given river basin district, the option useWaterbaseForMonitoringData = 'yes' is reported in the MonitoringProgrammes table, then the monitoring of physico-chemical and chemical parameters must NOT be reported in the Monitoring table. [T405\_WFD]
* - XC411\_WFD
  - BLOCKER
  - If, for a given RBD, useWaterbaseForMonitoringData = 'no' and there are monitoring sites in Surface Water Bodies, then at least one site MUST report a parameterCode NOT LIKE 'QE%'. [XC411\_WFD]
* - XC412\_WFD
  - BLOCKER
  - If, for a given RBD where useWaterbaseForMonitoringData = 'no', if there are monitoring sites associated with Groundwater Bodies, at least one of them MUST report a parameterCode != 'EEA\_00-01-1'. [XC412\_WFD]
* - RF401\_WISE5
  - BLOCKER
  - The euRBDCode must match a RiverBasinDistrict in the reference where wiseevolutiontype != 'deletion' [RF401\_WISE5]
* - XC411\_WISE5
  - BLOCKER
  - If, for a given RBD, useWaterbaseForMonitoringData = 'no' and there are monitoring sites in Surface Water Bodies, then at least one site MUST report a parameterCode NOT LIKE 'QE%'. [XC411\_WISE5]
* - XC412\_WISE5
  - BLOCKER
  - If, for a given RBD where useWaterbaseForMonitoringData = 'no', if there are monitoring sites associated with Groundwater Bodies, at least one of them MUST report a parameterCode != 'EEA\_00-01-1'. [XC412\_WISE5]
* - T405\_WISE5
  - BLOCKER
  - If, for a given river basin district, the option useWaterbaseForMonitoringData = 'yes' is reported in the MonitoringProgrammes table, then the monitoring of physico-chemical and chemical parameters must NOT be reported in the Monitoring table. [T405\_WISE5]
```

###### useWaterbaseForMonitoringData
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V432
  - BLOCKER
  - The value must not be missing or empty [V432]
* - V424
  - BLOCKER
  - The value is not a valid member of the referenced list. [V424]
```
