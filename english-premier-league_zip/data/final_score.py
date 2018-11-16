#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 08:38:41 2018

@author: mukul
"""
import pandas as pd
import numpy as np

w = [1,1,1,1,1,1,1,1,1] #weight list for each season
print(w[0])

#getting total team names 
filename = "points season-0910_csv.csv"
data = pd.read_csv(filename)
num = 10
teams = data['team'].tolist()
print(teams)
for i in range(8):
    filename = "points season-"+str(num) + str(num+1) +"_csv.csv"
    data3 = pd.read_csv(filename)
    teams += data3['team'].tolist()
    teams = list(set(teams))
    print(len(teams))
    #print(data2.team) 
    num += 1    
    
data = pd.DataFrame(columns = ['teams','points'])
number_rows = len(teams)
for i in  np.arange(0, number_rows):
    data.loc[i] = [teams[i],0]

num = 10
filename = "points season-0910_csv.csv"
data2 = pd.read_csv(filename)
for i in np.arange(0, len(data2)):
    name = data2.iat[i,1]
    print(data2.iat[i,2])
    data.loc[data.teams == name, 'points'] += w[0]*data2.iat[i,2]

for j in range(8):
    filename = "points season-"+str(num) + str(num+1) +"_csv.csv"
    data2 = pd.read_csv(filename)
    for i in np.arange(0, len(data2)):
        name = data2.iat[i,1]
        data.loc[data.teams == name, 'points'] += w[j+1]*data2.iat[i,2]
    num += 1 
    
print(data)
output_file = "total_points.csv"
data.to_csv(output_file, sep=',')