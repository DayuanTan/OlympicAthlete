#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 21:57:46 2018

@author: dyt
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import os
os.chdir("/Users/dyt/Library/Mobile Documents/com~apple~CloudDocs/1myfiles/coursera/PythonOlympic/useful")

# read data
df = pd.read_excel("奥运运动员数据.xlsx", sheet_name = 1)
data = df[["height","gender"]]

# data screening
data_male = data[data["gender"] == "男"]
data_female = data[data["gender"] == "女"]

data_male_hgmean = data_male["height"].mean()
data_female_hgmean = data_female["height"].mean()

# display
plt.figure(figsize = (10,6))
sns.distplot(data_male["height"], hist = False, kde = True, rug = True,
             rug_kws = {"color":"y", "lw":2, "alpha":0.5, "height":0.1},
             kde_kws = {"color":"y", "lw":2, "linestyle":"--"},
             label = "male height",
             )
sns.distplot(data_female["height"], hist = False, kde = True, rug = True,
             rug_kws = {"color":"g", "lw":2, "alpha":0.5},
             kde_kws = {"color":"g", "lw":2, "linestyle":"--"},
             label = "female height",
             )

# diaplay height mean
plt.axvline(data_male_hgmean, color = "y", linestyle = ":", alpha = 0.8)
plt.text(data_male_hgmean+1, 0.005, 'male athlete height mean: %0.2f cm' % (data_male_hgmean), color = "y", size = 14)

plt.axvline(data_female_hgmean,color = "g", linestyle = ":", alpha = 0.8)
plt.text(data_female_hgmean+1, 0.0035, "female athlete height mean: %0.2f cm" % data_female_hgmean, color = "g", size =14)

plt.grid(linestyle = "-.", alpha = 0.7)
plt.title("Athlete height.")

plt.savefig("pic1.png",dpi=1000)
print("finished.")
