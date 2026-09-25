##### Field QCs

###### euMonitoringSiteCode
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V425
  - BLOCKER
  - The value must not be missing or empty [V425]
* - XC410\_WISE5
  - BLOCKER
  - euMonitoringSiteCode must exist in the Spatial dataset if includesSpatialData = 'yes' with wisevolutiontype != 'deletion' and includesMonitoringData = 'yes' [XC410\_WISE5]
* - RF409\_WISE5
  - BLOCKER
  - euMonitoringSiteCode must exist in the Spatial Reference if includesSpatialData = 'no' with wisevolutiontype != 'deletion' [RF409\_WISE5]
```

###### monitoringPurpose
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V427
  - BLOCKER
  - The value must not be missing or empty [V427]
* - V428
  - BLOCKER
  - The value is not a valid member of the referenced list. [V428]
* - V429
  - BLOCKER
  - monitoringPurpose contains duplicate values [V429]
```

###### includesMonitoringData
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - XC410\_WFD
  - BLOCKER
  - euMonitoringSiteCode must exist in the Spatial dataset if includesSpatialData = 'yes' with wisevolutiontype != 'deletion' and includesMonitoringData = 'yes' [XC410]
```

###### wisevolutiontype
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - XC410\_WFD
  - BLOCKER
  - euMonitoringSiteCode must exist in the Spatial dataset if includesSpatialData = 'yes' with wisevolutiontype != 'deletion' and includesMonitoringData = 'yes' [XC410]
* - RF409\_WFD
  - BLOCKER
  - euMonitoringSiteCode must exist in the Spatial Reference if includesSpatialData = 'no' with wisevolutiontype != 'deletion' [RF409\_WFD]
```

###### includesSpatialData
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - XC410\_WFD
  - BLOCKER
  - euMonitoringSiteCode must exist in the Spatial dataset if includesSpatialData = 'yes' with wisevolutiontype != 'deletion' and includesMonitoringData = 'yes' [XC410]
* - RF409\_WFD
  - BLOCKER
  - euMonitoringSiteCode must exist in the Spatial Reference if includesSpatialData = 'no' with wisevolutiontype != 'deletion' [RF409\_WFD]
```
