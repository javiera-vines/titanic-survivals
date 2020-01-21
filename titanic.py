#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 09:51:50 2020

@author: javieravines
"""
import pandas as pd
#to read a cvs file using a pandas
df = pd.DataFrame() 
df = pd.read_csv("/Users/javieravines/Downloads/Master Big Data Courses/Machine Learning with python/titanic_data_ESCP.csv")
print(df.head(5))

#import as data frame
print(df)
#1.
#how many people are in titanic and suurvivors
print(df['PassengerId'].dtypes)
#there are 1309 passangers
len(df[df["Survived"]==1]) #342 survivors

#2.How many that survived were female and how many that died were female.
len(df[df["Sex"]=="female"]) #466
len(df[(df["Sex"]=="female") & (df["Survived"]==1)]) #233

#3.How many children were on the titanic, NB: you are a child if age < 17.
len(df[df["Age"]<17]) #134

#4.How many children died that were on the ship
len(df[(df["Age"]<17) & (df["Survived"]==0)]) #45

#5. How many people had families with them
len(df[(df["Siblings - Spouse"]==1) & (df["Parents - Children"]==1)]) #90


#6. What is the ratio of female to male
len(df[df["Sex"]=="male"]) 
print(len(df[df["Sex"]=="female"])/len(df[df["Sex"]=="male"])) #ratio is 0,5528

#7. What contributed to the survival of those who survived

#I want to find correlation between survival variable and the rest of df,
#but some data are categorical and needs to be transformed into number

def f(row):
    if row['Sex'] == "female":
        val = 1
    else:
        val = 0
    return val

df['Sex2'] = df.apply(f, axis=1) #I create the column Sex2 for 1=female
print(df)

df2 = df #now df contains the original data and df2 will contain the data that is going to be correlated
#here I eliminate the columns that I do not want
df2= df2.drop(['PassengerId',"Name","Sex","Ticket", "Fare","Cabin"], axis = 1) 
print(df2)

#until here, is fine but I still need to change "one to many" the "Port of embarkation"
#first I change to shorter name
df2 = df2.rename(columns={"Port of embarkation": "PortEmb"})

#define one to many function
def g(row):
    if row["PortEmb"] == "S":
        va = 1
    elif row["PortEmb"] == "Q":
        va = -1
    else:
        va = 0 ##"C"
    return va
#create column one to many
df2["PortEmb2"] = df2.apply(g, axis=1) 
print(df2)
df2= df2.drop(["PortEmb"],axis =1) #and delete the string column
print(df2) #now here we only have numerical variables

print(df2.columns) #show variables
df2.corr() #correlation matrix.
#Sex has a 54% the correlation which is the highest value of correlation
#Because Survived=1 are survivors and female=1, positive correlation shows more woman survived.
print("hola javi")
