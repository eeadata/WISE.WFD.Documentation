##### Field QCs

###### title

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V019
  - BLOCKER
  - The value must not be missing or empty. [V019]
* - V020
  - BLOCKER
  - The length of the value must be <= 4000. [V020]
```

###### creatorOrganisationName

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V005
  - BLOCKER
  - The value must not be missing or empty. [V005]
* - V004
  - BLOCKER
  - The length of the value must be <= 4000. [V004]
```

###### licenseDocument

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V013
  - BLOCKER
  - The value is not a valid member of the referenced list. [V013]
* - V014
  - BLOCKER
  - "licenseDocument" contains duplicate values. [V014]
* - R001
  - BLOCKER
  - licenseDocument must be reported if license is 'exactMatch\_CC\_BY\_4\_0' or 'narrowMatch\_CC\_BY\_4\_0'. [R001]
```

###### metadataDocument

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V015
  - BLOCKER
  - The value is not a valid member of the referenced list. [V015]
* - V016
  - BLOCKER
  - "metadataDocument" contains duplicate values. [V016]
```

###### creatorElectronicMailAddress

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V002
  - BLOCKER
  - The value must not be missing or empty. [V002]
* - V003
  - BLOCKER
  - The value does not follow the expected syntax for a valid email. [V003]
* - V021
  - BLOCKER
  - The length of the value must be <= 4000 [V021]
```

###### description

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V006
  - BLOCKER
  - The length of the value must be <= 4000. [V006]
```

###### language

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V009
  - BLOCKER
  - "language" contains duplicate values. [V009]
* - V029
  - BLOCKER
  - The value must not be missing or empty [V029]
* - V008
  - BLOCKER
  - The value is not a valid member of the referenced list. [V008]
```

###### rights

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V017
  - BLOCKER
  - The length of the value must be <= 4000. [V017]
```

###### rightsHolder

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V018
  - BLOCKER
  - The length of the value must be <= 4000. [V018]
```

###### license

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - R001
  - BLOCKER
  - licenseDocument must be reported if license is 'exactMatch\_CC\_BY\_4\_0' or 'narrowMatch\_CC\_BY\_4\_0'. [R001]
* - V010
  - BLOCKER
  - The value must not be missing or empty [V010]
* - V011
  - BLOCKER
  - The value is not a valid member of the referenced list. [V011]
```

###### includesSpatialData

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V022
  - BLOCKER
  - The value must not be missing or empty [V022]
* - V023
  - BLOCKER
  - The value is not a valid member of the referenced list. [V023]
* - V026
  - BLOCKER
  - The value must be 'yes' or 'no' [V026]
* - R002
  - BLOCKER
  - If one RBD is reported as includesSpatialData = 'yes', then all the RBDs needs to be reported includesSpatialData = 'yes' [R002]
* - XC001
  - BLOCKER
  - If includesSpatialData = 'yes' then Spatial dataset cannot be empty [XC001]
* - XC002
  - BLOCKER
  - If includesSpatialData = 'no' then Spatial dataset must be empty [XC002]
```

###### includesMonitoringData

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V024
  - BLOCKER
  - The value must not be missing or empty [V024]
* - V025
  - BLOCKER
  - The value is not a valid member of the referenced list. [V025]
* - V027
  - BLOCKER
  - The value must be 'yes' or 'no' [V027]
* - R003
  - ERROR
  - The RBD is reported as includesMonitoringData = no [R003]
```

###### euRBDCode

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V030
  - BLOCKER
  - The value must not be missing or empty [V030]
* - RF001\_WFD
  - BLOCKER
  - The value must be a valid RBDCode [RF001\_WFD]
* - T404\_WFD
  - BLOCKER
  - The Monitoring table must always list the groundwater monitoring sites for quantitative monitoring ('EEA\_00-01-1') for every river basin district with designated groundwater bodies. [T404\_WFD] Values: {%identifiers%}. Number of missing values: {%numberofrecords%} [T404\_WFD]
* - RF001\_WISE5
  - BLOCKER
  - The value must be a valid RBDCode [RF001\_WISE5]
* - T404\_WISE5
  - BLOCKER
  - The Monitoring table must always list the groundwater monitoring sites for quantitative monitoring ('EEA\_00-01-1') for every river basin district with designated groundwater bodies. Values: {%identifiers%}. Number of missing values: {%numberofrecords%} [T404\_WISE5]
```

###### created

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V001
  - BLOCKER
  - The value is not a valid date (YYYY-MM-DD) [V001]
```

###### includesmonitoringdata

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - XC006
  - BLOCKER
  - If includesmonitoringdata= 'no' then it is not possible to report any programme related with the RBD [XC006]
* - XC005\_WFD
  - BLOCKER
  - If includesmonitoringdata = 'no' then it is not possible to report any Monitoring Code in table Monitoring related with the RBD. [XC005\_WFD]
* - XC008\_WFD
  - BLOCKER
  - If includesmonitoringdata = 'no' then it is not possible to report any Monitoring Code in table MonitoringPurpose related with the RBD. [XC008\_WFD]
* - XC005\_WISE5
  - BLOCKER
  - If includesmonitoringdata = 'no' then it is not possible to report any Monitoring Code in table Monitoring related with the RBD. [XC005\_WISE5]
* - XC008\_WISE5
  - BLOCKER
  - If includesmonitoringdata = 'no' then it is not possible to report any Monitoring Code in table MonitoringPurpose related with the RBD. [XC008\_WISE5]
```
