#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

import requests

def pull(user_group, secret_key, arm):
	url = ('http://10.243.255.29:5787/pull_arm/%s/%s/%s' % (user_group,secret_key,str(arm)))
	
	while True:
		r = requests.get(url)
		if r.ok:
			output = r.json()['result']
			return(output)


# In[ ]:


armnumber = 24
p = 0.3
numberofpulls = 180

def epsilongreedy(p, numberofpulls):
    total_reward=0
    average_reward=[0]*number
    record_of_choice=[]
    record_of_best_arm=[]
    best_arm=0
    record_of_regret=[]
    
    for t in range(numberofpulls):
        if np.random.uniform() <= p:
            arm =np.random.randit(0,armnumber)
        else:
            arm = best_arm
        record_of_choice.append(arm)
        current_reward=pull("","",arm)['Reward']
        total_reward+=current_reward
        n=record_of_choice.count(arm)
        average_reward_of_arms[arm]=(n*average_reward_of_arms[arm]+current_reward)/(n+1)
        best_arm = average_reward_of_arms.index(max(average_reward_of_arms))
        record_of_best_arm.append(best_arm)
        
        regret = average_reward_of_arms[best_arm]*(t+1)
sum(average_reward_of_arms[record_of_choice[i]] for i in range(len(record_of_choice)))
record_of_regret.append(regret)

    return record_of_choice, record_of_best_arm, total_reward,record_of_regret
        


# In[ ]:


## Drop adaptive epsilon greedy
def epsilon_greedy(counts, epsilon=0.5, decrease_const=1000):
    """
    Adaptive epsilon greedy

    Parameters
    ----------
    counts : int 2d-array, shape(K, 2), where K = the total number of arms
        success and failures for each arm where column 0 represents 
        success, 1 represents failure

    epsilon : float
        the initial probability of choosing a random arm; 
        1 - epsilon is the probability of choosing the current best arm

    decrease_const : int
        parameter for the adaptive (annealing) epsilon, where the epsilon
        parameter will decrease as time goes by.

    Returns
    -------
    (int) the chosen arm
    """

    # calculate the empirical means and the total number of simulations that were ran
    n_arms = counts.shape[0]
    totals = counts.sum(axis=1)
    successes = counts[:, 0]
    empirical_means = successes / totals
    total_counts = counts.sum()

    epsilon /= (1 + total_counts / decrease_const)
    if np.random.rand() > epsilon:
        return np.argmax(empirical_means)
    else:
        return np.random.randint(0, n_arms)

# counts : stores the counts of success and failures for each arm
# where column 0 represents success, 1 represents failure.
# each arm's count is initialiated as 1 to ensure that each arm is
# played at least once, to prevent "cold start" problem and
# 0 division in the beginning
K = 2
counts = np.ones((K, 2))
print(counts)
epsilon_greedy(counts)

