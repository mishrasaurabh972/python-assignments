#!/usr/bin/env python
# coding: utf-8

# In[1]:


list1 = [0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]
new_list = []

while list1:
    minimum = list1[0]  
    for x in list1: 
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    list1.remove(minimum)    

c = new_list.count(0)
list2 = new_list[0:c]
list3 = new_list[c:]
list4 = list3+list2
print(list4)


# In[ ]:




