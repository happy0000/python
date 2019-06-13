#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
url="http://storage.googleapis.com/2017_ithome_ironman/data/iris.csv"

iris_df = pd.read_csv(url)
iris_df.head()


# In[4]:


iris_df.mean()


# In[5]:


iris_df['Sepal.Length'].median()


# # 本地端載入

# In[9]:


import pandas as pd
iris_df = pd.read_csv('iris.csv')
iris_df.head()


# # excel檔案載入

# In[10]:


import pandas as pd
url="http://storage.googleapis.com/2017_ithome_ironman/data/iris.xlsx"

iris_df = pd.read_excel(url)
iris_df.head()


# # CH8

# # 自訂函數

# In[11]:


import math

def circle(radius):
    area = radius * radius * math.pi
    return area
print(circle(10))


# In[12]:


import math

def circle(radius):
    area = radius * radius * math.pi
    return area

r=input("請輸入圓ㄉ半徑:")
print("圓面積為:",circle(float(r)))


# # 由小到大

# In[13]:


import random

def exchange_sort(input_list):
    a=input_list
    for i in range(0,len(input_list)-1):
        for j in range(i+1,len(input_list)):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]
    return a
my_vector = random.sample(range(0,100),10)
print(my_vector)
print(exchange_sort(my_vector))


# # 由大到小

# In[14]:


import random

def exchange_sort(input_list):
    a=input_list
    for i in range(0,len(input_list)-1):
        for j in range(i+1,len(input_list)):
            if a[i]<a[j]:
                a[i],a[j]=a[j],a[i]
    return a
my_vector = random.sample(range(0,100),10)
print(my_vector)
print(exchange_sort(my_vector))


# In[ ]:




