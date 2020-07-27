#!/usr/bin/env python
# coding: utf-8

# In[3]:


list1 = [1,2,3,4,5,7,8]
list2 = ["a", "b", "c", "d", "e"]
len1 = min(len(list1), len(list2))
dictnry = {}
for each in range(len1):
    dictnry[list1[each]]  = list2[each]
print(dictnry)


# In[ ]:




