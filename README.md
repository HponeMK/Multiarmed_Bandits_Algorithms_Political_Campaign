# Multiarmed_Bandits_Algorithms_Political_Campaign

#### Techniques Employed
Multiarmed Bandits Algorithms: UCB Linear, Greedy, Uniform

### Context
This project is based on an Obama’s fundraising campaign simulation where we are trying to find the best combinations of a sign-up button and a background media that maximises the number of visitor sign-ups. There are 4 buttons and 6 media available, giving a total of 24 possible combinations. Similar to real life, a budget constraint is imposed by capping the number of combination tries to 100 million views. Each try reflects the results of 100 visitors’ views, and so, we have a maximum of 1 million tries. <br>

<strong> Key objective: </strong> find the best sign-up button and media combination as efficiently as possible.<br><br>
  <strong> Approach:</strong> We choose to adopt a Multi Armed Bandit (MAB) approach instead of A/B split testing which is commonly used to determine best combinations. MAB is more efficient - able to find the best combination faster - as it adapts and shifts towards winning variations throughout the experiment, instead of waiting until the end. <br>
  
### Implications & Insights
Uniform distribution gave the highest reward for the campaign managers when rewards from available arms are constant or unchanging. However, it requires a waiting period to explore each arm before taking an action post-exploration phase. In real life, this might not be ideal as campaign managers might also face time constraint, on top of budget constraint. In that case, UCB1 offers a relatively faster alternative to determine a winning variation on a sign-up page. It also offers a better insight into the distribution of the next best alternative, as discussed in part 4.2.1. 

<br> Nonetheless, the strength of UCB1 is two-sided, as the current model will not explore unknown variations until a high degree of uncertainty is reached. This may merit either increasing ɑ (and promoting more exploration), or using the unused variations in other pages where the model is not deployed (for gathering data to create a prior). <br>

### Collaborators
Kyle Kenji Asano (@kasano)<br>
Widya Salim (@salimwid)<br>
Sae Jin Jang (@saejin123)<br>
Hpone Myat Khine (@HponeMK) <br>
Amy Mingxuan Yang (@mingxuanyang-amy)
