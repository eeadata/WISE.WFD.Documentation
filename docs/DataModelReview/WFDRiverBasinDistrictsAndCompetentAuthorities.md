# WFD - River Basin Districts And Competent Authorities

Water Framework Directive – Electronic reporting data model review 
River Basin Districts & Competent Authorities 

**PROPOSAL - Version 2026.02.13** {download}`PDF <pdf/WFD_4rd_cycle_RiverBasinDistrictsAndCompetentAuthorities_v20260213.pdf>`

## Purpose and overview
The document revises the River Basin Districts, Subunits and Competent
Authorities classes used in the 3ʳᵈ cycle of reporting of the
Water Framework Directive River Basin Management Plans ({numref}`RBDSUCA_3rdCycle`), as
well as the associated spatial data in the RiverBasinDistrict dataset
and SubUnit dataset ({numref}`RBDSU_3rdCycle_Spatial`).


```{mermaid} /DataModelReview/mmd/RBDsubunitsAndCompetentAuthority.mmd
:name: RBDSUCA_3rdCycle
:caption: Class diagram for River Basin Districts, Subunits and Competent Authorities schema - 3ʳᵈ cycle
:align: center
:zoom:
```
Source: [https://cdr.eionet.europa.eu/help/WFD/WFD_715_2022/UML%20Data%20specification/WFD2022.EAP](https://cdr.eionet.europa.eu/help/WFD/WFD_715_2022/UML%20Data%20specification/WFD2022.EAP)


```{mermaid} /DataModelReview/mmd/RBDsubunitsClassdiagram.mmd
:name: RBDSU_3rdCycle_Spatial
:caption: Partial class diagram for RiverBasinDistrict and Subunit classes - 3ʳᵈ cycle
:align: center
:zoom:
```

Source: [https://cdr.eionet.europa.eu/help/WFD/WFD_715_2022/UML%20Data%20specification/WFD2022.EAP ](https://cdr.eionet.europa.eu/help/WFD/WFD_715_2022/UML%20Data%20specification/WFD2022.EAP )

A proposal is presented for the electronic reporting in the 4ᵗʰ cycle (Figure 3).
The reporting of the units of management (i.e. the River Basin Districts) and of the competent authorities is combined into a single dataflow. The overall structure of the new **River Basin Districts and Competent Authorities** dataflow has been aligned with similar dataflows, e.g. under the Floods Directive [^floods-directive-footnote].

[^floods-directive-footnote]: See Floods Directive - Units of Management and Competent Authorities[2025] at https://reportnet.europa.eu/public/dataflow/1473

Reporting is only requested under the following conditions:

- If there are changes to the spatial delineation and/or the identifiers of one or more River Basin Districts (since the 3ʳᵈ cycle), the spatial dataset must be reported.

- If there are changes to the competent authorities or their roles, the descriptive data must be reported in accordance with Article 3(8) and 3(9) of the WFD.

Data providers can specify which datasets are being updated (spatial data, descriptive data, or both). Information about subunits is no longer requested. The reporting of metadata has also been simplified.



```{mermaid} /DataModelReview/mmd/RBDCA4thCycle.mmd
:name: RBDCA_4thCycle_Documents 
:caption:  River Basin Districts and Competent Authorities - 4ᵗʰ cycle - Documents
:align: center
:zoom:
```

```{mermaid} /DataModelReview/mmd/RBDdescriptiveData.mmd
:name: RBDCA_4thCycle_Descriptive
:caption:  River Basin Districts and Competent Authorities - 4ᵗʰ cycle - Descriptive Data
:align: center
:zoom:

```

```{mermaid} /DataModelReview/mmd/RBD.mmd
:name: RBDCA_4thCycle_Spatial
:caption:  River Basin Districts and Competent Authorities - 4ᵗʰ cycle - Spatial Data
:align: center
:zoom:
```

## Documents dataset - 4ᵗʰ cycle

The Documents dataset ({numref}`RBDCA_4thCycle_Documents`) follows the standard structure used in various WISE dataflows:

- The **dcMetadata** table is required and contains only one record per delivery (i.e. per country). It provides the basic Dublin Core metadata elements about the delivery.<br/>It also functions as a "manifest file" explaining if the delivery contains an update of the spatial data (updateSpatialData = 'Yes') and/or of the competent authorities (updateCompetentAuthorities= 'Yes'). If required by the data providers, and especially if spatial data is being reported, the licenseDocument and the metadataDocument attributes allow the provision of additional information.

- The structure of the **Document** table is standard in the WISE dataflows: it allows the upload of documents (for example, PDFs) or the provision of a link to a document stored in a publicly accessible national web site.


## Descriptive dataset - 4ᵗʰ cycle

The Descriptive dataset ({numref}`RBDCA_4thCycle_Descriptive`) contains two tables:

- The **CompetentAuthority** table contains basic information about each Competent Authority.

- The **RiverBasinDistrictCompetentAuthority** table associates each Competent Authority with a River Basin District and specifies the role(s) of the competent authority in that specific RBD.


## Spatial dataset - 4ᵗʰ cycle

The Spatial dataset ({numref}`RBDCA_4thCycle_Spatial`)  contains only the RiverBasinDistrict spatial table.
As stated before, Subunits are no longer requested in the 4ᵗʰ cycle of reporting.

The following changes have been made to the RiverBasinDistrict table (in comparison to version 7.06 used in the 3ʳᵈ cycle of reporting):

- Two attributes were removed, because they can be derived: sizeValue and sizeUom.

- Two attributes were removed, since they are not required at EU level: relatedTransboundaryIdentifier and relatedTransboundaryIdentifierScheme.

- The date values are now requested as simply as YYYY-MM-DD, because that is the format used by the data providers (beginLifespanVersion, endLifespanVersion, designationPeriodBegin, designationPeriodEnd).

- One attribute was moved from the descriptive data into the spatial data specialisedZoneType: {'internationalRiverBasinDistrict','nationalRiverBasinDistrict'}

- The attributes thematicIdIdentifierScheme and zoneType have been kept for clarity's sake, although all records in the national delivery will have the same fixed value.

- Likewise, the attributes successorsIdentifier and successorsIdentifierScheme have been kept for clarity's sake although their value will always be NULL - the appropriate value will be derived and included in the published WISE datasets that refer to the previous reporting cycles.
