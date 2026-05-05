# WFD - Protected Areas

```{warning}
The online version of the text is being reviewed.  
See **PROPOSAL - Version 2026.02.13** {download}`PDF <pdf/WFD_4th_cycle_ProtectedAreas_v20260220.pdf>`
```

## Purpose and overview

"According to Article 6 and Annex IV of the WFD, Member States shall ensure the establishment of a register or registers of all areas lying within each River Basin District which have been designated as requiring special protection under specific Community legislation for the protection of their surface water and groundwater, or for the conservation of habitats and species directly depending on water, including the protection of Natura 2000 sites and economically significant aquatic species (e.g. shellfish)."[^1].

The document revises the reporting of WFD Protected Areas in the 2ⁿᵈ and 3ʳᵈ cycle of reporting of the Water Framework Directive River Basin Management Plans (Figure 1), as well as the associated spatial data (Figure 2). A proposal is presented for the electronic reporting in the 4ᵗʰ cycle. Aspects related to exemptions are addressed in a later document.


```{mermaid} /DataModelReview/mmd/ProtectedAreasClassdiagram.mmd
:name: Figure1
:align: center
:caption: Partial class diagram for Protected Areas related data in the 3ʳᵈ cycle of reporting.
```

Source: [https://cdr.eionet.europa.eu/help/WFD/WFD_715_2022/UML%20Data%20specification/WFD2022.EAP](https://cdr.eionet.europa.eu/help/WFD/WFD_715_2022/UML%20Data%20specification/WFD2022.EAP)

---

*Figure 2. Partial class diagram for the ProtectedArea class – 3ʳᵈ cycle of reporting.*

```{mermaid} /DataModelReview/mmd/ProtectedAreasClassdiagram2.mmd
:align: center
```

Source: [https://cdr.eionet.europa.eu/help/WFD/WFD_715_2022/UML%20Data%20specification/WFD2022.EAP](https://cdr.eionet.europa.eu/help/WFD/WFD_715_2022/UML%20Data%20specification/WFD2022.EAP)

## Spatial data reporting – 2ⁿᵈ and 3ʳᵈ cycle

The WFD Protected Area spatial data reporting requirements were stable during the 2ⁿᵈ and 3ʳᵈ cycle of electronic reporting ({numref}`electronic_reporting`).

The following generic principles were applied:

1) If the spatial data was already reported under a specific dataflow(e.g. for bathing waters, sensitive areas, nitrate vulnerable zones,or Natura 2000 protected sites), then spatial data was neither required nor accepted under the WFD.
2) If no specific dataflow existed (e.g. for drinking water protection areas, freshwater fish designated areas and shellfish designated areas), then the spatial data was reported under the WFD.

Several issues affected the reporting, causing redundancies and inconsistencies:

- For the protected area types under case 1), not all the data models followed the basic requirements of the WFD ProtectedArea data model.For example, the nitrate vulnerable zones do not have a unique identifier consistent with the syntax of the WISE identifiers.
- For protected area types under case 2), most issues affected the reporting of the drinking water protection areas. If the drinking water protection area matched the entire water body and the identifier was the same, then reporting the geometry of the protected area was not required – however, this approach was not followed consistently by Member States.
- In all cases, the association between the WFD ProtectedArea and one or more WFD water bodies is not reported (e.g. for the Natura 2000 protected sites) or was an optional attribute (e.g. bathing waters,sensitive areas, etc). Therefore, the association between the protected area and the water body was requested again in the WFD descriptive data – creating redundancies and potential inconsistencies due to the different reporting timelines.

These issues are addressed in the simplification of the reporting for the 4ᵗʰ cycle:

- Using the same spatial data model across all WFD ProtectedArea dataflows and datasets, therefore guaranteeing the existence of WISE **unique identifiers**.
- Reporting the association between protected areas and water bodies **only once**, in the ProtectedArea dataset (i.e. removing it from the WFD descriptive data reporting).

The principles above were applied for all WFD protected area types,except Natura2000 protected sites.


```{include} tables/ProtectedArea_2ndand3rdcycleelectronicReporting_Table
```
Source: Text in *italics* extracted from the documents referenced in footnote (1).

## Spatial data reporting – 4ᵗʰ cycle

In keeping with the approach taken in the 3ʳᵈ cycle, the reporting of spatial data related to WFD protected areas in done under the dataflows pertaining to the legal instruments under which the protected areas were defined ({numref}`euinstruments`)

The WFD Protected Area spatial data reporting requirement for the 4ᵗʰ cycle of electronic reporting are detailed in ({numref}`spatialdata`)

- The reporting of drinking water protection areas is moved to under Article 8 of the recast DWD, on the risk assessment and management of catchment areas for abstraction points of water intended for human consumption.
- The data model for the Nitrate Vulnerable Zones reporting is aligned with the model used for the other protected areas (except Natura 2000 protected sites).
- The reporting of the association between the protected areas and the water bodies is done only once – in the spatial data reporting (except Natura 2000 protected sites).


```{include} tables/Protectedareas_EUinstruments_table
```



```{include} tables/ProtectedAreas_Spatialdata4thcycle_Table
```

({numref}`Figure1`) presents the class diagram for the proposed generic ProtectedArea dataset:

- Depending on the specific dataflow, different geometry types may be requested/allowed (either point, line or polygon).
- The relatedZoneIdentifier and relatedZoneIdentifierScheme are mandatory, and specific constraints will apply depending on the dataflow (i.e. on the type of protected area).
- The attribute confidentialityStatus was included (and applies to the drinking water protected areas) to address concerns about the publication of the location of some protected areas.
- The attributes sizeValue and sizeUom attributes are no longer requested.
- The attributes successorsIdentifier and successorsIdentifierScheme have been kept for clarity's sake although their value will always be NULL (the appropriate value will be derived and included in the
  published WISE datasets that refer to the previous reporting cycles).

*Figure 3. Class diagram for an abstract ProtectedArea dataset – 4ᵗʰ cycle of reporting.*

```{mermaid} /DataModelReview/mmd/ProtectedAreasDataset.mmd
:align: center
```

## Special case – the Natura2000 protected sites

The Natura2000 dataflows do not include information about the association between protected sites and WFD water bodies. Therefore, a different approach is necessary to simplify the WFD reporting.
A provisional prefilled list of "water-dependent" Natura 2000 protected sites will be created, based on the Natura2000 reporting based on the habitat type and species type [^2]

A Natura 2000 site should be designated as "water-dependent" if it contains Annex I habitat types or Annex II species (Habitats Directive),or bird species (Birds Directive),  whose presence was the primary reason for the area's designation and that meet the ecological criteria below:

- habitats consisting of surface water or occurring entirely within surface water as defined by the WFD
- habitats that depend on frequent inundation by surface water or specific groundwater levels
- aquatic species living directly in surface waters
- species with at least one aquatic life stage dependent on surface water for essential activities such as breeding, incubation, juvenile
  development, feeding, or roosting.

The provisional prefilled list will be provided to Member States, for validation purposes:

- If missing, additional Natura 2000 protected site identifiers may be added (from the reference list already reported under the Natura 2000 dataflows).
- If incorrect, Natura 2000 protected site identifiers present in the provisional list may be flagged for removal from the WFD register of protected areas.
- For the Natura 2000 sites to be included in the WFD register of protected areas (because where the maintenance or improvement of water status is a critical factor for their protection), the association to water bodies should be reported.

## Descriptive data reporting

Specific objectives may be set for some types of protected areas:

- Shellfish designated waters
- Drinking water protection areas
- Natura 2000 protected sites included in the WFD register of protected
  areas

For Freshwater fish designated waters, the WFD good ecological status fully integrates the integrate Fish Directive (2006/44/EC) objectives. Similarly, the WFD good status integrates the Nitrates Directive and UWWTD objectives related to eutrophication. Therefore, no information on specific objectives is requested or expected for these types of protected area or for bathing waters.

The data reported for the 3ʳᵈ cycle can be used to estimate the impact of the simplification:

- 46% of the 84560 records reported for groundwater associated protected areas would not have been reported.
- 72% of the 71726 records reported for surface water associated protected areas would not have been reported.

The analysis of the 3ʳᵈ cycle reveals that no specific objectives were set for Nationally Designated Areas (NatDA, formerly known as CDDA). Information about this type of protected sites will no longer be requested.

[def]: #purpose-and-overview
[def2]: #_Toc222336798
[^1]: Extracts from the “Clarification note in relation to the reporting of spatial data for Water Framework Directive (WFD) protected areas, in the context of the March 2016 reporting of the second River Basin Management Plans (RBMPs)” [http://cdr.eionet.europa.eu/help/WFD/WFD_521_2016/GISGuidance/Clarification%20note%20protected%20areas.pdf](http://cdr.eionet.europa.eu/help/WFD/WFD_521_2016/GISGuidance/Clarification%20note%20protected%20areas.pdf) See also the “Clarification note in relation to the reporting of spatial data for Water Framework Directive (WFD) protected areas, in the context of the March 2022 reporting of the third River Basin Management Plans (RBMPs) 28 April 2022” [https://cdr.eionet.europa.eu/help/WFD/WFD_780_2022/GISGuidance/PA_Clarification_Note.pdf](https://cdr.eionet.europa.eu/help/WFD/WFD_780_2022/GISGuidance/PA_Clarification_Note.pdf)
    
[^2]: See for example ({numref}`electronic_reporting`) in the document "Links between the Water Framework Directive (WFD 2000/60/EC) and Nature Directives (BirdsDirective 2009/147/EC and Habitats Directive 92/43/EEC)."[https://circabc.europa.eu/ui/group/3f466d71-92a7-49eb-9c63-6cb0fadf29dc/library/f214c3f5-bf5c-404a-a18b-02c0553b82ad/details](https://circabc.europa.eu/ui/group/3f466d71-92a7-49eb-9c63-6cb0fadf29dc/library/f214c3f5-bf5c-404a-a18b-02c0553b82ad/details?open=true)
