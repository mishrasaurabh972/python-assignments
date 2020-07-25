#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = int(input("Enter number:"))
number = n
addition = 0
while(number>0):
    addition+=number
    number = number-1
    print(addition)
print(f"The sum of the first {n} number is {addition}")

