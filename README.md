# rural-solar-viability
 
(3) explain what each script does and the order in which they should be run; 
(4) explain any additional files provided in the repository; and 
(5) discuss the results.

## Purpose of repository: Providing analysis of basic information to support decision makers involved in solar farm propagation in rural Upstate NY

The purpose of this repository is to compile data on groundwater and solar farms in Upstate New York. In particular, this repository focuses on understanding the proxmity of individual water wells on private property to **existing** solar projects.
Solar farms are an up-and-coming source of clean energy, which is vital to the nation's adoption of clean energy initatives. However, solar farms pose their own environmental drawbacks - land is often clear cut to make way for the panels, and the panels themselves are coated in chemicals that could contaminate the local groundwater. 
Groundwater is a vital source of freshwater for millions in the United States, and many who live in rural areas rely on wells to access groundwater. The construction of solar farms could threaten the potability of the groundwater resources of rual areas.

The goal of this repository is not to dissuade rural stakeholders and decisionmakers from adopting solar energy, but to make informed choices on the construction of solar farms for the best possible environmental and public health outcomes.

### Inputs

- Cartographic boundary data from the US Census Bureau
    - How to access:
        1. Visit https://www.census.gov/geographies/mapping-files/time-series/geo/cartographic-boundary.html
        2. Select the "2021" tab
        3. Scroll to each geography type's section on the page, select "New York" from the shapefile dropdown menu, and save the zip file to the repository:
            - Shapefiles:
            
               - Census Block Groups - 1:500,000 (state)
                   - File name: cb_2021_36_bg_500k.zip
                   - Select "New York State" from shapefile dropdown menu 
               
               - Counties - 1:500,000 (national)
                   - File name: cb_2021_36_bg_500k.zip
                   - National file is only available
               
               - County Subdivisions - 1:500,0000 (state)
                   - File name: cb_2021_36_bg_500k.zip
                   - Select "New York State" from shapefile dropdown menu

- Water wells locations and attribute data from the New York GIS Clearinghouse
    - File name: WellWaterProgram.zip
    - How to access:
        1. Visit https://gis.ny.gov/gisdata/inventories/details.cfm?DSID=1203
        2. Under the "Data Set Name" column of the table, click "Water Wells", and save the zip file to the repository
        3. Notes: 
            a. Dataset excludes well data from Nassau, Suffolk, Kings, and Queens counties (DEC Region 1)
            b. Data points may fall outside Census designated boundaries because of partial address data

 - Solar project data from the NY-Sun Solar Program
    - File name: Statewide_Solar_Projects_Beginning_2000.csv
    - How to access: 
        1. Visit https://data.ny.gov/Energy-Environment/Statewide-Solar-Projects-Beginning-2000/wgsj-jt5f
        2. Click "Export" and select "CSV"

### Scripts and Files

- groundwater_solar_mapping.qgz
    - Generates the .PNG map outputs using the Census, water well, and solar project data
    - Filters
    
### Outputs

- Map Image Files (.PNG)
    - NYS_Schenectady County_BlockGroups.png: shows a map of New York State with county boundaries, with Schenectady County highlighted in brown and displaying the block groups of that county
    - WaterWellProgram_NYS_County.png: shows a map of New York State with county boundaries, overlaid with well location data
    - WaterWellProgram_NYS_Schenectady County_Towns_BlockGroups.png: shows a map of Schenectady County with county subdivision (towns and cities) and  block group boundaries, overlaid with well location data

## Main Findings


## Further Analysis

Futher analysis of this topic could examine the other environmental impacts of potential solar farm construction, using groundwater vulnerability assessment procedures as discussed by Focazio et al. (2002). 
This could include:
    - Mapping out the use of land by property line to understand impact on residents
    - Mapping out the topography and vegetation of the land to understand impact on the local environment (such as increased stormwater runoff and reduction of tree cover)
    - Mapping out aquifer systems and surface level water bodies to understand the impact of contamination on the wider aquifer systems that feed groundwater wells
    - Refining wellwater data visualizations to shows the different attributes of each particular well (such as depth)
    - Visualizing data on changes in contaminate levels in areas ajacent to solar farms prior and after construction

## Bibliography

Focazio, M.J., Reilly, T.E., Rupert, M.G., Helsel, D.R. (2002). *Assessing ground-water vulnerability to contamination: Providing scientifically defensible information for decision makers*. U.S. Geological Survey. https://doi.org/10.3133/cir1224

United States Geological Survey. (2019, February 29). Groundwater quality in principal aquifers of the nation, 1991–2010 completed. Groundwater Quality in Principal Aquifers of the Nation, 1991–2010 | U.S. Geological Survey. Retrieved from https://www.usgs.gov/mission-areas/water-resources/science/groundwater-quality-principal-aquifers-nation-1991-2010 

Ren, M., Qian, X., Chen, Y., Wang, T., &amp; Zhao, Y. (2022). Potential lead toxicity and leakage issues on lead halide perovskite photovoltaics. Journal of Hazardous Materials, 426, 127848. https://doi.org/10.1016/j.jhazmat.2021.127848 


## Further Reading

DeMola, Peter. "Town of Duanesburg delays vote on PILOT solar deal as questions percolate". The Daily Gazette, 30 December 2019. https://dailygazette.com/2019/12/30/town-of-duanesburg-delays-vote-on-pilot-solar-deal-as-questions-percolate/

Nir, Sarah Maslin. “He Set Up a Big Solar Farm. His Neighbors Hated It.”. The New York Times, 18 Mar. 2020. https://www.nytimes.com/2020/03/18/nyregion/solar-energy-farms-ny.html. 

Rosen, Ellen. “As Demand for Green Energy Grows, Solar Farms Face Local Resistance”. The New York Times, 2 Nov 2021. https://www.nytimes.com/2021/11/02/business/solar-farms-resistance.html.

Duanesburg Neighbors. (2022). *Duanesburg Neighbors*. https://duanesburgneighbors.com/
