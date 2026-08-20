##### Field QCs

###### documentCode
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V118
  - BLOCKER
  - The value must not be missing or empty [V118]
* - V122
  - BLOCKER
  - The value of documentCode must follow the syntax of WISE identifiers [V122]
```

###### documentName
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V119
  - BLOCKER
  - The value must not be missing or empty [V119]
* - V121
  - BLOCKER
  - The length of the value must be <= 50 [V121]
```

###### hyperlink
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V120
  - BLOCKER
  - The value does not follow the expected syntax for a valid URL [V120]
* - R101
  - BLOCKER
  - Either hyperlink or documentFile must be reported, but not both [R101]
* - V131
  - BLOCKER
  - The length must be less than or equal to 2100. [V131]
```
