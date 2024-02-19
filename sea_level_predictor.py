import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv("epa-sea-level.csv")


    # Create scatter plot
    x=df["Year"]
    y=df["CSIRO Adjusted Sea Level"]

    fig,ax = plt.subplots(figsize=(12,12))
    ax=plt.scatter(x,y)

    # Create first line of best fit
    reg=linregress(x,y)
    x_forecast=pd.Series(([i for i in range(1850,2051)]))
    y_forecast=reg.slope*x_forecast+reg.intercept
    plt.plot(x_forecast,y_forecast,"r")

    df_forc=df.loc[df["Year"]>=2000]
    new_x=df_forc["Year"]
    new_y=df_forc["CSIRO Adjusted Sea Level"]


    # Create second line of best fit
    new_reg=linregress(new_x,new_y)
    new_x_forecast=pd.Series(([i for i in range(2000,2051)]))
    new_y_forecast=new_reg.slope*new_x_forecast+new_reg.intercept
    plt.plot(new_x_forecast,new_y_forecast,"orange")


    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()