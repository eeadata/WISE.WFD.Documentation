(modelling-convetions)=
# Modelling conventions

## Classes and tables

In the UML class diagrams used in the documentation, a class represents:

* a data table that will contain reported data,
    or a {term}`reference table` that is used for quality control purposes
* a {term}`controlled list of values` or {term}`codelist`, represented as an «enumeration»

UML stereotype can be used to specialise some classes (if required for clarity).
Stereotype are denoted a their name in double angle brackets: «stereotype_name».

Note that the UML diagrams are *visual* depictions of the model.
Some classes, attributes, or associations may be omitted for clarity.

## Association multiplicity

```{list-table} WISE modelling conventions - association multiplicity
:name: wise_association_multiplicity_table
:header-rows: 1
:width: 100%
:widths: 25 75

* - Multiplicity
  - Definition

* - 1 
  - Each instance of the class at one end of the association *must* 
  be associated with exactly one instance of the class at the other end. 
  It enforces a strict one-to-one relationship.  
  See the diagram below: in practice, each row in TableA must 
  be associated with one and only one row in TableB.

* - 0..1 
  - Each instance of the class at one end of the association *may* 
  be associated with exactly one instance of the class at the other end. 
  It represents an optional relationship. 
  See the diagram below: in practice, each row in TableC *may* 
  be associated with one and only one row in TableD.

* - 1..n
  - See the diagram below: each row in TableF *must* 
  be associated with one or more rows in TableG.

* - n..m
  - Many-to-many associations between classes are normally depicted 
  in conceptual UML diagrams. 
  The class diagrams in this documentation, show the logical model 
  (for implementation in a relational database model). 
  Therefore, this type of associations is resolved using an {term}`association entity`,
  to resolve and enforce the many-to-many multiplicity.  
  See the diagram below: 
  each row in TableK *must* be associated with one or more rows in TableK_TableL,
  each row in TableL *must* be associated with one or more rows in TableK_TableL.
```

```{mermaid}
:name: UML_ClassDiagram_AssociationMultiplicity
:caption: UML Class diagram - association multiplicity
:align: center
---
config:
  class:
    hideEmptyMembersBox: true
  layout: dagre
  theme: neutral
---
classDiagram
direction LR
TableA "1" -- "1" TableB
TableC "1" -- "0..1" TableD
TableF "1" -- "1..n" TableG
TableK "1" -- "1..n" TableK_TableL
TableK_TableL "1..n" -- "1" TableL
```

## Attribute multiplicity

The multiplicity of an attribute specifies the number of values
that you can associate with that attribute.

```{list-table} WISE modelling conventions - attribute multiplicity
:name: wise_attribute_multiplicity_table
:header-rows: 1
:width: 100%
:widths: 25 75

* - {abbr}`m (multiplicity)`
  - Definition

* - `[1]` 
  - Means exactly one value.
  The documentation will describe the attribute as a {term}`required attribute`.

* - `[0..1]` 
  - Means zero or one value.  
  The documentation may describe the attribute as 
  an {term}`optional attribute`, or as a {term}`conditional attribute` 
  (if it a value is required under certain circunstances).

* - `[0..n]` 
  - Means zero, one or many values. 
  (The notation [0..*] has the same meaning, 
  but is not the preferred notation in the documentation.)  
  In specific cases, a range of values may be specified: 
  for example, [0..2] means 0, 1 or 2 values.  
  By definition, all values *must* by distinct.

* - `[1..n]` 
  - Means one or many values.
  (The notation [1..*] has the same meaning, 
  but is not the preferred notation in the documentation.) 
  In specific cases, a range of values may be specified: 
  for example, [1..2] means 1 or 2 values.  
  By definition, all values *must* by distinct.
```

In a normalised relational database, attributes with multiplicity
greater than one are not used:
the first normal form (1NF) requires atomic values in all attributes.

For reporting purposes, a fully normalised struture would be too complex.
Therefore, some multivalued attributes are allowed and used
as sparsely as possible in the data models.
The {term}`datatype` of such attributes is always:

* a value from a {term}`codelist`
* an unique {term}`identifier` with a clear {term}`identifier scheme`.

In the Reportnet3, a {term}`comma-separated list of values`
is used when report multivalued attributes.

## Departures from UML best practice

The UML diagrams in the documentation are meant to be illustrative,
and do not always strictly adhere to the UML standard.

This section tries to briefly explain why.

### Literal values and reference values

Formally, attributes can take

* a literal value (governed by a datatype, and conceptually corresponding to owl:DatatypeProperty)
* a reference value (governed by a class, corresponding to owl:ObjectProperty).

In the real world, the distinction is less clear, for example between:

* an attribute with a "code" from a controlled list of values
* an attribute that implements an association from class A to class B
  (in practice, between table A and table B)
  by referencing the unique "code" or "identifier" in class B (table B).

### Attributes that implement associations

This also applies to associations between classes.
The following diagram shows a conceptual model, depicting that ClassA
is associated with ClassB via an attribute identifierB.

```{mermaid}
:name: UML_ClassDiagram_ConceptualModel
:caption: UML class diagrams
:align: center
---
config:
  class:
    hideEmptyMembersBox: true
  layout: dagre
  theme: neutral
---
classDiagram
direction LR
class ClassA{
    + identifierA : string
    + attributeA1 : string [0..1]
    + attributeA2 : nonNegativeInteger
}
class ClassB{
    + identifierB : string
    + attributeB1 : decimal
    + attributeB2 : CodelistB2 [1..2]
}

class CodelistB2{<<enumeration>>
    thisIsAnAllowedValue
    thisIsAlsoAnAllowedValue
}

ClassA "n" -- "1" ClassB : +identifierB
```

In the WISE UML diagrams, the diagram will depict the identifierB attribute
in both TableA and TableB.
The name of the attribute implementing the association between tables
will likely appear as a label next to the association line. (There will be
no visual indication that identifierB is the unique identifier in TableA.)

```{mermaid}
:name: UML_ClassDiagram_WISELogicalModel
:caption: WISE modelling conventions - UML class diagrams 
:align: center
---
config:
  class:
    hideEmptyMembersBox: true
  layout: dagre
  theme: neutral
---
classDiagram
direction TB
class TableA{
    + identifierA : string
    + identifierB : string
    + attributeA1 : string [0..1]
    + attributeA2 : nonNegativeInteger
    + attributeA3 : YesNoUnknown 
}
class TableB{
    + identifierB : string
    + attributeB1 : decimal
    + attributeB2 : CodelistB2 [1..2]
    + attributeB3 : VeryLongCodelistB3
}

class CodelistB2{<<enumeration>>
    thisIsAnAllowedValue
    thisIsAlsoAnAllowedValue
    butThisValueIsSometimesNotAllowed
    valuesShouldBeHumanReadable
    butSomeAreNot
    P1
    QE1-3
    CAS_14797-55-8
    RW
    TeW
}

class YesNoUnknown{<<enumeration>>
    yes
    no
    unknown
}

class VeryLongCodelistB3{<<enumeration>>
}

class TableX["AnotherDataset::TableX"]:::likeANote{
 + attributeX1
 + identifierB
}

TableA "n" -- "1" TableB : identifierB 
TableA .. YesNoUnknown
TableB .. CodelistB2
TableB .. VeryLongCodelistB3
TableX .. TableB : identifierB

classDef default fill:white,stroke:#000;
classDef forFixing fill:white,stroke:#f00;
classDef likeANote fill:lightyellow,stroke:#000;
```

## Terms

```{glossary}
:sorted: true

reference table
    Any table containing data that is used for quality control.

controlled list of values
    Any list of values controlled using a {term}`codelist` or {term}`vocabulary`

vocabulary
    When used in the WISE documentation, 
    the term will likely refer to one of the 
    [WISE vocabularies (https://dd.eionet.europa.eu/vocabularies?expand=true&expanded=&folderId=10#folder-10)]

association entity
    A table created for the purpose of resolving and enforcing
    a many-to-many relationship between tables.  
    In the most frequent case, the many-to-many relationship
    exists between two different tables.

codelist
    A {term}`controlled list of values` 
    represented by a enumeration class in UML diagrams,
    and implemented using a {term}`reference table` 
    for quality control purposes.

required attribute
    An attribute for which it is mandatory to provide a non-empty value.
    
optional attribute
    An attribute for which it is optional to provide a non-empty value.

conditional attribute
    An attribute that is mandatory under certain conditions.
    Attributes for which a value *should* be reported, if applicable - 
    but for which a quality control can not be devised 
    (to check if the condition applies) -, are also marked as *conditional*.

identifier
    «todo»
    
identifier scheme
    «todo»
    
comma-separated list of values
    «todo»

datatype
    «todo»
