#!/usr/bin/env python
# coding: utf-8

# In[4]:


list1=[(1,2,3),[1,2],["a","hit","less"]]
list2=list1[1]+list1[2]
list1=list(list1[0])
list1.append(list2)
print(list1)


# In[ ]:




