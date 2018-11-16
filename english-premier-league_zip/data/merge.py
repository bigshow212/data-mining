#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 06:23:15 2018

@author: mukul
"""
import pandas as pd
import numpy as np


# =============================================================================
# print(data.head())
# 
# data2 = pd.read_csv("season-1011_csv.csv")
# 
# print(data2.head())
# =============================================================================



# =============================================================================
# teams = data['team'].tolist()
# print(teams)
# =============================================================================
def merge_all_seasons():
    data = pd.read_csv("season-0910_csv.csv")
    num = 10
    for i in range(8):
        filename = "season-"+str(num) + str(num+1) +"_csv.csv"
        data2 = pd.read_csv(filename)
        data = data.append(data2)
        num += 1
    
    output_file = "merged_seasons.csv"
    data.to_csv(output_file, sep=',')

def form_of_teams():
    col_names = ['teams','res1','res2','res3','res4','res5','key']
    data = pd.DataFrame(columns = col_names)
    data2 = pd.read_csv("merged_seasons.csv")
    number_rows = len(data2.index) - 1
    print(number_rows)
    teams  = data2['HomeTeam'].tolist()
    teams = list(set(teams))
    for i in np.arange(0,len(teams)):
        data.loc[i] = [teams[i],1,1,1,1,1,1]
        
    for i in  np.arange(0, number_rows):
        home = data2.iat[i,2]
        home_result = 1
        away_result = 1
        away = data2.iat[i,3]
        if(data2.iat[i,6]=='A'):
            home_result  = 0
            away_result = 3
        elif(data2.iat[i,6]=='H'):
            home_result = 3
            away_result = 0
        key = list(data.loc[data['teams'] == home,'key'])
        if (key[0] == 1):
            data.loc[data['teams'] == home,'res1'] = home_result
        if (key[0] == 2):
            data.loc[data['teams'] == home,'res2'] = home_result
        if (key[0] == 3):
            data.loc[data['teams'] == home,'res3'] = home_result
        if (key[0] == 4):
            data.loc[data['teams'] == home,'res4'] = home_result
        if (key[0] == 5):
            data.loc[data['teams'] == home,'res5'] = home_result
        data.loc[data['teams'] == home,'key'] = (key[0])%5+1
            
        key = list(data.loc[data['teams'] == away,'key'])
        
        if (key[0] == 1):
            data.loc[data['teams'] == away,'res1'] = away_result
        if (key[0] == 2):
            data.loc[data['teams'] == away,'res2'] = away_result
        if (key[0] == 3):
            data.loc[data['teams'] == away,'res3'] = away_result
        if (key[0] == 4):
            data.loc[data['teams'] == away,'res4'] = away_result
        if (key[0] == 5):
            data.loc[data['teams'] == away,'res5'] = away_result
        
        data.loc[data['teams'] == away,'key']= (key[0])%5+1
        
    print(data.head())
    
def main():
    print("start")

# =============================================================================
#     merge_all_seasons()
# =============================================================================
    form_of_teams()


if __name__ == "__main__":
	main()
# =============================================================================
#     teams = list(set(teams))
#     print(len(teams))
# =============================================================================
    #print(data2.team) 
    
# =============================================================================
# print(data3.head())
# col_names = list(data3)
# col_names = ['team','points']
# output_df = pd.DataFrame(columns = col_names)
# teams = data3.HomeTeam.unique()
# print(teams)
# number_rows = len(teams)
# for i in  np.arange(0, number_rows):
#     output_df.loc[i] = [teams[i],0]
# print(output_df)
# =============================================================================
# =============================================================================
# 
# for i in np.arange(0, len(data3)):
#     if(data3.iat[i,3]>data3.iat[i,4]):
#         print("home_wins")
#         home = data3.iat[i,1]
#         output_df.loc[output_df.team == home, 'points'] += 3
# =============================================================================
# =============================================================================
#     elif(data3.iat[i,3]<data3.iat[i,4]):
#         print("away_wins")
#         away = data3.iat[i,2]
#         output_df.loc[output_df.team == away, 'points'] += 3
#     else:
# =============================================================================
# =============================================================================
#         home = data3.iat[i,1]
#         away = data3.iat[i,2]
#         output_df.loc[output_df.team == home, 'points'] += 1
#         output_df.loc[output_df.team == away, 'points'] += 1
# =============================================================================

    
        