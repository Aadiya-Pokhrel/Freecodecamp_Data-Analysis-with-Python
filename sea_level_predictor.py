#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


# In[8]:


def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(20,10))
    ax.scatter(x="Year", y="CSIRO Adjusted Sea Level", alpha=0.8, data=df)

    # Create first line of best fit
    
    years=pd.Series(range(1880,2051))
    slope, intercept, r_value, p_value, std_err = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    ax.plot(years, intercept + slope*years, 'r', color='m', label='First line of best fit', data=df)

    # Create second line of best fit
    
    years2=pd.Series(range(2000,2051))
    df2= df.loc[df['Year']>=2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df2["Year"], df2["CSIRO Adjusted Sea Level"])
    ax.plot(years2, intercept2 + slope2*years2, 'r', color='r', linestyle='dashed', label='First line of best fit', data=df)

    # Add labels and title
    
    plt.title("Rise in Sea Level", fontsize= 20)
    plt.xlabel('Year', fontsize= 15)
    plt.ylabel('Sea Level (inches)', fontsize= 15)
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()


# In[9]:


draw_plot()


# In[ ]:




