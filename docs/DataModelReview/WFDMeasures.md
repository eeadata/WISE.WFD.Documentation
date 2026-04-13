# WFD - Measures


**PROPOSAL - Version 2026.02.17** {download}`PDF <pdf/WFD_4rd_cycle_Measures_v20260217.pdf>`

**WD Data Models and Dataflows**



```{mermaid}
%%{init: {'theme': 'neutral'}}%%

flowchart 

%% 
title@{ shape: braces, label: "WISE Dataflow XPTO \n Status update: 2026-03-26" }

%% Defining the nodes and overall flow
        
initial([start])
final([end])

%% DATAFLOW for DATA COLLECTION

subgraph P4["DATA COLLECTION - Opening the dataflow"]
    direction LR
    
    %% activities
    P41["Update and publish documentation \n (release v1.0)"]
    P42["Create collections"]
    P43["Grant permissions \n (by data stewards)"]
    P44["Open data collection"]
    P45["Provide user support \n (by data stewards)"]
    P46["Provide final feedback \n (by data stewards)"]
    P47["Close data collection"]

    %% workflow
    P41 --> P42 --> P43 --> P44 
    P44 --- P45 --- P47
    P44 --- P46 --- P47

end

%% EXTERNAL TESTING

subgraph P3["EXTERNAL TESTING - Opening the dataflow for beta testing by Member States"]
    direction LR

    %% activities
    P31["Update and publish documentation \n (release v0.2)"]
    P32["Create collections"]
    P33["Grant permissions \n (by data stewards)"]
    P34["Open for testing"]
    P35["Provide user support \n (also by data stewards)"]
    
    %% workflow
    P31 --> P32 --> P33 --> P34 --> P35
end

%% INTERNAL TESTING
    
subgraph P2["INTERNAL TESTING - Opening the dataflow for alpha testing by Data Stewards and Data Steward Support roles"]
    direction LR

    %% activities
    P21["Update and publish documentation \n (release v0.1)"]
    P22["Create collections"]
    P23["Grant permissions"]
    P24["Open for testing"]

    %% workflow
    P21 --> P22 --> P23 --> P24
end

%% design and build

subgraph P1["Design and build the MASTER dataflow"]
    direction TB

    subgraph QC["Quality control"]
        direction TB

        %% activities
        QC1["Define and document"]
        QC2["Implement in \n SQL Server database"]
        QC3["Test in SQL Server"]
        QC4["Implement in RN3"]
        QC5["Test in RN3"]

        %% workflow
        QC1 --- QC2 --- QC3 --- QC4 --- QC5
    end

    subgraph TF["Template FILE(S)"]
        direction TB

        %% activities
        TF1["Define and document"]
        TF2["Generate TEMPLATE file(s)"]
        TF3["Create TEST file(s)"]   
        TF4["Test the RN3 import \n into the reporting dataset(s)"]
        TF5["Create PREFILLED file(s)"]   

        %% workflow 
        TF1 --- TF2 --- TF3 --- TF4 
        TF3 --- TF5 --- TF4
    end

    subgraph RefD["Reference DATASET"]
        direction TB

        %% activities
        RefD1["Define and document"]
        RefD2["Generate in \n SQL Server database"]
        RefD3["Implement in RN3"]
        RefD4["Create or configure \n RN3 import process"]
        RefD5["Populate in RN3"]
        RefD6["Create or configure automation \n (if required & possible)"]

        %% workflow
        RefD1 --- RefD2 --- RefD3 --- RefD4 --- RefD5
        RefD3 --- RefD6 --- RefD5
    end     
    
    subgraph CL["Codelist DATASET"]
        direction TB

        %% activities
        CL1["Define and document"]
        CL2["Generate in \n SQL Server database"]
        CL3["Implement in RN3"]
        CL4["Create or configure \n RN3 import process"]
        CL5["Populate in RN3"]

        %% workflow
        CL1 --- CL2 --- CL3 --- CL4 --- CL5 
    end

    subgraph RepD["Reporting DATASET(S)"]
        direction TB

        %% activities
        RepD1["Define and document"]
        RepD2["Generate in \n SQL Server database"]
        RepD3["Implement in RN3"]
        RepD4["Create or configure \n RN3 import process"]
        RepD5["Configure the metadata and data harvesting process"]

        %% workflow
        RepD1 --- RepD2 --- RepD3 --- RepD4 --- RepD5
    end

    subgraph MD["Modelling and documentation"]
        direction TB

        %% activities
        MD1["Define conceptual model"]
        MD2["Describe datasets, tables, columns and domains"]
        MD3["Create Enterprise Architect project"]
        MD4["Generate DRAFT reporting guidance"]
        MD5["Generate WISE documentation"]

        %% workflow
        MD1 --- MD2 --- MD3 --- MD4 --- MD5
    end
end

%% Main workflow
    
initial-->P1

P1 ==>|clone MASTER dataflow| P2 
P1 ==>|clone MASTER dataflow| P3
P1 ==>|clone MASTER dataflow| P4
P2 -->|revise and correct| P1
P3 -->|revise and correct| P1
P4 <-->|correct or optimise \n Quality Control| P1

P2 .->|after approval \n by data steward \n and data custodian| P3
P3 .->|after testing period| P4

P4-->final

%% JUST VISUALISATION 

final ~~~ Legend

subgraph Legend
    direction LR
    planned
    inProgress:::inProgress
    implemented:::implemented
    validated:::validated
    forFixing:::forFixing

    planned ~~~ forFixing ~~~ inProgress ~~~ implemented ~~~ validated
end

%% Define status styles

classDef inProgress stroke-width:3px, fill:transparent

classDef forFixing stroke-width:3px, stroke:red, fill:transparent
classDef implemented stroke-width:3px, stroke:orange, fill:transparent
classDef validated stroke-width:3px, stroke:green, fill:transparent
classDef initial fill:#000,stroke:#000,stroke-width:2px
classDef final fill:#000,stroke:#aaa,stroke-width:4px

%% STATUS UPDATES
%% 2026-03-26
class P1 inProgress
class MD inProgress

class MD1 validated;
class MD2 inProgress;
class MD3 implemented;
```
