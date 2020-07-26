#!/usr/bin/env python
# coding: utf-8

# # 1 . [ 0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4] sort increasing order but all zeroes should be at right hand side.

# In[7]:


list1 = [0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]
list1.sort()
s=list1.count(0);
print(list1[s:]+list1[:s])


# # 2. list1=[10,20,40,60,70,80]  sorted list ;list2=[5,15,25,35,45,60] sorted list. Merge these two sorted list products one sorted list .

# In[9]:


list1 = [10,20,40,60,70,80]
list2 = [5,15,25,35,45,60]
Mrgd = list1+list2
sortedlist = []
for a in range(min(Mrgd),max(Mrgd)+1):
    if a in Mrgd:
        sortedlist.append(a)
print(sortedlist)


# In[ ]:




