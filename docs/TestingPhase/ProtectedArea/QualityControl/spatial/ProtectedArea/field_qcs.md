##### Field QCs

###### thematicIdIdentifier
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V024
  - BLOCKER
  - The value must not be missing or empty [V024]
* - V005
  - BLOCKER
  - The thematicIdIdentifier value must be a string starting with the 2-letter country code. Upper case letters (A to Z) and digits (0 to 9) are allowed in the remaining part (the hifen and the underscore can be used as non-consecutive separators) [V005]
* - RF021
  - BLOCKER
  - A thematic identifier cannot be equal to an existing thematic identifier for a different type of ProtectedArea. [RF021]
* - RF022
  - BLOCKER
  - A ProtectedArea thematicIdIdentifier can not be the same as the thematicIdIdentifier of a waterbody. [RF022]
```

###### legalBasisLink
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V012
  - BLOCKER
  - The legalBasisLink value must be a valid URL [V012]
* - V064
  - BLOCKER
  - The legalBasisLink value must be an URL with less than 255 characters [V064]
* - V035
  - BLOCKER
  - The value must not be missing or empty [V035]
```

###### link
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V014
  - BLOCKER
  - The link value must be a valid URL. [V014]
* - V043
  - BLOCKER
  - The link value must be an URL with less than 255 characters [V043]
```

###### thematicIdIdentifierScheme
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V052
  - BLOCKER
  - WFD thematic identifiers must be used for all spatial objects [V052]
* - V016
  - BLOCKER
  - The value must not be missing or empty [V016]
* - V032
  - BLOCKER
  - The thematicIdIdentifierScheme value is not valid (see http://dd.eionet.europa.eu/vocabulary/wise/IdentifierScheme).[V032]
* - R038
  - BLOCKER
  - A spatial object with an 'eu' thematicIdIdentifierScheme must be associated with a related zone with an 'eu' relatedZoneIdentifierScheme. [R038]
```

###### predecessorsIdentifierScheme
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V053
  - BLOCKER
  - WFD thematic identifiers must be used for all spatial objects [V053]
* - R014
  - BLOCKER
  - The predecessorsIdentifier value must be reported, if the predecessorsIdentifierScheme value is reported.[R014]
* - R016
  - BLOCKER
  - The predecessorsIdentifierScheme value must be reported, if the predecessorsIdentifier value is reported.[R016]
* - R015
  - BLOCKER
  - The predecessorsIdentifier and predecessorsIdentifierScheme combination must not be equal to the thematicIdentifier and thematicIdentifierScheme combination (an identifier must not replace itself).[R015]
* - V044
  - BLOCKER
  - The predecessorsIdentifierScheme value is not valid (see http://dd.eionet.europa.eu/vocabulary/wise/IdentifierScheme).[V044]
```

###### relatedZoneIdentifierScheme
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V055
  - BLOCKER
  - WFD thematic identifiers must be used for all spatial objects [V055]
* - V030
  - BLOCKER
  - The relatedZoneIdentifierScheme value is not valid (see http://dd.eionet.europa.eu/vocabulary/wise/IdentifierScheme).[V030]
* - R038
  - BLOCKER
  - A spatial object with an 'eu' thematicIdIdentifierScheme must be associated with a related zone with an 'eu' relatedZoneIdentifierScheme. [R038]
* - R043
  - BLOCKER
  - The relatedZoneIdentifier value must be reported, if the relatedZoneIdentifierScheme value is reported.[R043]
* - R044
  - BLOCKER
  - The relatedZoneIdentifierScheme value must be reported, if the relatedZoneIdentifier value is reported.[R044]
* - R045
  - BLOCKER
  - relatedZoneIdentifier is mandatory. [R045]
* - FC141
  - BLOCKER
  - The value must not be missing or empty
```

###### predecessorsIdentifier
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - RF008
  - BLOCKER
  - The object has a predecessor that does not exist in the register [RF008]
* - R014
  - BLOCKER
  - The predecessorsIdentifier value must be reported, if the predecessorsIdentifierScheme value is reported.[R014]
* - R016
  - BLOCKER
  - The predecessorsIdentifierScheme value must be reported, if the predecessorsIdentifier value is reported.[R016]
* - R015
  - BLOCKER
  - The predecessorsIdentifier and predecessorsIdentifierScheme combination must not be equal to the thematicIdentifier and thematicIdentifierScheme combination (an identifier must not replace itself).[R015]
* - V071
  - BLOCKER
  - The predecessorIdIdentifier value must be a string with less than 501 characters. [V071]
* - V040
  - BLOCKER
  - The value does not match the pattern to be used for a WISE Identifier. Several identifiers can be reported separated by comma. [V040]
```

###### inspireIdLocalId
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V002
  - BLOCKER
  - The inspireIdLocalId value must be a non-empty string with less than 255 characters [V002]
* - V015
  - BLOCKER
  - The value must not be missing or empty [V015]
```

###### inspireIdVersionId
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V004
  - BLOCKER
  - If present, the inspireIdVersionId value must be less than 25 characters [V004]
* - R002
  - BLOCKER
  - The beginLifespanVersion value must be reported, if the inspireVersionId value is reported. [R002]
* - R022
  - WARNING
  - The inspireIdVersionId value must be reported, if the wiseEvolutionType value is 'change'.[R022]
```

###### nameTextInternational
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V007
  - BLOCKER
  - The nameTextInternational value must be a non-empty string with less than 255 characters. Upper case letters (A to Z) and digits (0 to 9) are allowed (spaces and hifens can be used as separators) [V007]
* - V023
  - BLOCKER
  - The value must not be missing or empty [V023]
```

###### nameText
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V008
  - BLOCKER
  - The nameText value must be a string with less than 255 characters [V008]
* - V022
  - BLOCKER
  - The value must not be missing or empty [V022]
* - V001
  - ERROR
  - The used encoding is not correct. Strange characters in nameText field. [V001]
```

###### legalBasisName
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V011
  - BLOCKER
  - The legalBasisName value must be a string with less than 255 characters [V011]
* - V036
  - BLOCKER
  - The value must not be missing or empty [V036]
```

###### wiseEvolutionType
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - RF011
  - BLOCKER
  - A spatial object with wiseEvolutionType value equal to 'changeCode' must not have the same predecessor of another spatial object [RF011]
* - R032
  - BLOCKER
  - At least one predecessor of an object with wiseEvolutionType value equal to 'splitting' or 'changeBothAggregationAndSplitting' must be reported as predecessor of another spatial object [R032]
* - RF006
  - BLOCKER
  - A spatial object with wiseEvolutionType value equal to 'changeCode' must not have the same predecessor of another spatial object of the registry table.[RF006]
* - V017
  - BLOCKER
  - The value must not be missing or empty [V017]
* - V027
  - BLOCKER
  - The wiseEvolutionType value is not valid (see http://dd.eionet.europa.eu/vocabulary/wise/WiseEvolutionTypeValue).[V027]
* - R022
  - WARNING
  - The inspireIdVersionId value must be reported, if the wiseEvolutionType value is 'change'.[R022]
* - R023
  - BLOCKER
  - The thematic identifier must be a valid identifier in the register, if the wiseEvolutionType value is 'deletion', 'noChange' or 'change'.[R023]
* - RF004
  - BLOCKER
  - The thematic identifier must not exist in the register, unless the wiseEvolutionType value is 'deletion', 'noChange' or 'change'.[RF004]
* - R024
  - WARNING
  - The beginLifespanVersion value must be reported, unless the wiseEvolutionType is 'creation' or 'noChange'.[R024]
* - R025
  - WARNING
  - The endLifespanVersion value must be reported, if and only if the wiseEvolutionType is 'deletion'.[R025]
* - R011
  - BLOCKER
  - The object must have zero predecessors, if the wiseEvolutionType value is 'creation'.[R011]
* - R026
  - BLOCKER
  - The object must have one and only one predecessor, if the wiseEvolutionType value is 'changeCode' or 'splitting'.[R026]
* - R027
  - BLOCKER
  - The object must have two or more predecessors, if the wiseEvolutionType value is 'aggregation' or 'changeBothAggregationAndSplitting'.[R027]
* - R028
  - BLOCKER
  - The object must have zero predecessors, if the wiseEvolutionType value is 'change' or 'noChange'.[R028]
* - R030
  - BLOCKER
  - The designationPeriodEnd date must be reported, if and only if, the wiseEvolutionType value is 'deletion'.[R030]
* - RF012
  - BLOCKER
  - If wiseEvolutionType in ('deletion','change','noChange'), the designationPeriodBegin must be equal to the designationPeriodBegin of the object in the register.[RF012]
* - RF013
  - ERROR
  - If wiseEvolutionType in ('splitting','aggregation','changeBothAggregationAndSplitting','changeExtendedArea','changeExtendedDepth','changeExtendedAreaAndDepth','changeReducedArea','changeReducedDepth','changeReducedAreaAndDepth'), the designationPeriodBegin value must be higher than the designationPeriodBegin value of the predecessor.[RF013]
* - RF014
  - BLOCKER
  - If wiseEvolutionType = 'changeCode', the designationPeriodBegin value must be equal to the designationPeriodBegin value of the predecessor.[RF014]
* - V061
  - BLOCKER
  - Invalid wiseEvolutionType value for this spatial object type. [V061]
* - R046
  - ERROR
  - If wiseEvolutionType = 'deletion then the designationPeriodEnd value must not be after @today [R046]
* - R047
  - ERROR
  - If wiseEvolutionType in ('creation', 'splitting','aggregation','changeBothAggregationAndSplitting') then the designationPeriodBegin value must not be after @today. [R047]
* - S013
  - BLOCKER
  - The geometry must not be empty or degenerate (e.g. zero-lenth line or zero-area polygon), except if the wiseEvolutionType value is 'deletion' [S013]
```

###### relatedZoneIdentifier
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - RF009
  - BLOCKER
  - The object has an 'eu' related zone that does not exist in the register [RF009]
* - V042
  - BLOCKER
  - The relatedZoneIdentifier value must be a string starting with the 2-letter country code. Upper case letters (A to Z) and digits (0 to 9) are allowed in the remaining part (the hifen and the underscore can be used as non-consecutive separators) [V042]
* - RF017
  - BLOCKER
  - The relatedZoneIdentifier is deprecated.[RF017]
* - R043
  - BLOCKER
  - The relatedZoneIdentifier value must be reported, if the relatedZoneIdentifierScheme value is reported.[R043]
* - R044
  - BLOCKER
  - The relatedZoneIdentifierScheme value must be reported, if the relatedZoneIdentifier value is reported.[R044]
* - R045
  - BLOCKER
  - relatedZoneIdentifier is mandatory. [R045]
* - FC140
  - ERROR
  - The value must not be missing or empty
```

###### zoneType
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V020
  - BLOCKER
  - The value must not be missing or empty [V020]
* - V029
  - BLOCKER
  - The value is not a valid member of the referenced list. [V029]
```

###### inspireIdNamespace
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V019
  - BLOCKER
  - The value must not be missing or empty [V019]
* - V003
  - BLOCKER
  - The inspireIdNamespace value must be a string with less than 255 characters [V003]
```

###### nameLanguage
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V018
  - BLOCKER
  - The value must not be missing or empty [V018]
* - V028
  - BLOCKER
  - The nameLanguage value is not a valid ISO 639-2/B language code [V028]
```

###### designationPeriodBegin
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V021
  - BLOCKER
  - The value must not be missing or empty [V021]
* - R004
  - BLOCKER
  - The designationPeriodBegin date must not be after the designationPeriodEnd.[R004]
* - RF012
  - BLOCKER
  - If wiseEvolutionType in ('deletion','change','noChange'), the designationPeriodBegin must be equal to the designationPeriodBegin of the object in the register.[RF012]
* - RF013
  - ERROR
  - If wiseEvolutionType in ('splitting','aggregation','changeBothAggregationAndSplitting','changeExtendedArea','changeExtendedDepth','changeExtendedAreaAndDepth','changeReducedArea','changeReducedDepth','changeReducedAreaAndDepth'), the designationPeriodBegin value must be higher than the designationPeriodBegin value of the predecessor.[RF013]
* - RF014
  - BLOCKER
  - If wiseEvolutionType = 'changeCode', the designationPeriodBegin value must be equal to the designationPeriodBegin value of the predecessor.[RF014]
* - R035
  - BLOCKER
  - Objects with the same predecessor must have the same designationPeriodBegin value: {%RECORDS%}. [R035]
* - R047
  - ERROR
  - If wiseEvolutionType in ('creation', 'splitting','aggregation','changeBothAggregationAndSplitting') then the designationPeriodBegin value must not be after @today. [R047]
* - V067
  - BLOCKER
  - The date must have the format YYYY-MM-dd [V067]
```

###### beginLifespanVersion
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - R002
  - BLOCKER
  - The beginLifespanVersion value must be reported, if the inspireVersionId value is reported. [R002]
* - R013
  - BLOCKER
  - The beginLifespanVersion value must be reported, if the endLifespanVersion value is reported [R013]
* - R003
  - BLOCKER
  - The beginLifespanVersion date must not be after the endLifespanVersion.[R003]
* - R024
  - WARNING
  - The beginLifespanVersion value must be reported, unless the wiseEvolutionType is 'creation' or 'noChange'.[R024]
* - V069
  - BLOCKER
  - The date must have the format YYYY-MM-dd [V069]
```

###### endLifespanVersion
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - R013
  - BLOCKER
  - The beginLifespanVersion value must be reported, if the endLifespanVersion value is reported [R013]
* - R003
  - BLOCKER
  - The beginLifespanVersion date must not be after the endLifespanVersion.[R003]
* - R025
  - WARNING
  - The endLifespanVersion value must be reported, if and only if the wiseEvolutionType is 'deletion'.[R025]
* - V070
  - BLOCKER
  - The date must have the format YYYY-MM-dd [V070]
```

###### designationPeriodEnd
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - R004
  - BLOCKER
  - The designationPeriodBegin date must not be after the designationPeriodEnd.[R004]
* - R030
  - BLOCKER
  - The designationPeriodEnd date must be reported, if and only if, the wiseEvolutionType value is 'deletion'.[R030]
* - R046
  - ERROR
  - If wiseEvolutionType = 'deletion then the designationPeriodEnd value must not be after @today [R046]
* - V068
  - BLOCKER
  - The date must have the format YYYY-MM-dd [V068]
```

###### geometry_point
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - S010
  - BLOCKER
  - The value does not follow the expected syntax for a valid multipoint {%reason%} [S010]
* - S002
  - BLOCKER
  - Unsupported SRID [S002]
* - S011
  - BLOCKER
  - Geometry is not valid. Reason: {%reason%} [S011]
```

###### successorsIdentifier
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V065
  - BLOCKER
  - successorIdentifier must be empty [V065]
```

###### successorsIdentifierScheme
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V066
  - BLOCKER
  - successorIdentifierScheme must be empty [V066]
```

###### geometry_polygon
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - S017
  - BLOCKER
  - The value does not follow the expected syntax for a valid multipolygon {%reason%} [S017]
* - S016
  - BLOCKER
  - Unsupported SRID [S016]
* - S012
  - BLOCKER
  - Geometry is not valid. Reason: {%reason%} [S012]
```

###### geometry_line
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - S009
  - BLOCKER
  - The value does not follow the expected syntax for a valid multilinestring {%reason%} [S009]
* - S008
  - BLOCKER
  - Unsupported SRID [S008]
* - S007
  - BLOCKER
  - Geometry is not valid. Reason: {%reason%} [S007]
```

###### confidentialityStatus
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V072
  - BLOCKER
  - The value is not a valid member of the referenced list. [V072]
```

###### specialisedZoneType
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V073
  - BLOCKER
  - The value must not be missing or empty [V073]
* - V046
  - BLOCKER
  - The value is not a valid member of the referenced list.[V046]
```

###### legalBasisLevel
```{list-table}
:widths: 10 15 75
:header-rows: 1

* - Code
  - Severity
  - Description
* - V034
  - BLOCKER
  - The value must not be missing or empty [V034]
* - V033
  - BLOCKER
  - The value is not a valid member of the referenced list. [V033]
```
