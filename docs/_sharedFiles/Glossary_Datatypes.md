# Glossary of datatypes

```{glossary}
:sorted: true

wiseIdentifier
    String with a maximum of 42 characters.
    WISE identifiers must start with the two-letter country code, followed by one character that can be a digit or an uppercase letter, followed by a sequence of characters (0 to 38 characters long) that can be digits or uppercase letters, with no consecutive double hyphens or double underscores, but allowing for single hyphens or underscores between characters.  The code can optionally end with one character that can be a digit or an uppercase letter.  Examples: FR123, FR1_XYZ1234_1, FR1-XYZ1234-1, FR1XYZ12341 but not FR1__XYZ1234__1 or FRa123. 

documentCode
    Character string following the {term}`wiseIdentifier` syntax that uniquely identifies a document provided in a data delivery.

referenceCode
    Character string following the {term}`wiseIdentifier` syntax that uniquely identifies a document reference (e.g. a chapter, bookmark, page, etc.) within a document provided in a data delivery.

string
    Character string. A maximum of 4000 characters is allowed, unless otherwise specified by indicating the number of characters. UTF8 encoding is mandatory.

gYear
    Gregorian year.

nonNegativeValue
    Non-negative numeric value.

date
    Date in the format yyyy-mm-dd.

Email
    Character string. Validate using REGEX pattern.

URL
    Character string with a maximum of 2100 characters. Validate using REGEX pattern.

Attachment
    File (typically a PDF) uploaded directly in Reportnet3.

AquiferMediaTypeValue
    Value from the `AquiferMediaTypeValue` controlled list of values. 

AssessmentMethod
    Value from the `AssessmentMethod` controlled list of values.

AssessmentConfidence
    Value from the `AssessmentConfidence` controlled list of values.

BiologicalQualityElement
    Value from the `BiologicalQualityElement` controlled list of values.

ExemptionPeriod
    Value from the `ExemptionPeriod` controlled list of values.

ExemptionRationale
    Value from the `ExemptionRationale` controlled list of values.

ExemptionType
    Value from the `ExemptionType` controlled list of values.

GroundwaterSurfacewaterLink
    Value from the `GroundwaterSurfacewaterLink` controlled list of values.

Language
    Value from the `Language` controlled list of values.  WISE dataflows use a subset of ISO 639-2, the alpha-3 code in Codes for the representation of names of languages-- Part 2. See https://www.loc.gov/standards/iso639-2/php/code_list.php

Licence
    Value from the `Licence` controlled list of values.  

MitigationMeasure
    Value from the `MitigationMeasure` controlled list of values.  

MixingZoneMeasure
    Value from the `MixingZoneMeasure` controlled list of values.  

PressureAssessmentMethod
    Value from the `PressureAssessmentMethod` controlled list of values. 

PressureType
    Value from the `PressureType` controlled list of values.  This is a hierarchical list.

ObservationStatus
    Value from the `ObservationStatus` controlled list of values. 

ReasonForFailure 
    Value from the `ReasonForFailure` controlled list of values. 

Role
    Value from the `Role` controlled list of values. 

SubstanceCode
    Value from the `SubstanceCode` controlled list of values.

UnitOfMeasure
    Value from the `UnitOfMeasure` controlled list of values. 

VolumeRevenueCost
    Value from the `VolumeRevenueCost` controlled list of values.

WFDWaterService
    Value from the `WFDWaterService` controlled list of values.

YesNo
    Value from the `YesNo` controlled list of values.  

YesNoNotApplicable
    Value from the `YesNoNotApplicable` controlled list of values.  

YesNoRBMP
    Value from the `YesNoRBMP` controlled list of values. 

YesNoUnknownInapplicable
    Value from the `YesNoNotApplicable` controlled list of values.

```


https://semiceu.github.io/style-guide/1.0.0/gc-conceptual-model-conventions.html