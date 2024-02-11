# Some notes while reading the docs and looking at the dataset

https://www.fiskeridir.no/Tall-og-analyse/AApne-data/elektronisk-rapportering-ers (original dataset before it was edited by bjørnar)
https://www.fiskeridir.no/Yrkesfiske/Registre-og-skjema/Fartoeyregisteret/api (api to find vessel register)
https://www.fiskeridir.no/Tall-og-analyse/AApne-data/Fangstdata-seddel-koblet-med-fartoeydata (register for receipts)

## Finding relevant info from "Samansette driftsdata for fangst (setel) og fartøy"

### Introduction to document

This document was last updated the 12.December in 2023, and it was written by [Randi S. Sletten Hopland](https://www.fiskeridir.no/Om-oss/Avdelinger-og-regioner/forvaltningsdivisjonen/statistikkseksjonen/Tove-Aasheim) and [Tove Aasheim](https://www.fiskeridir.no/Om-oss/Avdelinger-og-regioner/forvaltningsdivisjonen/statistikkseksjonen/Randi-Sofie-Sletten-Hopland). According to the document, this dataset sources its data from [the directorate of fisheries](https://www.fiskeridir.no/) final/landing receipts register and ship register.

The dataset records all fishing activities conducted by Norwegian registered fishing boats as well as foreign vessels operating in Norwegian waters. It encompasses not only commercial fishing operations but also includes fishing activities undertaken for research, educational purposes, and recreational fishing with revenue intentions. The data is comprehensive, including both final receipts and landing receipts. As per the system, the landing receipts are recorded as the catch is sold and finalized in the final receipt. Over time, this process results in most of the landing receipts displaying a quantity of zero. Any unsold catches, represented by remaining quotas on these landing receipts, are those that haven't been sold for various reasons.

### Interesting points from rest of document

#### "Metode for kopling av fangstdata og fartøydata" p.1

In the section where they describe their methodology for linking catch data and vessel data, they explain that the data from the landing receipt register and ship register are connected by comparing registration marks and radio call signs. It says that if the last catch data and vessels validity period are mismatched the vessels municipality, maximum length, gross tonnage, etc are undefined. I think we have to keep this in mind when preprocessing the data, when i printed the amount of gross tonnage (1969 and other) i got 71429 NaN values in 1969 and 230660 NaN. Meaning using this data we can figure out amount of fishing that doesn't match vessels validity period, this might be useful maybe? find where both, ship length, etc.

#### "Eining"

This part just talks about what the data is based on. Most of the data stems from the [landing/final receipt.](#final-and-landing-receipts)

#### "Datakvalitet" p.2

This part talks about the quality of data when it comes to catch data and vessel data.

##### "Fangst"

Seems like there is a variance in quality for catch data when it comes to locations and codes, this is due to new areas and stuff being added. (Might need to check [code list]())

Not all parts of the forms are required to be filled by the fishermen, this means some categories will be missing a lot of data.

##### "Fartøy"

Didn't find anything relevant here. (Unsure though might be something important that i've missed)

#### Rest of the document

The rest of the document seems to just be about explaining different codes in the dataset, will refer to this when it is relevant to the dataset.

### A quick look a the dataset

Looked at the dataset quickly using pandas, these are my findings:

- The dataset contains 305 434 different entries
- We are working with 45 different features
- Missing values seems to be left empty (NaN)
- Contains floats, ints, objects

#### Sample of the dataset

This is what the dataset looks like:<br />
<img src="./Images\sample1.png" alt="datasetimg1" width="1000" height="360"/>
<img src="./Images\sample2.png" alt="datasetimg2" width="1000" height="360"/>
<img src="./Images\sample3.png" alt="datasetimg3" width="700" height="360"/>

#### All 45 Categories Explained

Here is a brief summary of all categories in the dataset, i will note down a brief description of the category, the data type required and if they are mandatory or conditional.
I added all the code lists for FAO (Food and Agriculture Organization of the United Nations) i could find from [the directorate of fisheries](https://www.fiskeridir.no/Yrkesfiske/Rapportering-paa-havet/elektronisk-rapportering-ers/feilkoder%20og%20kodelister) in the documentations folder, if you are curios you can take a peak. Can't find the FDIR code list?

##### Melding ID (Message ID)

For more information refer to page 4 in datadokumentasjon-ers-rapport-varnivaa-5-140121

- System generated
- Data type: Int64

An identifier automatically assigned to each message upon its receipt by the Directorate of Fisheries.

##### Meldingstidspunkt (Message time)

For more information refer to page 4 in datadokumentasjon-ers-rapport-varnivaa-5-140121

- Mandatory
- Data type: Object

Date and time a message is sent, recorded in Coordinated Universal Time (UTC). This information is derived from the onboard GPS system.

##### Meldingsdato (Message date)

For more information refer to page 4 in datadokumentasjon-ers-rapport-varnivaa-5-140121

- Mandatory
- Data type: Object

Date and time a message is sent, recorded in Coordinated Universal Time (UTC). This information is derived from the onboard GPS system.

##### Meldingsklokkeslett (Message time)

For more information refer to page 4 in datadokumentasjon-ers-rapport-varnivaa-5-140121

- Mandatory
- Data type: Object

Date and time a message is sent, recorded in Coordinated Universal Time (UTC). This information is derived from the onboard GPS system.

##### Starttidspunkt (Start time)

For more information refer to page 7 in datadokumentasjon-ers-rapport-varnivaa-5-140121

- Mandatory
- Data type: Object

Date and time when fishing begins, formatted as YYYYMMDD for the date and HHMM for the time.

##### Startdato (Start date)

For more information refer to page 7 in datadokumentasjon-ers-rapport-varnivaa-5-140121

- Mandatory
- Data type: Object

Date and time when fishing begins, formatted as YYYYMMDD for the date and HHMM for the time.

##### Startklokkeslett (Start time)

For more information refer to page 7 in datadokumentasjon-ers-rapport-varnivaa-5-140121

- Mandatory
- Data type: Object

Date and time when fishing begins, formatted as YYYYMMDD for the date and HHMM for the time.

##### Startposisjon bredde (Start position latitude)

For more information refer to page 7 in datadokumentasjon-ers-rapport-varnivaa-5-140121

- Mandatory if fishing gear is deployed
- Data type: Object

The latitude at the beginning of the fishing operation is noted in degrees and decimals (DD.ddd) following the WGS-84 standard.

##### Startposisjon lengde (Start position longtitude)

For more information refer to page 7 in datadokumentasjon-ers-rapport-varnivaa-5-140121

- Mandatory if fishing gear is deployed
- Data type: Object

The longitude at the start of fishing is recorded in degrees and decimals (DDD.ddd) as per the WGS-84 standard.

##### Hovedområde start (kode) (Main area start code)

For more information refer to page 7 in datadokumentasjon-ers-rapport-varnivaa-5-140121 and page 21 in Dokumentasjon*Fangst_Fart¢y*Åpne_Data

- System generated
- Data type: Float64

A calculated value generated by the system based on the fisher's reported positions in the catch report. The code is two digits long.

##### Hovedområde start (main area start)

For more information refer to page 7 in datadokumentasjon-ers-rapport-varnivaa-5-140121

- System generated
- Data type: Object

A calculated location where the fishing operation began, derived from reported positions in the catch report.

##### Lokasjon start (kode) (Location start code)

For more information refer to page 8 in datadokumentasjon-ers-rapport-varnivaa-5-140121 and page 21 in Dokumentasjon*Fangst_Fart¢y*Åpne_Data

- System generated
- Data type: Float64

Calculated value from the system based on positions that the fisher reports in the catch report. The code is two digits long.

##### Havdybde start (Sea depth, start)

For more information refer to page 8 in datadokumentasjon-ers-rapport-varnivaa-5-140121

- System generated
- Data type: Int64

Depth of the sea at the location where the fishing operation begins.

##### Stopptidspunkt (Stop time)

For more information refer to page ** in **

- Not in any of the documents i assume its the same format as start
- Data type: Object

##### Stoppdato (Stop date)

For more information refer to page ** in **

- Not in any of the documents i assume its the same format as start
- Data type: Object

##### Stoppklokkeslett (Stop time)

For more information refer to page ** in **

- Not in any of the documents i assume its the same format as start
- Data type: Object

##### Varighet (Duration)

For more information refer to page 8 in datadokumentasjon-ers-rapport-varnivaa-5-140121

- Mandatory if fishing gear is deployed
- Data type: Int64

The time between the start and end of a fishing operation.
Vessels sometimes record hauling time instead of the duration of the fishing operation.

##### Fangstår (Catch year)

For more information refer to page 8 in datadokumentasjon-ers-rapport-varnivaa-5-140121

- Mandatory
- Data type: Int64

Date (YYYYMMDD) and time (HHMM) for the start of fishing

##### Stopposisjon bredde (Stop position latitude)

For more information refer to page 9 in datadokumentasjon-ers-rapport-varnivaa-5-140121

- Mandatory
- Data type: Object

The latitude at the beginning of the fishing operation is noted in degrees and decimals (DD.ddd) following the WGS-84 standard.

##### Stopposisjon lengde (Stop position longitude)

For more information refer to page 9 in datadokumentasjon-ers-rapport-varnivaa-5-140121

- Mandatory
- Data type: Object

The latitude at the beginning of the fishing operation is noted in degrees and decimals (DD.ddd) following the WGS-84 standard.

##### Hovedområde stopp (kode) (Main Area stop code)

For more information refer to page 9 in datadokumentasjon-ers-rapport-varnivaa-5-140121 and page 21 in Dokumentasjon*Fangst_Fart¢y*Åpne_Data

- System generated
- Data type: Float64

Location where the fishing operation ended
Calculated value from the system based on positions that the fisher reports in the catch report. Two digits long.

##### Hovedområde stopp (Main area stop)

For more information refer to page 9 in datadokumentasjon-ers-rapport-varnivaa-5-140121

- System generated
- Data type: Object

Calculated value from the system based on positions that the fisher reports in the catch report.

##### Lokasjon stopp (kode) (Location stop (code))

For more information refer to page 9 in datadokumentasjon-ers-rapport-varnivaa-5-140121 and page 21 in Dokumentasjon*Fangst_Fart¢y*Åpne_Data

- System generated
- Data quality varies
- Data type: Float64

A calculated value based on the positions reported by the fisher in the catch report. This value is represented with two digits.

##### Havdybde stopp (Sea depth stop)

For more information refer to page 9 in datadokumentasjon-ers-rapport-varnivaa-5-140121

- System generated
- Data type: Int64

A calculated value based on the positions reported in the catch report.

##### Trekkavstand (Drag distance)

For more information refer to page ** in **

- Data type: Float64

No description provided, i assume its the distance dragged by fishing equipments during an operation.

##### Redskap FAO (kode) (Gear FAO (code))

For more information refer to page 10 in datadokumentasjon-ers-rapport-varnivaa-5-140121 and page 19 in Dokumentasjon*Fangst_Fart¢y*Åpne_Data

- Mandatory
- Data type: Object

Refers to the fishing gear used, selected by the skipper from the FAO gear code list published on the Directorate of Fisheries' website.

##### Redskap FAO (Gear FAO)

For more information refer to page 10 in datadokumentasjon-ers-rapport-varnivaa-5-140121 and page 19 in Dokumentasjon*Fangst_Fart¢y*Åpne_Data

- Mandatory
- Data type: Object

Refers to the fishing gear used, selected by the skipper from the FAO gear code list published on the Directorate of Fisheries' website.

##### Redskap FDIR (kode) (Gear FDIR (code))

For more information refer to page ** in **

- Data type: Float64

No description provided, i assume its the same as gear FAO but uses FDIR (Fishing directory list) code list instead.

##### Redskap FDIR (Gear FDIR)

For more information refer to page ** in **

- Data type: Object

No description provided, i assume its the same as gear FAO but uses FDIR (Fishing directory list) code list instead.

##### Hovedart FAO (kode) (Main species FAO (code))

For more information refer to page 11 in datadokumentasjon-ers-rapport-varnivaa-5-140121

- Mandatory
- Data type: Object

Main species caught, reported using the FAO species code. Main species is chosen using highest estimated weight in round kilograms.

##### Hovedart FAO (Main species FAO)

For more information refer to page 11 in datadokumentasjon-ers-rapport-varnivaa-5-140121

- Mandatory
- Data type: Object

Main species caught, reported using the FAO species code. Main species is chosen using highest estimated weight in round kilograms.

##### Hovedart - FDIR (kode) (Main species - FDIR (code))

For more information refer to page ** in **

- Data type: Float64

No description provided, i assume its the same as Main species FAO but uses FDIR (Fishing directory list) code list instead.

##### Art FAO (kode) (Species FAO (code))

For more information refer to page 11 in datadokumentasjon-ers-rapport-varnivaa-5-140121 and page 27 in Dokumentasjon*Fangst_Fart¢y*Åpne_Data

- Mandatory if catch used fishing gear
- Data type: Object

Fish species reported using the FAO three-letter code.

##### Art FAO (Species FAO)

For more information refer to page 12 in datadokumentasjon-ers-rapport-varnivaa-5-140121 and page 27 in Dokumentasjon*Fangst_Fart¢y*Åpne_Data

- Data type: Object

Fish species reported using the FAO list.

##### Art - FDIR (kode) (Species - FDIR (kode))

For more information refer to page 26 in Dokumentasjon*Fangst_Fart¢y*Åpne_Data

- Data type: Float64

Code for species/fish types according to the Directorate of Fisheries' code list.

##### Art - FDIR (Species - FDIR)

For more information refer to page 26 in Dokumentasjon*Fangst_Fart¢y*Åpne_Data

- Data type: Object

Name for species/fish types according to the Directorate of Fisheries' list.

##### Art - gruppe (kode) (Species - group (code))

For more information refer to page 27 in Dokumentasjon*Fangst_Fart¢y*Åpne_Data

- Data type: Float64

Code for groups of species/fish types.

##### Art - gruppe (Species - group)

For more information refer to page 27 in Dokumentasjon*Fangst_Fart¢y*Åpne_Data

- Data type: Object

Name of groups of species/fish types caught.

##### Rundvekt (Round weight)

For more information refer to page 30 in datadokumentasjon-ers-rapport-varnivaa-5-140121

- Mandatory if catch used fishing gear
- Data type: Float64

Catch in kilos round weight for the species caught, chosen by highest weight

##### Lengdegruppe (kode) (Length group (code))

For more information refer to page 16 in Dokumentasjon*Fangst_Fart¢y*Åpne_Data

- Data type: Float64

Length group code generated from the vessel's maximum length, categorized according to the Finnmark model.

##### Lengdegruppe (Length group)

For more information refer to page 16 in Dokumentasjon*Fangst_Fart¢y*Åpne_Data

- Data type: Object

Length group from the vessel's maximum length, categorized according to the Finnmark model.

##### Bruttotonnasje 1969 (Gross weight 1969)

For more information refer to page 16 in Dokumentasjon*Fangst_Fart¢y*Åpne_Data

- Data type: Float64

Gross tonnage of the vessel measured according to the standards set by the London Convention 1969, only includes ships with a length of 24 meters or more.

##### Bruttotonnasje annen (Gross weight other)

For more information refer to page 17 in Dokumentasjon*Fangst_Fart¢y*Åpne_Data

- Data type: Float64

Gross tonnage of vessels under 24 meters in length, measured according to different rules than the London Convention 1969. This includes Norwegian Domestic Measurement Certificates (1982) for first-time measured ships under 24 meters, International Measurement Certificates (1947) according to the 1947 convention, and other previous measurement standards. For ships under 15 meters, gross tonnage is recorded based on identity certificates issued after dimensional measurements, with specific equivalents for length-to-tonnage calculations.

##### Bredde (Breadth)

For more information refer to page ** in **

- Data type: Object

No description provided, i assume its the vessel's breadth.

##### Fartøylengde (Vessel length)

For more information refer to page 16 in Dokumentasjon*Fangst_Fart¢y*Åpne_Data

- Data quality varies for some ships
- Data type: Object

The vessel's maximum length, some vessels have their registered length instead of their maximum length written. The maximum length is the length in meters measured from the front edge of the foremost part of the hull to the back edge of the aftmost part of the hull.

## Final and landing receipts

- final and landing receipts are mandatory forms that's required be filled when a boat docks and unloads fish.
- The goal of this practice is to ensure sustainability for wild maritime resources
- The forms are used to record every catch and using that data to implement quotas, statistical purposes, etc.
- Information to be filled in the form is referenced in section 9,10,11,12 and 13 in [landingsforskriften](https://lovdata.no/dokument/SF/forskrift/2014-05-06-607/%C2%A79#%C2%A79)

### Short summary of all the sections:

#### § 9

This section requires information from the entity landing the fish. The entity must provide their company name, organization number, flag state, and the name of the person responsible. If they have a vessel name, fishing mark, or other national registration of the vessel, including call sign and IMO number, these must be provided if applicable. Foreign actors are required to provide an ID number assigned to them by their sales organization, instead of an organization number. If they don't have an organization number, their national identification number must be provided.

It must also be stated if the vessel is the one used for harvesting the fish, or if it's used for transport, purchase, production, or other purposes.

In cases where harvesting is done with a vessel not assigned to the quota, the fishing marks of both vessels must be provided.

#### § 10

This section requires information from the entity receiving the fish. The receiver must provide their company name, organization number, business number, and the county number of the county where the landing is taking place, as well as the approval number of the receiving point if it has been assigned by the Norwegian Food Safety Authority (Mattilsynet), and the name of the receiver's representative.

In the case of landings overseas, the country must be stated, and an ID number assigned by their sales organization should be provided instead of an organization number.

During transshipment and when retrieving fish from traps/cages/bags, the receiving vessel's company name, organization number, flag state, and the name of the responsible person must be provided. If the vessel has a name, fishing mark, or other national registration and call sign, these should also be stated. It should also be indicated if the receiving vessel is a transport, purchase, or production vessel.

#### § 11

Both the receiver and the entity landing the fish must provide the date and time of the completed landing, as well as information about the species, product condition, preservation method, size composition, weight reading, exact quantity in kilograms, and delivery method. For landings of live fish, the number of individuals must be stated. In transactions occurring after the landing of live fish, the number of individuals must be stated on the final receipt, even if the fish are dead at the time of the transaction. The number of individuals must also be stated if required by regulations enacted under the Act of 6 June 2008 No. 37 on the management of wild living marine resources.

The entity landing the fish must provide the reporting number RN from the Port of Call Report (POR-report) on the receipt pertaining to the catch, in accordance with the Regulation of 21 December 2009 No. 1743 on position reporting and electronic reporting for Norwegian fishing and hunting vessels § 13.

Furthermore, the first and last catch dates, zone, fishing ground, gear, vessel role, and quota type must be provided. Information about fish caught in different zones, fishing years, and on different quota types must be stated separately.

#### § 12

The Directorate of Fisheries may establish requirements for equipment and its use to determine the composition of catches in industrial landings.

#### § 13

The seller must provide the company's name, organization number, flag state, and the name of the person responsible. Vessel name, fishing mark, or any other official registration of the vessel and call sign, must be provided if the vessel has these.

The buyer must provide the company's name, organization number, business number, the county number of the county where the landing takes place, the purchase site ID number assigned by the Directorate of Fisheries, the purchase site's approval number if it has been assigned by the Norwegian Food Safety Authority (Mattilsynet), and the name of the buyer's representative.

Foreign sellers and buyers must be identified with an ID number assigned to them by their sales organization instead of an organization number.

The seller and buyer must state the species, product condition, preservation method, size composition, exact quantity in kilograms, number of individuals if required, intended use, price, transaction date, and delivery method during the transaction.

**All information is fetched from [lovdata.no](https://lovdata.no/dokument/SF/forskrift/2014-05-06-607/%C2%A79#%C2%A79) and translated with ChatGPT**
