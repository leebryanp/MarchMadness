
# coding: utf-8

# In[1]:

import re
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from pandas.stats.api import ols
from subprocess import check_output


# In[2]:

TourneySeeds = pd.read_csv('C:/Users/LeeBryanP/Downloads/march-machine-learning-mania-2016-v1/TourneySeeds.csv')
SampleSubmission = pd.read_csv('C:/Users/LeeBryanP/Downloads/march-machine-learning-mania-2016-v1/SampleSubmission.csv')
Seasons = pd.read_csv('C:/Users/LeeBryanP/Downloads/march-machine-learning-mania-2016-v1/Seasons.csv')
Teams = pd.read_csv('C:/Users/LeeBryanP/Downloads/march-machine-learning-mania-2016-v1/Teams.csv')
TourneySlots = pd.read_csv('C:/Users/LeeBryanP/Downloads/march-machine-learning-mania-2016-v1/TourneySlots.csv')
TourneyDetailedResults = pd.read_csv('C:/Users/LeeBryanP/Downloads/march-machine-learning-mania-2016-v1/TourneyDetailedResults.csv')
TourneyCompactResults = pd.read_csv('C:/Users/LeeBryanP/Downloads/march-machine-learning-mania-2016-v1/TourneyCompactResults.csv')
RegularSeasonDetailedResults = pd.read_csv('C:/Users/LeeBryanP/Downloads/march-machine-learning-mania-2016-v1/RegularSeasonDetailedResults.csv')
team_dict = dict(zip(Teams['Team_Id'].values, Teams['Team_Name'].values))
TourneyDetailedResults['Wteam_name'] = TourneyDetailedResults['Wteam'].map(team_dict)
TourneyDetailedResults['Lteam_name'] = TourneyDetailedResults['Lteam'].map(team_dict)
RegularSeasonDetailedResults['Wteam_name'] = RegularSeasonDetailedResults['Wteam'].map(team_dict)
RegularSeasonDetailedResults['Lteam_name'] = RegularSeasonDetailedResults['Lteam'].map(team_dict)


# In[3]:

RegularSeasonDetailedResults.to_csv("NamedRegularSeasonDetailedResults.csv", sep=',', index=True)
TourneyDetailedResults.to_csv("NamedTourneyDetailedResults.csv", sep=',', index=True)


# In[5]:

TourneyDetailedResults


# In[6]:

RegularSeasonDetailedResults


# In[ ]:



