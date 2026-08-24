(heading_wfd_rbd_and_ca_testing_phase)=
# River Basin Districts and Competent Authorities

```{warning}
The definitions are being reviewed.
```

Last update: 2026-08-21

## Descriptive dataset

See additional information in the *data model review documentation*:

* {ref}`heading_wfd_rbd_and_ca_descriptive_dataset_4th_cycle`

```{sql-dataset} CompetentAuthority WFDRiverBasinDistrict
:connection_string: sqlite:///docs/TestingPhase/db/WFD_Documentation.db3
```

```{sql-dataset} RiverBasinDistrictCompetentAuthority WFDRiverBasinDistrict
:connection_string: sqlite:///docs/TestingPhase/db/WFD_Documentation.db3
```

## Spatial dataset

See additional information in the *data model review documentation*:

* {ref}`heading_riverbasindistrict_spatial_dataset_4th_cycle`

```{sql-dataset} RiverBasinDistrict WFDRiverBasinDistrict
:connection_string: sqlite:///docs/TestingPhase/db/WFD_Documentation.db3
```

## Documents dataset

See additional information in the *data model review documentation*:

* {ref}`heading_wfd_rbd_and_ca_documents_dataset_4th_cycle`

```{sql-dataset} dcMetadata WFDRiverBasinDistrict
:connection_string: sqlite:///docs/TestingPhase/db/WFD_Documentation.db3
```

```{sql-dataset} Document WFDRiverBasinDistrict
:connection_string: sqlite:///docs/TestingPhase/db/WFD_Documentation.db3
```
