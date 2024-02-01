# Some notes while reading the docs and looking at the dataset

## Finding relevant info from "Samansette driftsdata for fangst (setel) og fartøy"

### Introduction to document

This document was last updated the 12.December in 2023, and it was written by [Randi S. Sletten Hopland](https://www.fiskeridir.no/Om-oss/Avdelinger-og-regioner/forvaltningsdivisjonen/statistikkseksjonen/Tove-Aasheim) and [Tove Aasheim](https://www.fiskeridir.no/Om-oss/Avdelinger-og-regioner/forvaltningsdivisjonen/statistikkseksjonen/Randi-Sofie-Sletten-Hopland). According to the document, this dataset sources its data from [the directorate of fisheries](https://www.fiskeridir.no/) final and landing [receipts register](#final-landing-receipts) and ship register.

The dataset records all fishing activities conducted by Norwegian registered fishing boats as well as foreign vessels operating in Norwegian waters. It encompasses not only commercial fishing operations but also includes fishing activities undertaken for research, educational purposes, and recreational fishing with revenue intentions. The data is comprehensive, including both final receipts and landing receipts. As per the system, the landing receipts are recorded as the catch is sold and finalized in the final receipt. Over time, this process results in most of the landing receipts displaying a quantity of zero. Any unsold catches, represented by remaining quotas on these landing receipts, are those that haven't been sold for various reasons.

### Interesting points from rest of document

#### "Metode for kopling av fangstdata og fartøydata" p.1

In the section where they describe their methodology for linking catch data and vessel data, they explain that the data from the landing receipt register and ship register are connected by comparing registration marks and radio call signs. It says that if the last catch data and vessels validity period are mismatched the vessels municipality, maximum length, gross tonnage, etc are undefined. I think we have to keep this in mind when preprocessing the data, when i printed the amount of gross tonnage (1969 and other) i got 71429 NaN values in 1969 and 230660 NaN. Meaning using this data we can figure out amount of fishing that doesn't match vessels validity period, this might be useful maybe? find where both, ship length, etc.

## What are final and landing receipts {#final-landing-receipts}

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
