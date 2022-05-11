# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 08:16:09 2022

@author: mrkev
"""

import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns
import numpy as np
import scipy
import json
import requests
#%%

## Reading in data and trimming the dataset to generate solar.csv

solar=pd.read_csv("Statewide_Solar_Projects__Beginning_2000.csv",dtype={'County':str})
solar_trim=solar[["County",'Project ID',"Interconnection Date",'Number of Projects']]
solar_trim=solar_trim.set_index('County')
solar_trim.to_csv('solar.csv')
#%%

# Counts of Solar Projects

#generating the total count of completed solar projects in New York State from 2000-2021

project_count=solar_trim['Number of Projects'].sum()
print(project_count.sum())


print(project_count['Schenectady'].sum())
sch_tot=project_count['Schenectady'].sum()

#%%
date_project=solar_trim['Interconnection Date']
print(date_project['Schenectady'])

solar_trim['Year']=pd.DatetimeIndex(solar_trim['Interconnection Date']).year
print(solar_trim['Year'])

#%%

#%%
for c in solar_trim['County']:
    solar_trim['Number of Projects'].sum
    
    
#%%

#solar=solar.drop(solar['Data Through Date','Utility','City/Town','Zip','Division','Substation','Circuit ID','Developer','Metering Method','Estimated PV System Size (kWdc)','PV System Size (kWac)','Estimated Annual PV Energy Production (kWh)','Energy Storage System Size (kWac)']
#{'Zip':str,'Estimated PV System Size (kWdc)':int,'Estimated Annual PV Energy Production (kWh)':int}

#print(solar['Year'].sum(project_count['Schenectady']))
#%%
#drawing a figure showing change in number of projects per county and over time
fig1, ax1=plt.subplots(dpi=300)
solar.plot.barh("County","Number of Projects",ax=ax1)
ax1.set_title('Number of Solar Projects per County, 2000-2021')
fig1.tight_layout()
fig1.savefig('projects_by_county.png',dpi=300)