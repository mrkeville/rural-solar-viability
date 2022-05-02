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

## Reading in census population data

pop=pd.read.csv("co-est2021-alldata.csv")

## filtering to New York State
nys = pop.query("STATE == '36'")

## dropping columns

nys = nys.drop(nys['UMLEV','REGION','DIVISION','ESTIMATEBASE2020','POPESTIMATE2020','NPOPCHG2020','NPOPCHG2021','BIRTHS2020','BIRTHS2021','DEATHS2020',	'DEATHS2021','NATURALCHG2020',	'NATURALCHG2021', 'INTERNATIONALMIG2020','INTERNATIONALMIG2021', 'DOMESTICMIG2020',	'DOMESTICMIG2021', 'NETMIG2020', 'NETMIG2021','RESIDUAL2020','RESIDUAL2021','GQESTIMATESBASE2020','GQESTIMATES2020', 'GQESTIMATES2021',	'RBIRTH2021','RDEATH2021','RNATURALCHG2021','RINTERNATIONALMIG2021', 'RDOMESTICMIG2021,	RNETMIG2021']

nys.to_csv('2021_est_nys.csv')
