import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np
def draw_plot():
  # Read data from file
  df = pd.read_csv("epa-sea-level.csv");

    
  # Create scatter plot
  plt.scatter(x=df['Year'],y=df['CSIRO Adjusted Sea Level'])
  plt.xlim([1850,2075])
  
  # Create first line of best fit
  slope, intercept, r, p, se = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
  x_vals = np.arange(df['Year'].min(),2051,1)
  y_vals = intercept + slope * x_vals
  plt.plot(x_vals, y_vals,'r')
  # Create second line of best fit
  slope, intercept, r, p, se = linregress(x=df['Year'].loc[df['Year'] >= 2000], y=df['CSIRO Adjusted Sea Level'].loc[df['Year'] >= 2000])
  x_vals = np.arange(2000,2051,1)
  y_vals = intercept + slope * x_vals
  plt.plot(x_vals, y_vals,'g')
  
  # Add labels and title
  plt.xlabel('Year')
  plt.ylabel('Sea Level (inches)')
  plt.title('Rise in Sea Level')
  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()