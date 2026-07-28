##### Field QCs

###### inspireIdLocalId

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V212
  - BLOCKER
  - The value must not be missing or empty. [V212]
* - V213
  - BLOCKER
  - The length of the value must be <= 254. [V213]
```

###### inspireIdNamespace

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V214
  - BLOCKER
  - The value must not be missing or empty. [V214]
* - V215
  - BLOCKER
  - The length of the value must be <= 254. [V215]
```

###### thematicIdIdentifier

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V250
  - BLOCKER
  - The value must not be missing or empty. [V250]
* - V251
  - BLOCKER
  - The value of thematicIdIdentifier must follow the syntax of WISE identifiers [V251]
* - RF215\_WFD
  - BLOCKER
  - thematicIdIdentifier must be a valid identifier in the register if the wiseEvolutionType value is 'deletion', 'noChange' or 'change' [RF215\_WFD]
* - RF215\_WISE5
  - BLOCKER
  - thematicIdIdentifier must be a valid identifier in the register if the wiseEvolutionType value is 'deletion', 'noChange' or 'change' [RF215\_WISE5]
* - RF216\_WFD
  - BLOCKER
  - thematicIdIdentifier must not exist in the register unless the wiseEvolutionType value is 'deletion', 'noChange', 'reactivation' or 'change' [RF216\_WFD]
* - RF216\_WISE
  - BLOCKER
  - thematicIdIdentifier must not exist in the register unless the wiseEvolutionType value is 'deletion', 'noChange', 'reactivation' or 'change' [RF216\_WISE]
* - RF217\_WFD
  - ERROR
  - The monitoring site is associated with waterbody in a different category (surface water versus groundwater) than the waterbody previously reported [RF217\_WFD]
* - RF217\_WISE5
  - ERROR
  - The monitoring site is associated with waterbody in a different category (surface water versus groundwater) than the waterbody previously reported [RF217\_WISE5]
```

###### thematicIdIdentifierScheme

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V252
  - BLOCKER
  - The value must not be missing or empty. [V252]
* - V253
  - BLOCKER
  - The value is not a valid member of the referenced list. [V253]
* - R220
  - BLOCKER
  - wiseEvolutionType='reactivation' is not valid if thematicIdIdentifierScheme not in ('euMonitoringSiteCode','eionetMonitoringSiteCode') [R220]
* - V264
  - BLOCKER
  - Invalid thematicIdIdentifierScheme value for this spatial object type. [V264]
* - V249
  - BLOCKER
  - An 'eu' thematic identifier must not be replaced by an 'eionet' thematic identifier [V249]
* - V267
  - BLOCKER
  - EIONET thematic identifiers must be used for all spatial objects. [V267]
* - V268
  - BLOCKER
  - WFD thematic identifiers must be used for all spatial objects. [V268]
* - R231
  - BLOCKER
  - wiseEvolutionType= 'reactivation' is not valid if thematicIdIdentifierScheme = 'eionetMonitoringSiteCode' and countryCode not in ('CH','LI','TR','AL','BA','ME','MK','RS','XK') [R231]
```

###### wiseEvolutionType

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V254
  - BLOCKER
  - The value must not be missing or empty. [V254]
* - V255
  - BLOCKER
  - The value is not a valid member of the referenced list. [V255]
* - R206
  - BLOCKER
  - inspireIdVersionId must be reported if wiseEvolutionType is 'change'. [R206]
* - V260
  - BLOCKER
  - These wiseEvolutionType values are no valid for monitoring sites: 'changeExtendedArea', 'changeExtendedAreaAndDepth', 'changeExtendedDepth', 'changeReducedArea', 'changeReducedAreaAndDepth', 'changeReducedDepth'. [V260]
* - R220
  - BLOCKER
  - wiseEvolutionType='reactivation' is not valid if thematicIdIdentifierScheme not in ('euMonitoringSiteCode','eionetMonitoringSiteCode') [R220]
* - R208
  - BLOCKER
  - operationalActivityPeriodEnd must be reported if wiseEvolutionType is 'deletion''. [R208]
* - V256
  - BLOCKER
  - Invalid wiseEvolutionType value for this spatial object type [V256]
* - R224
  - BLOCKER
  - A spatial object with wiseEvolutionType value equal to 'changeCode' must not have the same predecessor of another spatial object. [R224]
* - R219
  - WARNING
  - Monitoring site has been reactivated. [R219]
* - R202
  - ERROR
  - beginLifespanVersion must be reported unless wiseEvolutionType is 'creation' or 'noChange'. [R202]
* - R204
  - BLOCKER
  - The endLifespanVersion value must be reported, if the wiseEvolutionType is 'deletion'. [R204]
* - R222
  - BLOCKER
  - At least one predecessor of an object with wiseEvolutionType value equal to 'splitting' or 'changeBothAggregationAndSplitting' must be reported as predecessor of another spatial object. [R222]
* - R225
  - BLOCKER
  - The monitoring site must have zero predecessors if the wiseEvolutionType value is 'creation' [R225]
* - R226
  - BLOCKER
  - The monitoring site must have one and only one predecessor if the wiseEvolutionType value is 'changeCode' or 'splitting' [R226]
* - R227
  - BLOCKER
  - The monitoring site must have two or more predecessors if the wiseEvolutionType value is 'aggregation' [R227]
* - R231
  - BLOCKER
  - wiseEvolutionType= 'reactivation' is not valid if thematicIdIdentifierScheme = 'eionetMonitoringSiteCode' and countryCode not in ('CH','LI','TR','AL','BA','ME','MK','RS','XK') [R231]
* - RF203\_WFD
  - BLOCKER
  - wiseEvolutionType='reactivation' is not valid if a former surface water monitoring site is now reactivated as a groundwater monitoring site, or vice-versa [RF203\_WFD]
* - RF203\_WISE5
  - BLOCKER
  - wiseEvolutionType='reactivation' is not valid if a former surface water monitoring site is now reactivated as a groundwater monitoring site, or vice-versa [RF203\_WISE5]
* - RF219\_WFD
  - BLOCKER
  - wiseEvolutionType='reactivation' is not valid if the object does not exist in the MonitoringSite register [RF219\_WFD]
* - RF219\_WISE5
  - BLOCKER
  - wiseEvolutionType='reactivation' is not valid if the object does not exist in the MonitoringSite register [RF219\_WISE5]
* - RF220\_WISE5
  - BLOCKER
  - wiseEvolutionType='reactivation' is not valid if the status of the object is 'valid' in the MonitoringSite register [RF220\_WISE5]
* - RF220\_WFD
  - BLOCKER
  - wiseEvolutionType='reactivation' is not valid if the status of the object is 'valid' in the MonitoringSite register [RF220\_WFD]
* - RF221\_WFD
  - BLOCKER
  - wiseEvolutionType='reactivation' is not valid if the status of the object is 'superseded' in the MonitoringSite register [RF221\_WFD]
* - RF221\_WISE5
  - BLOCKER
  - wiseEvolutionType='reactivation' is not valid if the status of the object is 'superseded' in the MonitoringSite register [RF221\_WISE5]
* - RF227\_WFD
  - ERROR
  - wiseEvolutionType='reactivation' is not a valid option if the featureOfInterestIdentifier is different to the previous one [RF227\_WFD]
* - RF227\_WISE5
  - ERROR
  - wiseEvolutionType='reactivation' is not a valid option if the featureOfInterestIdentifier is different to the previous one [RF227\_WISE5]
* - RF222\_WFD
  - BLOCKER
  - If an object is reported as 'deletion', it must have the same predecessors as before [RF222\_WFD]
* - RF222\_WISE5
  - BLOCKER
  - If an object is reported as 'deletion', it must have the same predecessors as before [RF222\_WISE5]
```

###### nameText

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V227
  - BLOCKER
  - The value must not be missing or empty. [V227]
* - V229
  - BLOCKER
  - The length of the value must be <= 254. [V229]
* - V228
  - BLOCKER
  - nameText contains invalid characters. [V228]
```

###### nameLanguage

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V225
  - BLOCKER
  - The value must not be missing or empty. [V225]
* - V226
  - BLOCKER
  - The value is not a valid member of the referenced list. [V226]
```

###### operationalActivityPeriodBegin

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V232
  - BLOCKER
  - The value must not be missing or empty. [V232]
* - V233
  - ERROR
  - operationalActivityPeriodBegin must not be set in the future. [V233]
* - V234
  - BLOCKER
  - operationalActivityPeriodBegin must contain a valid date (YYYY-MM-DD) [V234]
* - R207
  - BLOCKER
  - operationalActivityPeriodEnd must be greater than operationalActivityPeriodBegin. [R207]
* - RF204\_WFD
  - ERROR
  - operationalActivityPeriodBegin for the successor can not be the same as the operationalActivityPeriodBegin of the object being replaced, except if wiseEvolutionType is ‘changeCode ’[RF204\_WFD]
* - RF204\_WISE5
  - ERROR
  - operationalActivityPeriodBegin for the successor can not be the same as the operationalActivityPeriodBegin of the object being replaced, except if wiseEvolutionType is ‘changeCode’ [RF204\_WISE5]
* - RF205\_WISE5
  - ERROR
  - operationalActivityPeriodBegin value cannot be higher than the one stored in the registry for the same object if wiseEvolutionType value is equal to 'change', 'changeCode', 'noChange' or 'reactivation' [RF205\_WISE5]
* - RF205\_WFD
  - ERROR
  - operationalActivityPeriodBegin value cannot be higher than the one stored in the registry for the same object if wiseEvolutionType value is equal to 'change', 'changeCode', 'noChange' or 'reactivation' [RF205\_WFD]
```

###### featureOfInterestIdentifier

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V207
  - BLOCKER
  - The value must not be missing or empty. [V207]
* - V208
  - BLOCKER
  - The value of featureOfInterestIdentifier must follow the syntax of WISE identifiers [V208]
* - RF200\_WFD
  - BLOCKER
  - The monitoring site has a feature of interest (waterbody) that does not exist in the register [RF200\_WFD]
* - RF200\_WISE5
  - BLOCKER
  - The monitoring site has a feature of interest (waterbody) that does not exist in the register [RF200\_WISE5]
* - RF201\_WFD
  - BLOCKER
  - The featureOfInterestIdentifier is deprecated (only objects with wiseEvolutionType = 'deletion' can be have a deprecated featureOfInterest) [RF201\_WFD]
* - RF201\_WISE5
  - BLOCKER
  - The featureOfInterestIdentifier is deprecated (only objects with wiseEvolutionType = 'deletion' can be have a deprecated featureOfInterest) [RF201\_WISE5]
* - RF202\_WFD
  - ERROR
  - The Monitoring Site is for deletion and the featureOfInterestIdentifier is deprecated [RF202\_WFD]
* - RF202\_WISE5
  - ERROR
  - The Monitoring Site is for deletion and the featureOfInterestIdentifier is deprecated [RF202\_WISE5]
```

###### featureOfInterestIdentifierScheme

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V209
  - BLOCKER
  - The value must not be missing or empty. [V209]
* - V210
  - BLOCKER
  - The value is not a valid member of the referenced list. [V210]
* - V266
  - BLOCKER
  - Invalid featureOfInterestIdentifierScheme value for this spatial object type. [V266]
* - V271
  - BLOCKER
  - An EIONET thematic identifier must be used for all the spatial objects. [V271]
* - V272
  - BLOCKER
  - WFD thematic identifiers must be used for all spatial objects. [V272]
```

###### mediaMonitoredBiota

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V219
  - BLOCKER
  - The value must not be missing or empty. [V219]
* - V220
  - BLOCKER
  - The value is not a valid member of the referenced list. [V220]
```

###### mediaMonitoredWater

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V223
  - BLOCKER
  - The value must not be missing or empty. [V223]
* - V224
  - BLOCKER
  - The value is not a valid member of the referenced list. [V224]
```

###### mediaMonitoredSediment

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V221
  - BLOCKER
  - The value must not be missing or empty. [V221]
* - V222
  - BLOCKER
  - The value is not a valid member of the referenced list. [V222]
```

###### confidentialityStatus

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V204
  - BLOCKER
  - The value must not be missing or empty. [V204]
* - V205
  - BLOCKER
  - The value is not a valid member of the referenced list. [V205]
```

###### supersedesIdentifierScheme

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V245
  - BLOCKER
  - The value is not a valid member of the referenced list. [V245]
* - V247
  - BLOCKER
  - Invalid supersedesIdentifierScheme value for this spatial object type [V247]
* - V246
  - BLOCKER
  - WFD thematic identifiers must be used for all spatial objects [V246]
* - V269
  - BLOCKER
  - EIONET thematic identifiers must be used for all spatial objects. [V269]
* - R213
  - BLOCKER
  - supersedesIdentifierScheme must be reported if supersedesIdentifier is reported. [R213]
* - R211
  - BLOCKER
  - supersedesIdentifier must be reported if supersedesIdentifierScheme is reported. [R211]
```

###### supersededByIdentifierScheme

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V240
  - BLOCKER
  - The value is not a valid member of the referenced list. [V240]
* - V244
  - BLOCKER
  - An 'eu' thematic identifier must not be replaced by an 'eionet' thematic identifier [V244]
* - R232
  - BLOCKER
  - Reporting of supersededByIdentifierScheme & supersededByIdentifier is not allowed [R232]
```

###### purpose

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V236
  - BLOCKER
  - The value is not a valid member of the referenced list. [V236]
```

###### link

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V217
  - BLOCKER
  - The value does not follow the expected syntax for a valid URL. [V217]
* - V273
  - BLOCKER
  - The length of the value must be <= 2048 [V273]
```

###### beginLifespanVersion

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V201
  - BLOCKER
  - beginLifespanVersion must contain a valid date (YYYY-MM-DD). [V201]
* - V200
  - ERROR
  - beginLifespanVersion must not be set in the future. [V200]
* - R200
  - BLOCKER
  - beginLifespanVersion must be reported if endLifespanVersion is reported. [R200]
* - R201
  - BLOCKER
  - beginLifespanVersion must be reported if inspireIdVersionId is reported. [R201]
* - R202
  - ERROR
  - beginLifespanVersion must be reported unless wiseEvolutionType is 'creation' or 'noChange'. [R202]
* - R203
  - BLOCKER
  - endLifespanVersion must be greater than beginLifespanVersion. [R203]
```

###### endLifespanVersion

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V206
  - BLOCKER
  - endLifespanVersion must contain a valid date (YYYY-MM-DD). [V206]
* - R200
  - BLOCKER
  - beginLifespanVersion must be reported if endLifespanVersion is reported. [R200]
* - R203
  - BLOCKER
  - endLifespanVersion must be greater than beginLifespanVersion. [R203]
* - R204
  - BLOCKER
  - The endLifespanVersion value must be reported, if the wiseEvolutionType is 'deletion'. [R204]
```

###### inspireIdVersionId

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - R206
  - BLOCKER
  - inspireIdVersionId must be reported if wiseEvolutionType is 'change'. [R206]
* - V216
  - BLOCKER
  - The length of the value must be <= 25. [V216]
* - R201
  - BLOCKER
  - beginLifespanVersion must be reported if inspireIdVersionId is reported. [R201]
```

###### nameTextInternational

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V230
  - BLOCKER
  - The length of the value must be <= 254. [V230]
* - V231
  - BLOCKER
  - Only text with upper case letters (A to Z) and digits (0 to 9) is allowed. Spaces and hiphens can be used as separators. [V231]
* - V202
  - BLOCKER
  - The value must not be missing or empty [V202]
```

###### operationalActivityPeriodEnd

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V235
  - BLOCKER
  - operationalActivityPeriodEnd must contain a valid date (YYYY-MM-DD) [V235]
* - R208
  - BLOCKER
  - operationalActivityPeriodEnd must be reported if wiseEvolutionType is 'deletion''. [R208]
* - R207
  - BLOCKER
  - operationalActivityPeriodEnd must be greater than operationalActivityPeriodBegin. [R207]
```

###### supersedesIdentifier

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - R233
  - BLOCKER
  - The monitoring site must have zero predecessors if the wiseEvolutionType value is 'change' or 'noChange' [R233]
* - R212
  - BLOCKER
  - supersedesIdentifier and supersedesIdentifierScheme combination must not be equal to thematicIdentifier and thematicIdentifierScheme combination (an identifier must not replace itself). [R212]
* - V265
  - BLOCKER
  - The value of supersedesIdentifier must follow the syntax of one WISE identifiers or a comma-separated list of WISE identifiers. [V265]
* - R213
  - BLOCKER
  - supersedesIdentifierScheme must be reported if supersedesIdentifier is reported. [R213]
* - R211
  - BLOCKER
  - supersedesIdentifier must be reported if supersedesIdentifierScheme is reported. [R211]
* - RF212\_WFD
  - BLOCKER
  - The monitoring site has a predecessor in a different category of waterbody (surface water versus groundwater) [RF212\_WFD]
* - RF212\_WISE5
  - BLOCKER
  - The monitoring site has a predecessor in a different category of waterbody (surface water versus groundwater) [RF212\_WISE5]
* - RF213\_WFD
  - ERROR
  - The monitoring site has a predecessor in a different category of surface water body [RF213\_WFD]
* - RF213\_WISE5
  - ERROR
  - The monitoring site has a predecessor in a different category of surface water body [RF213\_WISE5]
* - RF214\_WFD
  - ERROR
  - The monitoring site has a predecessor in a different water body [RF214\_WFD]
* - RF214\_WISE5
  - ERROR
  - The monitoring site has a predecessor in a different water body [RF214\_WISE5]
* - RF223\_WFD
  - BLOCKER
  - The object has a predecessor that does not exist in the register. [RF223\_WFD]
* - RF222\_WFD
  - BLOCKER
  - If an object is reported as 'deletion', it must have the same predecessors as before [RF222\_WFD]
* - RF222\_WISE5
  - BLOCKER
  - If an object is reported as 'deletion', it must have the same predecessors as before [RF222\_WISE5]
```

###### thematicIdentifier

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - R212
  - BLOCKER
  - supersedesIdentifier and supersedesIdentifierScheme combination must not be equal to thematicIdentifier and thematicIdentifierScheme combination (an identifier must not replace itself). [R212]
```

###### wiseEvolution

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - R228
  - BLOCKER
  - If an identifier is the predecessor of two or more objects, then those objects must have wiseEvolution equal to 'splitting' or 'changeBothAggregationAndSplitting' [R228]
```

###### supersededByIdentifier

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - R232
  - BLOCKER
  - Reporting of supersededByIdentifierScheme & supersededByIdentifier is not allowed [R232]
* - V007
  - BLOCKER
  - The length of the value must be <= 500 [V007]
```

###### geometry_point

```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - S203
  - BLOCKER
  - The geometry must not be empty or degenerate (e.g. zero-lenth line or zero-area polygon). [S203]
* - S206
  - BLOCKER
  - The coordinate reference system (CRS) is not valid. (It must be one of the following:ETRS89-GRS80 (urn:ogc:def:crs:EPSG::4258),ETRS89-LAEA
* - S205
  - ERROR
  - The geometry must not have anomalous geometric points, such as self-intersections [S205]
* - S201\_WFD
  - ERROR
  - geometry\_point must be covered by or be within 200 metres of the geometry of the associated water body [S201\_WFD]
* - S201\_WISE5
  - ERROR
  - geometry\_point must be covered by or be within 200 metres of the geometry of the associated water body [S201\_WISE5]
* - S202\_WFD
  - ERROR
  - The position of the element has changed in more than 10 km. [S202\_WFD]
* - S202\_WISE5
  - ERROR
  - The position of the element has changed in more than 10 km. [S202\_WISE5]
* - FC121
  - BLOCKER
  - The value must not be missing or empty
* - FT122
  - BLOCKER
  - The value does not follow the expected syntax for a valid multipoint {%reason%}
* - FT123
  - BLOCKER
  - Unsupported SRID
* - FT124
  - BLOCKER
  - Geometry is not valid. Reason: {%reason%}
```
