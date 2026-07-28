##### Table QCs


```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - TU201
  - BLOCKER
  - The combination inspireIdLocalId + inspireIdNamespace must be unique. [TU201]
* - TU202
  - BLOCKER
  - The combination thematicIdIdentifier + thematicIdIdentifierScheme must be unique. [TU202]
* - T201
  - BLOCKER
  - If the object has successor(s), then the deleted object should not be reported. Only the successor object(s) must be reported, with their appropriate predecessor(s) and wiseEvolutionType value. [T201] Values: {%identifiers%} . Number of invalid values: {%numberofrecords%}
* - T202
  - BLOCKER
  - If the object is the predecessor of another object, then the deleted object should not be reported. Only the successor object(s) must be reported, with their appropriate predecessor(s) and wiseEvolutionType value. [T202] Values: {%identifiers%} . Number of invalid values: {%numberofrecords%}
* - S204
  - BLOCKER
  - Only one EPSG is allowed in the table [S204]
* - RF218\_WFD
  - BLOCKER
  - A valid 'eu' thematic identifier exists in the register but was not reported (either as a spatial object or as a predecessor) [RF218\_WFD]. Values: {%identifiers%}. Number of missing values: {%numberofrecords%}
* - RF218\_WISE5
  - BLOCKER
  - A valid 'eu' thematic identifier exists in the register but was not reported (either as a spatial object or as a predecessor) [RF218\_WISE5]. Values: {%identifiers%}. Number of missing values: {%numberofrecords%}
* - RF224\_WFD
  - BLOCKER
  - If an object is reported as 'reactivation', it must have the same predecessors as before. Identifiers affected: {%end\_result%} [RF224\_WFD]
* - RF224\_WISE5
  - BLOCKER
  - If an object is reported as 'reactivation', it must have the same predecessors as before. Identifiers affected: {%end\_result%} [RF224\_WISE5]
* - RF224\_WFD
  - BLOCKER
  - If an object is reported as 'reactivation', it must have the same predecessors as before. Identifiers affected: {%end\_result%} [RF224\_WFD]
* - RF224\_WISE5
  - BLOCKER
  - If an object is reported as 'reactivation', it must have the same predecessors as before. Identifiers affected: {%end\_result%} [RF224\_WISE5]
```
