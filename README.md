# Why are Clinical Trials important in Portugal
Programming for Data Science 2023 - Group. B1 TP. 2<br>
 - André Pereira (20221204@novaims.unl.pt, 20221204)<br>
 - Diogo Fernandes (20220507@novaims.unl.pt, 20220507)<br>
 - Gonçalo Matos (20221194@novaims.unl.pt, 20221194)<br>
 - M. Hortense Matos (20222167@novaims.unl.pt, 20222167)<br>



## Context

In a highly regulated ethical and legal framework, Clinical trials are essential for assessing the safety and efficacy of new drugs, representing an important step for these to be approved and made available for patients. Clinical trials also play a pivotal role in advancing medical knowledge, improving patient care, apart from ensuring the safety and effectiveness of new medical treatments, devices, and interventions, through carefully designed studies in human subjects.<br>
In our project we aimed to explore the existing clinical trials in Europe and specifically in Portugal to understand how they could contribute to tackling the most common diseases and potentially increase the quality or the life expectancy of patients. Through the use of data scraping techniques, we collected clinical trials registry information. We investigated the most frequent therapeutic areas of clinical trials in Portugal and in parallel explored Mortality Rates as well as Life Expectancy and Healthy Life Years to understand how the trials served those disease areas.

## Data Acquisition

#### Scrapper Bots:

- RNEC Scrapper - Gets trial info from RNEC and stores it in an csv file named [RNEC](https://github.com/Dpf050/Programming-Project/blob/59d364b01eb7bc6cc0d765ac57d1de6b4c7d65e3/DataSets/RNEC.csv).
- EUCTRegister - Gets trial info from EUCTRegister (multiple files) and merges them into one. Due to GitHub file constrictions they are stored in: [EU_data.zip](https://drive.google.com/file/d/1TlMjoSPUPPzriZOIh_PvQjVAw3Pml0nx/view?usp=share_link)(all files by batch) [EUCTRegister](https://drive.google.com/file/d/1Lo6zbyhzTMww79L3ssETF51_E8rUqZi_/view?usp=share_link)(merged csv).
- Health life years - Script to get Eurostat excel file regarding [Health Life Years](https://github.com/Dpf050/Programming-Project/blob/744abdc3d2ea6aff87ff4cba54e512fafb962381/DataSets/Healthy%20Life%20Years.xlsx).
- Life Expectancy - Script to get Eurostat excel file regarding [Life Expectancy](https://github.com/Dpf050/Programming-Project/blob/744abdc3d2ea6aff87ff4cba54e512fafb962381/DataSets/Life%20Expectancy.xlsx).

 (TG message - small script with function to send message through telegram in case the scrapers stop )

#### DataSets:

- [RNEC](https://github.com/Dpf050/Programming-Project/blob/59d364b01eb7bc6cc0d765ac57d1de6b4c7d65e3/DataSets/RNEC.csv) - All trial info scraped from [RNEC site](https://www.rnec.pt/) (on May 7th).
- [EUCTRegister](https://drive.google.com/file/d/1Lo6zbyhzTMww79L3ssETF51_E8rUqZi_/view?usp=share_link) - All trial info scraped from [EU Clinical Trials Register site](https://www.clinicaltrialsregister.eu/) (on May 15th).
- [Health Life Years](https://github.com/Dpf050/Programming-Project/blob/744abdc3d2ea6aff87ff4cba54e512fafb962381/DataSets/Healthy%20Life%20Years.xlsx) - Health life years data from 2011 until 2020 for european countries from [Eurostat](https://ec.europa.eu/eurostat/web/main/data/database) (on May 19th).
- [Life Expectancy](https://github.com/Dpf050/Programming-Project/blob/744abdc3d2ea6aff87ff4cba54e512fafb962381/DataSets/Life%20Expectancy.xlsx) - Life Expectancy data 2012 until 2021 for european countries from [Eurostat](https://ec.europa.eu/eurostat/web/main/data/database) (on May 19th).
- [Ghe2019](https://github.com/Dpf050/Programming-Project/blob/532b41d1de3e1240ffbc285ebc5a672b52df3179/DataSets/ghe2019_death-rates-country.xlsx) - Death rates by country and cause of death from [WHO](https://www.who.int/data/gho/data/themes/mortality-and-global-health-estimates/ghe-leading-causes-of-death) (on May 16th).
- [Trials](https://github.com/Dpf050/Programming-Project/blob/cafa31719723bb14f37eba1ed59a488158e951d2/DataSets/trials.csv) - Clean version of [EUCTRegister](https://drive.google.com/file/d/1Lo6zbyhzTMww79L3ssETF51_E8rUqZi_/view?usp=share_link).
- [Continents acording to our world in data](https://github.com/Dpf050/Programming-Project/blob/da0f2a22ec2196547bd771d2710799a935252466/DataSets/continents-according-to-our-world-in-data.csv) - data file containing countries and respective continents (used for filtering) from [Our World in Data](https://ourworldindata.org/grapher/continents-according-to-our-world-in-data) (on May 16th ).
- [Europe](https://github.com/Dpf050/Programming-Project/blob/9ed09a328415075e0a1f8b1cf21bec2af4c22d93/DataSets/europe.geojson) - geojson file with Europe data from [here](https://github.com/leakyMirror/map-of-europe/blob/master/GeoJSON/europe.geojson) (on May 20th).

## Data Cleaning & Visualization

#### Data Cleaning&Viz

- [Trials_Cleaning](https://github.com/Dpf050/Programming-Project/blob/1728534270800b88fe8bc65926765e6e1c046b76/Cleaning&Viz/Trials_Cleaning.ipynb) - Data cleaning nb of the EUCTRegister data set.
- [Eu_Pt_Comparison](https://github.com/Dpf050/Programming-Project/blob/1728534270800b88fe8bc65926765e6e1c046b76/Cleaning&Viz/Eu_Pt_Comparison.ipynb) - Data visualizations and manipulation of trials dataset regarding clinical trials European and Portuguese context.
- [Health_life_years](https://github.com/Dpf050/Programming-Project/blob/1728534270800b88fe8bc65926765e6e1c046b76/Cleaning&Viz/Healthy_life_years.ipynb) - Data visualizations and manipulation of the dataset with the same name.
- [Life_expectancy](https://github.com/Dpf050/Programming-Project/blob/1728534270800b88fe8bc65926765e6e1c046b76/Cleaning&Viz/Life_expectancy.ipynb) - Data visualizations and manipulation of the dataset with the same name.
- [Mortality_Rates](https://github.com/Dpf050/Programming-Project/blob/1728534270800b88fe8bc65926765e6e1c046b76/Cleaning&Viz/Mortality_Rates.ipynb) - Data visualizations and manipulation of Ghe dataset regarding Mortality rates.

#### Graphics

- Folder with all exported graphics from the notebooks
