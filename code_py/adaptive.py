#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import server_pull import pull
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


# In[ ]:


n = 100
epsilon = []
for i in range(n):
    a = 1/(i + 1)
    epsilon.append(a)
    
A=24
count={}
reward={}

bandits=[]
rewards=[]

for i in range(A):
    count[i] =0
    reward[i] = 0
    
def bandit(count,reward,A):
    avg={}
    for i in range(A):
        if count[i] != 0:
            avg[i] = reward[i]/count[i]
    return max(avg, key = avg.get)

for i in range(n):
    p = np.random.uniform(0,1)
    if p<epsilon[i]:
        current = np.random.randint(0,24,dtype=int)
    else:
        current = bandit(count,rewards,A)
    results = pull('','',current)
    count=count[current] +=1
    #rewards
    #bandits


# In[ ]:




