# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 08:16:09 2022

@author: mrkev
"""

import geopandas as gpd
import pandas as pd

#%%

## Reading in data and trimming the dataset to generate solar.csv

solar_org=pd.read_csv("Statewide_Solar_Projects__Beginning_2000.csv",dtype={'County':str})
solar_trim=solar_org[["County",'Project ID',"Interconnection Date",'Number of Projects']]
#solar_trim=solar_trim.set_index('County')
solar_trim.to_csv('solar.csv')
#%%

## Reading in county FIPS code data as a .txt file

county_fips=pd.read_csv('st36_ny_cou.txt',sep=",",header=None,names=['STATE','STATEFP','COUNTYFP','COUNTYNAME','CLASSFP'],dtype=str)
county_fips[['County','Geography']]=county_fips['COUNTYNAME'].str.split(" ",n=1,expand=True)
print(county_fips)

#%%

## Merging solar.csv with county FIPS codes

solar=pd.read_csv('solar.csv',dtype=str)

solar=solar.merge(county_fips, on='County', how='left', validate=1:1,)

#%%

## Sending solar.csv to a geopackage for joining onto the shapefiles in QGIS

### Trimming the dataframe again

solar_geo_trim=solar_trim[['County','Number of Projects']]

### joining onto the county shapefile

solar_geo=gpd.read_file('cb_2021_us_county_500k.zip')

solar_geo=solar_geo.merge(solar_geo_trim,on='County',how='left',validate='m:1', indicator=True)

print(solar_geo['_merge'].value_counts())

solar_geo=solar_geo.drop(columns='_merge')

solar_geo.to_file('solar_geo.gpkg',layer="solar_trim",index=False)

#%%

# Counts of Solar Projects

#generating the total count of completed solar projects in New York State from 2000-2021

project_count=solar_trim['Number of Projects'].sum()
print(project_count.sum())

