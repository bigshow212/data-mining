#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 06:23:15 2018

@author: mukul
purpose: this file will create new file with total points corresponding
to each team in the season.
"""
import pandas as pd
import numpy as np
filename = "season-1718_csv.csv"
data = pd.read_csv(filename)

print(data.head())
col_names = list(data)
col_names = ['team','points']
output_df = pd.DataFrame(columns = col_names)
teams = data.HomeTeam.unique()
print(teams)
number_rows = len(teams)
for i in  np.arange(0, number_rows):
    output_df.loc[i] = [teams[i],0]

for i in np.arange(0, len(data)):
    home = data.iat[i,1]
    away = data.iat[i,2]
    if(data.iat[i,3]>data.iat[i,4]):
        #print("home_wins")
        output_df.loc[output_df.team == home, 'points'] += 3
    elif(data.iat[i,3]<data.iat[i,4]):
        #print("away_wins")
        output_df.loc[output_df.team == away, 'points'] += 3
    else:
        output_df.loc[output_df.team == home, 'points'] += 1
        output_df.loc[output_df.team == away, 'points'] += 1

print(output_df)
output_file = "points " + filename
output_df.to_csv(output_file, sep=',')
        