
# coding: utf-8

# ___
# # Ecommerce Purchases Data - 
# 
# Please excuse anything that doesn't make "Real-World" sense in the dataframe, all the data is fake and made-up.
# 

# In[84]:


import pandas as pd


# In[86]:


ecom = pd.read_csv('Ecommerce Purchases')


# **Head of the DataFrame.**

# In[87]:


ecom.head()


# ** How many rows and columns are there? **

# In[88]:


ecom.info()


# ** Average Purchase Price **

# In[90]:


ecom['Purchase Price'].mean()


# ** Highest and lowest purchase prices **

# In[92]:


ecom['Purchase Price'].max()


# In[93]:


ecom['Purchase Price'].min()


# ** Number of people have English 'en' as their Language of choice on the website **

# In[94]:


ecom[ecom['Language']=='en'].count()


# ** Number of people have the job title of "Lawyer" **
# 

# In[95]:


ecom[ecom['Job'] == 'Lawyer'].info()


# ** How many people made the purchase during the AM and how many people made the purchase during PM ? **
# 

# In[96]:


ecom['AM or PM'].value_counts()


# ** The 5 most common Job Titles are - **

# In[97]:


ecom['Job'].value_counts().head(5)


# ** Someone made a purchase that came from Lot: "90 WT" , what was the Purchase Price for this transaction? **

# In[99]:


ecom[ecom['Lot']=='90 WT']['Purchase Price']


# ** What is the email of the person with the following Credit Card Number: 4926535242672853 **

# In[100]:


ecom[ecom["Credit Card"] == 4926535242672853]['Email'] 


# ** How many people have American Express as their Credit Card Provider *and* made a purchase above $95 ?**

# In[101]:


ecom[(ecom['CC Provider']=='American Express') & (ecom['Purchase Price']>95)].count()


# ** Hard: How many people have a credit card that expires in 2025? **

# In[102]:


sum(ecom['CC Exp Date'].apply(lambda x: x[3:]) == '25')


# ** Hard: What are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...) **

# In[56]:


ecom['Email'].apply(lambda x: x.split('@')[1]).value_counts().head(5)


# # Great Job!
