#!/usr/bin/env python
# coding: utf-8

# In[1]:


sum=0
count=1
while count <=10:
    sum=sum+count #sum += count
    count+=1
print('1+2+3+...+10=',sum)


# # 銀行利息規範

# In[2]:


x = 10000
year = 0
while x < 20000:
    year +=1
    x=x * 1.0104
print(str(year),'年後，存款金額加倍')


# # 帳號密碼程式

# In[3]:


id='tony'
pwd='1234'
while True:
    x=input('請輸入帳號:')
    y=input('請輸入密碼:')
    if(x==id and y==pwd):
        print('歡迎登入')
        break
    else:
        print('帳號/密碼輸入錯誤')


# # break, continue,pass範例

# In[4]:


mylist=['C#','Python','java','C++']
for i in mylist:
    if i == 'java':
        break
    else:
        print(i)


# In[5]:


import random
for i in range(0,10):
    print(random.random())


# In[6]:


for i in range(0,10):
    print(random.randint(1,9))


# In[7]:


import random
number=random.randint(1,99)
while True:
    guess=input('請輸入1-99的數字(q離開):')
    if guess =='q':
        print('離開遊戲,正確數字是',number)
        break
    else:
        if number==int(guess):
            print('恭喜,猜對了')
            break
        else:
            print('猜錯了')


# # numpy套件

# In[8]:


a_list=[1,2,3,4,5]
print(a_list*3)


# # numpy套件ndarray型態，提供eLement-wise的操作

# In[9]:


import numpy as np
a_ndarray=np.array([1,2,3,4,5])
print(a_ndarray*3)
print(type(a_ndarray))
print(a_ndarray.ndim) #ndarray的維度
print(a_ndarray.shape) #ndarray的shape
print(a_ndarray.dtype) #ndarray的資料型態


# In[10]:


z=np.zeros(6)
print(z)# 六個元素都為0的1d ndarray
print(np.zeros((2,6))) #12個援助都為0的2d ndarray
print(np.empty((2,6,2))) #24個元素都未初始化的值 長,寬,RGB
print(np.arange(10)) #10個元素都維0-9的1d ndarray


# In[11]:


my_array=np.arange(10)
print(my_array)
print(my_array[0])
print(my_array[0:5])


# # 2維ndarray取值

# In[12]:


my_2d_array = np.array([np.arange(0,5),np.arange(5,10)])
print(my_2d_array)
print(my_2d_array[1,:]) #第二列資料
print(my_2d_array[:,1]) #第二欄資料
print(my_2d_array[1,1]) #第二列第二欄資料


# In[13]:


#假設有六個組別"Modern Web", "DevOps","CLoud","Big Data","Security","自我挑戰組"
#其參加人數分別為56,8,19,14,6,71人
groups=["Modern Web", "DevOps","Cloud","Big Data","Security","自我挑戰組"]
ironman=[56,8,19,14,6,71]
groups_array=np.array(groups)
ironman_array=np.array(ironman)
print(groups_array)
print(ironman_array)


# # 用人數去篩選組別

# In[14]:


print(ironman_array >=10)
print(groups_array[ironman_array >=10])
print(groups_array != "自我挑戰組")
print(ironman_array[groups_array != "自我挑戰組"])


# # Ndarray轉置

# In[15]:


my_1d_array=np.arange(10)
print(my_1d_array)
my_2d_array=my_1d_array.reshape((2,5))
print(my_2d_array)
print(my_2d_array.T)


# In[16]:


print(np.arange(24).reshape(4,6))


# # ndarray nan(空值)

# In[17]:


nan_array=np.array([56,8,19,14,6,np.nan])
print(nan_array)


# # 第六章

# In[53]:


import pandas as pd
import numpy as np
groups = ["Modern Web","DevOps",np.nan,"Cloud","Big Data", "Security","自我挑戰組"]
ironmen = [59,9,19,14,6,77,np.nan]
ironmen_dict={
    "groups":groups,
    "ironmen":ironmen
}
ironmen_df = pd.DataFrame(ironmen_dict)

print(ironmen_df.loc[:,"groups"].isnull())
print(ironmen_df.loc[:,"ironmen"].notnull())

ironmen_df


# In[41]:


print(ironmen_df.ndim)
print(ironmen_df.shape)
print(ironmen_df.dtypes)


# In[44]:


print(ironmen_df.sum())
print(ironmen_df.ironmen.sum())
print(ironmen_df.mean())
print(ironmen_df.median)
print(ironmen_df.describe())


# In[56]:


a=ironmen_df.dropna()
b=ironmen_df.fillna(0)
c=ironmen_df.ironmen.fillna(ironmen_df.ironmen.mean)
#空值補平均數


# In[58]:


a


# In[59]:


b


# In[60]:


c


# In[61]:


import pandas as pd
groups = ["Modern Web","DevOps","Cloud","Big Data", "Security","自我挑戰組"]
ironmen = [59,9,19,14,6,77]
# 建立data frame
ironmen_df = pd.DataFrame(ironmen,columns=["ironmen"],index=groups)
ironmen_df.sort_index()


# In[62]:


ironmen_df.sort_values(by = "ironmen")


# In[ ]:




