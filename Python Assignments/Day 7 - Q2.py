#!/usr/bin/env python
# coding: utf-8

# In[25]:


list1 = [(1,2), (3,4), (5,6),(4,5)]
finallist = []
for tuple in list1:
     list1 = list(tuple)
     summ = 0
     for m in list1:
         summ+=m
     finallist.append(summ)
    
print(finallist)


# In[ ]:




