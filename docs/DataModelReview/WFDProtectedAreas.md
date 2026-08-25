(heading_wfd_protected_areas)=
# Protected areas

Last update: 2026-08-25

(heading_wfd_protected_areas_purpose_and_overview)=
## Purpose and overview

```{epigraph}
"According to Article 6 and Annex IV of the WFD, 
Member States shall ensure the establishment of a register 
or registers of all areas lying within each River Basin District 
which have been designated as requiring special protection 
under specific Community legislation for the 
protection of their surface water and groundwater, 
or for the conservation of habitats and species directly depending on water, 
including the protection of Natura 2000 sites 
and economically significant aquatic species (e.g. shellfish)." 
{footcite}`WFDProtectedAreasClarification2016`
{footcite}`WFDProtectedAreasClarification2022`
```

This section revises the reporting of WFD Protected Areas
in the 2nd and 3rd cycle of reporting of the Water Framework Directive River Basin Management Plans
({numref}`ProtectedAreas_3rdCycle_DescriptiveData_ClassDiagram`),
as well as the associated spatial data ({numref}`ProtectedAreas_3rdCycle_SpatialData_ClassDiagram`).

A proposal is presented for the electronic reporting in the 4th cycle.

```{mermaid} /DataModelReview/mmd/ProtectedAreas_3rdCycle_DescriptiveData_ClassDiagram.mmd
:name: ProtectedAreas_3rdCycle_DescriptiveData_ClassDiagram
:align: center
:caption: GWAssociatedProtectedArea and SWAssociatedProtectedArea - 3rd cycle - Obsolete
```

```{mermaid} /DataModelReview/mmd/ProtectedAreas_3rdCycle_SpatialData_ClassDiagram.mmd
:name: ProtectedAreas_3rdCycle_SpatialData_ClassDiagram
:align: center
:caption: ProtectedArea spatial datasets - 3rd cycle - Obsolete
```

The WFD Protected Area spatial data reporting requirements were stable
during the 2nd and 3rd cycle of electronic reporting
({numref}`ProtectedAreas_3rdCycle_Table`).

The following generic principles were applied
{footcite}`WFDProtectedAreasClarification2016`
{footcite}`WFDProtectedAreasClarification2022`:

1) If the spatial data was already reported under a specific dataflow
   (e.g. for bathing waters, sensitive areas, nitrate vulnerable zones, or Natura 2000 protected sites),
   then the *spatial data* was neither required nor accepted under the WFD.
2) If no specific dataflow existed
   (e.g. for drinking water protection areas, freshwater fish designated areas
   and shellfish designated areas),
   then the spatial data was reported under the WFD.

Several issues affected the reporting, causing redundancies and inconsistencies:

* For the protected area types under case 1),
  not all the data models followed the basic requirements of the WFD ProtectedArea data model.  
  For example, the nitrate vulnerable zones do not have a unique identifier consistent
  with the syntax of the WISE identifiers.
* For protected area types under case 2),
  the majority of the issues affected the reporting of the drinking water protection areas.
  If the drinking water protection area matched the entire water body
  and the identifier was the same,  
  then it was not required to report the geometry of the protected area.  
  However, this approach was not followed consistently by Member States.
* For the Natura2000 protected sites,
  the association to one or more WFD water bodies is not reported in the original dataflow.
  Therefore, the association must reported under the WFD descriptive (i.e. non-spatial) data reporting.
* For the remaining types of WFD Protected Areas,
  the association to a WFD water body
  was an *optional* attribute (e.g. bathing waters, sensitive areas, etc).  
  Therefore, the association between the protected area and the water body
  was requested again in the WFD descriptive data reporting.
  This approach created redundancies and potential inconsistencies due to the different reporting timelines.

```{include} tables/ProtectedAreas_3rdCycle_Table
```

These issues are addressed in the simplification of the reporting for the 4th cycle:

* The *same spatial data model* is used for all the WFD ProtectedArea dataflows and datasets,
  guaranteeing the existence of WISE *unique identifiers*
* The association between protected areas and water bodies is reported *only once*,
  in the ProtectedArea spatial dataset (i.e. removing it from the WFD descriptive data reporting)

These principles (same model, unique identifiers, report only once)
were applied for all WFD protected area types, *except Natura2000 protected sites*.

(heading_wfd_protected_areas_proposed_structure_4th_cycle)=
## Proposed structure - 4th cycle

For the 4th cycle of reporting, the requested information detailed in (see also {numref}`ProtectedArea_4thCycle_Overview_ClassDiagram`):

* {ref}`heading_wfd_protected_areas_spatial_data_reporting_4th_cycle`
* {ref}`heading_wfd_protected_areas_descriptive_data_reporting`
* {ref}`heading_wfd_protected_areas_documents_dataset_4th_cycle`

```{mermaid} /DataModelReview/mmd/ProtectedArea_4thCycle_Overview_ClassDiagram.mmd
:name: ProtectedArea_4thCycle_Overview_ClassDiagram
:caption:  WFD Protected Areas dataflow - overview - 4th cycle
:align: center
```

(heading_wfd_protected_areas_spatial_data_reporting_4th_cycle)=
## Spatial data - 4th cycle

The reporting of spatial data related to WFD protected areas in done under the dataflows
pertaining to the legal instruments under which the protected areas were defined
({numref}`ProtectedAreas_LegalInstruments_Table`).  

**Only designated waters (freshwater fish and shellfish designated waters)
are reported in directly in the 4th RBMP dataflow.**

```{include} tables/ProtectedAreas_LegalInstruments_Table
```

The WFD Protected Area spatial data reporting requirement for the 4th cycle of electronic reporting
are detailed in ({numref}`ProtectedAreas_4thCycle_Table`)

* The reporting of drinking water protection areas is moved to under Article 8 of the recast DWD,
  on the risk assessment and management of catchment areas
  for abstraction points of water intended for human consumption.
* The data model for the Nitrate Vulnerable Zones reporting
  is aligned with the model used for the other protected areas (except Natura 2000 protected sites).
* The reporting of the association between the protected areas
  and the water bodies is done only once – in the spatial data reporting
  (except Natura 2000 protected sites).

```{include} tables/ProtectedAreas_4thCycle_Table
```

{numref}`Spatial_4thCycle_ProtectedArea_ClassDiagram` presents the class diagram
for the proposed generic ProtectedArea dataset:

* Depending on the specific dataflow, different geometry types may be requested/allowed
  (either point, line or polygon).
* The `relatedZoneIdentifier` and `relatedZoneIdentifierScheme` are mandatory,
  and specific constraints will apply depending on the dataflow
  (i.e. on the type of protected area).
* The attribute `confidentialityStatus` was included
  (and applies to the drinking water protected areas)
  to address concerns about the publication of the location of some protected areas.
* The attributes `sizeValue` and `sizeUom` attributes are no longer requested.
* The attributes `successorsIdentifier` and `successorsIdentifierScheme`
  have been kept for clarity's sake although their value will always be `NULL`
  (the appropriate value will be derived and included in the
  published WISE datasets that refer to the previous reporting cycles).

```{mermaid} /DataModelReview/mmd/Spatial_4thCycle_ProtectedArea_ClassDiagram.mmd
:name: Spatial_4thCycle_ProtectedArea_ClassDiagram
:caption: Class diagram for an abstract ProtectedArea dataset – 4th cycle
:align: center
```

(heading_wfd_protected_areas_special_case_the_natura2000_protected_sites)=
## Special case - Natura2000 sites

The Natura2000 dataflows do not include information about the association
between protected sites and WFD water bodies.
Therefore, a different approach is necessary to simplify the WFD reporting.

A Natura 2000 site should be designated as "water-dependent"
if it contains Annex I habitat types
or Annex II species (Habitats Directive), or bird species (Birds Directive),
whose presence was the primary reason for the area's designation
and that meet the ecological criteria below:

* habitats consisting of surface water or occurring entirely
  within surface water as defined by the WFD
* habitats that depend on frequent inundation by surface water or specific groundwater levels
* aquatic species living directly in surface waters
* species with at least one aquatic life stage dependent
  on surface water for essential activities
  such as breeding, incubation, juvenile development, feeding, or roosting.

A provisional prefilled list of "water-dependent" Natura 2000 protected sites was created,
based on the Natura2000 reporting and the habitat type {footcite}`links_between_wfd_nature_directives`.

The provisional prefilled list is available {download}`here <files/WFD_RelatedNatura2000Sites.sqlite>`
for validation purposes:

* If missing, additional Natura 2000 protected site identifiers
  may be added (from the reference list already reported under the Natura 2000 dataflows).
* If incorrect, Natura 2000 protected site identifiers present in the provisional list
  may be flagged for removal from the WFD register of protected areas.
* For those Natura 2000 sites that were related to WFD surface water bodies in the 3rd reporting cycle
  please review, in the provided SQLite file, the distance value (expressed in kilometers)
  from the Natura 2000 site to the associated water body to detect possible issues.
* For the Natura 2000 sites to be included in the WFD register of protected areas
  (because where the maintenance or improvement of water status
  is a critical factor for their protection), the association to water bodies should be reported.

The list of related Natura2000 sites has been generated with the following published datasets:

```{include} tables/ProtectedAreas_Natura2000Datasets_Table
```

(heading_wfd_protected_areas_descriptive_data_reporting)=
## Descriptive data - 4th cycle

Specific objectives may be set for the water body due to an associated protected areas.  
This only applies for the following types of protected areas:

* Shellfish designated waters
* Drinking water protection areas
* Natura 2000 protected sites
  included in the WFD register of protected areas

For Freshwater fish designated waters, the WFD good ecological status
fully integrates the integrate Fish Directive (2006/44/EC) objectives.
Similarly, the WFD good status integrates the Nitrates Directive
and UWWTD objectives related to eutrophication.
Therefore, no information on specific objectives is requested or expected
for these types of protected area or for bathing waters.

The analysis of the 3rd cycle reveals that no specific objectives
were set for Nationally Designated Areas (NatDA, formerly known as CDDA).
Information about this type of protected sites will no longer be requested.

{numref}`ProtectedArea_4thCycle_SWAssociatedProtectedArea_ClassDiagram` illustrates the reporting
of surface water bodies with specific objectives related to protected areas:

* For shellfish designated areas, report *only* if specific objectives have been set.
* For drinking water protection areas, report *only* if specific objectives have been set.
* For Natura2000 sites, report if specific objectives have been set *or*
  if the Natura2000 site is not part of the "pre-filled" list (to be provided).

```{mermaid} /DataModelReview/mmd/ProtectedArea_4thCycle_SWAssociatedProtectedArea_ClassDiagram.mmd
:name: ProtectedArea_4thCycle_SWAssociatedProtectedArea_ClassDiagram
:caption: Surface water bodies with specific objectives associated with protected areas - 4th cycle
:align: center
```

{numref}`ProtectedArea_4thCycle_GWAssociatedProtectedArea_ClassDiagram` illustrates the reporting
of groundwater bodies with specific objectives associated with protected areas:

* For shellfish designated areas, report *only* if specific objectives have been set.
* For drinking water protection areas, report *only* if specific objectives have been set.

```{mermaid} /DataModelReview/mmd/ProtectedArea_4thCycle_GWAssociatedProtectedArea_ClassDiagram.mmd
:name: ProtectedArea_4thCycle_GWAssociatedProtectedArea_ClassDiagram
:caption: Groundwater bodies with specific objectives associated with protected areas - 4th cycle
:align: center
```

The following conditions will raise a quality control *blocker*:

* `euProtectedAreaType = 'shellfishDesignatedWater' AND protectedAreaObjectivesSet = 'no'`
* `euProtectedAreaType = 'drinkingWaterProtectionArea' AND protectedAreaObjectivesSet = 'no'`
* `euProtectedAreaType = 'shellfishDesignatedWater' AND euProtectedAreaCode IS NOT NULL`
* `euProtectedAreaType = 'drinkingWaterProtectionArea' AND euProtectedAreaCode IS NOT NULL`
* `euProtectedAreaType = 'natura2000' AND euProtectedAreaCode IS NULL`
* `protectedAreaObjectivesSet = 'yes' AND protectedAreaObjectivesMet = 'inapplicable'`

The following checks against other datasets will also raise a quality control *blocker*:

* if `euProtectedAreaType = 'shellfishDesignatedWater'`
  but there is no drinking water protected area associated with that water body
* if `euProtectedAreaType = 'drinkingWaterProtectionArea'`
  but there is no drinking water protected area associated with that water body
* if `euProtectedAreaType = 'natura2000'`
  but there is corresponding Natura2000 identifier in
  https://dd.eionet.europa.eu/vocabulary/biodiversity/n2000sites

(heading_wfd_protected_areas_surface_water_bodies_exemptions)=
### Exemptions for surface water bodies associated with protected areas

Specific objectives may be expressed in terms of WFD Water quality elements
for surface water bodies associated with some types of protected areas:

* Shellfish designated waters
* Drinking water protection areas
* Natura2000 protected sites included in the WFD register of protected areas

If the specific objectives have been expressed in terms of WFD quality elements,
and have not been met, then exemptions may be reported.
(Note that the euProtectedAreaCode value is only requested for Natura2000 sites.)

Based on the data reported in the 3rd cycle, the expected number of exemptions is relatively low.
Therefore the attributes related to exemptions were simply
added to the SWAssociatedProtectedArea table ({numref}`SWAssociatedProtectedAreaClass`).  
See also {ref}`heading_wfd_exemptions_codelists_associated_with_the_reporting_of_exemptions`.

```{mermaid} /DataModelReview/mmd/Exemptions_4thCycle_SWAssociatedProtectedArea_ClassDiagram.mmd
:name: SWAssociatedProtectedAreaClass
:caption: Surface water body associated protected area - Exemptions - 4th cycle
:align: center
```

```{todo}
Exemptions - {ref}`heading_wfd_protected_areas_surface_water_bodies_exemptions`

DG ENV to provide draft flowchart and quality control criteria 
for {ref}`heading_wfd_protected_areas_surface_water_bodies_exemptions`.
```

(heading_wfd_protected_areas_groundwater_bodies_exemptions)=
### Exemptions for groundwater bodies associated with protected areas

Specific objectives may be set for water bodies associated with some types of protected areas:

* Drinking water protection areas
* Natura 2000 protected sites included in the WFD register of protected areas

*If the specific objectives have not been met*, then exemptions may be reported.

(Note that the euProtectedAreaCode value is only requested for Natura 2000 sites.)

Based on the data reported in the 3rd cycle, the expected number of exemptions is relatively low.
Therefore the attributes related to exemptions were simply
added to the GWAssociatedProtectedArea table ({numref}`GWAssociatedProtectedAreaClass`).  
See also {ref}`heading_wfd_exemptions_codelists_associated_with_the_reporting_of_exemptions`.

```{todo}
Exemptions: {ref}`heading_wfd_protected_areas_groundwater_bodies_exemptions`

DG ENV to provide draft flowchart and quality control criteria
```

```{mermaid} /DataModelReview/mmd/Exemptions_4thCycle_GWAssociatedProtectedArea_ClassDiagram.mmd
:name: GWAssociatedProtectedAreaClass
:caption: Groundwater body associated protected area - Exemptions - 4th cycle
:align: center
```

(heading_wfd_protected_areas_documents_dataset_4th_cycle)=
## Documents dataset - 4th cycle

The Documents dataset follows the standard structure used in various WISE dataflows
({numref}`ProtectedArea_4thCycle_Documents_ClassDiagram`):

* The `dcMetadata` table provides the basic Dublin Core metadata elements about the delivery.
  
  - If required by the data providers, and especially if spatial data is being reported,
    the `licenseDocument` and the `metadataDocument` attributes allow the provision
    of additional information about the dataset.
  - The `dcMetadata` table also functions as a "manifest file"
    explaining if the delivery contains data for a given river basin district or not.

* The `Document` table allows the upload of documents (for example, PDFs)
  or the provision of a `hyperlink` to a document stored in a publicly accessible national web site.

* The `Reference` table is also standard in the WISE dataflows:
  the `bookmark` it allows the identification of the chapter(s), sections(s) or page range(s)
  where the relevant information about a `subject`
  can be found within a document.

```{mermaid} /DataModelReview/mmd/ProtectedArea_4thCycle_Documents_ClassDiagram.mmd
:name: ProtectedArea_4thCycle_Documents_ClassDiagram
:caption: WFD Protected Area - 4th cycle - Documents
:align: center
```

The following criteria apply:

01. The `dcMetadata` table must contain *one and only one* record
    for each of the country's river basin districts, identified by the `euRBDCode`.

02. The spatial dataset is **national**.
    The `includesSpatialData` value must be the same for all river basin districts.

03. If `includesSpatialData = 'no'` then no spatial data is expected,
    and the quality control of the descriptive dataset will run
    against **the designated areas (freshwater fish and shellfish) reported in the 3rd cycle**,
    plus the last technically accepted deliveries of the
    other types of WFD protected areas in the WISE register.

04. The descriptive dataset tables are also **national**,
    but the quality control will allow deliveries
    where some, or all, the river basin districts have `includesDescriptiveData = no`.

## Annexes - Data analysis - 3rd cycle

```{include} FragmentAnnexesDataAnalysis3rdCycle
```

The data reported for the 3rd cycle can be used to estimate the impact of the simplification
of the descriptive data reporting:

* 46% of the 84560 records reported for groundwater associated protected areas
  would not have been reported.
* 72% of the 71726 records reported for surface water associated protected areas
  would not have been reported.

(heading_wfd_protected_areas_references)=
## References

```{warning}
The original document containing this revised model can still be downloaded but should not be used.
See **PROPOSAL - Version 2026.02.13** {download}`PDF <pdf/WFD_4th_cycle_ProtectedAreas_v20260220.pdf>`
```

```{footbibliography}
```
