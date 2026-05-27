(heading_wfd_monitoring_testing_phase)=
# WFD Monitoring

```{warning}
The fields definitions are being reviewed.
```

Last update: 2026-05-25

(heading_wfd_monitoring_fields_definition)=
## Fields definition

### Monitoring

```{include} tables/Monitoring_Monitoring
```

### MonitoringProgrammes

```{include} tables/Monitoring_MonitoringProgrammes
```

### MonitoringSite

Monitoring Sites: Location used for the collection of data about physical-chemical, ecological, quantitative or other observable properties of a surface or groundwater body. Monitoring location included in a WFD surveillance, operational or investigative monitoring programme. Monitoring location included in the EIONET WISE SoE network.Uniqueness: uniqueness 1: inspireIdLocalId + inspireIdNamespace uniqueness 2: thematicIdIdentifier + thematicIdIdentifierScheme

```{include} tables/Monitoring_MonitoringSite
```

### dcMetadata

Metadata. One record per country.

```{include} tables/Monitoring_dcMetadata
```

### Document

This table contains information about reported documents. Each document must have a unique identifier, a name and it can be either an external link represented by URL or a local file uploaded.`Uniqueness: documentCode

```{include} tables/Monitoring_Document
```

### DocumentReference

```{include} tables/Monitoring_DocumentReference
```
