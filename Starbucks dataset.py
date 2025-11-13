#!/usr/bin/env python
# coding: utf-8

# In[53]:


import pandas as pd 

drink_menu_df = pd.read_csv("/Users/blah/Downloads/starbucks_drinkMenu_expanded.csv")
drink_nutrition_df = pd.read_csv("/Users/blah/Downloads/starbucks-menu-nutrition-drinks.csv")

# initially gave UnicodeDecodeError (Some files from Kaggle, etc use encodings like utf-16, latin1, or ISO-8859-1) fixed error with , encoding="utf-16"
menu_nutrition_df = pd.read_csv("/Users/briannacarlisle/Downloads/starbucks-menu-nutrition-food.csv", encoding="utf-16") 

print ("_____________________")
print("\n Menu Items")
print ("_____________________\n")
print (drink_menu_df.head(5))

print ("_____________________")
print("\n Drink Menu Nutrition")
print ("_____________________\n")
print(drink_nutrition_df.head(5))

print ("_____________________")
print("\n Food Menu Nutrition")
print ("_____________________\n")
print(menu_nutrition_df.head(5))


# In[50]:


# df.info() - gives summary of data's structure (# of rows, columns and column names and data types, # of non null values)
print ("__________________")
print("\nDrink Menu Info")
print ("__________________\n")
drink_menu_df.info()

print ("__________________")
print("\nDrink Nutrition Info")
print ("__________________\n")
drink_nutrition_df.info()

print ("__________________")
print("\nMenu Nutrition Info")
print ("__________________\n")
menu_nutrition_df.info()


# In[56]:


# df.describe() - column (non null) count, column average, column standard deviation, minimum value in column,
# 25% percentile, 50% percentile, 75% percentile, maximum value in column

print("Drink Menu")
print ("_____________________")
drink_menu_df.describe()


# In[57]:


print("Drink Nutrition")
print ("_____________________")
drink_nutrition_df.describe()


# In[58]:


print("Menu Nutrition")
print ("_____________________")
menu_nutrition_df.describe()


# In[61]:


#any null(missing) values?
drink_menu_df.isnull().values.any()


# In[62]:


drink_nutrition_df.isnull().values.any()


# In[63]:


menu_nutrition_df.isnull().values.any()


# In[64]:


#only one dataset had missing values

#how many missing values?
drink_menu_df.isnull().sum()


# In[ ]:


# Removing Missing Values (dropna) vs. Filling Missing Values (fillna)


# When to remove:
# The missing data is sparse (only a few rows are missing)
# The column isn’t critical, or you have enough other data
# Removing the row won’t bias your analysis

# When to fill:
# The column is important, and you can reasonably estimate the missing values
# You want to keep all rows
# The missing values are numeric or categorical and a reasonable default exists

# Fill missing values with mean (numerical) and mode (categorical)


# In[92]:


#removing missing data

drink_menu_df = drink_menu_df.dropna(subset=['Beverage_category', 'Beverage', 'Beverage_prep'])


# In[93]:


drink_menu_df.isnull().values.any()


# In[102]:





# In[ ]:




