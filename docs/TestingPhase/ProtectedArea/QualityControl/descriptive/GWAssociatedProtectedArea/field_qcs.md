##### Field QCs

###### euProtectedAreaType
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V200
  - BLOCKER
  - euProtectedAreaType must be one of: shellfishDesignatedWater, drinkingWaterProtectionArea [V200]
* - V206
  - BLOCKER
  - The value must not be missing or empty [V206]
* - V207
  - BLOCKER
  - The value is not a valid member of the referenced list. [V207]
```

###### protectedAreaObjectivesSet
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V202
  - BLOCKER
  - protectedAreaObjectivesSet must be a valid Yes value [V202]
* - R200
  - BLOCKER
  - For shellfish designated waters, protectedAreaObjectivesSet cannot be 'no'. [R200]
* - R201
  - BLOCKER
  - For drinking water protection areas, protectedAreaObjectivesSet cannot be 'no'. [R201]
* - R202
  - BLOCKER
  - protectedAreaObjectivesMet cannot be 'inapplicable' when protectedAreaObjectivesSet is 'yes'. [R202]
* - V208
  - BLOCKER
  - The value must not be missing or empty [V208]
* - V209
  - BLOCKER
  - The value is not a valid member of the referenced list. [V209]
```

###### protectedAreaObjectivesMet
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V203
  - BLOCKER
  - protectedAreaObjectivesMet must be a valid YesNoUnknown value. [V203]
* - R202
  - BLOCKER
  - protectedAreaObjectivesMet cannot be 'inapplicable' when protectedAreaObjectivesSet is 'yes'. [R202]
* - V210
  - BLOCKER
  - The value must not be missing or empty [V210]
* - V211
  - BLOCKER
  - The value is not a valid member of the referenced list. [V211]
```

###### euGroundwaterBodyCode
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V204
  - BLOCKER
  - The value of euGroundWaterBodyCode must follow the syntax of WISE identifiers [V204]
* - V205
  - BLOCKER
  - The value must not be missing or empty [V205]
```
