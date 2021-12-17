
"""
Bennett Thompson
Final Project Data Science
All data from dClimate API

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

#get mountain.csv data and clean data
def mountain():
    #use panda to read csv file
    moun_data = pd.read_csv("mountain_vectors.csv")
    
    #set variable 
    wind_u= moun_data["u-vector"]
    wind_v= moun_data["v-vector"]
    
    #Your given speed formula(Speed(single day observation)=
    # sqrt(wind_u(single day observation)^2 + wind_v(single day observation)^2))
    moun_data["Speed"] = np.sqrt((wind_u*wind_u) + (wind_v*wind_v))
    
    # Splits out only the actual date i.e. 2010-12 as a str without the hour time stamp
    # lambda function allows a short function to be defined without a name
    # .apply allow the users to pass a function and apply it on every single value 
    moun_data["only_date"] = moun_data['date'].apply(lambda 
                                                     date: "-".join
                                                     (str(date).split(" ")[0]
                                                      .split("-")[0:2]))   
    #View data after adding Speed column
    grouped_by_date_mou = moun_data.groupby('only_date').mean()
    
    print('Mountain Wind Farm Data:')
    print(grouped_by_date_mou.head)
    
    #mean
  

    
    #convert date to date format
    grouped_by_date_mou["date"] = pd.to_datetime(grouped_by_date_mou.index)
    #create date_ordinal column and change date to ordinal
    grouped_by_date_mou['date_ord'] = grouped_by_date_mou["date"].map(
        dt.datetime.toordinal)
    print(grouped_by_date_mou.head)
    
    
    
    return grouped_by_date_mou
mountain_data = mountain()
    

#get ocean.csv data and clean data     
def ocean():
    #use panda to read csv file
    ocean_data = pd.read_csv("ocean-wind.csv")
   
    #set variable
    wind_u=ocean_data["u-value"]
    wind_v=ocean_data["v-value"]
    
    #Your given speed formula(Speed(single day observation)=
    #sqrt(wind_u(single day observation)^2 + wind_v(single day observation)^2))
    ocean_data["Speed"] = np.sqrt((wind_u*wind_u) + (wind_v*wind_v))
    
    # Splits out only the actual date i.e. 2010-12 as a str without the hour time stamp
    # lambda function allows a short function to be defined without a name
    # .apply allow the users to pass a function and apply it on every single value 
    ocean_data["only_date"] = ocean_data['date'].apply(
        lambda date: "-".join(str(date).split(" ")
        [0].split("-")[0:2])) 
    
    #View data after adding Speed column
    grouped_by_date_ocean = ocean_data.groupby('only_date').mean()
    
    print('Ocean Wind Farm Data:')
    print(grouped_by_date_ocean)
    
    

    #convert date to date format
    grouped_by_date_ocean["date"] = pd.to_datetime(grouped_by_date_ocean.index)
    #create date_ordinal column and change date to ordinal
    grouped_by_date_ocean['date_ord'] = grouped_by_date_ocean["date"].map(
        dt.datetime.toordinal)
    print(grouped_by_date_ocean.head)

    return grouped_by_date_ocean
    
ocean_data = ocean()

#get field.csv data and clean data
def field():
    #use pandas read file
    f_data = pd.read_csv("field_vectors.csv")
    
    #set variable
    wind_u=f_data["u-value"]
    wind_v=f_data["v-value"]
    
    #Your given speed formula(Speed(single day observation)=
    # sqrt(wind_u(single day observation)^2 + wind_v(single day observation)^2))
    f_data["Speed"] = np.sqrt((wind_u*wind_u) + (wind_v*wind_v))
    
    # Splits out only the actual date i.e. 2010-12 as a str without the hour time stamp
    # lambda function allows a short function to be defined without a name
    # .apply allow the users to pass a function and apply it on every single value 
    f_data["only_date"] = f_data['date'].apply(lambda
                                date: "-".join(str(date).split(" ")
                                               [0].split("-")[0:2])) 
    
    #View data after adding Speed column and combine data
    grouped_by_date_field = f_data.groupby('only_date').mean()
    
    print('Field Wind Farm Data:')
    print(grouped_by_date_field)
    
    #convert date to date format
    grouped_by_date_field["date"] = pd.to_datetime(grouped_by_date_field.index)
    #create date_ordinal column and change date to ordinal
    grouped_by_date_field['date_ord'] = grouped_by_date_field["date"].map(
        dt.datetime.toordinal)
    
    
    print(grouped_by_date_field.head)
    
    return grouped_by_date_field
    
field_data = field()

#create a function to get scatter plot and regression line
def plot_regression(dataset = mountain_data,color = "red",title = "Mountain",
                    scatter = True,show = True,legend=["legend"]):
    
    #use seaborn library for graph
    ax = sns.regplot(data=dataset,
                     x="date_ord",scatter=scatter,
                     y="Speed",
                     line_kws = {"color": color})
    
    #set the x label as date
    ax.set_xlabel('Date')
    #use datetime library to change  format to year scale
    new_labels = [dt.datetime.fromordinal(int(item)).year 
                  for item in ax.get_xticks()]
    #change xstick to years
    ax.set_xticklabels(new_labels)
    #create a title for the graph
    ax.set_title(title)
    #creat a legend for the graph
    ax.legend(legend)
    #use if function to choose if we want combine lines in a graph 
    if show is True:
        plt.show()

#plot 3 scatters and regression graph for 3 sets of data
def plot_separate():
    
    #call plot_regression function to generate 3 sepepate graph
    plot_regression(dataset = mountain_data,color = "red",
                    title = "Mountain Winds Speed Data(10 years) ",
                       scatter = True,show = True,legend=["Mountain"])
    plot_regression(dataset = ocean_data,color = "green",
                    title = "Ocean Winds Speed Data(10 years) ",
                       scatter = True,show = True,legend = ["Ocean"])
    plot_regression(dataset = field_data,color = "purple",
                    title = "Field Winds Speed Data(10 years) ",
                       scatter = True,show = True,legend = ["Field"])
plot_separate()

#create a function to plot threes lines of regression together
def plot_linear_together():
    plot_regression(dataset = mountain_data,color = "red",
                    title = "Mountain Winds Speed Data(10 years)",
                       scatter = False,show = False)
    plot_regression(dataset = ocean_data,color = "green",
                    title = "Ocean Winds Speed Data(10 years)",
                       scatter = False,show = False)
    plot_regression(dataset = field_data,color = "purple",
                    title = "Three locations Winds Speed Data(10 years)",
                       scatter = False,show = False,
                       legend = ["Mountain","Ocean","Field"])
    
plot_linear_together()

#create a function to print out some key statistics
def key_stat(dataset=mountain_data,location="mountain",col ="Speed"):
    
    #print mean
    print(location ,"mean speed is:",dataset[col].mean())
    #print max
    print(location, "max speed is:",dataset[col].max())
    #print min
    print(location,"min speed is:",dataset[col].min())
    #print std
    print(location,"speed standard deviation is:",
          dataset[col].std())
    

#create a function to print keys statistics of three sets of data
def stat_summary():
    key_stat(dataset=mountain_data,location="mountain",col ="Speed")
    key_stat(dataset=ocean_data,location="ocean",col ="Speed")
    key_stat(dataset=field_data,location="field",col ="Speed")
stat_summary()
