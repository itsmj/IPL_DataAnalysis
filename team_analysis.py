#All the results is from used dataset and queries are performed in jupiter notebook.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('matches.csv')
df.head()

df.shape[0] #result will give total matches played by all teams

len(df['city'].unique()) #total no.of all venues where matches played

df['team1'].unique() #total teamsnames who played matches

len(df['team1'].unique())#no of teams who played matches

df['player_of_match'].value_counts()#gives count of player of match

df['toss_winner'].value_counts()#count of team wins toss

df['win_by_runs'].max()#gives maximum margin win by runs of a team 


filter= df['win_by_wickets'].max()
df[df['win_by_wickets']==filter] #showing dataframe of maximum margin win by by wickets of a team

sns.countplot(x='season', hue="toss_decision",data=df)#gives a plot between field or bat selected bya ateam view at readme.

df['toss_winner'].value_counts().plot(kind='bar')#graph of no. of toss win by teams shon in readme

df['season'].value_counts()#no of all matches played in seasons

sns.countplot(df['season'])#graph of above shown

def season_wins(df,team_name):
    return df[df['winner']==team_name]['season'].value_counts()#gives count of season wise winning of teams


season_wins(df,'Mumbai Indians').plot(kind='bar') #plotting graph of mumbai indians all wins in different seasons shown in readme file.
