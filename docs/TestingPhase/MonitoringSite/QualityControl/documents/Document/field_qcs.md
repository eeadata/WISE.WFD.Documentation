##### Field QCs

###### documentCode

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V102
  - BLOCKER
  - The value must not be missing or empty. [V102]
* - V101
  - BLOCKER
  - The value of documentCode must follow the syntax of WISE identifiers [V101]
```

###### documentName

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V104
  - BLOCKER
  - The value must not be missing or empty. [V104]
* - V103
  - BLOCKER
  - The length of the value must be <= 50. [V103]
```

###### hyperlink

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V105
  - BLOCKER
  - The value does not follow the expected syntax for a valid URL. [V105]
* - R101
  - BLOCKER
  - Either hyperlink or documentFile must be reported, but not both. [R101]
* - V106
  - BLOCKER
  - The length of the value must be <= 2048 [V106]
```

###### documentFile

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - R101
  - BLOCKER
  - Either hyperlink or documentFile must be reported, but not both. [R101]
```
