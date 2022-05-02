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

## Reading in data

solar=pd.read_csv("Statewide_Solar_Projects__Beginning_2000.csv")
solar=solar.set_index('County')
#%%

## plotting number of solar projects per county and over time

project_count=solar['Number of Projects']
print(project_count.sum())
print(project_count['Schenectady'].sum())

date_project=solar['Interconnection Date']
print(date_project['Schenectady'])

solar['Year']=pd.DatetimeIndex(solar['Interconnection Date']).year
print(solar['Year'])


