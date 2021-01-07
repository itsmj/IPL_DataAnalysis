#Analysing performance of Rohit Sharma in the listed year in dataset.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('deliveries.csv')#reading dataset
df.head()

fil = df['batsman']=='RG Sharma' #batsman rohit sharma
df_rg = df[filt]
df_rg['dismissal_kind'].value_counts() #gives type of dismissala of player

df_rg['dismissal_kind'].value_counts().plot.pie() #pie plot of dismissals


def count(df,runs):
    return len(df[df['batsman_runs']==runs]) #no of sixes by using function

count(df_rg,1) #passing 1 as rum type willgive no. of 1's hit by rohit
count(df_rg,2)
count(df_rg,3)
count(df_rg,4)
count(df_rg,5)
count(df_rg,6)

def count(df,runs):
    return len(df[df['batsman_runs']==runs])*runs#no of runs by sixes


slices =[1379, 354, 15, 1416, 5, 1038] #these are no. of 1,2,3,4,5,6 hit by rohit 
labels = [1,2,3,4,5,6] #passing label
explode=[0,0,0,0.1,0,0] #exploding no. of 4's area
plt.pie(slices,labels=labels,autopct= '%1.1f&&', explode=explode) #plotting pie chart shown in readme.
