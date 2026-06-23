(heading_wfd_monitoring_testing_phase)=
# WFD Monitoring

```{warning}
The definitions are being reviewed.
```

Last update: 2026-05-25

(heading_wfd_monitoring_monitoring_table_testing_phase)=
## Monitoring table

```{include} tables/Monitoring_Monitoring
```

(heading_wfd_monitoring_monitoringprogrammes_table_testing_phase)=
## MonitoringProgrammes table

```{include} tables/Monitoring_MonitoringProgrammes
```

(heading_wfd_monitoring_monitoringsite_table_testing_phase)=
## MonitoringSite spatial table

Monitoring Sites: Location used for the collection of data about physical-chemical, ecological, quantitative or other observable properties of a surface or groundwater body. Monitoring location included in a WFD surveillance, operational or investigative monitoring programme. Monitoring location included in the EIONET WISE SoE network.Uniqueness: uniqueness 1: inspireIdLocalId + inspireIdNamespace uniqueness 2: thematicIdIdentifier + thematicIdIdentifierScheme

```{include} tables/Monitoring_MonitoringSite
```

(heading_wfd_monitoring_dcmetadata_table_testing_phase)=
## dcMetadata table

Metadata. One record per country.

```{include} tables/Monitoring_dcMetadata
```

(heading_wfd_monitoring_document_table_testing_phase)=
## Document table

This table contains information about reported documents. Each document must have a unique identifier, a name and it can be either an external link represented by URL or a local file uploaded. Uniqueness: documentCode

```{include} tables/WISE_Document
```

(heading_wfd_monitoring_documentreference_table_testing_phase)=
## DocumentReference table

```{include} tables/Monitoring_DocumentReference
```
