# rural-solar-viability

Author: Mary Rachel Keville

## Purpose of repository

The purpose of this repository is to compile data on groundwater and solar farms in Upstate New York. 

In particular, this repository focuses on understanding the proxmity of individual water wells on private property to **existing** solar projects. Solar farms are an up-and-coming source of clean energy, which is vital to the nation's adoption of clean energy initatives. However, solar farms pose their own environmental drawbacks - land is often clear cut to make way for the panels, and the panels themselves are coated in chemicals that could contaminate the local groundwater. Groundwater is a vital source of freshwater for millions in the United States, and many who live in rural areas rely on wells to access groundwater. The construction of solar farms could threaten the potability of the groundwater resources of rual areas.

The goal of this repository is not to dissuade rural stakeholders and decisionmakers from adopting solar energy, but to provide information crucial to making informed choices on the construction of solar farms for the best possible environmental and public health outcomes.

### Inputs

- Cartographic boundary data from the US Census Bureau
    - How to access:
        1. Visit the US Census Bureau https://www.census.gov/geographies/mapping-files/time-series/geo/cartographic-boundary.html
        2. Select the "2021" tab
        3. Scroll to each geography type's section on the page, select "New York" from the shapefile dropdown menu, and save the zip file to the repository:
            - Shapefiles:
            
               - Census Block Groups - 1:500,000 (state)
                   - File name: cb_2021_36_bg_500k.zip
                   - Select "New York State" from shapefile dropdown menu 
               
               - Counties - 1:500,000 (national)
                   - File name: cb_2021_us_county_500k.zip
                   - National file is only available
               
               - County Subdivisions - 1:500,0000 (state)
                   - File name: cb_2021_36_cousub_500k.zip
                   - Select "New York State" from shapefile dropdown menu

- Water wells data from the New York GIS Clearinghouse
    - Data on locations of water wells across New York State (last updated June 2021)
        - Notes:
            - Dataset excludes well data from Nassau, Suffolk, Kings, and Queens counties (DEC Region 1)
            - Data points may fall outside Census designated boundaries because of partial address data
    - File name: WellWaterProgram.zip
    - How to access:
        1. Visit the New York GIS Clearinghouse at https://gis.ny.gov/gisdata/inventories/details.cfm?DSID=1203
        2. Under the "Data Set Name" column of the table, click "Water Wells", and save the zip file to the repository

 - Solar project data from the NY-Sun Solar Program
    - Data on completed solar projects from 2000-2021 in New York State
    - File name: Statewide_Solar_Projects__Beginning_2000.csv
    - How to access: 
        1. Visit the Open NY Data Portal at https://data.ny.gov/Energy-Environment/Statewide-Solar-Projects-Beginning-2000/wgsj-jt5f
        2. Click "Export" and select "CSV"

### Scripts and Files

1. Run solar_projects_county.py
    - Imports and cleans Statewide_Solar_Projects__Beginning_2000.csv, preparing it for use in the mapping stage of the repository
    - Returns numbers on the number of solar projects:
        - In New York State, by county
        - In Schenectady County, by town and by year
    - Removes all variables except
        - County
        - Project ID
        - Interconnection Date
        - Number of Projects
    - Generates a clean version of the original data, solar.csv
    
2. Open groundwater_solar_mapping.qgz
    - Generates the .PNG map outputs using the Census, water well, and solar project data
    - Imports and filters Census shapefiles to desired state, counties, and block groups, generating new layers:
        - County_Schenectady_NewYork
            - Schenectady County boundary layer
            - Formed from filtering cb_2021_us_county_500k.shp to the state level and the county level
        - Countysub_Schenectady_NY
            - Schenectady County subdivision boundary layer
            - Formed from filtering cb_2021_36_cousub_500k.shp to the county level
        - Countyblockgroup_Schenectady_NewYork
            - Schenectady County block group boundary layer
            - Formed from filtering cb_2021_36_bg_500k.shp to the county level
    - Imports and filters Water Well Program data shapefile to the county level
    - Imports and filters solar.csv file generated in Step 1 to the appropriate county level
    
### Outputs

- solar.csv: a cleaned version of Statewide_Solar_Projects__Beginning_2000.csv
- Map Image Files
    - NYS_Schenectady County_BlockGroups.png: shows a map of New York State with county boundaries, with Schenectady County highlighted in brown and displaying the block groups of that county
    - WaterWellProgram_NYS_County.png: shows a map of New York State with county boundaries, overlaid with well location data
    - WaterWellProgram_NYS_Schenectady County_Towns_BlockGroups.png: shows a map of Schenectady County with county subdivision (towns and cities) and block group boundaries, overlaid with well location data
    - SolarFarm_NYS_County.png: shows a map of New York State with county boundaries, overlaid with solar farm data
    - SolarFarm_NYS_Schenectady County_Towns_BlockGroups.png: shows a map of Schenectady County with county subdivision (towns and cities) and block group boundaries, overlaid with solar farm data 

## Main Findings

### New York State Overview:

Number of Completed Solar Projects in New York State 2000-2021: 165,336
County with Most Completed Solar Projects: 
Year with Highest Number of Solar Projects Completed:

### Schenectady County:

Number of Completed Solar Projects in
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
