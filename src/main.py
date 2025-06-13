import streamlit as st
from utilities import load_medication, load_user, check_medication #Getting stuff from utilities

st.title("Medicine Reminder AI")

schedule = load_medication("data/medication_schedule.json")
user_logs = load_user("data/user_samples.csv")


