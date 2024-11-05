import pandas as pd
import certifi
import json
import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

game_logs = pd.read_csv('game_logs.csv')
advanced_stats = pd.read_csv('advanced_stats.csv')

'''
Create a subset of the advanced stats dataframe with desired attributes
- Offensive Rating
- Defensive Rating
- Net Rating
- Pace
'''

advanced_stats = advanced_stats[['ORtg','DRtg','NRtg','Pace',]]

# Merge the DataFrames by matching 'Opp' in game_logs with "Team" in advanced_stats
merged_df = pd.merge(game_logs, advanced_stats, left_on='Opp', right_on='Team', how='left')

merged_df.to_csv("data.csv")

# install these commands 
# !pip install pymongo
# !pip install python-dotenv

import certifi
import urllib3
http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where()
)

load_dotenv()

uri = os.getenv('MONGODB_URI')

# Create a new client and connect to the server with certifi’s CA certificates
client = MongoClient(uri, server_api=ServerApi('1'), tlsCAFile=certifi.where())

df = pd.read_csv("data.csv")

data = df.to_dict(orient = "records")

db = client["NBA-player-data"]

db.gameLogs.insert_many(data)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)