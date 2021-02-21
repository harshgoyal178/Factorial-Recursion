#!/usr/bin/env python
# coding: utf-8

# In[10]:


def factorial(x):
    if x==1:
        return 1
    else:
        product=x*factorial(x-1)
        x=x-1
        return product

n=int(input())
p=factorial(n)
print(p)


# In[ ]:




