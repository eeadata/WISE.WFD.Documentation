(glossary-datatypes)=
# Attribute types (datatypes)

## Glossary

```{glossary}
:sorted: true

wiseIdentifier
    String with a maximum of 42 characters. A WISE identifier: 

    * must start with the ISO 3166-1 alpha-2 country code, 
    except for Greece ('EL') and the United Kingdom ('UK')
    * must use only upper case letters [A to Z] and digits [0 to 9]
    * may use the underscore character ('_') or the hyphen character ('-') 
    as separator characters within the identifier 
    (but not immediately after the country code, and not at the end of the code)
    * must not have consecutive separator characters 
    * be unique at national level, within the context to which they apply

    Valid examples: FR123, FR1_XYZ1234_1, FR1-XYZ1234-1, FR1XYZ12341.  
    *Invalid* examples: FR1__XYZ1234__1, FRa123, FR123_. 

documentCode
    Character string following the {term}`wiseIdentifier` syntax 
    that uniquely identifies a document provided in a data delivery.

referenceCode
    Character string following the {term}`wiseIdentifier` syntax 
    that uniquely identifies a document reference 
    (e.g. a chapter, bookmark, page, etc.) 
    within a document provided in a data delivery.

string
    Character string. A maximum of 4000 characters is allowed, 
    unless otherwise specified by indicating the number of characters. 
    UTF8 encoding is mandatory.

gYear
    Gregorian year.

nonNegativeValue
    Non-negative numeric value.

date
    Date in the format yyyy-mm-dd.

range
    Range of values. The data type follows the Postgre range type implementation 
    of the ISO 80000-2:2019(E) standard.
    {footcite}`postgresql-rangetypes`
    {footcite}`iso80000-2-2019`

Email
    Character string with a maximum length of 250 characters. 
    Validate using REGEX pattern.

URL
    Character string with a maximum of 2100 characters. 
    Validate using REGEX pattern.

Attachment
    File (typically a PDF) uploaded directly in Reportnet3.

geometry
    A geometry object represents points, curves, and surfaces in coordinate space. 
    {footcite}`GeoJSON`

point
    A {term}`geometry` object representin a bidimensional location in space. 
    {footcite}`GeoJSON`

AquiferMediaTypeValue
    Value from the `AquiferMediaTypeValue` controlled list of values. 

AssessmentMethod
    Value from the `AssessmentMethod` controlled list of values.

AssessmentConfidence
    Value from the `AssessmentConfidence` controlled list of values.

BiologicalQualityElement
    Value from the `BiologicalQualityElement` controlled list of values, 
    which is a subset of the {term}`QualityElement` controlled list of values.

ChemicalMatrixType
    Value from the `ChemicalMatrixType` controlled list of values.

ChemicalPurpose
    Value from the `ChemicalPurpose` controlled list of values.

ChemicalStatus
    Value from the `ChemicalStatus` controlled list of values.

ClassificationSystem  
    Value from the `ClassificationSystem` controlled list of values. 
    See https://dd.eionet.europa.eu/vocabulary/wise/ClassificationSystem

ConfidentialityStatus
    Value from the `ConfidentialityStatus` controlled list of values. 
    {footcite}`sdmxclconfstatus2014`
    {footcite}`sdmxconfidentialityguideline2018`

Country
    Value from the `Country` controlled list of values.

EcologicalStatus
    Value from the `EcologicalStatus` controlled list of values.

EnvironmentalQualityStandard
    Value from the `EnvironmentalQualityStandard` controlled list of values. 

ExemptionPeriod
    Value from the `ExemptionPeriod` controlled list of values.

ExemptionRationale
    Value from the `ExemptionRationale` controlled list of values.

ExemptionType
    Value from the `ExemptionType` controlled list of values.

GroundwaterSurfaceWaterLink
    Value from the `GroundwaterSurfaceWaterLink` controlled list of values.

IdentifierScheme
    Value from the `IdentifierScheme` controlled list of values.

ImpactType
    Value from the `ImpactType` controlled list of values.

IntercalibrationType
    Value from the `IntercalibrationType` controlled list of values.

Language
    Value from the `Language` controlled list of values.  
    WISE dataflows use a subset of the ISO 639-2 alpha-3 code 
    for the representation of names of languages {footcite}`iso639-2`

Licence
    Value from the `Licence` controlled list of values.  
    Because all WFD datasets fall under the HVD regulation 
    {footcite}`hvdRegulation`, the `Licence` options are:

    |notation|label|
    |---|---|
    |`'CC0'`|http://publications.europa.eu/resource/authority/licence/CC0|
    |`'CC_BY_4_0'`|http://publications.europa.eu/resource/authority/licence/CC_BY_4_0|
    |`'exactMatch_CC_BY_4_0'`|skos:exactMatch http://publications.europa.eu/resource/authority/licence/CC_BY_4_0|
    |`'narrowMatch_CC_BY_4_0'`|skos:narrowMatch http://publications.europa.eu/resource/authority/licence/CC_BY_4_0|

LithologyValue
    Value from the `LithologyValue` controlled list of values. *To be defined*. 

MitigationMeasure
    Value from the `MitigationMeasure` controlled list of values.  

MixingZoneMeasure
    Value from the `MixingZoneMeasure` controlled list of values.  

MonitoringFrequency
    Value from the `MonitoringFrequency` controlled list of values.  

MonitoringCycle
    Value from the `MonitoringCycle` controlled list of values.  

NaturalAWBHMWB
    Value from the `NaturalAWBHMWB` controlled list of values.  

ObservationStatus
    Value from the `ObservationStatus` controlled list of values. 

Parameter
    Value from the `Parameter` controlled list of values. 
    Depending of the scope in which it is being used, 
    the subset of allowed values may be restricted by the quality control.

Percentage
    Integer value in the interval [0,100].

PercentageInterval
    Value from the `PercentageInterval` controlled list of values.  

PressureAssessmentMethod
    Value from the `PressureAssessmentMethod` controlled list of values. 

PressureType
    Value from the `PressureType` controlled list of values.  
    This is a hierarchical list.

QualityElement
    Value from the `QualityElement` controlled list of values, 
    which is a subset of the {term}`Parameter` controlled list of values.

QuantitativeStatus
    Value from the `QuantitativeStatus` controlled list of values. 

ReasonForFailure 
    Value from the `ReasonForFailure` controlled list of values. 

ReservoirType
    Value from the `ReservoirType` controlled list of values. 

Role
    Value from the `Role` controlled list of values. 

UnitOfMeasure
    Value from the `UnitOfMeasure` controlled list of values. 

VolumeRevenueCost
    Value from the `VolumeRevenueCost` controlled list of values.

WaterBodyCategory
    Value from the `WaterBodyCategory` controlled list of values.

WFDWaterService
    Value from the `WFDWaterService` controlled list of values.

WFDMonitoringPurpose
    Value from the `WFDMonitoringPurpose` controlled list of values.

WiseEvolutionType
    Value from the `WiseEvolutionType` controlled list of values.

WisePurposeOfCollectionValue
    Value from the `WisePurposeOfCollectionValue` controlled list of values.

YesNo
    Value from the `YesNo` controlled list of values.  

YesNoNotApplicable
    Value from the `YesNoNotApplicable` controlled list of values.  

YesNoRBMP
    Value from the `YesNoRBMP` controlled list of values. 

YesNoUnknownInapplicable
    Value from the `YesNoNotApplicable` controlled list of values.

YesNoUnknownNotApplicableNotAssessed
    Value from the `YesNoUnknownNotApplicableNotAssessed` controlled list of values.

YesNoUnknownNotAssessed
    Value from the `YesNoUnknownNotAssessed` controlled list of values.  

```

## References

```{footbibliography}
```
