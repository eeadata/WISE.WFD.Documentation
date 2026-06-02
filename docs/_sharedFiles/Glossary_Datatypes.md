# Glossary of datatypes

```{glossary}
:sorted: true

wiseIdentifier
    String with a maximum of 42 characters.
    WISE identifiers must start with the two-letter country code, followed by one character that can be a digit or an uppercase letter, followed by a sequence of characters (0 to 38 characters long) that can be digits or uppercase letters, with no consecutive double hyphens or double underscores, but allowing for single hyphens or underscores between characters.  
    The code can optionally end with one character that can be a digit or an uppercase letter.  
    Examples: FR123, FR1_XYZ1234_1, FR1-XYZ1234-1, FR1XYZ12341 but not FR1__XYZ1234__1 or FRa123. 

Language
    Value from the `Language` controlled lists of values.  
    
URL
    String with a maximum of 2100 characters.
```


https://semiceu.github.io/style-guide/1.0.0/gc-conceptual-model-conventions.html