# Glossary of datatypes

```{glossary}
:sorted: true

wiseIdentifier
    String with a maximum of 42 characters.
    WISE identifiers must start with the two-letter country code, followed by one character that can be a digit or an uppercase letter, followed by a sequence of characters (0 to 38 characters long) that can be digits or uppercase letters, with no consecutive double hyphens or double underscores, but allowing for single hyphens or underscores between characters.  The code can optionally end with one character that can be a digit or an uppercase letter.  Examples: FR123, FR1_XYZ1234_1, FR1-XYZ1234-1, FR1XYZ12341 but not FR1__XYZ1234__1 or FRa123. 

documentCode
    Character string following the {term}`wiseIdentifier` syntax that uniquely identifies a document in a data delivery.

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

Language
    Value from the `Language` controlled list of values.  

Licence
    Value from the `Licence` controlled list of values.  

UnitOfMeasure
    Value from the `UnitOfMeasure` controlled list of values. 

ObservationStatus
    Value from the `ObservationStatus` controlled list of values. 

YesNo
    Value from the `YesNo` controlled list of values.  

YesNoNotApplicable
    Value from the `YesNoNotApplicable` controlled list of values.  

WFDWaterService
    Value from the `WFDWaterService` controlled list of values.

```


https://semiceu.github.io/style-guide/1.0.0/gc-conceptual-model-conventions.html