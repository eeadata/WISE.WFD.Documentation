##### Field QCs

###### title
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V100
  - BLOCKER
  - The value must not be missing or empty [V100]
* - V117
  - BLOCKER
  - The length of the value must be <= 4000 [V117]
```

###### creatorElectronicMailAddress
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V108
  - BLOCKER
  - The value must not be missing or empty [V108]
* - V109
  - BLOCKER
  - The value does not follow the expected syntax for a valid email [V109]
* - V132
  - BLOCKER
  - The length must be less than or equal to 250 [V132]
```

###### creatorOrganisationName
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V102
  - BLOCKER
  - The value must not be missing or empty [V102]
* - V110
  - BLOCKER
  - The length of the value must be <= 4000. [V110]
```

###### description
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V111
  - BLOCKER
  - The length of the value must be <= 4000. [V111]
```

###### language
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V112
  - BLOCKER
  - "language" contains duplicate values [V112]
* - V103
  - BLOCKER
  - The value must not be missing or empty [V103]
* - V101
  - BLOCKER
  - The value is not a valid member of the referenced list. [V101]
```

###### licenseDocument
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V113
  - BLOCKER
  - "licenseDocument" contains duplicate values. [V113]
* - V125
  - BLOCKER
  - The value is not a valid member of the referenced list.[V125]
```

###### metadataDocument
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V114
  - BLOCKER
  - "metadataDocument" contains duplicate values [V114]
* - V126
  - BLOCKER
  - The value is not a valid member of the referenced list. [V126]
* - R004
  - BLOCKER
  - metadataDocument must be reported if includesSpatialData = 'yes' [R004]
```

###### rights
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V115
  - BLOCKER
  - The length of the value must be <= 4000 [V115]
```

###### rightsHolder
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V116
  - BLOCKER
  - The length of the value must be <= 4000 [V116]
```

###### license
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V123
  - BLOCKER
  - The value must not be missing or empty [V123]
* - V104
  - BLOCKER
  - The value is not a valid member of the referenced list. [V104]
* - R005
  - BLOCKER
  - Document(s) about licensing information must be reported if license IN ('exactMatch\_CC\_BY\_4\_0', 'narrowMatch\_CC\_BY\_4\_0') [R005]
```

###### includesSpatialData
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V133
  - BLOCKER
  - The value must not be missing or empty [V133]
* - V134
  - BLOCKER
  - includesSpatialData must be a valid YesNo value. [V134]
* - R004
  - BLOCKER
  - metadataDocument must be reported if includesSpatialData = 'yes' [R004]
* - XC001
  - BLOCKER
  - If includesSpatialData = 'yes' then Spatial dataset cannot be empty [XC001]
* - XC002
  - BLOCKER
  - If includesSpatialData = 'no' then Spatial dataset must be empty [XC002]
```

###### includesDescriptiveData
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V136
  - BLOCKER
  - The value must not be missing or empty [V136]
* - V135
  - BLOCKER
  - includesDescriptiveData must be a valid YesNo value. [V135]
* - R003
  - ERROR
  - It been reported includesDescriptiveData = no [R003]
* - XC003
  - BLOCKER
  - If includesdescriptivedata= 'no' then it is not possible to report any waterbody related with the protected area [XC003]
* - XC004
  - BLOCKER
  - If includesdescriptivedata= 'yes' then you need to report a waterbody related with the protected area [XC004]
```

###### created
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V107
  - BLOCKER
  - The value is not a valid date (YYYY-MM-DD) [V107]
```
