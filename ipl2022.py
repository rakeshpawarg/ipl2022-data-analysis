#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('IPL2022PlayerAuction_List_Sets.csv')


# In[3]:


df.columns


# In[15]:


df.shape


# In[4]:


df.info()


# In[17]:


df.describe()


# In[5]:


import seaborn as sns
sns.histplot(df.Age,kde=True)


# In[14]:


#df['Player Name']=df['First Name']+' '+df['Surname']


# In[16]:


#df=df.rename(columns={'First Name1':'First Name1'})


# In[18]:


#df['First Name1']=df['First Name1']+' '+df['Surname']


# In[22]:


#df=df.drop('Surname',axis=1)
#df=df.drop('Surname',axis=1)


# In[23]:


#df=df.drop('Player Name',axis=1)


# In[25]:


df=df.rename(columns={'First Name1':'Player Name'})


# In[26]:


df


# In[32]:


df.drop(603,axis=0,inplace=True)


# In[33]:


df


# In[52]:


df.isnull().sum()


# In[56]:


import matplotlib.pyplot as plt


# In[61]:


plt.figure(figsize=(,55))
pie=df.groupby(['Country']).count().plot(kind='pie',radius=2,y='Set No.')


# In[70]:


#import seaborn as sns
df.groupby(by='State Association')['Set No.'].count()


# In[81]:


df.groupby(by='Specialism')['Set No.'].count()


# In[82]:


sns.countplot(y='Specialism',data=df)


# In[83]:


df.columns


# In[86]:


df=df.rename(columns={'Unnamed: 10':'Right/left'})


# In[87]:


df['Right/left']


# In[ ]:


w=0.4
x=["All rounder","Bowler","W-keeper","Batsmen"]
men=(22, 30, 35, 35, 26)
women=(25, 32, 30, 35, 29)
bar1=np.arange(len(x))
bar2=[i+w for i in bar1]
plt.bar(bar1,men,w,label="men")
plt.bar(bar2,women,w,label="women")
plt.xticks(bar1+w/2,x)
plt.show()


# In[89]:


df1=pd.DataFrame({'All rounder':[227],'Bowler':[215],'W-Keeper':[59],'Batsmen':[102]})
df1


# In[92]:


df1.plot.bar()
plt.xlabel("Specilazation")
plt.ylabel("Counts")


# In[98]:


df.groupby(by='Right/left')['Set No.'].count()


# In[106]:


423+180


# In[97]:


pie=df.groupby(['Right/left']).count().plot(kind='pie',radius=2,y='Set No.')


# In[103]:


df.columns


# In[105]:


df.loc[(df['Right/left']=='RHB'),['Player Name','Country']]


# In[108]:


df.columns


# In[111]:


df[['Player Name','IPL']].sortby


# In[115]:


a=df.sort_values(by=['Age'], ascending=False)


# In[119]:


df[['Age']].min()


# In[ ]:




