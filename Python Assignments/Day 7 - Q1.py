#!/usr/bin/env python
# coding: utf-8

# In[25]:


port1 = {21: "FTP", 22:"SSH", 23: "telnet", 80: "http"}
i = port1.keys()
j = port1.values()
port2 = dict(zip(j,i))
print("Port2 = ", port2)


# In[ ]:




