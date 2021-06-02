#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Title: Matplotlib Example Code I
Date: 28MAY2021
Author: John Koenig
Purpose: Provide example code for simple matplotlib plots
    - Scatterplot
    - Line Plot
    - Bar Plot
    - Horizontal Bar Plot
    
Inputs: 
Outputs: 
Notes:
     For Data Visalization Class (Regis University)
     Summer 2021
    
'''

#%%
# import libraries

import os

import pandas as pd
import matplotlib.pyplot as plt

dpi = 300

# if you are on windows, you are going to have to change the file path to
# windows style
project_dir = r'/home/md33a/Python Projects/matplotlib1_examples/'
#project_dir = os.getcwd() + 'matplotlib1_examples/'
data_dir = project_dir + r'data/'

#%%
# Horizontal Bar Chart - Hospitals
# Data Source: Homeland Infrastructure Foundation-Level Data (HIFLD)
# https://hifld-geoplatform.opendata.arcgis.com/datasets/6ac5e325468c4cb9b905f1728d6fbf0f_0

df1_filename = 'Hospitals.csv'
df1 = pd.read_csv(data_dir + df1_filename)
df1_head = df1.iloc[:100,:]
columns = list(df1.columns)


state_counts = df1['STATE'].value_counts(ascending=True)
states = pd.Series(list(state_counts.index))
state_counts.index = range(len(state_counts))

# create horizontal bar chart
fig, ax = plt.subplots(figsize=(6,8))

ax.barh(states, state_counts)
ax.set_title('Count of Hospitals by State')
ax.set_xlabel('Hostpital Count')
ax.set_ylabel('State')
ax.set_yticklabels(states, fontsize=7)

plt.tight_layout()


plot1_filename = 'Hospitals.png'
fig.savefig(project_dir + plot1_filename, dpi=dpi)


#%%
# Scatterplot - Culture by City
# Data Source: Greater London Authority
# https://data.london.gov.uk/dataset/global-city-data

labels_visible = ["London",
                  "Amsterdam",
                  "Beijing",
                  "Berlin",
                  #"Chicago",
                  "Dubai",
                  "Frankfurt",
                  "Geneva",
                  "Guangzhou",
                  "Hamburg",
                  "Helsinki",
                  #"Ho Chi Minh City",
                  "Hong Kong",
                  "Houston",
                  "Istanbul",
                  #"Jakarta",
                  "Jerusalem",
                  #"Karachi",
                  #"Kolkata",
                  "Lima",
                  "Los Angeles",
                  "Madrid",
                  #"Manila",
                  "Mexico City",
                  "Moscow",
                  #"Mumbai",
                  "New York City",
                  #"Oslo",
                  "Paris",
                  "Prague",
                  "Rio de Janeiro",
                  "San Francisco",
                  "Sao Paulo",
                  "Seoul",
                  "Shanghai",
                  #"Shenzhen",
                  "Singapore",
                  "St. Petersburg",
                  #"Stockholm",
                  "Sydney",
                  "Taipei",
                  "Tokyo"]

label_up = ["Shanghai",
            "Dubai",
            "Moscow",
            "Houston",
            "Frankfurt",
            "Seoul"]

label_down = ["Prague",
              "Taipei",
              "Jerusalem",
              "Helsinki"]

df2_filename = 'museums_culture_by_city_v1.csv'
df2 = pd.read_csv(data_dir + df2_filename)
df2_head = df2.iloc[:100,:]
columns = list(df2.columns)

# create scatterplot
fig, ax = plt.subplots(figsize=(12,8))

labels = df2.iloc[:,0]
x = df2.iloc[:,1]
y = df2.iloc[:,2]

ax.scatter(x.values, y.values, alpha=.5)
ax.set_title('Musuems and Cultural Orgs by City')
ax.set_xlabel('Museums')
ax.set_ylabel('Cultural Organizations')

# create data labels
x_cutoff = 60
y_cutoff = 250

x_offset = (x.max() - x.min()) * .01
y_offset = (y.max() - y.min()) * .01

for index, label in labels.iteritems():
    
    if label in labels_visible:
        if label == "Madrid":
            ax.annotate(label, (x[index], y[index] + y_offset * 1.5))
        elif label in label_up:
            ax.annotate(label, (x[index] + x_offset, y[index] + y_offset))
        elif label in label_down:
            ax.annotate(label, (x[index] + x_offset, y[index] - y_offset))
        else:
            ax.annotate(label, (x[index] + x_offset, y[index]))

plt.tight_layout()

plot2_filename = 'museums_culture_by_city_v1.png'
fig.savefig(project_dir + plot2_filename, dpi=dpi)


#%%
# Line Plot - Top Selling Video Games by Year and Lifetime Sales (as of 2019)
# Data Source: kaggle.com
# https://www.kaggle.com/gregorut/videogamesales

label_big_up = ['Call of Duty: Modern Warfare 3',
                'Grand Theft Auto: Vice City',
                'Super Mario Land 2: 6 Golden Coins',
                'Gran Turismo 3: A-Spec']

label_up = ['Call of Duty: Modern Warfare 3',
            'Call of Duty: Black Ops II']

label_down = ['Grand Theft Auto V',
              'Call of Duty: Black Ops 3',
              'Donkey Kong Country 2: Diddy\'s Kong Quest',
              'Super Mario All-Stars']

df3_filename = 'vgsales.csv'
df3 = pd.read_csv(data_dir + df3_filename).dropna(0, subset=['Year'])
df3_head = df3.iloc[:100,:]
columns = list(df3.columns)

# sort data by year
sorted_df = df3.sort_values(['Year', 'Global_Sales'])
sorted_df = sorted_df[sorted_df['Year'] <= 2017]      # remove data after 2017
sorted_df.index = range(len(sorted_df))

# find year ticks/labels
previous_year = 1900
x_ticks = []
x_labels = []
early_years = [1980, 1990, 1995]

y = sorted_df['Global_Sales'].values

for index, row in sorted_df.iterrows():
    year = int(row[3])
    
    if year != previous_year:
        if year >= 1995 or year in early_years:
            x_ticks.append(index)
            x_labels.append(year)
    
    previous_year = year

# create line plot
fig, ax = plt.subplots(figsize=(16,8))

ax.plot(sorted_df['Global_Sales'].values)
ax.set_title('Top Selling Video Games by Year and Lifetime Sales (as of 2019)', fontsize=18)
ax.set_xlabel('Year of Release - Sorted by Lifetime Sales', fontsize=12)
ax.set_xticks(x_ticks)
ax.set_xticklabels(x_labels, rotation=45)
ax.set_ylabel('Lifetime Sales', fontsize=12, labelpad=1.5)
ax.set_yticklabels(['$0', '$0', '$20', '$40', '$60', '$80'], fontsize=12)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# annotate top games
previous_year = 1900
sales_cutoff = 10
y_offset = (y.max() - y.min()) * .01

for index, row in sorted_df.iterrows():
    year = int(row[3])
    
    if year != previous_year:
        if sorted_df.iloc[index - 1, 10] > sales_cutoff or previous_year >= 1995:
            game_title = sorted_df.iloc[int(index) - 1, 1]
            
            if game_title in label_big_up:
                ax.annotate(game_title, (index - 1, sorted_df.iloc[index - 1, 10] + y_offset * 2))
            elif game_title in label_up:
                ax.annotate(game_title, (index - 1, sorted_df.iloc[index - 1, 10] + y_offset))
            elif game_title in label_down:
                ax.annotate(game_title, (index - 1, sorted_df.iloc[index - 1, 10] - y_offset))
            else:
                ax.annotate(game_title, (index - 1, sorted_df.iloc[index - 1, 10]))
    
    previous_year = year

plt.tight_layout()

plot3_filename = 'vgsales.png'
fig.savefig(project_dir + plot3_filename, dpi=dpi)


#%%
# Bar Plot - Heavy Metal Bands
# Data Source: kaggle.com
# https://www.kaggle.com/rtatman/fun-beginner-friendly-datasets


df4_filename = 'metal_bands_2017.csv'
df4 = pd.read_csv(data_dir + df4_filename).drop_duplicates(['band_name'])
df4_head = df4.iloc[:100,:]
columns = list(df4.columns)


# clean data
country_series = df4['origin'].value_counts()

x_cutoff = 50

country_series = country_series.iloc[:x_cutoff]
country_series = country_series.sort_values(ascending=True)

# create bar plot
x = list(country_series.index)
y = country_series.values

fig, ax = plt.subplots(figsize=(8,10))

ax.barh(x, y)

ax.set_title('Number of Heavy Metal Bands by Country', fontsize=18)
ax.set_xlabel('Total Heavy Metal Bands', fontsize=12)
ax.set_ylabel('Country', fontsize=12, labelpad=1.5)
ax.set_yticklabels(list(country_series.index), fontsize=8)

plot4_filename = 'metal_bands_2017.png'
fig.savefig(project_dir + plot4_filename, dpi=dpi)


#%%
# Line Plot - CFPB Credit History
# Data Source: data.world
# https://data.world/adamhelsinger/cfpb-credit-card-history

df5_filename = 'CFPB_data.csv'
df5 = pd.read_csv(data_dir + df5_filename)
df5_head = df5.iloc[:100,:]
columns = list(df5.columns)


# create bar plot
labels = ['New Credit Cards', 'Dollar Volume on New Cards']

x = df5['Month'].values
y = df5.iloc[:,1:]

fig, ax = plt.subplots(figsize=(8,10))
ax.axhline(0, xmin=0, xmax=df5['Month'].max(), color='black')

handles = ax.plot(x, y)  # I need to save references to the handles so I can fix the legend

ax.set_title('New Credit Cards Count and Dollar Volume - Percent Change YoY', fontsize=14)
ax.set_xlabel('Month Number', fontsize=12)
ax.set_ylabel('Percent Change (Year Over Year)', fontsize=12, labelpad=1.5)

ax.legend(handles, labels, loc='lower right')



plot5_filename = 'CFPB_data.png'
fig.savefig(project_dir + plot5_filename, dpi=dpi)




































