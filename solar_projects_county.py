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

## Reading in data and setting the index to the project ID

pd.read.csv("Statewide_Solar_Projects_Beginning_2000.csv", index="Project ID")




