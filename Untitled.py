#!/usr/bin/env python
# coding: utf-8

# # numpy 套件
# 

# In[1]:


a_list = [1,2,3,4,5]
print(a_list*3)


# In[2]:


#nupy套件ndarray型態，提供eLement-wise的操作
import numpy as np
a_ndarray = np.array([1,2,3,4,5])
print(a_ndarray*3)


# In[3]:


print(type(a_ndarray))
print(a_ndarray.ndim) #ndarray的維度
print(a_ndarray.shape) #ndarray的shape
print(a_ndarray.dtype) #ndarray的資料型態


# In[5]:


z=np.zeros(6)
print(z) #六個元素都為0的 1d ndarray
print(np.zeros((2,6))) #12個元素都為0的 2d ndarray
print(np.empty((2,6,2))) #24個元素都未初始化的值
print(np.arange(10)) #10個元素維0-9的 1d ndarray
      


# In[6]:


my_array=np.arange(10)
print(my_array)
print(my_array[0])
print(my_array[0:5])


# In[ ]:




