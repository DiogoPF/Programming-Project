# Cols

EudraCT Number:
Sponsor's Protocol Code Number:
National Competent Authority:
Clinical Trial Type:
Trial Status:
Date on which this record was first entered in the EudraCT database:
Trial results
Member State Concerned
EudraCT number
Full title of the trial
Title of the trial for lay people, in easily understood, i.e. non-technical, language
Name or abbreviated title of the trial where available
Sponsor's protocol code number
US NCT (ClinicalTrials.gov registry) number
Trial is part of a Paediatric Investigation Plan
EMA Decision number of Paediatric Investigation Plan
Name of Sponsor
Country
Status of the sponsor
Name of organisation providing support
Name of organisation
Functional name of contact point
Street Address
Town/ city
Post code
E-mail
IMP Role
IMP to be used in the trial has a marketing authorisation
Trade name
Name of the Marketing Authorisation holder
Country which granted the Marketing Authorisation
The IMP has been designated in this indication as an orphan drug in the Community
Orphan drug designation number
Product name
Pharmaceutical form
Specific paediatric formulation
Routes of administration for this IMP
Active substance of chemical origin
Active substance of biological/ biotechnological origin (other than Advanced Therapy IMP (ATIMP)
Advanced Therapy IMP (ATIMP)
Somatic cell therapy medicinal product
Gene therapy medical product
Tissue Engineered Product
Combination ATIMP (i.e. one involving a medical device)
Committee on Advanced therapies (CAT) has issued a classification for this product
Combination product that includes a device, but does not involve an Advanced Therapy
Radiopharmaceutical medicinal product
Immunological medicinal product (such as vaccine, allergen, immune serum)
Plasma derived medicinal product
Extractive medicinal product
Recombinant medicinal product
Medicinal product containing genetically modified organisms
Herbal medicinal product
Homeopathic medicinal product
Another type of medicinal product
Is a Placebo used in this Trial?
Pharmaceutical form of the placebo
Route of administration of the placebo
Medical condition(s) being investigated
Medical condition in easily understood language
Therapeutic area
Condition being studied is a rare disease
Main objective of the trial
Secondary objectives of the trial
Trial contains a sub-study
Principal inclusion criteria
Principal exclusion criteria
Primary end point(s)
Timepoint(s) of evaluation of this end point
Secondary end point(s)
Diagnosis
Prophylaxis
Therapy
Safety
Efficacy
Pharmacokinetic
Pharmacodynamic
Bioequivalence
Dose response
Pharmacogenetic
Pharmacogenomic
Pharmacoeconomic
Others
Human pharmacology (Phase I)
First administration to humans
Bioequivalence study
Other
Other trial type description
Therapeutic exploratory (Phase II)
Therapeutic confirmatory (Phase III)
Therapeutic use (Phase IV)
Controlled
Randomised
Open
Single blind
Double blind
Parallel group
Cross over
Other medicinal product(s)
Placebo
Number of treatment arms in the trial
The trial involves single site in the Member State concerned
The trial involves multiple sites in the Member State concerned
Number of sites anticipated in Member State concerned
The trial involves multiple Member States
Trial being conducted both within and outside the EEA
Trial being conducted completely outside of the EEA
Trial has a data monitoring committee
Definition of the end of the trial and justification where it is not the last visit of the last subject undergoing the trial
In the Member State concerned years
In the Member State concerned months
In the Member State concerned days
In all countries concerned by the trial years
In all countries concerned by the trial months
Trial has subjects under 18
In Utero
Preterm newborn infants (up to gestational age < 37 weeks)
Newborns (0-27 days)
Infants and toddlers (28 days-23 months)
Children (2-11years)
Adolescents (12-17 years)
Adults (18-64 years)
Number of subjects for this age range:
Elderly (>=65 years)
Female
Male
Healthy volunteers
Patients
Specific vulnerable populations
Women of child-bearing potential using contraception
Pregnant women
Nursing women
Emergency situation
Subjects incapable of giving consent personally
In the member state
Plans for treatment or care after the subject has ended the participation in the trial (if it is different from the expected normal treatment of that condition)
Competent Authority Decision
Date of Competent Authority Decision
Ethics Committee Opinion of the trial application
Ethics Committee Opinion: Reason(s) for unfavourable opinion
Date of Ethics Committee Opinion
End of Trial Status
Date of the global end of the trial
Product code
CAS number
Other descriptive name
Version
Level
Classification code
Term
System Organ Class
In all countries concerned by the trial days
Details of subjects incapable of giving consent
INN - Proposed INN
Concentration unit
Concentration type
Concentration number
Telephone number
EV Substance Code
Fax number
Current sponsor code
Other Identifiers
Full title, date and version of each sub-study and their related objectives
Comparator description
Will this trial be conducted at a single site globally?
Will this trial be conducted at multiple sites globally?
Specify the countries outside of the EEA in which trial sites are planned
In the whole clinical trial
Third Country in which the trial was first authorised:
Other trial design description
Other scope of the trial description
Other medicinal product type
Number of sites anticipated in the EEA
In the EEA
ISRCTN (International Standard Randomised Controlled Trial) Number
If E.8.6.1 or E.8.6.2 are Yes, specify the regions in which trial sites are planned
Name of Organisation
Network Country
Details of other specific vulnerable populations
WHO Universal Trial Reference Number (UTRN)
CAT classification and reference number

# Structure

- Snapshot of European and Portuguese Trials
  - Country - geo graph
  - Year added
  - Public or private funding? (maybe by country too - which countries spend the most on trials)
  - Main characteristics of trials that are made in more than one country
  - Therapeutic Areas
  - ? Rare disease
  - More common trial objectives ( Diagnosis, prophylaxis, therapeutic, safety...)
  - Phase - more common phases
  - Duration Months/Years
  - Nr of subjects
  - Sample Age and Gender
  - Healthy subjects or patients


- Portuguese Setting

### Random Code snippets

```python
import pandas as pd

# Assuming your DataFrame is called 'df'
columns = ['Diagnosis', 'Prophylaxis', 'Therapy', 'Safety', 'Efficacy', 'Pharmacokinetic',
           'Pharmacodynamic', 'Bioequivalence', 'Dose response', 'Pharmacogenetic',
           'Pharmacogenomic', 'Pharmacoeconomic', 'Others']

# Replace "yes" with 1 and "no" with 0 in the specified columns
df[columns] = df[columns].replace({'Yes': 1, 'No': 0})

# Combine the columns to create a new column that represents the combination
df['combination'] = df[columns].apply(lambda x: ''.join(x.astype(str)), axis=1)

df['combination'].value_counts()

```
