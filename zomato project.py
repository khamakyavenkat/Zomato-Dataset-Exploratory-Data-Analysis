#!/usr/bin/env python
# coding: utf-8

# # Q:1

# # read_csv()

# In[2]:


import pandas as pd
df = pd.read_csv('zomato dataset.csv')
df


# # info()

# In[4]:


import pandas as pd
df = pd.read_csv('zomato dataset.csv')
df.info()


# # Q:2

# # isnull().sum()

# In[7]:


import pandas as pd 

df = pd.read_csv('zomato dataset.csv')

missing_values = df.isnull().sum()

print("Number of missing values in each column:")

print(missing_values)


# # Q:3

# # describe()

# In[10]:


import pandas as pd 

df = pd.read_csv('zomato dataset.csv')

summary = df.describe()

summary


# # Q:4

# # select_dtypes()

# In[16]:


import pandas as pd

df = pd.read_csv('zomato dataset.csv')

categorical_columns =  df.select_dtypes(include=['object','category']).columns
categorical_columns


# # Q:5

# # countplot()

# In[42]:


import pandas as ps
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('zomato dataset.csv')

plt.figure(figsize=(14,6))

sns.countplot(data = df)
plt.title('zomato dataset')
plt.xlabel('Count')


# # Q:6

# # histplot()

# In[40]:


import pandas as pd  
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('zomato dataset.csv')

sns.histplot(df['Aggregate rating'] , bins = 20 )

plt.title("RATING")


# # Q:7

# # scatter plot()

# In[35]:


import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

df = pd.read_csv('zomato dataset.csv')

sns.scatterplot(x='Aggregate rating' , y='Votes' , data=df)

plt.title('Relationship between Aggregate rating and Votes ')
plt.xlabel('Aggregate rating')
plt.ylabel('Votes')


# # Q:8

# # Barplot()

# In[34]:


import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('zomato dataset.csv')

plt.figure(figsize=(14,6))

sns.barplot(x='Aggregate rating' , y='Votes' , data=df)

plt.title('Relationship between Aggregate rating and Votes ')
plt.xlabel('Aggregate rating')
plt.ylabel('Votes')


# # Q:9

# In[39]:


import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 

df = pd.read_csv('zomato dataset.csv')

plt.figure(figsize=(15,5))

sns.boxplot(x='Aggregate rating' , y='Votes' , data=df)

plt.show()


# # Q:10

# In[55]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('zomato dataset.csv')

print(df.isnull().sum())

df = df.dropna(subset=['Aggregate rating', 'Votes'])
df


# In[ ]:




