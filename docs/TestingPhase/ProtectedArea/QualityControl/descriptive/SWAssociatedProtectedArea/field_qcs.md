##### Field QCs

###### protectedAreaObjectivesSet
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V101
  - BLOCKER
  - The value is not a valid member of the referenced list. [V101]
* - R100
  - BLOCKER
  - For shellfish designated waters, protectedAreaObjectivesSet cannot be 'no'. [r100]
* - R101
  - BLOCKER
  - For drinking water protection areas, protectedAreaObjectivesSet cannot be 'no'. [R101]
* - R105
  - BLOCKER
  - protectedAreaObjectivesMet cannot be 'inapplicable' when protectedAreaObjectivesSet is 'yes'. [R105]
* - V108
  - BLOCKER
  - The value must not be missing or empty [V108]
* - V109
  - BLOCKER
  - The value is not a valid member of the referenced list. [V109]
```

###### protectedAreaObjectivesMet
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V102
  - BLOCKER
  - The value is not a valid member of the referenced list. [V102]
* - R105
  - BLOCKER
  - protectedAreaObjectivesMet cannot be 'inapplicable' when protectedAreaObjectivesSet is 'yes'. [R105]
* - V110
  - BLOCKER
  - The value must not be missing or empty [V110]
* - V111
  - BLOCKER
  - The value is not a valid member of the referenced list. [V111]
```

###### euProtectedAreaCode
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - R102
  - BLOCKER
  - For shellfish designated waters, euProtectedAreaCode must not be reported. [R102]
* - R103
  - BLOCKER
  - For drinking water protection areas, euProtectedAreaCode must not be reported. [R103]
* - R104
  - BLOCKER
  - For Natura2000 sites, euProtectedAreaCode must be reported. [R104]
* - V104
  - BLOCKER
  - The value of euProtectedAreaCode must follow the syntax of WISE identifiers [V104]
```

###### euSurfaceWaterBodyCode
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V103
  - BLOCKER
  - The value of euSurfaceWaterBodyCode must follow the syntax of WISE identifiers [V103]
* - V105
  - BLOCKER
  - The value must not be missing or empty [V105]
```

###### euProtectedAreaType
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V106
  - BLOCKER
  - The value must not be missing or empty [V106]
* - V107
  - BLOCKER
  - The value is not a valid member of the referenced list.[V107]
```
