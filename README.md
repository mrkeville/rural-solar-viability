# rural-solar-viability

Author: Mary Rachel Keville

## Description of Repository

### Purpose

The purpose of this repository is to compile data on groundwater and solar farms in Upstate New York. 

In particular, this repository focuses on understanding the proxmity of individual water wells on private property to **existing** solar projects. Solar farms are an up-and-coming source of clean energy, which is vital to the nation's adoption of clean energy initatives. However, solar farms pose their own environmental drawbacks - land is often clear cut to make way for the panels, and the panels themselves are coated in chemicals that could contaminate the local groundwater. Groundwater is a vital source of freshwater for millions in the United States, and many who live in rural areas rely on wells to access groundwater. The construction of solar farms could threaten the potability of the groundwater resources of rual areas.

The goal of this repository is not to dissuade rural stakeholders and decisionmakers from adopting solar energy, but to provide information crucial to making informed choices on the construction of solar farms for the best possible environmental and public health outcomes.

### Inputs

- Cartographic boundary data from the US Census Bureau
    - Files:

       - Census Block Groups - 1:500,000 (state)
           - File name: cb_2021_36_bg_500k.zip
           - Select "New York State" from shapefile dropdown menu 
       
       - Counties - 1:500,000 (national)
           - File name: cb_2021_us_county_500k.zip
           - National file is only available
       
       - County Subdivisions - 1:500,0000 (state)
           - File name: cb_2021_36_cousub_500k.zip
           - Select "New York State" from shapefile dropdown menu
    - How to access:
        1. Visit the US Census Bureau: https://www.census.gov/geographies/mapping-files/time-series/geo/cartographic-boundary.html
        2. Select the "2021" tab
        3. Scroll to each geography type's section on the page, select "New York" from the shapefile dropdown menu, and save the zip file to the repository:

- County FIPS Code Data from the US Census Bureau
    - File name: st36_ny_cou.txt
    - How to access:
        1. Vist the US Census Bureau: https://www.census.gov/library/reference/code-lists/ansi.html#county
        2. Scroll to "County and County Equivalents" and select "New York" from the dropdown menu
        3. A .txt file will open in the browser; save that as a .txt file to the repository
      
- Water wells data from the New York GIS Clearinghouse
    - File name: WellWaterProgram.zip
    - Data on locations of water wells across New York State (last updated June 2021)
        - Notes:
            - Dataset excludes well data from Nassau, Suffolk, Kings, and Queens counties (DEC Region 1)
            - Data points may fall outside Census designated boundaries because of partial address data
    - How to access:
        1. Visit the New York GIS Clearinghouse at https://gis.ny.gov/gisdata/inventories/details.cfm?DSID=1203
        2. Under the "Data Set Name" column of the table, click "Water Wells", and save the zip file to the repository

 - Solar project data from the NY-Sun Solar Program
    - File name: Statewide_Solar_Projects__Beginning_2000.csv
    - Data on completed solar projects from 2000-2021 in New York State
    - How to access: 
        1. Visit the Open NY Data Portal at https://data.ny.gov/Energy-Environment/Statewide-Solar-Projects-Beginning-2000/wgsj-jt5f
        2. Click "Export" and select "CSV"

### Scripts and Project Files

1. Run solar_projects_county.py
    - Inputs:
        - Statewide_Solar_Projects__Beginning_2000.csv
        - st36_ny_cou.txt
        - cb_2021_us_county_500k.zip
    - Returns numbers on the number of solar projects in New York State
    - Generates a clean version of the original data, solar.csv
    - Imports NYS county FIPS codes and joins onto solar.csv for mapping
    - Generates a geopackage with solar projects and county variables
    
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
    - Imports solar_geo.gpkg file generated in Step 1 
    
### Outputs

- solar.csv: a cleaned version of Statewide_Solar_Projects__Beginning_2000.csv with county FIPS code data joined
- solar_geo.gpkg: a geopackage joining solar farm data onto the county shapefile
- Map Image Files
    - NYS_Schenectady County_BlockGroups.png: shows a map of New York State with county boundaries, with Schenectady County highlighted in brown and displaying the block groups of that county
    - WaterWellProgram_NYS_County.png: shows a map of New York State with county boundaries, overlaid with well location data
    - WaterWellProgram_NYS_Schenectady County_Towns_BlockGroups.png: shows a map of Schenectady County with county subdivision (towns and cities) and block group boundaries, overlaid with well location data
    - SolarFarm_NYS_County.png: shows a map of New York State with county boundaries, overlaid with solar farm data

## Main Findings

### New York State Overview:

Number of Completed Solar Projects in New York State 2000-2021: 165,336
County with Most Completed Solar Projects: Suffolk County (43,451)

### Schenectady County:

Number of Completed Solar Projects in Schenectady County 2000-2021: 2,336
Ranking for Number of Solar Projects in NYS: #15
Town/City within Schenectady County with Most Completed Solar Projects: Schenectady, NY
Year with Highest Number of Solar Projects Completed: 2015

### Analysis of Maps

The analysis of the NYS map overlaid with the water well data shows that a majority of the non-urban areas in the state have pre-existing wells for groundwater (with a notable dearth in the Adirondack Region).
Drilling down to Schenectady County, a good deal of the county is covered by water wells. Overlaying the block group boundaries with the county subdivisions provides an indicator of urban vs rural area in this county - the City of Schenectady has more block groups of a smaller land area (indicating a higher population). Taking block groups as an indicator of population size, they gradually becoming larger in area moving towards the north and west of the city. As the number of block groups decreases, the number of well locations generally increases, supporting the idea that rural areas are more reliant on groundwater drawn from wells than their urban neighbors.
Zooming back out to the state level, we can see that while the number of solar farms constructed over the past couple of decades are numerous, the majority are concentrated in the major urban areas of the state (ie. New York City/Long Island). However, other areas of the state are growing in solar farm capacity - the Capital Region and Erie County have a significant amount of solar projects, especially in comparison to its neighboring regions. It's especially notable that these are areas of greater urbanization, yet similar metropolitan areas in the middle of the state don't have as many solar farms per county.
Further analysis at the subdivsion and block group level is needed to better understand the impacts of existing solar farms on rural areas with respect to groundwater, but at a county level, the bulk of solar farm construction is confined to urban areas.

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
