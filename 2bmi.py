#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 13:52:08 2018

@author: dyt
"""

import numpy as np # numpy is for number calculation
import pandas as pd # panda is for data processing based on numpy
import matplotlib.pyplot as plt # matplotlib is python 2D plot tool
import seaborn as sns # seaborn is visualization tool based on matplotlib

import os
os.chdir("/Users/dyt/Library/Mobile Documents/com~apple~CloudDocs/1myfiles/coursera/PythonOlympic/useful")

# read data
rawdata = pd.read_excel('奥运运动员数据.xlsx', sheetname = 1, header = 0)
data = rawdata[['name', 'event', 'height', 'weight']]

# drop nan
data.dropna(inplace = True)

# drop events which has two few numbers 
event_number = data['event'].value_counts()
event_wantdrop = event_number[event_number<15].index[0] # figure out which one is less than 15
data2 = data[data['event'] != event_wantdrop] # drop it

# calculate BMI = weight / (height using meter)^2
data2['BMI'] = data2['weight'] / (data2['height'] / 100)**2 

# label range of BMI
data2['BMI_range'] = pd.cut(data2['BMI'], 
                             [0, 18.5, 24, 28, 10000],
                             labels = ['Thin', 'Normal', 'Strong', 'Extremely Strong'])

## begin draw picture
# set picture style 
sns.set_style('ticks') # "white", "dark", "whitegrid", "darkgrid", "ticks"

# set picture size
plt.figure(figsize = (8,5))

# choose violin figure
sns.violinplot(x = 'event', y = 'BMI', data = data2, # set x, y axis labels and data
                scale = 'count', # more members, more wider the violin will be
                palette = 'hls', # colors. 'reds', 'blues'
                inner = 'quartile') # display quartile in inner zone

# add dots inside
sns.swarmplot(x = 'event', y = 'BMI', data = data2, color = 'w', alpha = 0.7, s = 2)

# add grid inside
plt.grid(linestyle = '--')

plt.title("Athlete's BMI")
plt.xlabel('Events')
plt.ylabel('BMIs')

plt.savefig('pic2_BMI.png', dpi = 800)