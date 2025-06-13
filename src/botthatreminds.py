import json #Importing json for the dataset 
import pandas as pd 
from datetime import datetime, timedelta #Importing datetime for the time in the dataset

def load_medication(path="data/medication_schedule.json"): # I googled this, this helps to load the dataset
  with open(path, "r") as f: #Reading the data
    schedule = json.load(f)
  return schedule

def load_user(path="data/user_samples.csv"):
  return pd.read_csv(path) #Reading the csv file

