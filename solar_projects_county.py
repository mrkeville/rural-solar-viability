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

#%%

## Reading in county FIPS code data as a .txt file

county_fips=pd.read_csv('st36_ny_cou.txt',sep=",",header=None,names=['STATE','STATEFP','COUNTYFP','COUNTYNAME','CLASSFP'],dtype=str)
county_fips[['County','Geography']]=county_fips['COUNTYNAME'].str.split(" ",n=1,expand=True)
county_fips=county_fips.drop(columns='Geography')
county_fips['GEOID']=county_fips['STATEFP']+county_fips['COUNTYFP']

print(county_fips)

#%%

## Grouping solar data by county

solar_groupcounty=solar_trim.groupby('County')
num_projects=['Number of Projects']
solar_grouped=solar_groupcounty[num_projects].sum()
solar_grouped=solar_grouped.sort_values(num_projects)

print(solar_grouped)

#%%

## Merging solar_trim with county FIPS codes

solar_grouped=solar_grouped.merge(county_fips, on='County', how='left', validate='1:1',indicator=True)
print(solar_grouped['_merge'].value_counts())
solar_grouped=solar_grouped.drop(columns='_merge')

print(solar_grouped)
solar_grouped.to_csv('solar.csv', index=False)

#%%

# Counts of Solar Projects

#generating the total count of completed solar projects in New York State from 2000-2021

project_count=solar_trim['Number of Projects'].sum()
print(project_count.sum())

#generating the total count of completed solar projects in Schenectady County from 2000-2021

sch_count=solar_trim.loc[solar_trim['County']=='Schenectady','Number of Projects'].sum()
print(sch_count)

#%%

## Sending solar.csv to a geopackage for joining onto the shapefiles in QGIS

### Trimming the dataframe again

solar_geo_trim=solar_grouped[['GEOID','Number of Projects']]

### joining onto the county shapefile

solar_geo=gpd.read_file('cb_2021_us_county_500k.zip')

solar_geo=solar_geo.merge(solar_geo_trim,on='GEOID',how='left',validate='1:m', indicator=True)

print(solar_geo['_merge'].value_counts())

solar_geo=solar_geo.drop(columns='_merge')

solar_geo.to_file('solar_geo.gpkg',layer="solar_org",index=False)