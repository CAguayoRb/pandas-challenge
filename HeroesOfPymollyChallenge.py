#!/usr/bin/env python
# coding: utf-8

# # Heroes Of Pymolly

# In[4]:


#!pip install pandas


# In[1]:


# Dependencies and Setup.
import pandas as pd
import os

# File to Load.
cvs_path = os.path.join("purchase_data.csv")
# cvs_path = "Resources/purchase_data.csv" 

# Read Purchasing File and store into Pandas data frame
purchase_data_df = pd.read_csv(cvs_path)
purchase_data_df.head()

#purchase_data_df = pd.read_csv(cvs_path,)
#purchase_date_df.head()


# In[2]:


#Player Count, dispaly the total number of players.
#Get value of how many players.
total = purchase_data_df["Gender"].value_counts()
total


# In[4]:


#Purchasing Analysis (Total).
#Run basic calculations to obtain # of unique items, average price, number of purchases and total revenue.
#Create a summary data frame to hold the results.
#Give data a cleaner formatting. Optional.
#Display summary data frame.

items_count = len(purchase_data_df["Item ID"].unique())
average_price = purchase_data_df["Price"].mean()
purchase_count = purchase_data_df["Purchase ID"].value()
total_revenue = df['Price'].sum()

summary_df = pd.DataDrame({"Number of Unique Items": [items_count],
                          "Average Price": [average_price],
                          "Number of Purchases": [purchase_count],
                          "Total Revenue": [total_revenue]})
summary_df


# In[16]:


#Gender demographics. 
#Get the values of Gender. Percentage and Count of Male players, Female players and Other/Non-disclosed.
#gender_count = purchase_data_df["Gender"].value_counts()
total = purchase_data_df["Gender"].value_counts()
total

purchase_datagender_df = {
        "Gender": ["Male", "Female", "Other/Non Discolsed"]
         "Total" : [652, 113, 15]
                                }
dfg1 = purchase_datagender_df (dfg1,
                              columns = ["Gender",
                                          "Total"])


dfg1[percent] = (purchase_datagender_df["Gender"]/ 
                 df["Gender"].sum())*100

print dfg1

#summary2_df = pd.DataDrame({"Total Count": [],
                          #"Percentage of Players": []})
#summary2_df


# In[12]:


#Purchasing Analysis (Gender).
#Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender. 
#Create a summary data frame to hold the results. 
#Give displayed data a cleaner formatting. Optional.

purchase_count =
avg_purchase_price =
total_purchase_value =
avg_purchase_total_pperson =

summary3_df = pd.DataDrame({"Purchase Count": [purchase_count],
                          "Average Purchase Price": [avg_purchase_price],
                          "Total Purchase Value": [totak_purchase_value],
                          "Avg Total Purchase per Person": [avg_purchase_total_pperson]})
summary3_df


# In[ ]:


#Age Demographics:
#Establish bins for ages.
#bins = [>10, 10-14, 15-19, 20-24, 25-29, 30-34, 35-39, 40+]
bins = [0, 9.9, 14.9, 19.9, 24.9, 29.9, 34.9, 39.9]
names = [>10, 10-14, 15-19, 20-24, 25-29, 30-34, 35-39, 40+]

#Categorize the existing players using the age bins. Hint: use pd.cut()
df[purchase_data_age]= pd.cut(df["Age"], bins, label=names,)

#Calculate the numbers and percentages by age group.
len(purchase_data['SN'].unique())

purchase_countt = purchase_data["Age Group", "SN"]]
print(pdd.head())
percentage_players = pdd.groupby(["Age Group"])
percentage_players['Age Group'].count()

#Create a summary data frame to hold the results.
#Round the percentage column to two decimal points. Optional.
#Display Age Demographics Table.

summary4_df = pd.DataDrame({"Total Count": [purchase_countt],
                          "Percentage of Players": [percentage_players]})

summary4_df                           


# In[ ]:


#Purchasing Analysis (Age).
#Bin the purchase_data data frame by age.
bins = [0, 9.9, 14, 19, 24, 29, 34, 39]
names = [>10, 10-14, 15-19, 20-24, 25-29, 30-34, 35-39, 40+]

#Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below.
#Create a summary data frame to hold the results
#Give the displayed data cleaner formatting. Optional.
#Display the summary data frame.

purchase_count_pa = 
avg_purchase_price_pa =
total_purchase_value_pa =
avg_totalpperson_pa =


summary5_df = pd.DataDrame({"Purchase Count": [purchase_count_pa],
                          "Average Purchase Price": [avg_purchase_price_pa],
                          "Total Purchase Value": [total_purchase_value_pa],
                          "Avg Total Purchase per Person": [avg_totalpperson_pa]})
summary5_df


# In[ ]:


#Top Spenders
#Run basic calculations to obtain the results.
#Create a summary data frame to hold the results
#Sort the total purchase value column in descending order
#Optional: give the displayed data cleaner formatting
#Display a preview of the summary data frame.

purchase_count_ts =
avg_purchase_price_ts =
total_purchasevalue_ts =


summary6_df = pd.DataDrame({"Purchase Count": [purchase_count_ts],
                          "Average Purchase Price": [avg_purchase_price_ts],
                          "Total Purchase Value": [total_purchasevalue_ts]})
summary6_df


# In[ ]:


#Most Popular Items

#Retrieve the Item ID, Item Name, and Item Price columns
#Group by Item ID and Item Name. Perform calculations to obtain purchase count, average item price, and total purchase value
#Create a summary data frame to hold the results
#Sort the purchase count column in descending order
#Optional: give the displayed data cleaner formatting
#Display a preview of the summary data frame.


summary7_df = pd.DataDrame({"Item ID": [],
                          "Item Name": [],
                          "Purchase Count": [],
                          "Item Frame": [],
                           "Total Purchase Value": []})
summary7_df


# In[ ]:


#Most Profitable Items
#Sort the above table by total purchase value in descending order
#Optional: give the displayed data cleaner formatting
#Display a preview of the data frame.


summary8_df = pd.DataDrame({"Item ID": [],
                          "Item Name": [],
                          "Purchase Count": [],
                           "Total Purchase Value": []})
summary8_df

