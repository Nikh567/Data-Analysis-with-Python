#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np, pandas as pd, matplotlib.pyplot as plt, seaborn as sns, os


# In[2]:


os.getcwd()
os.chdir('C:\\Users\\mycsv\\')


# In[4]:


dg=pd.read_csv('BigMartSalesData.csv')
dg


# In[5]:


dg.describe(include='all')


# In[6]:


dg.info()


# In[7]:


dg.isnull().any()


# In[8]:


dg.isnull().sum()


# In[9]:


list(dg)


# In[10]:


dg['InvoiceNo'].value_counts()


# In[11]:


dg['InvoiceNo'].head(10)


# In[12]:


dg['InvoiceNo'].describe()


# In[13]:


dg['InvoiceNo'].isna().sum()


# In[14]:


dg['Description'].describe()


# In[17]:


dg['Description'].isnull().sum()


# In[20]:


dg.median()


# In[22]:


dg.shape


# In[24]:


dg['Description'].unique()


# In[27]:


dg['Description'].value_counts()


# In[29]:


type(dg)


# In[31]:


type(dg['InvoiceNo'])


# In[32]:


dg['InvoiceNo'].dtype


# In[33]:


dg['Amount'].dtype


# In[34]:


dg['Quantity'].dtype


# In[35]:


dg.info()


# In[40]:


dg['Day']=pd.to_datetime(dg['Day'])
dg['Month']=pd.to_datetime(dg['Month'])
dg['Year']=pd.to_datetime(dg['Year'])


# In[41]:


dg.info()


# In[42]:


dg['Description'].mode()


# In[45]:


dg.mode()


# In[48]:


dg['Description'].iloc[0]


# In[50]:


dg['Description'].fillna(dg['Description'].mode().iloc[0],inplace=True)


# In[52]:


dg['Description'].isnull().sum()


# In[54]:


dg.isnull().sum()


# In[56]:


dg['CustomerID'].dtype


# In[58]:


dg['CustomerID'].value_counts()


# In[61]:


dg['CustomerID'].mean()


# In[64]:


dg['CustomerID'].fillna(dg['CustomerID'].mean(),inplace=True)


# In[66]:


dg['CustomerID'].isnull().sum()


# In[67]:


dg.info()


# In[69]:


dg[dg.duplicated()]


# In[71]:


dg_corr=dg.corr()


# In[72]:


dg_corr


# In[74]:


plt.figure(dpi=135,facecolor='violet')
sns.heatmap(dg_corr,annot=True)


# In[79]:


dg[dg.loc[:,'Quantity']>500]


# In[82]:


dg[['Amount']].tail(20)


# In[84]:


dg2=sum(dg.loc[:,'Amount'])


# In[85]:


dg2


# In[87]:


dg2=dg.loc[:,['Amount','Quantity']]
dg2


# In[3]:


df=pd.read_csv('HollywoodMovies.csv')
df


# In[4]:


df.isnull().any()


# In[5]:


df[df['LeadStudio'].isnull()]


# In[6]:


df[['LeadStudio']]


# In[7]:


df['LeadStudio'].mode()


# In[8]:


df['LeadStudio'].value_counts()


# In[9]:


df['LeadStudio'].fillna(df['LeadStudio'].mode().loc[0],inplace=True)


# In[10]:


df['LeadStudio'].isnull().any()


# In[11]:


df.isnull().sum()


# In[12]:


df['RottenTomatoes'].mean()


# In[13]:


df['RottenTomatoes'].isnull().sum()


# In[14]:


df['RottenTomatoes'].fillna(df['RottenTomatoes'].median(),inplace=True)


# In[18]:


df['Story'].fillna(df['Story'].mode().loc[0],inplace=True)


# In[19]:


df.isnull().sum()


# In[20]:


df['Genre'].fillna(df['Genre'].mode().loc[0],inplace=True)


# In[21]:


df.info()


# In[24]:


df[df['ForeignGross']==0]


# In[46]:


df['ForeignGross'].fillna(df['ForeignGross'].mean(),inplace=True)
df['AudienceScore'].fillna(df['AudienceScore'].median(),inplace=True)
df['TheatersOpenWeek'].fillna(df['TheatersOpenWeek'].mean(),inplace=True)
df['OpeningWeekend'].fillna(df['OpeningWeekend'].median(),inplace=True)
df['BOAvgOpenWeekend'].fillna(df['BOAvgOpenWeekend'].mean(),inplace=True)
df['WorldGross'].fillna(df['WorldGross'].median(),inplace=True)
df['Budget'].fillna(df['Budget'].mean(),inplace=True)
df['Profitability'].fillna(df['Profitability'].mean(),inplace=True)
df['OpenProfit'].fillna(df['OpenProfit'].mean(),inplace=True)


# In[47]:


df['OpenProfit']


# In[48]:


df.isnull().sum()


# In[51]:


df['ForeignGross'].replace(0,df['ForeignGross'].mean(),inplace=True)


# In[52]:


df[df['ForeignGross']==0]


# In[61]:


lab=df['Genre']
plt.figure(dpi=125)
plt.bar(x=df['Profitability'],height=lab,data=df)
plt.xlim(0,50)


# In[66]:


plt.figure(dpi=200)
sns.swarmplot(x=df['Genre'],y=df['Budget'],data=df)
plt.xlim(left=7)


# In[ ]:





# In[ ]:




