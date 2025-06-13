import json #Importing json for the dataset 
import pandas as pd 
from datetime import datetime, timedelta #Importing datetime for the time in the dataset

def load_medication(path="data/medication_schedule.json"): #I googled this, this helps to load the dataset
  with open(path, "r") as f: #Reading the data
    schedule = json.load(f)
  return schedule

def load_user(path="data/user_samples.csv"):
  return pd.read_csv(path) #Reading the csv file

def check_medication(schedule, user_logs, user_id="user_001", time_window_minutes=30):
  now = datetime.now() #Gets the date and time now
  medications_due = []

for x in schedule["medications"]:
  name = x["name"]
  str_time = x["time"]
  time = datetime.strptime(str_time, "%H:%M").replace(year=now.year, month=now.month, day=now.day) #Conversions and stuff
  
  
