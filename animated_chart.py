#!/usr/bin/env python
# coding: utf-8

# In[93]:


import pandas as pd


# In[94]:


df = pd.read_excel("C:/Users/firas/Desktop/GDP.xlsx")
df.head()


# In[95]:


df_pivot = df.pivot(index=df.columns[0], columns=df.columns[1], values=df.columns[2])
df_pivot.head()


# In[96]:


df_pivot.head()


# In[97]:


import warnings
warnings.filterwarnings("ignore", message="FixedFormatter should only be used together with FixedLocator")


# In[101]:


import bar_chart_race as bcr
import warnings

warnings.filterwarnings("ignore", message="FixedFormatter should only be used together with FixedLocator")

bcr.bar_chart_race(df_pivot, filename='C:/Users/firas/Desktop/animated_chart.mp4', fixed_max=True,
                   steps_per_period=10, period_length=750, title='GDP by Country', dpi=300)
print ("animated chart created")


# In[ ]:




