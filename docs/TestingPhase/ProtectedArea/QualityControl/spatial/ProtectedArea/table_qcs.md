##### Table QCs

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - TU001
  - BLOCKER
  - Mandatory table has no records [TU001]
* - TU003
  - BLOCKER
  - The thematicIdIdentifier and thematicIdIdentifierScheme combination must be unique for any ProtectedArea [TU003]
* - TU002
  - BLOCKER
  - The inspireIdLocalId and inspireIdNamespace combination must be unique for each object. [TU002]
* - R029
  - BLOCKER
  - If an identifier is the predecessor of 2 or more objects, then those objects must have wiseEvolution in ('splitting','changeBothAggregationAndSplitting') [R029]
* - RF005
  - BLOCKER
  - If an object is reported as 'deletion', it must have the same predecessors as before [RF005]
* - R017
  - BLOCKER
  - An 'eu' thematic identifier must not be replaced by an 'eionet' thematic identifier. [R017]
* - S014
  - WARNING
  - The geometry of the protected areas must be covered by or be within 200 metre of the geometry of the associated water body.[S014]
* - RF007
  - BLOCKER
  - The object has a predecessor with a different zone type.[RF007]
* - RF001
  - BLOCKER
  - A valid 'eu' thematic identifier exists in the register but was not reported in the spatial file (either as a spatial object or as a predecessor).[RF001] Number of missing identifiers: {%NUMBEROFRECORDS%}. Missing identifiers: {%IDENTIFIERS%}
* - R031
  - BLOCKER
  - The spatial object reported as predecessor, cannot be reported again..[R031]
* - S015
  - ERROR
  - The position of the element has changed in more than 10 km. [S015]
* - S005
  - BLOCKER
  - The coordinate reference system (CRS) is not valid. (It must be one of the following:ETRS89-GRS80 (urn:ogc:def:crs:EPSG::4258),ETRS89-LAEA [S005]
* - S006
  - ERROR
  - The geometry must not have anomalous geometric points, such as self-intersections [S006]
* - R048
  - BLOCKER
  - The geometry must not be missing or empty. [R048]
* - S018
  - BLOCKER
  - ProtectedArea geometries use more than one CRS : {%srid\_list%} [S018]
* - XC002
  - BLOCKER
  - More than one geometry type detected in the same record. [XC001]
* - S019
  - ERROR
  - The geometry of the protected areas must not be disjoint of the geometry of the surface water body's river basin district (except for coastal and territorial waters).[S019]
```
