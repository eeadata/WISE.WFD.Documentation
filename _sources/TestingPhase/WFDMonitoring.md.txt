(heading_wfd_monitoring_testing_phase)=
# Monitoring

Last updated: 2026-08-20

```{warning}
The online version of the text is being reviewed.  
```

See additional information in the *data model review documentation*:

* {ref}`heading_wfd_monitoring_proposed_structure_4th_cycle`

## Descriptive dataset

See additional information in the *data model review documentation*:

* {ref}`heading_wfd_monitoring_4th_cycle`

```{sql-dataset} MonitoringProgrammes WFDMonitoring
:connection_string: sqlite:///docs/TestingPhase/db/WFD_Documentation.db3
```

```{sql-dataset} Monitoring WFDMonitoring
:connection_string: sqlite:///docs/TestingPhase/db/WFD_Documentation.db3
```

```{sql-dataset} MonitoringPurpose WFDMonitoring
:connection_string: sqlite:///docs/TestingPhase/db/WFD_Documentation.db3
```

## Spatial dataset

See additional information in the *data model review documentation*:

* {ref}`heading_monitoringsite_spatial_dataset_4th_cycle`

```{sql-dataset} MonitoringSite WFDMonitoring
:connection_string: sqlite:///docs/TestingPhase/db/WFD_Documentation.db3
```

## Documents dataset

See additional information in the *data model review documentation*:

* {ref}`heading_wfd_monitoring_documents_dataset_4th_cycle`

```{sql-dataset} dcMetadata WFDMonitoring
:connection_string: sqlite:///docs/TestingPhase/db/WFD_Documentation.db3
```

```{sql-dataset} Document WFDMonitoring
:connection_string: sqlite:///docs/TestingPhase/db/WFD_Documentation.db3
```

```{sql-dataset} DocumentReference WFDMonitoring
:connection_string: sqlite:///docs/TestingPhase/db/WFD_Documentation.db3
```
