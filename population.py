# -*- coding: utf-8 -*-
"""
Created on Sun May  1 19:09:51 2022

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

co-est2021-alldata

# =============================================================================
# #%%
# 
# ## Setting up the variable list 
# 
# var_info=pd.read_csv('census-variables.csv')
# 
# var_name=var_info['variable'].to_list()
# 
# var_list=['NAME']+var_name
# 
# var_string=','.join(var_list)
# 
# #%%
# 
# ## API Call for ACS 2020 5 Year Data
# 
# api = 'https://api.census.gov/data/2020/acs/acs5'
# 
# for_clause='county:*'
# 
# in_clause='state:36'
# 
# key_value='85274c1d9323d846593ef42b16dc7ae9ea883936'
# 
# payload={'get':var_string,'for':for_clause, 'in':in_clause, 'key':key_value}
# 
# response=requests.get(api,payload)
# 
# if response.status_code==200:
#     print( '\n' )
#     print( 'url:', response.url )
# else:
#     print( 'status:', response.status_code )
#     print( response.text )
#     assert False
# 
# row_list=response.json()
# colnames=row_list[0]
# datarows=row_list[1:]
# 
# attain=pd.DataFrame(columns=colnames, data=datarows)
# attain.set_index('NAME', inplace=True)
# 
# attain.to_csv('census_data.csv')
# =============================================================================
