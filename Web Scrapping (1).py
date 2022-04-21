#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import csv


# In[2]:


output_file = csv.writer(open('prem_table_bs.csv', 'w'))


# In[3]:


output_file.writerow(['Position', 'Team', 'Played', 'Won', 'Drawn', 'Lost', 'For', 'Against', 'GD', 'Points'])


# In[4]:


result = requests.get("https://www.bbc.co.uk/sport/football/tables")


# In[5]:


src = result.content


# In[6]:


soup = BeautifulSoup(src, 'html.parser')


# In[7]:


table = soup.find_all("table")
league_table = table[0]


# In[8]:


teams = league_table.find_all("tr")


# In[9]:


for team in teams[1:21]:

    stats = team.find_all("td")

    position = stats[0].text
    team_name = stats[2].text
    played = stats[3].text
    won = stats[4].text
    drawn = stats[5].text
    lost = stats[6].text
    for_goals = stats[7].text
    against_goals = stats[8].text
    goal_diff = stats[9].text
    points = stats[10].text
    
    output_file.writerow([position, team_name, played, won, drawn, lost, for_goals, against_goals, goal_diff, points])


# In[10]:


soup


# In[16]:


teams


# In[17]:


src


# In[18]:


result


# In[19]:


output_file


# In[20]:


table


# In[21]:


league_table


# In[22]:


points


# In[23]:


stats


# In[24]:


position


# In[26]:


team_name


# In[27]:


played


# In[28]:


won


# In[29]:


drawn


# In[30]:


lost


# In[31]:


for_goals


# In[32]:


against_goals


# In[35]:


goal_diff


# In[ ]:





# In[38]:





# In[ ]:




