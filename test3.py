import pandas as pd              #This is used to load .csv and perform analysis on the data
import matplotlib.pyplot as plt  #This is used for plotting

x=input("Please enter:\n 1 for PopChange.csv\n 2 for Housing.csv\n\n ")

#POPCHANGE:
if x==1:
   popchange=pd.read_csv("PopChange.csv") #loading .csv file into the dataframe(popchange)
   popchange_selected = popchange[["Pop Apr 1","Pop Jul 1", "Change Pop"]] 
   popchange_selected.hist(bins=50, figsize=(20,15)) 
   plt.show() 
   print(popchange_selected.describe())
#HOUSING:
if x==2:
   housing=pd.read_csv("Housing.csv")
   housing_selected=housing[["AGE", "BEDRMS", "BUILT", "ROOMS", "UTILITY"]] 
   housing_selected.hist(bins=50, figsize=(20,15))
   plt.show()  
   print(housing_slected.describe())