(heading_wfd_protectedarea_testing_phase)=
# Protected Area

Last updated: 2026-08-19

```{warning}
The online version of the text is being reviewed.  
```

See additional information in the *data model review documentation*:

* {ref}`heading_wfd_protected_areas_purpose_and_overview`

## Descriptive dataset

See additional information in the *data model review documentation*:

* {ref}`heading_wfd_protected_areas_descriptive_data_reporting`

```{sql-dataset} GWAssociatedProtectedArea WFDProtectedArea
:connection_string: sqlite:///docs/TestingPhase/db/WFD_Documentation.db3
```

```{sql-dataset} SWAssociatedProtectedArea WFDProtectedArea
:connection_string: sqlite:///docs/TestingPhase/db/WFD_Documentation.db3
```

## Spatial dataset

See additional information in the *data model review documentation*:

* {ref}`heading_wfd_protected_areas_spatial_data_reporting_4th_cycle`

```{sql-dataset} ProtectedArea WFDProtectedArea
:connection_string: sqlite:///docs/TestingPhase/db/WFD_Documentation.db3
```

## Documents dataset

```{sql-dataset} dcMetadata WFDProtectedArea
:connection_string: sqlite:///docs/TestingPhase/db/WFD_Documentation.db3
```

```{sql-dataset} Document WFDProtectedArea
:connection_string: sqlite:///docs/TestingPhase/db/WFD_Documentation.db3
```
